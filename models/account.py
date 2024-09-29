from peewee import CharField, DateField, BooleanField, ForeignKeyField, Model
from database import db  # Removido
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class BaseModel(Model):
    class Meta:
        database = db  # Associa a base de dados aqui

class User(BaseModel):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    created_at = DateField()
    update_at = DateField()
    is_active = BooleanField(default=False)
    is_admin = BooleanField(default=False)
    
    @classmethod
    def create_user(cls, username, email, password, is_active=False, is_admin=False):
        try:
            hashed_password = generate_password_hash(password)  # Gerar hash da senha
            user = cls.create(
                username=username,
                email=email,
                password=hashed_password,  # Armazenar a senha hash
                created_at=datetime.now(),
                update_at=datetime.now(),
                is_active=is_active,
                is_admin=is_admin
            )
            return user
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
            return None

class Email_Verific(BaseModel):
    user_id = ForeignKeyField(User, backref='users')
    verific_code = CharField(unique=True)
    created_at = DateField()
    expires_at = DateField()  # Corrigido typo de "expires_ate"
    is_verified = BooleanField(default=False)

class Sessions(BaseModel):
    user_id = ForeignKeyField(User, backref='users')
    session_token = CharField(unique=True)
    created_at = DateField()
    expires_at = DateField()  # Corrigido typo de "expires_ate"
    is_active = BooleanField(default=False)
