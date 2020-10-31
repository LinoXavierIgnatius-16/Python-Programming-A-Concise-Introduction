import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    L = []
    random.seed(70)
    for n in range(0,10):
        L.append(random.random()*5 + 30)
    print(L)
