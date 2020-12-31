commandset = ['ju', 'sae', 'no', 'bo']
bo = 0

def ju():
    global bo
    bo += 1

def sae():
    global bo
    bo -= 1

def no():
    print(chr(bo))
