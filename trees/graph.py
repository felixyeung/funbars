class Graph:
    def __init__(self, options):
        self.directed =  options['directed']
        self.nodes = {}
    
    def addNode(self, key, value):
        n = Node(key, value)
        self.nodes[n.key] = n

    def addNodeSet(self, node_set):
        self.nodes = node_set

    def shortestPath()

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.adj = []

    def addPath(self, node, weight):
        e = Edge(node.key, weight)
        self.adj.append(e)

class Edge:
    def __init__(self, key, weight):
        self.target = key
        self.weight = weight

G = Graph({"directed": False})

nodes = {}
nodes['a'] = Node('a', 'cat')
nodes['b'] = Node('b', 'dog')
nodes['c'] = Node('c', 'fish')
nodes['d'] = Node('d', 'pig')
nodes['e'] = Node('e', 'cow')
nodes['f'] = Node('f', 'bear')
nodes['g'] = Node('g', 'lamb')

nodes['a'].addPath(nodes['b']
    , 2)
nodes['a'].addPath(nodes['c'], 1)
nodes['b'].addPath(nodes['d'], 6)
nodes['b'].addPath(nodes['e'], 3)
nodes['c'].addPath(nodes['e'], 8)
nodes['c'].addPath(nodes['g'], 50)
nodes['d'].addPath(nodes['e'], -1)
nodes['e'].addPath(nodes['f'], 5)
nodes['f'].addPath(nodes['g'], 4)

G.addNodeSet(nodes)

print [(node.key, node.val) for key, node in G.nodes.iteritems()]
