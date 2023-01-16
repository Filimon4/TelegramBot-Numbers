from peewee import *

db = SqliteDatabase('TgBot.db')

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db

class User(BaseModel):
    name = CharField()

    class Meta:
        db_table = "User"