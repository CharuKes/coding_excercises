'''This code supports vocabulary learning and word manipulation tasks by providing functions to add the prefix "un" to 
words, create word groups with different prefixes, remove the "ness" suffix from words, and transform adjectives into
verbs. The code includes test cases to validate the expected outputs. It serves as a tool for English homework,
helping little sister's to understand word formation and practice applying prefixes and suffixes.'''


# Task 1: Add a prefix to a word
def add_prefix_un(word):
    # Concatenate 'un' prefix with the word
    return 'un' + word


# Task 2: Add prefixes to word groups
def make_word_groups(vocab_words):
    # Extract the prefix from the first word in the list
    prefix = vocab_words.pop(0)  # Used pop to remove and store the first word in the list

    # Add the prefix to each word in the list using a list comprehension
    prefixed_words = [prefix + word for word in vocab_words]

    # Join the prefixed words using ' :: ' as the separator
    return ' :: '.join([prefix] + prefixed_words)


# Task 3: Remove a suffix from a word
def remove_suffix_ness(word):
    if word.endswith('iness'):
        # Used endswith, if the word ends with 'iness', remove 'iness' and add 'y'
        return word[:-5] + 'y'
    elif word.endswith('ness'):
        # If the word ends with 'ness', remove 'ness'
        return word[:-4]


# Task 4: Extract and transform a word
def adjective_to_verb(sentence, index):
    # Split the sentence into individual words
    words = sentence.split()

    # Extract the adjective at the specified index
    adjective = words[index].strip('.,')  # Remove leading and trailing punctuation

    # Add 'en' suffix to transform the adjective into a verb
    return adjective + 'en'


# Test Task 1: Add a prefix to a word
print("'" + add_prefix_un("happy") + "'")  # Output: 'unhappy'
print("'" + add_prefix_un("manageable") + "'")  # Output: 'unmanageable'

# Test Task 2: Add prefixes to word groups
print("'" + make_word_groups(['en', 'close', 'joy', 'lighten']) + "'")  # Output: 'en :: enclose :: enjoy :: enlighten'
print("'" + make_word_groups(['pre', 'serve', 'dispose', 'position']) + "'")  # Output: 'pre :: preserve :: predispose :: preposition'
print("'" + make_word_groups(['auto', 'didactic', 'graph', 'mate']) + "'")  # Output: 'auto :: autodidactic :: autograph :: automate'
print("'" + make_word_groups(['inter', 'twine', 'connected', 'dependent']) + "'")  # Output: 'inter :: intertwine :: interconnected :: interdependent'

# Test Task 3: Remove a suffix from a word
print("'" + remove_suffix_ness("heaviness") + "'")  # Output: 'heavy'
print("'" + remove_suffix_ness("sadness") + "'")  # Output: 'sad'

# Test Task 4: Extract and transform a word
print("'" + adjective_to_verb('I need to make that bright.', -1) + "'")  # Output: 'brighten'
print("'" + adjective_to_verb('It got dark as the sun set.', 2) + "'")  # Output: 'darken'
