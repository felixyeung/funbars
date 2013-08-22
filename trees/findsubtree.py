from tree import MyNode
import copy

class stMyNode(MyNode):
    def findSubtree(self, st):
        if not self.left == None:
            self.left.findSubtree(st)
        if self.val == st.val:
            if matchTree(self, st):
                print "Subtree found"
        if not self.right == None:
            self.right.findSubtree(st)

def matchTree(src, target):
    if src == None and target == None:
        return True
    print 'Match %s to %s' % (src.val, target.val)    
    
    if src.val == target.val:
        return matchTree(src.left, target.left) and matchTree(src.right, target.right)
    else:
        #print 'Falling into false on %s and %s' % (src.val, target.val)
        return False
    return True

root = stMyNode('d')
a = stMyNode('a')
b = stMyNode('b')
c = stMyNode('c')
e = stMyNode('e')
f = stMyNode('f')
g = stMyNode('g')
h = stMyNode('h')
i = stMyNode('i')
j = stMyNode('j')
k = stMyNode('k')

root.addLeft(c)
root.addRight(h)

c.addLeft(b)
c.addRight(e)

b.addLeft(a)

h.addLeft(g)
h.addRight(k)

g.addLeft(f)
g.addRight(j)

f.addRight(i)

g2 = copy.deepcopy(g)
x = stMyNode('x')
y = stMyNode('y')

g2.addLeft(x)
g2.addRight(y)

print root.findSubtree(g)
print root.findSubtree(g2)