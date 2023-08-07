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
    
# max_len = -1
# index = -1
# for i, item in enumerate(paragraphs):
#     if (len(encoding.encode(item[0])) > max_len):
#         index = i
#         max_len = len(item[0])

# print(paragraphs[index])
# print(max_len)

with open('trans_paragraphs.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    
    writer.writerow(['Paragraphs', 'Translation - Simple'])
    
    for paragraph in paragraphs[1:]:
        original = paragraph[0]

        prompt = f"Please rephrase this paragraph in simple language: {original}"
        
        max_tokens=16,300-len(encoding.encode(prompt))

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                      {"role": "user", "content": prompt}
            ],
        )

        simple = response["choices"][0]["message"]["content"]
        
        row = [original, simple]
        writer.writerow(row)

print("CSV generated with translations")