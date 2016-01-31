# Implement the Queue with constant time to peek Max element
# present in the queue

from collections import deque
class MaxQueue(object):
    def __init__(self):
        self.q = deque()
        # For potential maxes
        self.maxq = deque()

    def enqueue(self, val):
        while self.maxq and self.maxq[-1] < val:
            self.maxq.pop()
        self.maxq.append(val)
        self.q.append(val)

    def dequeue(self):
        if self.q[0] == self.maxq[0]:
            self.maxq.popleft()
        return self.q.popleft()

    def peek(self):
        return self.q[0]

    def peek_max(self):
        return self.maxq[0]


if __name__ == "__main__":
    val = [1,3,8,5,9,12,2,7,10]
    queue = MaxQueue()
    print("Enqueue Operations")
    for v in val:
        queue.enqueue(v)
        print("Element in queue: ", queue.q)
        print("Potentail Max: ",queue.maxq)

    print("Dequeue Operations")
    for i in range(len(val)):
        print("Element in queue: ",queue.q)
        print("Potentail Max: ",queue.maxq)
        print("Max: ", queue.peek_max())
        queue.dequeue()
