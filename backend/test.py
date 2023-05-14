import os


def get_file_extension(filename):
    return os.path.splitext(filename)[1]
a = 'C:/Users/Bharadwaj/Source/Repos/MLH-AI-Hackathon/backend/ehllo.txt'
with open (a, 'r') as f:
    text = f.read()

print(text)