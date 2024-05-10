import sys
import os

# Adicione o diretório raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from unittest.mock import MagicMock, patch
from app.get_midia.requisicao_http import requisicao_memedroid, get_meme_aleatorio


class TestMemedroidFunctions(unittest.TestCase):

    def test_requisicao_memedroid(self):
        # Mock da resposta da requisição
        response_mock = MagicMock()
        response_mock.status_code = 200

        # Mock da função requests.get para retornar a resposta mockada
        with patch(
            "app.get_midia.requisicao_http.requests.get", return_value=response_mock
        ) as mock_get:
            # Chamada da função
            response = requisicao_memedroid(
                "https://pt.memedroid.com/memes/tag/programa%C3%A7%C3%A3o"
            )

            # Verificação de que requests.get foi chamado com os argumentos corretos
            mock_get.assert_called_once_with(
                "https://pt.memedroid.com/memes/tag/programa%C3%A7%C3%A3o",
                stream=None,
                timeout=10,
            )

            # Verificação de que o retorno é igual à resposta mockada
            self.assertEqual(response, response_mock)

    @patch("app.get_midia.requisicao_http.requisicao_memedroid")
    @patch("app.get_midia.requisicao_http.extrair_urls_imagens")
    @patch("app.get_midia.requisicao_http.extrair_url_video")
    def test_get_meme_aleatorio(
        self,
        mock_extrair_url_video,
        mock_extrair_urls_imagens,
        mock_requisicao_memedroid,
    ):
        # Mock da resposta da requisição
        response_mock = MagicMock()
        response_mock.status_code = 200

        # Mock da função de extração de URLs de imagens para retornar uma lista de URLs
        mock_extrair_urls_imagens.return_value = [
            "https://example.com/image1.jpg",
            "https://example.com/image2.jpg",
        ]

        # Mock da função de extração de URL de vídeo para retornar uma lista de URLs
        mock_extrair_url_video.return_value = ["https://example.com/video1.mp4"]

        # Mock da função de requisição memedroid para retornar a resposta mockada
        mock_requisicao_memedroid.return_value = response_mock

        # Chamada da função
        urls_meme = get_meme_aleatorio()

        # Verificação de que a função de requisição foi chamada com a URL correta
        mock_requisicao_memedroid.assert_called_once_with(
            "https://pt.memedroid.com/memes/tag/programa%C3%A7%C3%A3o"
        )

        # Verificação de que as funções de extração de URLs de imagens e vídeo foram chamadas com a resposta correta
        mock_extrair_urls_imagens.assert_called_once_with(response_mock)
        mock_extrair_url_video.assert_called_once_with(response_mock)

        self.assertIsNotNone(urls_meme)  # Verifica se a lista não é None
        self.assertGreater(
            len(urls_meme), 0
        )  # Verifica se o comprimento da lista é maior que zero


if __name__ == "__main__":
    unittest.main()
