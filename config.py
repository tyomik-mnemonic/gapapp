import sqlalchemy as sal
from sqlalchemy import create_engine

class PGconfig:
    def __init__(self, host, user, psw, db, port=5432):
        self.host = host
        self.user = user
        self.psw = psw
        self.db = db

        self.engine = create_engine(f'postgresql://{user}:{psw}@{host}:{5432}/{db}')


pgstorage = PGconfig(host='34.116.128.59',
                    user='gapuser', 
                    psw='u3IGkErFJ1jkenO1',
                    db='vector_storage')
