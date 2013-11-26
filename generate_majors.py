class Course:
    def __init__(self, params):
        self.key = params['key']
        self.diffculity = params['diffculity']
        self.prereqs = params['prereqs']
        self.directs_to = []

    def addEdges(self):
        for prereq in self.prereqs:
            if prereq:
                prereq.addEdgeTo(self)

    def addEdgeTo(self, target):
        self.directs_to.append({"course": target, "valid": 1})


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
    # go ahead and traverse its adjacencies recusively.
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
        if not visited.get(target["course"].key):
            topologicalSortHelper(target["course"], visited, sorted_courses)

    # Prepending to our list at the end ensures that the nodes
    # with at the end of the graph (e.g. No adjacencies) would be listed
    # last.
    sorted_courses.append(course)

def createLongestPaths(sorted_courses):
    # Iterate over each course in the sorted order.
    # for each node in list, the longest path is node + longest path of its adjacencies.
    # for each root node:
    # path
    reduced_graph = {"HEAD": {"key": "HEAD", "diffculity": 1337, "prereqs": [None]}}
    visited = {}
    for course in sorted_courses:
        createLongestPathsHelper(course, visited)

    return False

def createLongestPathsHelper(course, visited):
    print "looking at %s" % (course.key)
    #visited[course.key] = True;
    for target in course.directs_to:
        if not visited.get(target["course"].key):
            visited[target["course"].key] = True;
        else:
            target["valid"] = 0

# Begin data:
I = Course({"key": "I", "diffculity": 9, "prereqs": [None]})
J = Course({"key": "J", "diffculity": 10, "prereqs": [None]})
A = Course({"key": "A", "diffculity": 1, "prereqs": [None]})
B = Course({"key": "B", "diffculity": 5, "prereqs": [A]})
C = Course({"key": "C", "diffculity": 8, "prereqs": [A, J]})
D = Course({"key": "D", "diffculity": 7, "prereqs": [B, A, I]})
E = Course({"key": "E", "diffculity": 6, "prereqs": [A, C]})
F = Course({"key": "F", "diffculity": 4, "prereqs": [D, A, E]})
G = Course({"key": "G", "diffculity": 2, "prereqs": [F]})
H = Course({"key": "H", "diffculity": 3, "prereqs": [C, F]})

my_courses = [B, C, H, G, A, J, I, F, E, D]

# The first step is to create a directed graph of our coureses
createEdges(my_courses)

for course in my_courses:
    print "Course %s has the directed edges of %s." % (course.key, [course["course"].key for course in course.directs_to])

# Next, we want to sort our courses such that the classes with no prereqs
# are on the top of the stack.
sorted_courses = topologicalSortByDFS(my_courses)
print [course.key for course in topologicalSortByDFS(my_courses)]

# Popping off the stack, we want to invalidate all paths that are not the longest.
createLongestPaths(sorted_courses)


for course in my_courses:
    print "Course %s has the directed edges of %s." % (course.key, {course["course"].key for course in course.directs_to if (course["valid"] == 1)})
