from bson.objectid import ObjectId
from pymongo import MongoClient
from typing import List

class CollectionCRUD:
    """
    Classe de CRUD (Create, Read, Update, Delete) de uma collection
    do MongoDB.

    Methods:
        - insert
        - get
        - update
        - delete
    """
    def __init__(self, mongo_client: MongoClient, database_name: str, collection_name: str):
        self.mongo = mongo_client
        
        self.database_name = database_name
        self.db = self.mongo[database_name]

        self.collection_name = collection_name
        self.collection = self.db[collection_name]


    def insert(self, document: dict) -> ObjectId:
        """
        Método que faz a inserção de um documento na coleção da classe

        Parameters:
            document (dict): dicionário/json com os dados que serão inseridos
        
        Returns:
            ObjectId: id do documento inserido na collection
        """
        inserted_document = self.collection.insert_one(document)
        inserted_id = inserted_document.inserted_id

        return inserted_id


    def insert_many(self, documents: List[dict]) -> List[ObjectId]:
        """
        Método que faz a inserção de vários documentos na coleção da classe

        Parameters:
            documents (List[dict]): lista contendo os dicionários/jsons com os dados que serão inseridos
        """
        inserted_documents = self.collection.insert_many(documents)
        inserted_ids = inserted_documents.inserted_ids

        return inserted_ids


    def get(self, query_parameters: dict) -> list:
        """
        Método que obtém todos os documentos filtrados de acordo com os `query_parameters`
        passados como parâmetros.

        Parameters:
            query_parameters (dict): dicionário/json com os campos que serào filtrados
        """
        query = self.collection.find(query_parameters)
        query_list = list(query)

        return query_list


    def update(self, query_parameters: dict, update_values: dict) -> int:
        """
        Método que atualiza um objeto de uma collection com os valores passados
        como parâmetros.

        Parameters:
            query_parameters (dict): dicionário/json com os campos que serào filtrados
            update_values (dict): dicionário/json com os campos e os valores que serão atualizados/adicionados
        """
        update_dict = {"$set": update_values}

        updated_document = self.collection.update_one(query_parameters, update_dict, upsert=False)
        updated_count = updated_document.modified_count

        return updated_count


    def update_many(self, query_parameters: dict, update_values: dict) -> List[int]:
        """
        Método que atualiza uma lista de objetos de uma collection com os valores 
        passados como parâmetros.

        Parameters:
            query_parameters (dict): dicionário/json com os campos que serào filtrados
            update_values (dict): dicionário/json com os campos e os valores que serão atualizados/adicionados
        """
        update_dict = {"$set": update_values}

        updated_document = self.collection.update_many(query_parameters, update_dict, upsert=False)
        updated_count = updated_document.modified_count

        return updated_count


    def delete(self, query_parameters: dict) -> int:
        """
        Método que deleta todos os objetos de uma collection com os valores 
        passados como parâmetros.

        Parameters:
            query_parameters (dict): dicionário/json com os campos que serào filtrados
        """
        deleted_documents = self.collection.delete_many(query_parameters)
        deleted_count = deleted_documents.deleted_count
        
        return deleted_count


    def clean_collection(self) -> int:
        """
        Método que deleta todos os objetos de uma collection.
        """
        deleted_count = self.delete({})
        return deleted_count
