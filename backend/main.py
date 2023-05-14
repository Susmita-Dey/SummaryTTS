import input_methods as im
from summarizer import gpt
from braille import textToBraille as convertText
from gtts import gTTS as speak
from flask import Flask, request, send_file, jsonify
import os

app = Flask(__name__)

@app.route('/youtube', methods = ['POST'])
def adf():
    pass
file = request.files['file']
text = im.youtube(file)

summary = gpt (text)    

@app.route('/upload', methods = ['POST'])
def get_file_extension(filename):
    return os.path.splitext(filename)[1]

file = request.files['file']
filename = file.filename
extension = get_file_extension(filename)
try:
    if extension == '.pdf':
        text = im.pdf(file)
    elif extension == '.txt':
        text = im.text_file(file)
    else:
        text = im.audio(file)
    summary = gpt (text)
except:
    raise Exception('Something wrong happened during the text extraction from file')

@app.route('/summary', methods=['POST'])
def summarize(text):
    
    # convert summary to braille format
    braille_summary = convertText(summary)
    
    # generate audio summary
    text = text.lower().strip()
    audio = speak(summary,lang='en',tld='us')
    audio.save('audio-summary.mp3')
    audio_summary_path = os.path.abspath('audio-summary.mp3')
    
    # return summary in different formats
    return jsonify({
        'text_summary': text,
        'braille_summary': braille_summary,
        'audio_summary': audio_summary_path
    })
summarize ( summary )

if __name__ == '__main__':
    app.run()

