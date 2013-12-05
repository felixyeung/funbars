class Node:
    def __init__(self, substring, char):
        if substring == None or char == None:
            # We are probably creating a root
            self.key = None
            self.char = None
            self.fail = None
            self.transitions = []
            self.complete = []
        else:
            self.key = substring
            self.char = char
            self.fail = None # root is the default failure transition
            self.transitions = [] # transition contains string keys 
            self.complete = []

    def addTrasition(self, node):
        self.transitions.append(node.key)

    def setTargetWord(self):
        self.complete.append(self.key)

    def isRoot(self):
        return self.key == None and self.fail == None



class Machine:
    def __init__(self):
        self.nodes = {} #dictionary of nodes index by node.key
        self.root = Node(None, None)

    def addNode(self, node):
        self.nodes[node.key] = node

    def createTree(self, words):
        root = self.root
        for word in words:
            curr_node = root
            prefix = ''
            for char in word:
                prefix = prefix + char
                # If there's a transition to an existing node with this prefix,
                # go ahead and "walk" to it.
                if prefix in curr_node.transitions:
                    curr_node = self.nodes[prefix]
                # Otherwise, build a new node.
                else:
                    new_node = Node(prefix, char)
                    new_node.fail = None

                    curr_node.addTrasition(new_node)
                    self.addNode(new_node)
                    curr_node = new_node
            # After completeing all characters, the current node must be
            # a word we want to look for
            curr_node.setTargetWord()

    def buildFailureTransitions(self):
        root = self.root
        queue = []
        visited = []
        queue.append(root)
        while queue:
            curr_node = queue[0]
            queue = queue[1:]

            if not curr_node in visited:
                visited.append(curr_node)
                # If the current node is not root, attempt to create
                # a failure transition to the longest suffix.
                if not curr_node == root:
                    self.linkLongestSuffix(visited, curr_node)
                for key in curr_node.transitions:
                    queue.append(self.nodes[key])

    def linkLongestSuffix(self, visited, node):
        # Loop over suffixes, as soon as one is found
        # add it as a failure transition of the current node
        for i in range (1, len(node.key)):
            suffix = node.key[i:]
            if self.nodes.get(suffix) and self.nodes[suffix] in visited:
                node.fail = suffix
                # In addition, add all the complete words in the longest suffix to this node
                node.complete = node.complete + self.nodes[suffix].complete
                return True;
        return False;

    def debugTree(self, node, depth):
        print '%-20s %-15s %-30s %-30s %-15s' % (depth * '---',
                                                 node.key,
                                                 [each for each in node.transitions],
                                                 [each for each in node.complete],
                                                 node.fail)
        for transition in node.transitions:
            self.debugTree(self.nodes[transition], depth + 1)

    def search(self, string):
        result = []
        root = m.root
        curr_node = root
        for char in string:
            curr_node = searchHelper(self, curr_node, char, result)
            # We are unable to land exit the node
            if curr_node == None:
                # We will either remain at root, or be able to advance.
                curr_node = searchOnceAtRoot(self, char, result)
            print 'moving onto the next node'
        return result

def searchHelper(machine, curr_node, char, result):
    target_name = targetName(curr_node, char)

    print 'looking for %s in %s' % (target_name, curr_node.key)

    if target_name in curr_node.transitions:
        print '   %s found.' % (target_name)
        addToResults(result, machine.nodes[target_name].complete)
        return machine.nodes[target_name]
    else:
        if curr_node.fail == None:
            return None
        else:
            return searchHelper(machine, machine.nodes[curr_node.fail], char, result)

def searchOnceAtRoot(machine, char, result):
    root = machine.root
    target_name = targetName(root, char)

    print 'looking for %s in root' % (target_name)

    if target_name in root.transitions:
        addToResults(result, root.complete)
        return machine.nodes[target_name]
    else:
        return root

def targetName(node, char):
    if node.key == None:
        prefix = ''
    else:
        prefix = node.key
    return prefix + char

def addToResults(result, complete):

    for word in complete:
        result.append(word)

string = 'foobarbazcatarmtszfo'
matches = ['ar', 'foo', 'zfoo', 'fooo', 'foobar', 'ba', 'cat', 'bar', '343', 'bazz', 'barb', 'baz', 'arm']

m = Machine()
m.createTree(matches)


m.buildFailureTransitions()
print '%-20s %-15s %-30s %-30s %-15s' % ('depth',
                                         'unique label',
                                         'nodes accessible',
                                         'target words completed',
                                         'longest suffix')
m.debugTree(m.root, 0)

print m.search(string)
