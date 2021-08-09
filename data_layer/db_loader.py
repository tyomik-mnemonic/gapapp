import sqlalchemy
from flask import request
from config import pgstorage

pgstorage=pgstorage.engine

class RelDBSingletone(type):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance

class RelDBConnector(metaclass=RelDBSingletone):

    def __init__(self, engine):
        self.engine = engine
        self.conn = engine.connect()

    def make_request(self, req:str):

        result = self.engine.execute(f"""{req}""").fetchall()
        return result