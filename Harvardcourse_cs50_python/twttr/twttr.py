def main():
    user_input = input("Enter a string: ")
    print(shorten(user_input))

def shorten(word):
    my_vowel = 'aieou'
    my_vowel1 = 'AIEOU'
    output_str = ''
    for i in word:
        if i not in my_vowel and i not in my_vowel1:
            output_str += i
    return output_str

if __name__ == "__main__":
    main()