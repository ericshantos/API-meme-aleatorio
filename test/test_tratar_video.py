import sys
import os

# Adicione o diretório raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest.mock import MagicMock, patch
from requests.models import Response
from app.tratar_midia.tratar_video import processar_video


class TestProcessarVideo(unittest.TestCase):

    @patch("app.tratar_midia.tratar_video.BytesIO")
    def test_processar_video(self, mock_bytesio):
        # Simular uma resposta de requisição com bytes de vídeo
        resposta_mock = MagicMock(spec=Response)
        resposta_mock.content = b"video_bytes"

        # Chamar a função para processar o vídeo
        processar_video(resposta_mock)

        # Verificar se a função BytesIO foi chamada corretamente
        mock_bytesio_instance = mock_bytesio.return_value
        mock_bytesio_instance.write.assert_called_once_with(b"video_bytes")
        mock_bytesio_instance.seek.assert_called_once_with(0)


if __name__ == "__main__":
    unittest.main()
