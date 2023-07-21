import spacy

# Load the language model
nlp = spacy.load('en_core_web_md')


def get_most_similar_movie(description):
    # Read movie descriptions from the file
    movie_list = []
    with open('movies.txt', 'r') as file:
        movie_list = file.read().splitlines()

    # Calculate similarity scores
    similarity_scores = []
    for movie_description in movie_list:
        similarity_scores.append(nlp(movie_description).similarity(nlp(description)))

    # Find the index of the most similar movie
    most_similar_index = similarity_scores.index(max(similarity_scores))

    # Return the title of the most similar movie
    return movie_list[most_similar_index]


# Test the function
description = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the 
                 Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
                 planet where the Hulk can live in peace. Unfortunately, Hulk lands on the
                 planet Sakaar where he is sold into slavery and trained as a gladiator."""

recommended_movie = get_most_similar_movie(description)
print("The movie you should watch next is:", recommended_movie)