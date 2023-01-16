from peewee import *
from .models.user import *

def register_database():
    db.connect()
    with db:
        db.create_tables([User, Pets])
        user = User.get(User.id == 2)
        print(user)
    print("Done")
    db.close()


