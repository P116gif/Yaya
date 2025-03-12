from pydub import AudioSegment
from pydub.playback import play
import io
import gtts
from pydub.utils  import which

# Manually set FFmpeg path
AudioSegment.converter = 
print(which("ffmpeg"))
def text_to_speech(text):
    tts = gtts.gTTS(text=text, lang='en', slow=False)

    # Store MP3 in memory
    buffer = io.BytesIO()
    tts.write_to_fp(buffer)
    buffer.seek(0)

    # Convert MP3 to WAV and play it
    audio = AudioSegment.from_file(buffer, format="mp3")
    play(audio)

text_to_speech("Hello! FFmpeg is now working!")
