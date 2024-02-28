# Program to build movie recommendation system using NLP

import os
os.system('cls||clear')

# Load movies text file
import pandas as pd
#Create a dataframe to store movie title, description and similarity scores
df = pd.read_csv('movies.txt', sep=' :', engine='python',
                 names=["Movies", "Description", "Similarity_Score"])

# Load spacy
import spacy
nlp = spacy.load('en_core_web_md')

# Function to recommend a movie based on watched movie
def rec_engine(movie_description, data):
    for index in range(len(data)):      #Tokenise every description in the daraframe
        doc = nlp(data['Description'][index])
        #Score similarity score in for each movie in the dataframe 
        df['Similarity_Score'][index] = nlp(movie_description).similarity(doc)
        print(f"\nHere are the similarity scores:\n {data}")    #Print all movies and respective scores

    max_similarity_score = max(df['Similarity_Score'])
    recommended_movie = df[df['Similarity_Score'] == max_similarity_score] #Find the movie with max. score
    # return recommended_movie[['Movies','Description']]
    return recommended_movie.iloc[0,0], recommended_movie.iloc[0,1] #Return movie and description
    
# Provide input for the watched movie and call the function
movie_watched = 'Planet Hulk'
movie_watched_description = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land son the planet Sakaar where he is sold into slavery and trained as a gladiator.'
rec_movie_title, rec_movie_decription = rec_engine(movie_watched_description, df)  #Call Function
print(f"\n\nYour movie recommendation is:\n{rec_movie_title} -> {rec_movie_decription}\n\n")