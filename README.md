# MVC-Auth

Este projeto é uma aplicação web construída com Flask que permite a autenticação de usuários, oferecendo funcionalidades como login, registro, logout e uma página protegida que só pode ser acessada por usuários autenticados.

## Funcionalidades

A aplicação possui as seguintes rotas:

- **`/home`**: Uma página de apresentação do projeto.
- **`/login`**: Um formulário para usuários se autenticarem.
- **`/register`**: Um formulário para novos usuários se registrarem.
- **`/logout`**: Uma rota que encerra a sessão do usuário e o redireciona para a página inicial.
- **`/protected`**: Uma página que só pode ser acessada por usuários logados. Caso um usuário não autenticado tente acessá-la, será redirecionado para a rota `/home`.

## Tecnologias Utilizadas

- **Flask**: Microframework para construção de aplicações web.
- **Flask-SQLAlchemy**: Extensão do Flask que adiciona suporte a bancos de dados SQL.
- **Flask-Migrate**: Ferramenta para gerenciar migrações de banco de dados.
- **Flask-Login**: Extensão para gerenciar sessões de usuários.
- **Flask-WTF**: Extensão que facilita o uso de formulários em Flask.
