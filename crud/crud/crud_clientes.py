from pymongo import MongoClient
from .crud import CollectionCRUD

class ClientesCRUD(CollectionCRUD):
    """
    Classe de CRUD da collection `clientes` do banco `loja`
    """
    
    def __init__(self, mongo_client: MongoClient):
        DATABASE = "loja"
        COLLECTION = "clientes"

        super().__init__(mongo_client, DATABASE, COLLECTION)