from json import load as json_load

from pymongo import MongoClient
from unittest import TestCase

from crud.crud_clientes import ClientesCRUD


class CRUDTestCase(TestCase):
    """
    Classe base para os testes de CRUD do projeto
    """

    def setUp(self) -> None:
        """
        Método executado antes dos testes.
        """
        HOSTNAME = "crud_mongo_db"
        PORT = 27017

        self.mongo_client = MongoClient(HOSTNAME, PORT)
        self.clientes_crud = ClientesCRUD(self.mongo_client)

        # Lendo arquivo `tests/data.json` para obter
        # os objetos que serão inseridos
        with open('tests/data.json') as data_json:
            self.clientes = json_load(data_json)


    def tearDown(self) -> None:
        """
        Método executado após os testes.
        """
        self.clientes_crud.clean_collection()