import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QRadioButton, QMessageBox
#from pytube import YouTube
from ytdownload import download_video



def clicked_btn():
    url = textbox.text()
    download_video(url)

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle('Janela de exemplo')
window.setFixedSize(500, 300)


label = QLabel('Digite uma url:', parent=window)
label.move(20, 20)

mp3_radiobtn = QRadioButton(".MP3", parent=window)
mp3_radiobtn.move(20, 60)
mp4_radiobtn = QRadioButton(".MP4", parent=window)
mp4_radiobtn.move(20, 85)
mp4_radiobtn.setChecked(True)

textbox = QLineEdit("Url aqui.", parent=window)
textbox.move(130, 20)

button = QPushButton('OK', parent=window)
button.move(230, 20)
 

button.clicked.connect(clicked_btn)


if __name__ == '__main__':
    window.show()
    sys.exit(app.exec_())

    