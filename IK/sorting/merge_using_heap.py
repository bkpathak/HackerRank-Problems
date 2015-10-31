import heapq

def addtoheap(h, i, it):
    try:
        heapq.heappush(h, (next(it), i))
    except StopIteration:
        pass

def mergek(*lists):
    its = map(iter, lists)
    h = []
    for i, it in enumerate(its):
        addtoheap(h, i, it)
    while h:
        v, i = heapq.heappop(h)
        addtoheap(h, i, its[i])
        yield v

data = [
[]
]
for x in mergek([1, 3, 5], [2, 4, 6], [7, 8, 9], [10]):
    print x,
