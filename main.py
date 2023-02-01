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


label = QLabel('Digite uma url', parent=window)
label.move(20, 20)

textbox = QLineEdit("Url aqui.", parent=window)
textbox.setGeometry(20, 50, 310, 30)
textbox.move(20, 50)

button = QPushButton('Baixar', parent=window)
button.setGeometry(20, 50, 310, 30)
button.move(20, 85)                     #9ACD32 #ADFF2F
button.setStyleSheet("background-color: #ADFF2F;")

lbl_ext_opts = QLabel('Selecione a extensão deseja baixar:', parent=window)
lbl_ext_opts.setGeometry(20, 120, 310, 30)
lbl_ext_opts.move(20, 120)

mp3_radiobtn = QRadioButton(".MP3", parent=window)
mp3_radiobtn.move(20, 150)
mp4_radiobtn = QRadioButton(".MP4", parent=window)
mp4_radiobtn.move(20, 175)
mp4_radiobtn.setChecked(True)


button.clicked.connect(clicked_btn)


if __name__ == '__main__':
    window.show()
    sys.exit(app.exec_())

    