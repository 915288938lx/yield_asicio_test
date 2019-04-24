from collections import  namedtuple

Result = namedtuple('Result','count average')
def averager():
    total = 0
    count =0
    average = None
    while True:
        term = yield # 这里也可以写成yield average效果一样
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)

import time
start = time.clock()
coro_avg = averager()
next(coro_avg)
coro_avg.send(10)
coro_avg.send(33)
coro_avg.send(44)
try:
    coro_avg.send(None)
except StopIteration as st:
    result = st.value
    print(result)
elaped_time = time.clock()-start
print(elaped_time) #0.00005