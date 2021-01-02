import sys
commandset = ['kkal', 'kki', 'kkol']
commanddis = {
    "kkal": "parameter-2|callable",
    "kki": "parameter-2|callable",
    "kkol": "callable"
}

def kkal(f, t):
    return 0, f

def kki(f, t):
    return f, f+t

def kkol():
    sys.exit()
