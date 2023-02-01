from pytube import YouTube
from PyQt5.QtWidgets import QMessageBox
import os


def createMsg(type, text):
    msg = QMessageBox()
    if type == 'Error':
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text)
        return msg
    elif type == 'Info':
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        return msg

def download_video(u) -> None:
    try:
        # Cria uma instância do YouTube com a URL fornecida
        yt = YouTube(u)

        video = yt.streams.filter(progressive=True, file_extension='mp4', mime_type='video/mp4').first()
        video.download('Downloads')
        
        msg = createMsg('Info', 'Video baixado com sucesso')
        msg.exec_()

    except:
        print("Ocorreu um erro durante o processo de download :(")
        msg = createMsg('Error', 'Ocorreu um erro durante o processo de download :(. Verifique a URL e tente de novo')
        msg.exec_()
        

def download_audio(u):
    try:
        yt = YouTube(u)
        audio = yt.streams.filter(only_audio=True).first()
        download_file = audio.download('Downloads')
        base, ext = os.path.splitext(download_file)

        new_file = base + '.mp3'
        os.rename(download_file, new_file)

        msg = createMsg('Info', 'Audio baixado com sucesso')
        msg.exec_()
    except:
        msg = createMsg('Error', 'Ocorreu um erro durante o processo de download :(. Verifique a URL e tente de novo')
        msg.exec_()
    