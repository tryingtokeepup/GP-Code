# Feel free to add more classes/helper functions if you like, code quality counts!
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


class RobotRouter:
    # This class will be initialized with the map features from the problem input.
    # barriers and laserCoordinates are arrays of Coordinate objects.
    # laserDirections is an array of strings representing the direction of
    # the corresponding laser in laserCoordinates.
    def __init__(self, barriers, laserCoordinates, laserDirections):
        # self.barriers = barriers
        # self.laserCoordinates = laserCoordinates
        # self.laserDirections = laserDirections
        pass
    # This method will be called to get your optimal route.
    # origin and destination are Coordinate objects (with x and y properties)
    # It should return a list of Coordinate objects,
    # starting with the origin and ending with the destination.
    # If you could not find a valid route, return an empty list.

    def exploreNeighbors(self, coordinate, visited):
        # Let's initialize some starting vectors: North, South, East, and West

        dY = [1, -1, 0, 0]
        dX = [0, 0, 1, -1]
        neighbors = {}

        for i in range(4):
            # we need to check the north, south, east, and west adj. block of the starting block
            print(coordinate)
            # not sure why, but I can't retrieve the X and Y value I need from coordinate, gah.
            Y = coordinate[1]
            X = coordinate[0]
            newY = Y + dY[i]
            newX = X + dX[i]
            if newY < 0 or newX < 0:
                continue
            if [newX, newY] in visited:
                continue
            if [newX, newY] == 'X':
                continue
            neighbors.append([newX, newY])
        return neighbors

    def route(self, origin, destination):
        # we need a counter and a flag to raise once we reach the destination

        # grab the starting coordinates from origin
        # starting_y = origin[0]
        # starting_x = origin[1]

        queue = Queue()
        queue.enqueue([origin])
        visited = set()

        while queue.size() > 0:

            path = queue.dequeue()

            coordinate = path[-1]
            print("Hello")
            print(coordinate)
            if coordinate not in visited:
                if coordinate == destination:

                    return path
                visited.add(coordinate)
                neighbors = self.exploreNeighbors(coordinate, visited)
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.enqueue(new_path)

        return None
