# delete text inside of parenthases
# split data by sentence
# split data by new line

import os
import csv
import re

input_folders = ['./raw_data/papers', './raw_data/paragraphs']
output_file = 'sentences.csv'

with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(['Sentences'])
    
    for folder in input_folders:
        for filename in os.listdir(folder):
            if filename.endswith('.txt'): 
                file_path = os.path.join(folder, filename)

                with open(file_path, 'r') as f:
                    text = f.read()
                    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)

                    for sentence in sentences:
                        sentence = re.sub(r'\([^)]*\)', '', sentence)
                        if sentence:
                            csvwriter.writerow([sentence])

print('Extracted sentences saved to:', output_file)

output_file = 'paragraphs.csv'

with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(['Paragraphs'])

    for folder in input_folders:
        for filename in os.listdir(folder):
            if filename.endswith('.txt'):
                file_path = os.path.join(folder, filename)

                with open(file_path, 'r') as f:
                    lines = f.readlines()

                    for line in lines:
                        paragraph = line.strip()
                        paragraph = re.sub(r'\([^)]*\)', '', paragraph)
                        csvwriter.writerow([paragraph])

print('Extracted paragraphs saved to:', output_file)

# make corresponding data for each data point
# ask chatgpt for alternating styles (simple, funny, bullet points, elif, )