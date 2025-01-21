import utils
import spacy
import json

# Load the SpaCy German model
nlp = spacy.load("de_core_news_sm")

# Load the raw dataset
raw_data = utils.load_dataset_file('data/Phonexi-2014T/labels.train')

# Initialize a dictionary to store word-to-POS mappings
data_dict = {}

# Iterate through the dataset
for key, value in raw_data.items():
    sentence = value['text']
    # Process the sentence using SpaCy
    doc = nlp(sentence)
    for token in doc:
        if token.pos_ == "VERB":
            data_dict[token.text] = "VERB"
        elif token.pos_ == "NOUN":
            data_dict[token.text] = "NOUN"
        elif token.pos_ == "PROPN":
            data_dict[token.text] = "PROPN"

# Print the dictionary for verification
print(data_dict)

# Write the dictionary to a JSON file
with open('word_to_pos.json', 'w', encoding='utf-8') as f:
    json.dump(data_dict, f, ensure_ascii=False, indent=4)

print("JSON file 'word_to_pos.json' has been written successfully.")
