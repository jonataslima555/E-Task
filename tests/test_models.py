import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))


import pytest
from peewee import SqliteDatabase
from account import User
from task import Tasks
from datetime import datetime 


test_db = SqliteDatabase(':memory:')

@pytest.fixture
def setup_database():
    """
    Configura um banco de dados temporário em memória para os testes.
    """

    test_db.bind([User, Tasks], bind_refs=False, bind_backrefs=False)
    

    test_db.connect()
    test_db.create_tables([User, Tasks])
    
    yield  
    
    # Fechar a conexão e apagar as tabelas após os testes
    test_db.drop_tables([User, Tasks])
    test_db.close()

def test_create_user(setup_database):
    """
    Testa se um usuário pode ser criado corretamente.
    """
    user = User.create_user(username='testuser', email='testuser@example.com', password='password123')
    
    # Verificar se o usuário foi criado
    assert user is not None
    assert user.username == 'testuser'
    assert user.email == 'testuser@example.com'
    assert user.is_active is False  # Valor padrão
    assert user.is_admin is False  # Valor padrão

def test_create_task(setup_database):
    """
    Testa se uma tarefa pode ser criada corretamente para um usuário.
    """
    user = User.create_user(username='testuser', email='testuser@example.com', password='password123')
    
    task = Tasks.create_task(user=user, title='Test Task', descr='This is a test task', due_data=datetime.now())
    
    # Verificar se a tarefa foi criada
    assert task is not None
    assert task.title == 'Test Task'
    assert task.descr == 'This is a test task'
    assert task.user_id == user  # Verificar a associação com o usuário
