from summarizer import gpt
from braille import textToBraille as convertText
from gtts.tts import gTTS as speak
import os

# Read in the TEXT FILE
with open("text.txt", "r") as f:
    text = f.read()

# SUMMARIZE

summary = gpt(text)

# TEXT FORMAT
with open ('summary.txt','w') as f:
  f.writelines(summary)

# BRAILLE FORMAT
b_summary = convertText(summary)

with open ('braille-summary.txt', 'w') as f:
  f.writelines(b_summary)

# AUDIO FORMAT
au_ac = input ( 
    "Enter the accent you the auio to be in: \nus - United States \nuk - United Kindom \nin - Indian\n"
    ).lower().strip()

if au_ac == 'us':
  audio = speak(summary,lang='en',tld='us')
elif au_ac == 'uk':
  audio = speak(summary,lang='en',tld='co.uk')
else:
  audio = speak(summary,lang='en',tld='co.in')
audio.save('audio-summary.mp3')
