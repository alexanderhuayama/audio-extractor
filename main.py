from os import getenv
from dotenv import load_dotenv
from moviepy.editor import VideoFileClip


load_dotenv()


video_path = getenv('VIDEO_PATH')
audio_path = getenv('AUDIO_PATH')

video_audio = VideoFileClip(video_path).audio
video_audio.write_audiofile(audio_path)
