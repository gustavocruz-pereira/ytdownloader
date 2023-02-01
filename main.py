import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QRadioButton
from ytdownload import download_video, download_audio

def clicked_btn():
    url = textbox.text()
    if mp4_radiobtn.isChecked():
        download_video(url)
    elif mp3_radiobtn.isChecked():
        download_audio(url)


app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle('Youtube Downloader')
window.setFixedSize(350, 300)


label = QLabel('Digite uma url:', parent=window)
label.move(20, 20)

mp3_radiobtn = QRadioButton(".MP3", parent=window)
mp3_radiobtn.move(20, 60)
mp4_radiobtn = QRadioButton(".MP4", parent=window)
mp4_radiobtn.move(20, 85)
mp4_radiobtn.setChecked(True)

textbox = QLineEdit("Url aqui.", parent=window)
textbox.move(130, 20)

button = QPushButton('Baixar', parent=window)
button.move(230, 20)


button.clicked.connect(clicked_btn)


if __name__ == '__main__':
    window.show()
    sys.exit(app.exec_())

    