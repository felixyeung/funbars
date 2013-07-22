class MyNode:
    def __init__(self, val):
        self.val = val
        self.adjacenies = []
    def addPath(self, node):
        if node not in self.adjacenies:
            self.adjacenies.append(node)

    def dfs(self, visited):
        #self is root.
        print "Visiting %s" % (self.val)
        visited.append(self)
        for each in self.adjacenies:
            if each not in visi
            ted:
                each.dfs(visited)



root = MyNode('a')
b = MyNode('b')
c = MyNode('c')
d = MyNode('d')
e = MyNode('e')

root.addPath(b)
root.addPath(e)
b.addPath(c)
b.addPath(d)
c.addPath(d)
e.addPath(root)

root.dfs([])