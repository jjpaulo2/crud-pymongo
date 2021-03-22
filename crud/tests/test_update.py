from .crud_test_case import CRUDTestCase


class CRUDUpdateTestCase(CRUDTestCase):
    """
    Casos de teste de atualização
    """

    def setUp(self) -> None:
        """
        Método executado antes dos testes.
        """
        super().setUp()
        self.clientes_crud.insert_many(self.clientes)


    def test_update_one_document(self) -> None:
        """
        Testes do método `CollectionCRUD.update` que atualiza
        um documento por vez na collection
        """
        update_where = {"nome": "Elaini Cristina"}
        update_to = {"idade": 21}

        updated_count = self.clientes_crud.update(update_where, update_to)

        self.assertEqual(updated_count, 1)


    def test_update_many_documents(self) -> None:
        """
        Testes do método `CollectionCRUD.update_many` que atualiza
        vários documentos por vez na collection
        """
        update_where = {"nome": "João Paulo"}
        update_to = {"telefone": "40028922"}

        updated_count = self.clientes_crud.update_many(update_where, update_to)

        self.assertEqual(updated_count, 2)