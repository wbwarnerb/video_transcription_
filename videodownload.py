from pytube import YouTube


class Video_Download:

    def __init__(self, url):
        self.url = url
        # self.ac = Audio_Capture()
        # self.get_video_stream(url)

    def get_video_stream(self, url):
        YouTube(url).streams.first().download()
        yt = YouTube(url)
        file = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        return(file)

# vd = Video_Download("https://youtu.be/9bZkp7q19f0")
