class MyNode:
    def __init__(self, val):
        self.parent = None
        self.val = val
        self.left = None
        self.right = None

    def addLeft(self, node):
        node.parent = self
        self.left = node

    def addRight(self, node):
        node.parent = self
        self.right = node
