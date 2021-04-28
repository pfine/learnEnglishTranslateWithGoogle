import os
from gtts import gTTS

text = 'Your sentence requiring text to speech'
file_path = 'text.mp3'

while not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(file_path)
    except Exception as e:
        print(e.message)