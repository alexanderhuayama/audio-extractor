from os import getenv
from dotenv import load_dotenv
from pydub import AudioSegment


load_dotenv()

audio_path = getenv('AUDIO_PATH')
audio_path_short = getenv('AUDIO_PATH_SHORT')
audio_start_time_sec = int(getenv('AUDIO_START_TIME_SEC'))
audio_end_time_sec = int(getenv('AUDIO_END_TIME_SEC'))


def seconds_to_ms(seconds):
    return seconds * 1000

audio = AudioSegment.from_file(audio_path, "mp3")
start_time_ms = seconds_to_ms(audio_start_time_sec)
end_time_ms = seconds_to_ms(audio_end_time_sec)
audio_fragment = audio[start_time_ms:end_time_ms]
audio_fragment.export(audio_path_short, format='mp3')
