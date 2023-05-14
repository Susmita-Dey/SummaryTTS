from summarizer import gpt
from braille import textToBraille as convertText
from gtts.tts import gTTS as speak


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

from flask import Flask, request, jsonify, send_file
import io

app = Flask(__name__)

# Function to convert text to Braille format
def convert_to_braille(text):
    # Your code to convert text to Braille format
    pass

@app.route('/summarize', methods=['POST'])
def summarize():
    # Get the uploaded file
    file = request.files['file']
    
    # Extract the text from the file
    text = extract_text(file)
    
    # Summarize the text
    summary = summarize_text(text)
    
    # Convert summary to Braille format if requested
    if request.form.get('braille'):
        b_summary = convert_to_braille(summary)
        braille_file = io.BytesIO(b_summary.encode())
        braille_file.seek(0)
        return send_file(braille_file, mimetype='text/plain',
                         as_attachment=True, attachment_filename='braille-summary.txt')
    
    # Return the summary as plain text
    return summary

if __name__ == '__main__':
    app.run()
