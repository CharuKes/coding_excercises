my_vowel = 'aeiou'
my_vowel1 = 'AEIOU'
user_input = input("Enter:")
for i in user_input:
    if i not in my_vowel and i not in my_vowel1:
        print(i, end='')
