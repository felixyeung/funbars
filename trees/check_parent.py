from tree import MyNode

class CommonParent(MyNode):
    def getCommonParent(self, target):
        if findNode(self, target):
            return self.val
        else:
            next = self.parent
            while not next == None:
                print "looking at parent of %s (%s)" % (self.val, self.parent.val)
                if findNode(next, target):
                    return next.val
                next = next.parent
            return None

def findNode(src, target):
    if src == None:
        return False
    else:
        if (src.val == target.val):
            return True
        return findNode(src.left, target) or findNode(src.right, target)


# D is root
a = CommonParent('a')
b = CommonParent('b')
c = CommonParent('c')
d = CommonParent('d')
e = CommonParent('e')
f = CommonParent('f')
g = CommonParent('g')
h = CommonParent('h')
x = CommonParent('x')

d.addLeft(c)
d.addRight(h)

c.addLeft(b)
c.addRight(g)

b.addLeft(a)
b.addRight(f)

f.addLeft(e)

print e.getCommonParent(g)

print findNode(d, b)
print findNode(d, e)
print findNode(d, h)
print findNode(d, x)