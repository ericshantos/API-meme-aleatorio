import sys
import os

# Adicione o diretório raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest.mock import MagicMock, patch, ANY
from io import BytesIO
from app.tratar_midia.tratar_imagem import processar_imagem


class TestTratarImagemPIL(unittest.TestCase):

    @patch("app.tratar_midia.tratar_imagem.Image")
    def test_tratar_imagem_pil(self, mock_image):
        # Simular uma resposta de requisição com um objeto de imagem
        resposta_mock = MagicMock()
        imagem_mock = MagicMock()
        resposta_mock.__enter__.return_value = imagem_mock
        mock_image.open.return_value = resposta_mock

        # Chamar a função para processar a imagem
        meme_processado = processar_imagem(BytesIO())

        # Verificar se a função retornou um objeto BytesIO
        self.assertIsInstance(meme_processado, BytesIO)

        # Verificar se o ponteiro de leitura/escrita está no início do objeto BytesIO
        self.assertEqual(meme_processado.tell(), 0)

        # Verificar se a função Image.open foi chamada com os parâmetros corretos
        mock_image.open.assert_called_once_with(ANY)


if __name__ == "__main__":
    unittest.main()
