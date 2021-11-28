import sqlalchemy
from flask import request
from config import pgstorage
from abc import ABC

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

vector_storage = RelDBConnector(engine=pgstorage)

class DbLoader(ABC):

    def __init__(self, request:str=None):
        self.request = request

class VectorDbLoader(DbLoader):
    def __init__(self):
        self.connector = vector_storage
        super().__init__()

    def make_request(self):
        self.connector.make_request(self.request)

class VectorDbLoaderFabric(ABC):

    @staticmethod
    def loader():
        return VectorDbLoader()

