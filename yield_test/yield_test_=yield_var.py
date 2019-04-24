def averager():
    total = 0
    count = 0
    average = None
    while True:
        term = yield average
        print(term)
        total += term
        count += 1
        average = total/count

coro_avg = averager()
next(coro_avg)
print(coro_avg.send(10))
print(coro_avg.send(20))
print(coro_avg.send(30))
print(coro_avg.send(100))
print(coro_avg.send(50))
#print(coro_avg.send('spam'))

