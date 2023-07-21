import spacy

nlp = spacy.load('en_core_web_md')
# Uncomment the line below and comment out the line above to use the 'en_core_web_sm' model
# nlp = spacy.load('en_core_web_sm')

# Create word objects for 'cat', 'monkey', 'banana', and 'jungle'
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("jungle")

# Calculate the similarity between the words using spaCy
similarity1 = nlp(word1).similarity(nlp(word2))
similarity2 = nlp(word3).similarity(nlp(word2))
similarity3 = nlp(word3).similarity(nlp(word1))
similarity4 = nlp(word4).similarity(nlp(word3))

# print the similarity scores between word pairs
print(f"Similarity between '{word1}' and '{word2}': {similarity1}")   # Similarity between 'cat' and 'monkey'
print(f"Similarity between '{word3}' and '{word2}': {similarity2}")   # Similarity between 'banana' and 'monkey'
print(f"Similarity between '{word3}' and '{word1}': {similarity3}")   # Similarity between 'banana' and 'cat'
print(f"Similarity between '{word4}' and '{word3}': {similarity3}")   # Similarity between 'jungle' and 'banana'

'''It's interesting to note that the words 'cat' and 'monkey' have a higher similarity compared to 'banana' and 'monkey'.
This is because 'cat' and 'monkey' both belong to the category of animals, while 'banana' is a fruit, which is a different
category. What's even more intriguing is that the word 'jungle' has a lower similarity with 'banana'. Even though we might
expect 'jungle' and 'banana' to be somewhat similar because they are associated with natural habitats and tropical regions,
the word embeddings show otherwise. This showcases how word embeddings can understand the subtle relationships between words 
based on how they are used in context. By looking at the surrounding words, the models can recognize and measure the connections
between words based on shared meanings or patterns of appearance. For example, if we compare the words 'car' and 'bicycle',
we would expect a lower similarity since they belong to different transportation categories. Similarly, the words 'hot' and
'cold' would have a lower similarity as they are antonyms. These examples demonstrate how word embeddings capture diverse
semantic relationships and can be applied in various natural language processing tasks such as information retrieval,
text classification, and recommendation systems.'''

# Create tokens from the input string 'cat monkey banana jungle'
tokens = nlp('cat monkey banana jungle')

# Iterate over each token and calculate and print the similarity with every other token
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

'''The main difference between the 'en_core_web_sm' and 'en_core_web_md' models is their size and capabilities. Here's a comparison:

Size: The 'en_core_web_sm' model is smaller in size compared to the 'en_core_web_md' model. It includes only the core vocabulary,
 syntax, and word vectors. On the other hand, the 'en_core_web_md' model is larger and includes more word vectors and more
 accurate similarity scores.

Speed: Due to its smaller size, the 'en_core_web_sm' model is faster to load and process than the 'en_core_web_md' model.

Accuracy: The 'en_core_web_md' model tends to provide more accurate similarity scores because it has larger word vectors
and captures more semantic information. The 'en_core_web_sm' model, being smaller, may not capture as much semantic detail
and could result in slightly less accurate similarity scores.

In summary, if you require more accurate similarity scores and have sufficient computational resources,
 it's recommended to use the 'en_core_web_md' model. However, if speed and efficiency are a priority, the 'en_core_web_sm' 
 model can be a good choice, even though the similarity scores might be slightly less accurate.'''

# Define the sentence to compare
sentence_to_compare = "Why is my cat on the car"

# Define the sentences to compare against
sentences = [
    "Where did my dog go",
    "Hello, there is my car",
    "I've lost my car in my car",
    "I'd like my boat back",
    "I will name my dog Diana",
]

# Calculate the similarities between the sentence and each sentence in the list using spaCy
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = model_sentence.similarity(nlp(sentence))
    print(f"Similarity between '{sentence}' and '{sentence_to_compare}': {similarity}")

# Add another example to compare using spaCy
example_sentence = "I love eating pizza"
example_sentences = [
    "I enjoy cooking pasta dishes",
    "I've been craving sushi lately",
    "I'd like to try a new dessert recipe",
    "I will order a burger for lunch",
]

# Calculate the similarities between the sentence and each sentence in the list using spaCy
model_sentence = nlp(example_sentence)

for sentence in example_sentences:
    similarity = model_sentence.similarity(nlp(sentence))
    print(f"Similarity between '{sentence}' and '{example_sentence}': {similarity}")


#AND

# Comparing word similarities and entity recognition between two language models

# Load the medium-sized language model
nlp_medium = spacy.load('en_core_web_md')

# Load the small-sized language model
nlp_small = spacy.load('en_core_web_sm')

# Text to analyze
text = "cat monkey banana jungle"

'''The interesting aspect about the similarities between the words "cat," "monkey," and "banana" is that they are all
recognized as nouns by spaCy's language models. Despite being distinct entities, the models correctly identify them 
as objects or things. This highlights the models' ability to understand the grammatical category of words and provide
accurate part-of-speech tags. This feature allows the models to capture the basic syntactic structure of sentences
and facilitate further linguistic analysis.It showcases the models' proficiency in identifying and categorizing common
 types of words, which is fundamental in natural language understanding tasks.'''

# Analyze text with the medium-sized language model
doc_medium = nlp_medium(text)
print("Medium-sized Language Model:")
for token in doc_medium:
    print(f"{token.text} | POS: {token.pos_} | Entity Type: {token.ent_type_}")

# Analyze text with the small-sized language model
doc_small = nlp_small(text)
print("\nSmall-sized Language Model:")
for token in doc_small:
    print(f"{token.text} | POS: {token.pos_} | Entity Type: {token.ent_type_}")

'''When comparing the outputs of the medium-sized language model and the small-sized language model, 
I noticed a difference in the entity recognition. The medium-sized model correctly identified "cat," "monkey," 
"banana" and "jungle" as proper nouns and assigned them the entity type "PERSON." However, the small-sized model did not 
assign any specific entity type to these words.This suggests that the medium-sized model has a more extensive
 knowledge base and is able to recognize and classify named entities more accurately.'''
