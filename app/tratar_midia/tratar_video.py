# -*- coding: utf-8 -*-
"""
@Author: Eric dos Santos (ericshantos13@gmail.com)
Módulo responsável por tratar os frames de vídeo.
"""

from typing import Generator
import cv2, os, tempfile, requests


def processar_video(
    midia_video: requests.models.Response,
) -> Generator[bytes, None, None]:
    """
    Processa um vídeo recebido como uma resposta HTTP.
    """
    try:
        if midia_video is None:
            raise ValueError("A resposta de vídeo é None.")

        # Lê o conteúdo do vídeo
        video_bytes = midia_video.content

        # Verifica se o conteúdo do vídeo está vazio
        if not video_bytes:
            raise ValueError("O conteúdo do vídeo está vazio.")

        # Salva o vídeo em um arquivo temporário
        with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as temp_file:
            temp_file.write(video_bytes)
            temp_filename = temp_file.name

        # Cria um objeto VideoCapture para ler o vídeo
        video = cv2.VideoCapture(temp_filename)

        # Verifica se a decodificação foi bem-sucedida
        if not video.isOpened():
            raise ValueError("Falha ao decodificar o conteúdo do vídeo.")

        # Loop para processar cada frame do vídeo
        while True:
            ret, frame = video.read()
            if not ret:
                break

            # Converte o frame para um formato adequado para resposta HTTP
            ret, buffer = cv2.imencode(".jpg", frame)
            frame_bytes = buffer.tobytes()
            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
            )

        # Libera os recursos do vídeo
        video.release()

    except ValueError as ve:
        print(f"Erro ao processar o vídeo: {ve}")

    except Exception as e:
        print(f"Erro inesperado ao processar o vídeo: {e}")

    finally:
        # Remove o arquivo temporário
        if temp_filename:
            os.unlink(temp_filename)
