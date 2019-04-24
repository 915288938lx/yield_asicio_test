def corut():
    x = yield
    print(x)
    print('a')
    print('b')
    print('c')
    print('d')
    print('e')
my_coru = corut()
next(my_coru)
my_coru.send(43)
my_coru.send(20)
my_coru.send(96)
my_coru.send(489)
my_coru.send(4387)


def coru2(a):
    print(a)
    b = yield a
    print(b)
    c = yield a+b
    print(c)

my_coru2 = coru2(14)
next(my_coru2)
my_coru2.send(28)
my_coru2.send(99)
