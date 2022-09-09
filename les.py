st = 'abcdefghijklmnop'
# st = 'paypalishiring'

co = 5
x = 0

print(len(st))

if len(st) % co * 2 - 2 == 0:
    n = len(st) // co * 2 - 2
    pass
else:
    n = (len(st) // co * 2 - 2) + 1
# print(n)

lists = [[] for _ in range(n)]




for i in range(n+1):
    if x < co * i -2:
        if i % 2 != 0:
            for w in range(co):
                # print(x)
                lists[i - 1].append(st[x])
                x += 1

            pass
        else:
            lists[i - 1].append('')
            for w in range(co-2):
                # print(x)
                lists[i - 1].append(st[x])
                x += 1
            lists[i - 1].append('')
            lists[i - 1].reverse()

            pass
    # print(x)
# lists = map(str,lists)
# lists_out = map(sum,lists)
# lists_out = list(lists_out)

res = []
print(lists)

for x in range(n):
    for i in range(co - 1):
        res.append(lists[i][x])


res_ = ''
for d in res:
    print(d)
    res_ += d


print(res_)
# aibhjpcgkodflnem