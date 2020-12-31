commandset = ['sa', 'bi', 'ru', 'saa']
saa = 0

def sa():
    global saa
    saa += 1

def bi():
    global saa
    saa -= 1

def ru():
    global saa
    print(chr(saa), end="")
