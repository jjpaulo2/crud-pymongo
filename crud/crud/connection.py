from pymongo import MongoClient
from os import getenv

class CRUDMongoClient:
    """
    Classe de conexão com o banco de dados MongoDB
    """

    def __init__(self) -> None:
        self.__get_db_vars()
        self.client = MongoClient(self.HOST, self.PORT)


    @property
    def connection(self) -> MongoClient:
        """
        Instância da conexão com o MongoDB
        """
        return self.client


    def __get_db_vars(self) -> None:
        """
        Método que obtém as constantes de configuração
        das vairáveis de ambiente definidas
        """
        self.HOST = getenv("MONGODB_HOST")
        self.PORT = getenv("MONGODB_PORT")

        if not self.HOST:
            self.HOST = "localhost"

        if self.PORT:
            self.PORT = int(self.PORT)
        else:
            self.PORT = 27017
