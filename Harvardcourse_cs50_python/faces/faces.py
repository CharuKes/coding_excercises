def main():
    user_input = input("")
    return convert(user_input)
def convert(a):
    a = a.replace(':)','🙂')
    a = a.replace(':(','🙁')
    return a
print(main())