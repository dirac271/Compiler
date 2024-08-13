def tokinizer(text):
    text = text.lower()
    
    for char in [',','!',':',';']:
        text = text.replace(char,' ')
    
    tokens = text.split()

    return tokens


test_1 = input("Text the first line of the compiler\n")
tokens = tokinizer(test_1)
print(tokens)


