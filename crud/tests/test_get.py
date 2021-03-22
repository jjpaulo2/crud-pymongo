from .crud_test_case import CRUDTestCase


class CRUDGetTestCase(CRUDTestCase):
    """
    Casos de teste de leitura
    """
    
    def setUp(self) -> None:
        """
        Método executado antes dos testes.
        """
        super().setUp()
        self.clientes_crud.insert_many(self.clientes)


    def test_get_one_document(self) -> None:
        """
        Teste do método `CollectionCRUD.get` que retorna apenas 1 resultado
        """
        query_params = {"telefone": "+5586981426986"}
        result = self.clientes_crud.get(query_params)

        quant_result = len(result)
        self.assertEqual(quant_result, 1)


    def test_get_many_documents(self) -> None:
        """
        Testes do método `CollectionCRUD.get` que retorna mais de 1 resultado
        """
        query_params = {"nome": "João Paulo"}
        result = self.clientes_crud.get(query_params)

        quant_result = len(result)
        self.assertEqual(quant_result, 2)

        query_params = {"nome": "João Paulo", "idade": 19}
        result = self.clientes_crud.get(query_params)

        quant_result = len(result)
        self.assertEqual(quant_result, 2)