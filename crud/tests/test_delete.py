from .crud_test_case import CRUDTestCase


class CRUDDeleteTestCase(CRUDTestCase):
    """
    Casos de teste de remoção
    """

    def setUp(self) -> None:
        """
        Método executado antes dos testes.
        """
        super().setUp()
        self.clientes_crud.insert_many(self.clientes)


    def test_delete_one_document(self) -> None:
        """
        Testes do método `CollectionCRUD.delete` que deleta
        um documento por vez na collection
        """
        for cliente in self.clientes:
            deleted_count = self.clientes_crud.delete(cliente)
            self.assertEqual(deleted_count, 1)


    def test_delete_many_documents(self) -> None:
        """
        Testes do método `CollectionCRUD.delete` que deleta
        vários documentos por vez na collection
        """
        deleted_count = self.clientes_crud.delete({})
        self.assertEqual(deleted_count, 4)