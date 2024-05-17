from pytube import YouTube

def download(ytlink: str):
    try:
        ytvid = YouTube(ytlink).streams
        ytname = ytvid.first().default_filename
        ytvid.get_highest_resolution().download("./temp/")

        return ytname
    except Exception as e:
        print("Ошибка при скачивании:", e)
        return "Exception"
