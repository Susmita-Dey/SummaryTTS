from pytube import YouTube
import PyPDF2
import whisper
from flask import Flask, request, jsonify
import os


app = Flask(__name__)

"""# Different Input methods

The program can take in in file formats of `txt`,`pdf`,`mp3`, `mp4`, `mpeg`, `mpga`,`m4a`,`wav` and `webm`.
"""

# 1. YouTube links

# formats the file path for YouTube links

try:
    @app.route('/youtube', methods=['POST'])
    def get_filepath( path ) -> str:
        path2 = ''
        for i in range(len(path)):
            if path[i].isalnum() or path[i] ==' ':
                path2 += str(path[i])
        return path2 + '.mp4'

    save_path =

    url = request.form.get('url') # get the YouTube URL from the frontend
    # download the video using the code you already have
    
    yt = YouTube(url)
    mp4 = yt.streams.get_highest_resolution()
    mp4.download(save_path)
    v_title = get_filepath(mp4.title)

    # get the absolute path of the downloaded video
    filepath = os.path.abspath(v_title) 

    # Transcribe the audio file
    model = whisper.load_model("tiny")
    text_file = model.transcribe( v_title )

    with open('text.txt','w') as f:
        f.writelines(text_file['text'])

except: 
    raise AssertionError('Enter valid YouTube link only')
else:
    pass




# 2. File upload method
@app.route('/upload', method = ['POST'])
def get_file_extension(filename):
    return os.path.splitext(filename)[1]

file = request.files['file']
filename = file.filename
extension = get_file_extension(filename)



# 3. PDF method
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

FILE_PATH = ""
text_file = extract_text_from_pdf(FILE_PATH)

with open('text.txt','w') as f:
  f.writelines(text_file)

#4. Text files

FILE_PATH = ""

with open( FILE_PATH , 'r' ) as f:
  text = f.read()

with open ( 'text.txt', 'w') as f:
  f.writelines()