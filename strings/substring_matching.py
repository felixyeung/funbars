class Node:
    def __init__(self, substring, char):
        if substring == None or char == None:
            # We are probably creating a root
            self.key = None
            self.char = None
            self.fail = None
            self.transitions = []
            self.complete = False
        else:
            self.key
             = substring
            self.char = char
            self.fail = None # root is the default failure transition
            self.transitions = [] # transition contains string keys 
            self.complete = False

    def addTrasition(self, node):
        self.transitions.append(node.key)

    def setTargetWord(self):
        self.complete = True

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
                    new_node.fail = root

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
                    linkLongestSuffix(visited, node)
                for key in curr_node.transitions:
                    queue.append(self.nodes[key])

    def linkLongestSuffix(visited, node):
        # Loop over suffixes, as soon as one is found
        # add it as a failure transition of the current node
        for i in range (1, len(node.key)):
            suffix = node.key[i:]
            if self.nodes[suffix] in visited:
                node.fail = suffix
                return True;
        return False;

string = 'foobarbazcatarmts'
matches = ['foo', 'foobar', 'ba', 'cat', 'bar', 'arm']

m = Machine()
m.createTree(matches)