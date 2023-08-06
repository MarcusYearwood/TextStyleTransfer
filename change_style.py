import csv
import openai

import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("API_KEY")

with open('paragraphs.csv', 'r') as file:
    reader = csv.reader(file)
    paragraphs = list(reader)

with open('trans_paragraphs.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    
    writer.writerow(['Paragraphs', 'Translation - Simple'])
    
    for paragraph in paragraphs[1:3]:
        original = paragraph[0]

        prompt = f"Please rephrase this paragraph in simpler terms: {original}"

        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
        )

        simple = response["choices"][0]["text"]
        
        row = [original, simple]
        writer.writerow(row)

print("CSV generated with translations")