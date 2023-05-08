def is_palindrome(word):
    a = word.lower().replace(" ", "")
    for i in a:
        if a[0:] == a[::-1]:
            return True
        else:
            return False

print(is_palindrome("Hello"))
print(is_palindrome("racecar"))
print(is_palindrome("raCecar"))