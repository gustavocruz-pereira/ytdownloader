from pytube import YouTube
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QRadioButton, QMessageBox

def download_video(u) -> None:
    try:
        # Cria uma instância do YouTube com a URL fornecida
        yt = YouTube(u)

        video = yt.streams.filter(progressive=True, file_extension='mp4', mime_type='video/mp4').first()

        video.download()
        
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("O vídeo foi baixado com sucesso!")
        msgBox.exec_()
    except:
        print("Ocorreu um erro durante o processo de download :(")
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Ocorreu um erro durante o processo de download :(")
        msgBox.exec_()

    


    