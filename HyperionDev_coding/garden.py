import spacy

nlp = spacy.load('en_core_web_sm')

gardenpathSentences = [
    "The man pushed through the door fell.",
    "Because he always jogs a mile seems a short distance to him.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("Sentence:", sentence)
    print("Tokens:")
    print([(token.text, token.pos_, token.ent_type_) for token in doc])
    print()

# the meaning of entities using spacy.explain
print(spacy.explain("PERSON"))  # Explanation for "PERSON" entity type
print(spacy.explain("GPE"))  # Explanation for "GPE" entity type

# Comment about the entities looked up:
'''
2 Entities Looked Up:
1. PERSON - Represents a person, including fictional characters.
   Explanation: The entity 'PERSON' represents individuals, including both real and fictional people. It helps to identify
   and categorize names of people in the text.

2. GPE - Represents Geopolitical Entity.
   Explanation: The entity 'GPE' stands for "Geopolitical Entity" and represents countries, cities, states, or other named
   geopolitical locations. It helps to identify and categorize these types of entities in text.

In terms of the words associated with the entities:
- The entity 'PERSON' correctly identifies the names "Mary" and "Jill" in the respective sentences, which align with the
  meaning of a person.
- The entity 'GPE' correctly identifies the word "Mississippi" in the sentence "The cotton clothing is made of grows in Mississippi,"
  which refers to a specific geopolitical entity (a state in the United States).'''