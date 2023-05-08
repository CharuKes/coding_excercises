def main(input):
    return count_nine(input)

def count_nine(input):
    a = [i for i in range(1, (input+1))]
    b = str(a).replace(', ', '')
    count_9 = b.count('9')
    return count_9

print(main(100))
print(main(98))