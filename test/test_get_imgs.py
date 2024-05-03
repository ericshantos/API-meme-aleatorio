import unittest
from unittest.mock import patch, Mock
from app.get_midia.requisicao_http import requisicao_memedroid, extrair_urls_imagens


class TestGetImgs(unittest.TestCase):

    def setUp(self):

        # URL do Memedroid
        self.base_url = "https://www.memedroid.com/memes/tag/programming"

    @patch("app.get_imgs.get_imgs.requisicao_memedroid")
    def test_requisicao_memedroid(self, mock_get):
        """
        Testa a função requisicao_memedroid para garantir que ela está fazendo a requisição corretamente.

        Utiliza um objeto de mock para substituir a função requisicao_memedroid original, configurando-o para retornar
        um objeto de resposta com status 200. Então, chama a função requisicao_memedroid com a base_url especificada
        e verifica se a resposta retorna um status_code igual a 200.

        Caso o teste falhe, uma AssertionError será levantada.
        """
        # Configurando o comportamento do mock para retornar um objeto de resposta com status 200
        mock_requisicao_memedroid = Mock()
        mock_requisicao_memedroid.status_code = 200
        mock_get.return_value = mock_requisicao_memedroid

        # Chamando a função que será testada
        resposta = requisicao_memedroid(self.base_url)

        self.assertEqual(resposta.status_code, 200)

    def test_get_meme_aleatorio(self):
        """
        Testa a função get_meme_aleatorio para garantir que ela está obtendo corretamente uma lista de URLs de imagens.

        Realiza uma requisição à base URL especificada para obter uma lista de URLs de imagens usando a função
        requisicao_memedroid. Em seguida, extrai as URLs das imagens da resposta obtida. Verifica se a lista de URLs não
        está vazia.

        Caso a lista esteja vazia, uma AssertionError será levantada.
        """
        # chama a lista de urls
        requisicao = requisicao_memedroid(self.base_url)

        lista_urls = extrair_urls_imagens(requisicao)

        # Verifica se a lista não está vazia
        self.assertTrue(lista_urls)


if __name__ == "__main__":
    unittest.main()
