from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)  # Considere usar um hash de senha
    name = db.Column(db.String)
    email = db.Column(db.String)

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password  # Considere usar um hash de senha
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<User {self.username}>"


