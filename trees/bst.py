class BstNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, node):
        #If the value is duplicated, it does not go into the bst
        if node.val == self.val:
            return False
        if node.val < self.val:
            if self.left == None:
                self.left = node
            else:
                self.left.insert(node)
        elif node.val > self.val:
            if self.right == None:
                self.right = node
            else:
                self.right.insert(node)

    def inOrderPrint(self):
        if not self.left == None:
            self.left.inOrderPrint()
        print self.val
        if not self.right == None:
            self.right.inOrderPrint()

root = BstNode(8)
a = BstNode(3)
b = BstNode(7)
c = BstNode(2)
d = BstNode(26)
e = BstNode(1)
f = BstNode(7)
g = BstNode(6)
h = BstNode(4)
i = BstNode(7)
j = BstNode(3)
k = BstNode(14)
l = BstNode(12)
m = BstNode(5)
n = BstNode(11)
o = BstNode(1)
p = BstNode(11)

root.insert(a)
root.insert(b)
root.insert(c)
root.insert(d)
root.insert(e)
root.insert(f)
root.insert(g)
root.insert(h)
root.insert(i)
root.insert(j)
root.insert(k)
root.insert(l)
root.insert(m)
root.insert(n)
root.insert(o)
root.insert(p)

root.inOrderPrint()