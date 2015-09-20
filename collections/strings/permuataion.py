def permute1(lst):
    if len(lst) == 0:
        yield []
    elif len(lst) == 1:
        yield lst
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i]+lst[i+1:]
            for p in permute1(xs):
                yield [x] + p
        return l


def permute(str,left,right):
    if left == right:
        print(str)
    else:
        for i in range(left,right):
            str[i], str[left] = str[left], str[i]
            permute1(str,left+1,right)
            str[i], str[left] = str[left], str[i]
data = list("ABC")
#permute2(data)
for p in permute1(data):
    print(p)
