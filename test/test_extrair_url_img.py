import sys
import os

# Adicione o diretório raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest.mock import MagicMock
from app.get_midia.extrair_url_img import extrair_urls_imagens


class TestExtrairUrlsImagens(unittest.TestCase):

    def test_extrair_urls_imagens(self):
        # Criar uma instância de resposta mock
        mock_response = MagicMock()

        # Definir o conteúdo HTML mock
        mock_response.content = """
        <html>
            <body>
                <div class="item-aux-container">
                    <img class="img-responsive" src="https://exemplo.com/imagem1.jpg">
                </div>
                <div class="item-aux-container">
                    <img class="img-responsive" src="https://exemplo.com/imagem2.jpg">
                </div>
                <div class="item-aux-container">
                    <img class="img-responsive" src="https://exemplo.com/imagem3.jpg">
                </div>
            </body>
        </html>
        """

        # Chamar a função e obter a lista de URLs
        urls = extrair_urls_imagens(mock_response)

        # Verificar se a função retornou a lista correta de URLs
        self.assertEqual(
            urls,
            [
                "https://exemplo.com/imagem1.jpg",
                "https://exemplo.com/imagem2.jpg",
                "https://exemplo.com/imagem3.jpg",
            ],
        )


if __name__ == "__main__":
    unittest.main()
