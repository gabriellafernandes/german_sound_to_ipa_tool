import pandas as pd

# Dataset transformation into pandas format from https://frequencylists.blogspot.com/2015/12/the-2000-most-frequent-german-nouns.html
with open('most_used_german_words.txt', 'r', encoding='utf-8') as file: lines = file.readlines()

data = []
for line in lines:
    parts = line.strip().split('\t')
    parts[0] = parts[0].split('. ', 1)[1]
    data.append(parts)

# Create DataFrame
df = pd.DataFrame(data, columns=['English', 'German_Singular', 'German_Plural'])

df.to_csv('german_words_dataset.csv', index=True)