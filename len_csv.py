import csv

with open('sentences.csv', 'r') as file:
    reader = csv.reader(file)
    paragraphs = list(reader)
    
print(len(paragraphs))
