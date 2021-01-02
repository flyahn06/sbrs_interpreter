commandset = ['ju', 'sae', 'no', 'bo']
commanddis = {
    "ju": "callable",
    "sae": "callable",
    "no": "callable",
    "bo": "stack"
}
bo = 0

def ju():
    global bo
    bo += 1

def sae():
    global bo
    bo -= 1

def no():
    print(chr(bo), end="")
