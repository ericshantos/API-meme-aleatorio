import unittest
from PIL import Image
from io import BytesIO
from app.tratar_midia.tratar_imagem_pil import tratar_imagem_pil


class TestTratarImagemPIL(unittest.TestCase):
    def test_tratar_imagem_pil(self):
        """
        Testa se a função tratar_imagem_pil está retornando corretamente um objeto BytesIO contendo uma imagem no
        formato JPEG.

        Cria uma imagem de exemplo, chama a função tratar_imagem_pil para obter o objeto BytesIO e verifica se:
        - O objeto retornado é uma instância de BytesIO.
        - O conteúdo do objeto BytesIO começa com os bytes de um arquivo JPEG.

        Caso algum dos testes falhe, uma AssertionError será levantada.
        """
        # Crie uma imagem de exemplo
        imagem = Image.new("RGB", (100, 100), color="red")

        # Chame a função para obter o objeto BytesIO
        meme_io = tratar_imagem_pil(imagem)

        # Verifique se o objeto BytesIO está no formato JPEG
        self.assertTrue(isinstance(meme_io, BytesIO))

        # Verifique se o conteúdo do objeto BytesIO está no formato JPEG
        self.assertEqual(
            meme_io.getvalue()[:2], b"\xff\xd8"
        )  # Verifica os primeiros bytes do conteúdo


if __name__ == "__main__":
    unittest.main()
