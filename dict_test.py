a ={"ok":"sdfasd", "no":"88"}
print(a[0][0])
a = b'\xe9'
print(type(a))
a.decode('cp1252')
print(a)

open('cafe.txt','w',encoding='utf-8').write('café')
print(open('cafe.txt').read())



keys = ('a','b','c')
values = ('haode','no','thanks')

dic = {key:value for key in keys for value in values}
print(dic)
print(dic.get('w','ong'))


from collections import OrderedDict
with open('dd.txt') as fp:
    lines = fp.readlines()

    # print(lines)

enu = enumerate(lines,1)
# print(list(enu))
orderd = OrderedDict(enu)

for k,v  in orderd.items():
    print(k,v)
a = list
dic = {str(key):str.strip(value) for key, value in enumerate(lines,1)}
# print(dic)


import collections
from collections import Counter
li = 'asdfasdtadfbvcxzhujtyjhchnvuioyuewrwafdsgvstwatdsgvfxdhs'
ct = Counter(li)
ct
defautdict = collections.defaultdict(list)
defautdict['w'].append('a')
print(defautdict.get('s'))

set_ = {1,2,'ok'}
print([value_ for value_ in set_])



