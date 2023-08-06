import csv
import openai

openai.api_key = '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'

with open('paragraphs.csv', 'r') as file:
    reader = csv.reader(file)
    paragraphs = list(reader)

with open('trans_paragraphs.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    
    writer.writerow(['Paragraphs', 'Translation - Simple'])
    
    for paragraph in paragraphs[1:2]:
        original = paragraph[0]

        prompt = f"Please rephrase this paragraph in simpler terms: {original}"

        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
        )

        simple = response["choices"][0]["text"]
        
        row = [original, simple]
        writer.writerow(row)

print("CSV generated with translations")