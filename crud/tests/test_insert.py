from bson.objectid import ObjectId
from .crud_test_case import CRUDTestCase


class CRUDInsertTestCase(CRUDTestCase):
    """
    Casos de teste de inserção
    """

    def test_insert_one_document(self) -> None:
        """
        Testes do método `CollectionCRUD.insert` que insere
        um documento por vez na collection
        """
        for cliente in self.clientes:
            id = self.clientes_crud.insert(cliente)            
            type_id = type(id)

            self.assertEqual(type_id, ObjectId)


    def test_insert_many_documents(self) -> None:
        """
        Testes do método `CollectionCRUD.insert_many` que insere
        vários documentos por vez na collection
        """
        ids = self.clientes_crud.insert_many(self.clientes)
        type_ids = [type(id) for id in ids]

        for type_id in type_ids:
            self.assertEqual(type_id, ObjectId)