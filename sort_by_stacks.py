class StackSort:
    def __init__(self, stack):
        self.stack = stack
        self.buff = []

    def sort(self):
        # if the original stack is empty, we are done
        if not self.stack:
            return self.buff

        p1 = self.stack.pop()
        if (not self.buff) or (p1 <= self.buff[-1]):
            self.buff.append(p1)
            # print "pushing %d onto buff" % p1
            # print self.stack
            # print self.buff
        else:
            while self.buff:
                if p1 != None and p1 <= self.buff[-1]:
                    self.stack.append(p1)
                    p1 = None
                # append poped val back as soon as its GT something
                self.stack.append(self.buff.pop())
            if p1 != None:
                self.stack.append(p1)
            # print "popping everything back into the stack"
            # print self.stack
            # print self.buff

        return self.sort()





ss = StackSort([2, 7, 1, 3, 5, 4])
print ss.sort()
ss = StackSort([4, 63, 2, 24214, 24, 654, 2, 4, 1, 24, 65])
print ss.sort()