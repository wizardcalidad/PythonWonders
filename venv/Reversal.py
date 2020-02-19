text = input("The string to reverse: ")
def rev(text):
    if len(text)== 1:
        return text
    else:
        return rev(text[1:]) + text[0]
print(rev(text))