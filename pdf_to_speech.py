from pypdf import PdfReader
from gtts import gTTS

import os

language = 'en'

reader = PdfReader('Enter the path of the PDF file here')

text = ''

for page in reader.pages:
    text += page.extract_text()
    
tts = gTTS(text=text, lang=language, slow=False)

tts.save('example.mp3')
os.system('start example.mp3')