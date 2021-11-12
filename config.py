import sqlalchemy as sal
from sqlalchemy import create_engine

class PGconfig:
    def __init__(self, host, user, psw, db, port=5432):
        self.host = host
        self.user = user
        self.psw = psw
        self.db = db

        self.engine = create_engine(f'postgresql://{user}:{psw}@{host}:{5432}/{db}')


pgstorage = PGconfig(host='',
                    user='', 
                    psw='',
                    db='')
