import sys
commandset = ['kkal', 'kki', 'kkol']

def kkal(f, t):
    return 0, f

def kki(f, t):
    return f, f+t

def kkol():
    sys.exit()
