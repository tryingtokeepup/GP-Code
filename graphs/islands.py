'''
Write a function that takes a 2D binary array and returns the number of islands (made of 1s). An island consists of 1s that are connected to the north, south, east, and west. For example:





island_counter(islands)  # 4
'''
# Translate the problem into graph terminology
# Build the graph
# Traverse the graph!

# Build your graph
# traverse the graph w/BFS
# count # of connected components

# Visited Matrix => make another matrix that has the same height, width, and number
# of cells as the islands matrix
# Carbon Paper style -> we start all cells as False, if we visit, we turn it True


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop(-1)
        else:
            return 0


def island_counter(matrix):
    # Create a visited matrix
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    island_count = 0
    # Walk through each cel in the matrix
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            # if it has not been visited
            if not visited[y][x]:
                # When I reach a 1
                if matrix[y][x] == 1:
                    # do a DFT and mark each as visited
                    visited = dft(x, y, matrix, visited)  # STUB
                    # Then increment counter by 1
                    island_count += 1
    print(island_count)
    return island_count


def dft(x, y, matrix, visited):
    # Create an empty Stack
    s = Stack()
    # Push the starting vertex to the stack
    s.push((x, y))
    # While the Stack is not empty...
    while s.size() > 0:
        # Pop the first vertex
        v = s.pop()
        x = v[0]
        y = v[1]
        # If it has not been visited...
        if not visited[y][x]:
            # Mark it as visited (print it and add it to the visited set)
            visited[y][x] = True
            # Then push each of its neighbors onto the Stack
            for neighbor in get_neighbors((x, y), matrix):  # STUB
                s.push(neighbor)
    return visited


# def get_neighbors(vertex, matrix):
#     x = vertex[0]
#     y = vertex[1]
#     neighbors = []
#     # north
#     if x > 0 and matrix[y - 1][x] == 1:
#         neighbors.append((x, y-1))
#     # check south
#     if x < len(matrix) - 1 and matrix[y + 1][x]:
#         neighbors.append((x, y + 1))
#     # check west
def get_neighbors(vertex, graph_matrix):
    x = vertex[0]
    y = vertex[1]
    neighbors = []
    # Check north
    if y > 0 and graph_matrix[y - 1][x] == 1:
        neighbors.append((x, y - 1))
    # Check south
    if y < len(graph_matrix) - 1 and graph_matrix[y + 1][x] == 1:
        neighbors.append((x, y+1))
    # Check east
    if x < len(graph_matrix[0]) - 1 and graph_matrix[y][x + 1] == 1:
        neighbors.append((x + 1, y))
    # Check west
    if x > 0 and graph_matrix[y][x - 1] == 1:
        neighbors.append((x - 1, y))
    return neighbors


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands)
