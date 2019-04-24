# def gen():
#     for c in 'ab':
#         yield c
#     for i in range(2,5):
#         yield i
#
# x = gen()
# for aa in x :
#     print(aa    )

a = range(2,9)
# print(a)
def gen2():
    yield from 'aaaasdfasdfasdfasdf'
    # yield from range(2,99) # yield from 函数 def range() : ***
    # print(y)


print(list(gen2()))
