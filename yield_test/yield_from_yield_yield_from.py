# BEGIN YIELD_FROM_AVERAGER
from collections import namedtuple
import time
Result = namedtuple('Result', 'count average')


# the subgenerator
def averager():  # <1> 虽说没有往这个函数里传入参数, 但是yield关键字能够接收外面传进的参数
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield  # <2>
        if term is None:  # <3>
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)  # <4>


# the delegating generator
def grouper(results, key):  # <5>
    while True:  # <6>
        results[key] = yield from averager()  # <7> 接受协程返回的namedtuple, 作为管道接收子生成器averager()return的值, 每次都能执行到这里, 但最终四次接收协程返回的值


# the client code, a.k.a. the caller
def main(data):  # <8>
    results = {}
    for key, values in data.items():
        group = grouper(results, key)  # <9>
        next(group)  # <10>
        for value in values:
            group.send(value)  # <11>
        group.send(None)  # important! <12> 为什么这句重要, 是因为发送完None之后, averager()可以跳出while true循环

    # print(results)  # uncomment to debug
    report(results)


# output report
def report(results):
    print(results)
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
              result.count, group, result.average, unit))


data = {
    'girls;kg':
        [40.9, 38.5,56,53 ],
    'girls;m':
        [1.6, 1.51,1.6,1.8 ],
    'boys;kg':
        [39.0, 40.8,45,37 ],
    'boys;m':
        [1.38, 1.5,1.2,1.6 ],
}


if __name__ == '__main__':
    start = time.clock()
    main(data)

    print( time.clock()-start)
# END YIELD_FROM_AVERAGER
#
# ri = namedtuple('test','kkk')
# di = {}
# di['a']='kk'
# di
