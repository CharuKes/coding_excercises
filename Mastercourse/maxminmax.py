def main(input):
    return max_min_max(input)

def max_min_max(a):
    largest = max(a)
    smallest = min(a)
    maximum_absent = max(a)-1
    return [largest, maximum_absent, smallest]

print(main([-6, 2, 8, -21, 300]))
print(main([3, 3, -8, -2, 8, -1]))