from pytube import YouTube


def download_video(u) -> None:
    try:
        # Cria uma instância do YouTube com a URL fornecida
        yt = YouTube(u)

        video = yt.streams.filter(progressive=True, file_extension='mp4', mime_type='video/mp4').first()

        video.download()
        print("O vídeo foi baixado com sucesso!")
    except:
        print("Ocorreu um erro durante o processo de download :(")
    


    