import time
from random import randint
data = 0
def a():
    # sent_value = 0
    while True:
        print('-----A-----')



        data = yield

        print(data)




        time.sleep(0.5)

def b(c):
    while True:
        print('-----B-----')
        next(c)
        c.send(randint(1,9))
        time.sleep(0.5)

if __name__ == '__main__':

    x = a()
    b(x)