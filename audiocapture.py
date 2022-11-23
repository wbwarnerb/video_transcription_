import speech_recognition as sr
import moviepy.editor as mp
from videodownload import Video_Download

class Audio_Capture:

    def __init__(self, url):
        self.url = url
        self.vd = Video_Download
        self.download_and_convert_audio(url)

    def download_and_convert_audio(self, url):
        video_download = self.vd.get_video_stream(self, url)
        video_clip = mp.VideoFileClip(video_download)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile("output.wav")
        audio_clip.close()
        video_clip.close()
        self.speech_to_text()

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.AudioFile("output.wav") as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            print(text)

ac = Audio_Capture("https://youtu.be/LiKDDw7NH04")
