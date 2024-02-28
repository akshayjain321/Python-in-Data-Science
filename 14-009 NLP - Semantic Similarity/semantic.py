# Program to perform semantic similarity using spaCy

import os
os.system('cls||clear')

import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(f"\nSimilarity between {word1} and {word2} is {word1.similarity(word2)}")
print(f"Similarity between {word3} and {word2} is {word3.similarity(word2)}")
print(f"Similarity between {word3} and {word1} is {word3.similarity(word1)}\n")

# Observations
# 1. Greater similarity between cat &  monkey as both are animals
# 2. Some similarity between banana & monkey as monkey eats banana
# 3. Least similairty between banana and cat as cat does not eat/like banana

# ------ Example of my own ------- #

word1 = nlp("Job")
word2 = nlp("Salary")
word3 = nlp("Morning")
print(f"\nSimilarity between {word1} and {word2} is {word1.similarity(word2)}")
print(f"Similarity between {word3} and {word2} is {word3.similarity(word2)}")
print(f"Similarity between {word3} and {word1} is {word3.similarity(word1)}\n")

# Observations
# 1. Greater similarity between Job and salary as both are related
# 2. No similarity between Morning and Salary as both are unrelated
# 3. Some (very less) similairty between Job and Morning as jobs usually start at Morning


# -------- Running rest of the code extracts in the pdf document ------- #
tokens = nlp('cat apple monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# -------- Running rest of the code extracts in the pdf document ------- #
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + "-" + str(similarity))