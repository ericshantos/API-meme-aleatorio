import sys
import os

# Adicione o diretório raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest.mock import MagicMock
from app.get_midia.extrair_url_video import extrair_url_video


class TestExtrairUrlVideo(unittest.TestCase):

    def test_extrair_url_video(self):
        # Criar uma instância de resposta mock
        mock_response = MagicMock()

        # Definir o conteúdo HTML mock
        mock_response.content = """
        <html>
            <body>
                <video class="item-video gallery-item-video grey-background">
                    <source src="https://exemplo.com/video1.mp4" type="video/mp4">
                </video>
                <video class="item-video gallery-item-video grey-background">
                    <source src="https://exemplo.com/video2.mp4" type="video/mp4">
                </video>
                <video class="item-video gallery-item-video grey-background">
                    <source src="https://exemplo.com/video3.mp4" type="video/mp4">
                </video>
            </body>
        </html>
        """

        # Chamar a função e obter a lista de URLs de vídeo
        urls = extrair_url_video(mock_response)

        # Verificar se a função retornou a lista correta de URLs de vídeo
        self.assertEqual(
            urls,
            [
                "https://exemplo.com/video1.mp4",
                "https://exemplo.com/video2.mp4",
                "https://exemplo.com/video3.mp4",
            ],
        )


if __name__ == "__main__":
    unittest.main()
