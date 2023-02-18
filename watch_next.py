import spacy

nlp = spacy.load("en_core_web_md")

# Provide the planet_hulk description within a list 
planet_hulk = ["Will he save their world or destroy it? When the hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."]

# Create function that opens the movies.txt file and loops over it, then loop through the planet_hulk description and compares the similarities of the 2. Use an if statement to find the highest value and return that value. 
def movie_next(desc):
    
    file = open("movies.txt", "r").readlines()
    
    for item in file:   
        films = item.strip()
        films = nlp(films)
   
        for token_ in planet_hulk:  
            token_ = nlp(token_)
            compare = films.similarity(token_)
            if compare >= 0.877:
                return films[:2]
        
final_film = movie_next(planet_hulk)

print(f"The film title that best correlates with Planet Hulk is {final_film}")       

