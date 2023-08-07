import csv
import openai
import tiktoken

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

with open('paragraphs.csv', 'r') as file:
    reader = csv.reader(file)
    paragraphs = list(reader)
    
max_len = -1
index = -1
for i, item in enumerate(paragraphs):
    if (len(encoding.encode(item[0])) > max_len):
        index = i
        max_len = len(item[0])

print(paragraphs[index])
print(max_len)

style = 'bulleted'

with open(f'./trans_paragraphs_{style}.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    
    writer.writerow(['Paragraphs', style.title()])
    
    for paragraph in paragraphs[1:]:
        original = paragraph[0]

        prompts = {
            "Simple": f"Please rephrase this paragraph in simple language: {original}", 
            "Bulleted": f"Please convert this paragraph to bulletpoints: {original}",
            "Reworded": f"Please reword this paragraph: {original}"
        }

        prompt = prompts[style.title()]
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                      {"role": "user", "content": prompt}
            ],
        )

        translated = response["choices"][0]["message"]["content"]
        
        row = [original, translated]
        writer.writerow(row)

print("CSV generated with translations")
print(len(paragraphs))