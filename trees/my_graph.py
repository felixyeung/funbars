from collections import deque


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
            if each not in visited:
                each.dfs(visited)

    def bfs(self):
        q = deque([])
        visited = []

        q.append(self)
        while q:
            curr = q.popleft()
            if curr not in visited:
                print "Visiting %s" % (curr.val)
                visited.append(curr)
                for each in curr.adjacenies:
                    q.append(each)



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
print "DFS:"
root.dfs([])
print "BFS:"
root.bfs()