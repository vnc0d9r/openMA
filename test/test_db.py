from core.db import  *

def test_db():
    db=OpenMADatabase()
    print db.get_task()
