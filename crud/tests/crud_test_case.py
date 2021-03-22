from json import load as json_load

from unittest import TestCase

from crud.connection import CRUDMongoClient
from crud.crud_clientes import ClientesCRUD


class CRUDTestCase(TestCase):
    """
    Classe base para os testes de CRUD do projeto
    """

    def setUp(self) -> None:
        """
        Método executado antes dos testes.
        """
        self.mongo_client = CRUDMongoClient()
        self.mongo_client = self.mongo_client.client
        
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