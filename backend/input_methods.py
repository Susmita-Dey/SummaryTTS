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
def youtube(a):
    try:
        def get_filepath( path ) -> str:
            path2 = ''
            for i in range(len(path)):
                if path[i].isalnum() or path[i] ==' ':
                    path2 += str(path[i])
            return path2 + '.mp4'

        save_path = '/downloads'

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

        text = text_file['text']

    except: 
        raise AssertionError('Enter valid YouTube link only')
    else:
        pass
    return text



#  File upload method

def get_file_extension(filename):
    return os.path.splitext(filename)[1]
'''
file = request.files['file']
filename = file.filename
extension = get_file_extension(filename)
'''

# 2. Text file method
def text_file(file):
    text = file.read()
    return text

# 3. PDF method
def pdf(FILE_PATH):
    #FILE_PATH = request.files['file']
    def extract_text_from_pdf(file_path):
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ''
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
        return text
    
    text = extract_text_from_pdf(FILE_PATH)
    '''
    file = request.files['file']
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in range(pdf_reader.pages()):
        text += pdf_reader.getPage(page).extractText()
        '''
    return text
#4. Audio files

def audio(file):
    model = whisper.load_model("tiny")
    text= model.transcribe( file )
    return text