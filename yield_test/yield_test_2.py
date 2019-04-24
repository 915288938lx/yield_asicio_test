def coru2(a):
    print(a)
    b = yield a
    print(b)
    c = yield a + b
    d = a+b
    print(d)
    print(c)


my_coru2 = coru2(14)
next(my_coru2)
my_coru2.send(28)
my_coru2.send(99)