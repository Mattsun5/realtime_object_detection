import fitz
from gtts import gTTS
from playsound import playsound

# pip install pymupdf
# pip install fitz
def speech(text):
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)

    output.save("./sounds/audio.mp3")
    playsound("./sounds/audio.mp3")
doc = fitz.open('./test.pdf')

text = ""
for page in doc:
   text+=page.get_text()
print(text)
speech(text)