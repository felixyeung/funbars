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

    def getDepthLists(self, depth, lol):
        if not depth in lol:
            lol[depth] = []
        lol[depth].append(self.val)
        if not self.left == None:
            self.left.getDepthLists(depth + 1, lol)
        if not self.right == None:
            self.right.getDepthLists(depth + 1, lol)
        return lol

    def isBst(self, node):
        #check self and left -> if > return
        #check self and right -> if < return
        #if left not empty check left tree
        #if right not empty check right tree
        #both true
        if node == None:
            return True
        if not node.left == None and node.val < node.left.val:
            return False
        if not node.right == None and node.val > node.right.val:
            return False
        return self.isBst(node.left) and self.isBst(node.right)

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

print root.getDepthLists(0, {})

bst = MyNode(4)
one = MyNode(1)
two = MyNode(2)
three = MyNode(3)
five = MyNode(5)
six = MyNode(6)
seven = MyNode(7)

bst.addLeft(two)
bst.addRight(six)

two.addLeft(one)
two.addRight(three)

six.addLeft(five)
six.addRight(seven)

print bst.isBst(bst)
print root.isBst(root)

bst.addLeft(six)
bst.addRight(two)

print bst.isBst(bst)