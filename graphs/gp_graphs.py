
"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

        else:
            raise IndexError("Hey, that vertex doesn't exist!")

    def bft(self, starting_vertex):
        # Create an empty queue and enqueue the starting vertex ID
        queue = Queue()
        queue.enqueue(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while queue.size() > 0:
            # Dequeue the first vertex
            vertex = queue.dequeue()

            # if that vertex has not been visted ...
            if vertex not in visited:
                print(vertex)
                # Mark it as visted ... You can just use the .add syntax for sets, very useful!
                visited.add(vertex)

                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[vertex]:
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        # Create an empty STACK and push the starting vertex ID
        stack = Stack()
        stack.push(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while stack.size() > 0:

            # POP the firxt vertex
            vertex = stack.pop()
            # print(vertex)
            # if that vertex has not been visted ...
            if vertex not in visited:
                # Mark it as visted ...
                visited.add(vertex)
                print(vertex)
                # Then PUSH all of its neighbors to the back of the STACK
                for neighbor in self.vertices[vertex]:
                    stack.push(neighbor)
        return visited

    def dft_recursive(self, starting_vertex, visited=None):
        # base case
        # you don't need to explicitedly set a base case; the code just needs to work to an ending, and exit out appropiately
        # the visited set should probably have ... the starting_vertex already inside it
        if visited is None:
            visited = set()

        visited.add(starting_vertex)
        print(starting_vertex)
        # well, let's ... check all the neighbors of that starting_vertex, and run dft_recursive on them
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

# starting_vertex = 1
# visited = { 1 }

# neighbor = 2

# starting_vertex = 2
# visited = { 1 , 2 }

# neighbor = 3, 5


# starting_vertex = 3
# visited = { 1 , 2 , 3}

# neighbor =


    def bfs(self, starting_vertex, destination_vertex):
        # create an empty queue, add the starting vertex
        if starting_vertex is destination_vertex:
            print("Lol that's funny")
            return starting_vertex
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()
        print(visited)
        while queue.size() > 0:
            # dequeue the first path
            path = queue.dequeue()
            print(path)
            # we need to grab the last vertex of the path (hint, path is an array)
            vertex = path[-1]
            if vertex == destination_vertex:
                return path
            if vertex not in visited:
                visited.add(vertex)
            for neighbor in self.vertices[vertex]:

                # create a copy path for each of those neighbors, and then append neighbor to that copy
                path_copy = path.copy()
                path_copy.append(neighbor)
                if neighbor == destination_vertex:

                    return path_copy
                queue.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        # create an empty queue, add the starting vertex
        if starting_vertex is destination_vertex:
            print("Lol that's funny")
            return starting_vertex
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()
        print(visited)
        while stack.size() > 0:
            # dequeue the first path
            path = stack.pop()
            print(path)
            # we need to grab the last vertex of the path (hint, path is an array)
            vertex = path[-1]
            if vertex == destination_vertex:
                return path
            if vertex not in visited:
                visited.add(vertex)
            for neighbor in self.vertices[vertex]:

                # create a copy path for each of those neighbors, and then append neighbor to that copy
                path_copy = path.copy()
                path_copy.append(neighbor)
                if neighbor == destination_vertex:

                    return path_copy
                stack.push(path_copy)


# BFS
        # Create an empty QUEUE and enqueue the starting vertex ID
        # Create a set to store visited vertices
        # While the queue is not empty...
        # Dequeue the firxt vertex
        # if that vertex has not been visted ...
        # Mark it as visted ...
        # Then add all of its neighbors to the back of the queue
        # DFS
        # Create an empty STACK and push the starting vertex ID
        # Create a set to store visited vertices
        # While the queue is not empty...
        # POP the firxt vertex
        # if that vertex has not been visted ...
        # Mark it as visted ...
        # Then PUSH all of its neighbors to the back of the STACK
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # print(graph.dft(1))

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft_recursive(1)
    # print("---0----")
    # graph.dft_recursive(1)
    #print("what the heck?")

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    #print(graph.bfs(1, 3))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
