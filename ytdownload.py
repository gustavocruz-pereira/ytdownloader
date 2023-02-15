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
    elif type == 'Warn':
        msg.setIcon(QMessageBox.Warning)
        msg.setText(text)
        return msg

def download_progress():
    msg = createMsg('Warn', 'Aguarde, download em andamento!')
    msg.exec_()


def download_video(u) -> None:
    try:
        # Cria uma instância do YouTube com a URL fornecida
        yt = YouTube(u, on_progress_callback=download_progress())
        video = yt.streams.filter(progressive=True, file_extension='mp4', mime_type='video/mp4').first()
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        video.download(downloads_path)
        
        msg = createMsg('Info', 'Video baixado com sucesso na pasta "Downloads"')
        msg.exec_()

    except Exception as e:
        print("Ocorreu um erro durante o processo de download :(")
        msg = createMsg('Error', f'Ocorreu um erro durante o processo de download :(. Verifique a URL e tente de novo. {e}')
        msg.exec_()
        

def download_audio(u):
    try:
        yt = YouTube(u)
        audio = yt.streams.filter(only_audio=True).first()
        download_file = audio.download(on_progress_callback=download_progress)
        base, ext = os.path.splitext(download_file)

        new_file = base + '.mp3'
        os.rename(download_file, new_file)

        msg = createMsg('Info', 'Audio baixado com sucesso na pasta "Downloads"')
        msg.exec_()
    except:
        msg = createMsg('Error', 'Ocorreu um erro durante o processo de download :(. Verifique a URL e tente de novo')
        msg.exec_()
    