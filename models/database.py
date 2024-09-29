from peewee import SqliteDatabase
from dotenv import load_dotenv
import os

load_dotenv()

db_name = os.getenv('DB_NAME', 'default.db') 
db = SqliteDatabase(db_name)

def create_tables():
    from account import User, Email_Verific, Sessions
    from task import Tasks, Tasks_History

    with db.atomic():
        db.create_tables([User, Email_Verific, Sessions, Tasks, Tasks_History])
        print('Tabelas criadas com sucesso')

if __name__ == "__main__":
    try:
        create_tables()
    except Exception as e:
        print('Erro ao criar tabelas: ', e)
