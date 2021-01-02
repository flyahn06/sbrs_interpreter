c = 0
with open("first.sbrs", 'w') as f:
    for letter in "Hello, world!\n":
        if c < ord(letter):
            for _ in range(ord(letter) - c):
                f.write("sa\n")
            f.write("ru\n")
            c = ord(letter)
        elif c > ord(letter):
            for _ in range(c - ord(letter)):
                f.write("bi\n")
            f.write("ru\n")
            c = ord(letter)

        else:
            f.write("ru\n")