"""# GPT summarizer"""

import re
import openai
from braille import textToBraille as convertText

# Set up the OpenAI API credentials
openai.api_key = "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"


# Define a function to summarize the text using GPT-3

def davinci(text):

    # Preprocess the input text to remove any extra line breaks or whitespace
    text = re.sub('\n+', '\n', text)
    text = text.strip()

    # Use the OpenAI GPT-3 API to summarize the text
    prompt = "You are a text summarizer that summarizes text from videos, audio clips and books. Provide a text summary in respective length of the text.Let the summary be in bullet points where ever necessary. Here's the text:\n\n" + text
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=512,
        temperature=0.5,
        n = 1,
        stop=None,
        timeout=20
    )
    # Extract the summary from the API response
    summary = response.choices[0].text.strip()

    return summary

def gpt( text ):

    # Preprocess the input text to remove any extra line breaks or whitespace
    text = re.sub('\n+', '\n', text)
    text = text.strip()

    # Use OpenAI gpt 3.5 turbo to summarize the text
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages =[
            {'role': 'system', 'content': "You are a text summarizer that summarizes text from videos, audio clips and books. Provide a text summary in respective length of the text. Let the summary be in bullet points where ever necessary. Here's the text"},
            {'role' : 'system', 'content' : text}
        ]
    )
            

    # Extract the summary from the API response
    summary = response['choices'][0]['message']['content'].strip()

    return summary
