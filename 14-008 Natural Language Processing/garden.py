# Program to perform NLP/ NER on garden path sentences

import os
os.system('cls||clear')

import spacy
nlp = spacy.load('en_core_web_md')

# Create the list to store garden path sentences
gardenpathSentences = ['The man who hunts ducks out on weekends.',
                    'When Fred eats food gets thrown.']

# Create another list for 3 additioal sentences
list_another = ['Mary gave the child a Band-Aid.',      
                        'That Jill is never here hurts.',
                        'The cotton clothing is made of grows in Mississippi.']

gardenpathSentences = gardenpathSentences + list_another  # add additional sentences to first list 

for sentence in gardenpathSentences:    # Run NLP on each sentence in the list 
    doc = nlp(sentence)
    for ent in doc.ents:                # Perform NER on each sentence
        print(f"{ent.text:{15}} {ent.label_}")  # Print words and associated named entities

print(f"\nORG: {spacy.explain('ORG')}")   # Explain the two entities
print(f"GPE: {spacy.explain('GPE')}\n")

# ---- Questions ----- #
# What were the Entities you looked up
# Did the Entity make sense in terms of the word associated with it

# ---- Answers ----- #
# (1) ORG: Organisation i.e Companies, agencies, institutions. 
# No, the Entity ORG does not make much sense
# as Band-Aid is 'not' organisation but an object/thing

# (2) GPE: Geo-Political Entity such as Countries, cities, states
# Yes, the Entity GPE makes sense as Mississippi is a state in the USA.








