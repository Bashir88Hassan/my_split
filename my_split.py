text = input("enter the text: ")
delimiter = input("enter the delimiter: ")
word = []
words = []


def my_split():
    # text to array
    for n in text:
        word.append(n)

    # clere text
    r = ""
    for n in word:
        if n != delimiter:
            r = r + n
        elif n == delimiter:
            if r == "":
                continue
            words.append(r)
            r = ""
    print("words:/n", words)


my_split()
