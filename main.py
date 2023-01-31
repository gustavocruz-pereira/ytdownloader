import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QRadioButton
from pytube import YouTube


def clicked_btn():
    url = textbox.text()
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension='mp4', mime_type='video/mp4').first()
    label2 = QLabel("Carregando...")
    label2.move(100, 150)


app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle('Janela de exemplo')
window.setFixedSize(500, 300)


label = QLabel('Digite uma url:', parent=window)
label.move(20, 20)

textbox = QLineEdit("Url aqui.", parent=window)
textbox.move(130, 20)

button = QPushButton('OK', parent=window)
button.move(230, 20)
 

button.clicked.connect(clicked_btn)


if __name__ == '__main__':
    window.show()
    sys.exit(app.exec_())

    