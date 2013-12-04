class CharNode:
    def __init__(self, char):
        self.char = char       # contains a character (the same character might have multiple nodes!)
        self.links = {}        # Edges leading to the next character
        self.completes = []    # contains all words that can be complete if a tree walk stops at this node.
        self.fail = None       # points to a shallower node holding the same character, this allows us to continue
                               # to search under a different path if the current path ends in failure
                               # (i.e. no transition to the next node)

    # This function returns true if there exists a path from the
    # current node to a node holding a character 'char'
    def hasLinkToChar(self, char):
        if char in self.links:
            return True
        return False

def buildTree(words):
    # First, create a root Node that holds no char and fails to itself
    root = CharNode(None)
    root.fail = root

    for word in words:
        # restart our building from root
        curr_node = root
        for char in word:
            # If this character is linked from the node we are on,
            # move on to that linked node
            if curr_node.hasLinkToChar(char):
                curr_node = curr_node.links[char]
            # If a path to this character does not exist that from our current
            # node, create it and move to it
            else:
                new_node = CharNode(char)
                # In addition, if we are currently at root, everything coming from
                # root will fail to root.
                if curr_node == root:
                    new_node.fail = root
                curr_node.links[char] = new_node
                curr_node = new_node
        # at this point, we have looked at each character of a word
        # we know that this word must terminate at the current node.
        curr_node.completes.append(word)

        # At this point, we have a graph wit

    return root

def debugTree(node, depth):
    print '%s %s (%s)' % ('---' * depth, node.char, node.completes)
    for key, target in node.links.iteritems():
        debugTree(target, depth + 1)

def buildFailFuncs(tree):
    return false

val = 'foobarbazcatdogpig'
match = ['foo', 'bar', 'baz', 'foobar', 'root', 'zoo']

root = buildTree(match)

debugTree(root, 0)