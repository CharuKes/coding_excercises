vowel = "aeiouAEIOU"
def shortcut(a):
    output_str = ""
    for i in a:
        if i not in vowel:
            output_str += i
    return (output_str)
print(shortcut("Hello"))
print(shortcut("Masterschool"))
print(shortcut("PythOn"))
