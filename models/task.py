from peewee import CharField, DateField, BooleanField, ForeignKeyField, TextField, IntegerField
from account import User, BaseModel
from datetime import datetime

class Tasks(BaseModel):
    user_id = ForeignKeyField(User, backref='users')
    title = CharField(default='Task title')
    descr = TextField(default='Task description')
    category = CharField(default='Task')
    status = IntegerField(default=0)
    due_data = DateField()
    created_at = DateField()
    updated_at = DateField()
    completed_at = DateField(null=True)
    recurring = BooleanField(default=0)
    recurring_until = DateField(null=True)

    @classmethod
    def create_task(cls, user, title, descr, category='Task', due_data=None, recurring=0, recurring_until=None):
        try:
            task = cls.create(
                user_id=user,
                title=title,
                descr=descr,
                category=category,
                status=0,
                due_data=due_data if due_data else datetime.now(),
                created_at=datetime.now(),
                updated_at=datetime.now(),
                recurring=recurring,
                recurring_until=recurring_until,
                completed_at=None
            )
            return task
        except Exception as e:
            print(f"Erro ao criar tarefa: {e}")
            return None

class Tasks_History(BaseModel):
    task_id = ForeignKeyField(Tasks, backref='tasks')
    user_id = ForeignKeyField(User, backref='users')
    status_before = IntegerField(default=0)
    status_after = IntegerField(default=0)
    action_type = IntegerField(default=0)
    timestamp = DateField()
