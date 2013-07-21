class MyQueue:
    def __init__(self):
        self.buff = []
        self.queue = []

    def push(self, val):
        self.buff.push(val)
        while self.queue:
            self.buff.append(self.queue.pop())
        self.buff.append(val)

    def shift(self):
        if not self.queue
            while self.buff:
                self.queue.append(self.buff.pop())
        return self.queue.pop()

mq = MyQueue()
mq.push('a')
mq.push('b')
mq.push('c')
mq.push('d')
mq.push('e')
print mq.queue
print mq.shift()
print mq.shift()
print mq.shift()
mq.push('f')
mq.push('o')
mq.push('o')
mq.push('b')
mq.push('a')
mq.push('r')
print mq.queue