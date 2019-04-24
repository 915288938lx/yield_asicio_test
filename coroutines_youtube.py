def corou(text):
    while True:
        input_search = yield
        if input_search in text:
            print('yes "%s" it is in it!'%input_search)
        else:
            print('better lucky next time, because "%s" is not in text'%input_search)


x = corou('i come from china , not america, not england')
next(x)
x.send('i')
x.send('come')
x.send('not')
x.send('is')
x.send('b')


