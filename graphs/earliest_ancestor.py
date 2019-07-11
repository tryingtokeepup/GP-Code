

def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    # Build edges in reverse, so we can traverse downwards and get the ancestors
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])
    # print(graph.vertices)
    # Do a BFS from the starting_node to each other node
    earliest_ancestor = -1
    max_path_len = 1
    longest_path = []
    queue = Queue()
    queue.enqueue([starting_node])
    while queue.size() > 0:
        path = queue.dequeue()
        vertex = path[-1]
        if (len(path) >= max_path_len and vertex < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = vertex
            max_path_len = len(path)
            longest_path = path
        for neighbor in graph.vertices[vertex]:
            path_copy = path.copy()
            path_copy.append(neighbor)
            queue.enqueue(path_copy)
    print(earliest_ancestor)
    print(longest_path)
    return earliest_ancestor


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


earliest_ancestor(test_ancestors, 6)
