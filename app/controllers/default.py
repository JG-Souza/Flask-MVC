# Todas as importações necessárias
from flask import render_template, flash, redirect, url_for
from app import app, db, lm
from flask_login import login_user, logout_user, current_user, login_required
from app.models.tables import User
from app.models.forms import LoginForm, RegisterForm

@lm.user_loader # É um decorador fornecido pelo Flask-Login que registra a função load_user como a função de carregamento de usuário. O Flask-Login usa essa função para recuperar um objeto de usuário com base no ID do usuário armazenado na sessão.
def load_user(user_id):
    return User.query.get(int(user_id))


# Criando a rota Home
@app.route('/home')
def home():
    return render_template('home.html')


# Criando a rota Login
@app.route('/login', methods=['GET', 'POST']) # Permitindo os métodos
def login():
    form = LoginForm() # Cria uma instância do formulário de login
    if form.validate_on_submit(): # Verifica se o formulário foi enviado. Essa função retorna True se o método da requisição for POST (ou seja, o formulário foi enviado) e se todos os campos do formulário são válidos. Se qualquer campo não for válido, ela retorna False.
        user = User.query.filter_by(username=form.username.data).first() # Busca um usuário no banco de dados com o nome de usuário fornecido. Cria uma consulta que filtra com base no nome fornecido

        # Verificar se o usuário foi encontrado e se a senha fornecida corresponde à senha armazenada.
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember_me.data) # a função é fornecida pelo Flask-Login e é usada para autenticar o usuário na sessão. O parâmetro remember indica se a sessão do usuário deve ser lembrada
            flash('Logged in successfully.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password.', 'danger')

    # Renderizando formulário para login
    return render_template('form_login.html', form=form)


# Criando rota Logout
@app.route('/logout')
def logout():
    logout_user() # A função é fornecida pelo Flask-Login e é usada para encerrar a sessão do usuário.
    flash('Logged out successfully.', 'success')
    return redirect(url_for('home')) # Retorna o usuário para a página home


# Criando rota para Cadastro
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Redireciona para a página inicial se o usuário já estiver logado
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm() # Cria uma instância do formulário de registro
    if form.validate_on_submit(): # Verifica se o formulário foi submetido e é válido
        # Verifica se o nome de usuário já existe
        if User.query.filter_by(username=form.username.data).first():
            flash('Username already exists. Please choose a different one.', 'danger')
            return redirect(url_for('register'))

        # Cria um novo usuário
        new_user = User(
            username=form.username.data,
            password=form.password.data,
            name=form.name.data,
            email=form.email.data
            )
        
        db.session.add(new_user) # Adiciona o novo usuário à sessão do banco de dados
        db.session.commit() # Comita a transação para salvar o novo usuário no banco de dados
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login')) # Redireciona o usuário para a página de login
    
    # Renderiza o template do formulário de registro
    return render_template('form_registro.html', form=form)

# Rota para acessar uma página protegida, disponível apenas para usuários autenticados
@app.route('/protected')
@login_required # Decorador que exige que o usuário esteja autenticado para acessar esta rota
def protected():

    # Renderiza o template da página protegida
    return render_template('protected.html')


