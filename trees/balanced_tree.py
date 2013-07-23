class MyNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def addLeft(self, node):
        self.left = node

    def addRight(self, node):
        self.right = node

    def isBalanced(self):
        return self.countDepth(self.left) == self.countDepth(self.right)

    def countDepth(self, node):
        if node == None:
            return 0;
        else:
            depth = 1 + max(self.countDepth(node.left), self.countDepth(node.right))
            print "looking at node %s at depth %d" % (node.val, depth)
            return  depth

root = MyNode('a')
b = MyNode('b')
c = MyNode('c')
d = MyNode('d')
e = MyNode('e')
f = MyNode('f')
g = MyNode('g')
h = MyNode('h')
i = MyNode('i')
j = MyNode('j')
k = MyNode('k')
l = MyNode('l')
m = MyNode('m')

root.addLeft(b)
root.addRight(c)

b.addLeft(d)
b.addRight(g)

d.addLeft(e)
d.addRight(f)

e.addRight(h)

c.addLeft(i)
c.addRight(j)

i.addLeft(k)

j.addLeft(l)

l.addLeft(m)

root.isBalanced()
