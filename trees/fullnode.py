class fullNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val 

def findPathWithCost(tree, cost, path):
    if not tree == None:
        # instead of doing this we should seek up the tree somehow
        # from the current node so we can account for paths that
        # dont start with root
        path.append(tree)
        # read in reverse will trace our path from the current node up to the root,
        # printing out any sum matches
        readInReverse(path)
        findPathWithCost(tree.left, cost, path)
        findPathWithCost(tree.right, cost, path)
    return True

def printPath(path, start):
    print path[start::-1]

def readInReverse(path, cost):
    sum = 0
    start = len(path) - 1
    while not len < 0:
        if sum path[start:] == cost:
            printPath(path, start)
        start -= 1


a = fullNode('a', 1)
b = fullNode('b', 2)
c = fullNode('c', 3)
d = fullNode('d', -1)
e = fullNode('e', 2)
f = fullNode('f', 1)
g = fullNode('g', 1)
b = fullNode('h', 3)
a = fullNode('i', 3)
b = fullNode('j', 4)