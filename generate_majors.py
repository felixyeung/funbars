class Course:
    def __init__(self, params):
        self.key = params['key']
        self.diffculity = params['diffculity']
        self.prereqs = params['prereqs']
        self.directs_to = []

    def addEdges(self):
        for prereq in self.prereqs:
            if prereq:
                prereq._addEdgeTo(self)

    def _addEdgeTo(self, target):
        self.directs_to.append(target)


# HELPER CLASS
# This is an implementation of a binary tree
# That will serve as our binary serach tree for
# managing the diffculity of classes.
#
# Each node of the tree consist of key, which is a diffculity, and 
# a list of Course objects of that diffculity
class BST:
    def __init__(self, course):
        self.key = course
        self.items = []

# This function will take a list of Course objects.
# and create directed edges from each class that preceeds another
# class. 
def createEdges(list):
    for course in list:
        course.addEdges()

# This function leverages DFS on our courses graph to sort
# them in topological order
def topologicalSortByDFS(courses):
    sorted_courses = []
    visited = {}
    # Look over each node, if the node is not visited,
    # go ahead and traverse its adjancies recusively.
    for course in courses:
        if not visited.get(course.key):
            topologicalSortHelper(course, visited, sorted_courses)
    return sorted_courses

def topologicalSortHelper(course, visited, sorted_courses):
    # Mark current node as visited
    visited[course.key] = True

    # For each node in its adjacenies, visit recursively if it
    # hasnt been visited already.
    for target in course.directs_to:
        if not visited.get(target.key):
            topologicalSortHelper(target, visited, sorted_courses)

    # By appending to our topo list at the end, we ensure that the
    # final nodes of our directed graph are appeneded first.
    sorted_courses.append(course)


# Begin data:
A = Course({"key": "A", "diffculity": 1, "prereqs": [None]})
B = Course({"key": "B", "diffculity": 5, "prereqs": [A]})
C = Course({"key": "C", "diffculity": 8, "prereqs": [A]})
D = Course({"key": "D", "diffculity": 7, "prereqs": [B, A]})
E = Course({"key": "E", "diffculity": 6, "prereqs": [A, C]})
F = Course({"key": "F", "diffculity": 4, "prereqs": [D, A, E]})
G = Course({"key": "G", "diffculity": 2, "prereqs": [F]})
H = Course({"key": "H", "diffculity": 3, "prereqs": [C, F]})

my_courses = [A, B, C, D, E, F, G, H]

createEdges(my_courses)

for course in my_courses:
    print "Course %s has the directed edges of %s." % (course.key, [course.key for course in course.directs_to])

print [course.key for course in topologicalSortByDFS(my_courses)]
