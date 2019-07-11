import random
import time


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


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


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users = time complexity = O(n)
        for i in range(numUsers):
            self.addUser(f"User {i + 1 }")
        # print(self.users)
        # Create friendships = time complexity = O(n^2)
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))
        # print(possibleFriendships)
        random.shuffle(possibleFriendships)
        numFriendshipsToCreate = ((numUsers * avgFriendships // 2))
        # we are trying to only create a certain number of friendships
        friendshipsToCreate = possibleFriendships[:numFriendshipsToCreate]
        for friendship in friendshipsToCreate:
            self.addFriendship(friendship[0], friendship[1])

    def populateGraphLinear(self, numUsers, avgFriendships):
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        for i in range(numUsers):
            self.addUser(f"User {i + 1 }")
        # note to brady this might confuse some people, maybe.
        targetFriendships = numUsers * avgFriendships
        totalFriendships = 0
        collisions = 0
        traversals = 0
        while totalFriendships < targetFriendships:
            userID = random.randint(1, self.lastID)
            friendID = random.randint(1, self.lastID)
            if self.addFriendship(userID, friendID):  # This is a truth check
                totalFriendships += 2
            else:
                collisions += 1

            traversals += 1
        print(f"COLLISIONS: {collisions}")
        print(f"TRAVERSALS: {traversals}")

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        queue = Queue()
        queue.enqueue([userID])
        while queue.size() > 0:
            path = queue.dequeue()
            vertex = path[-1]
            if vertex not in visited:
                visited[vertex] = path
                for neighbor in self.friendships[vertex]:
                    path_copy = path.copy()  # list(path)
                    path_copy.append(neighbor)
                    queue.enqueue(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    start_time = time.time()
    numUsers = 100
    avgFriendships = 99
    start_time = time.time()
    sg.populateGraphLinear(numUsers, avgFriendships)
    # print(sg.friendships)
    end_time = time.time()
    print(f"Linear runtime: {end_time - start_time} seconds")
    sg = SocialGraph()
    start_time = time.time()
    sg.populateGraph(numUsers, avgFriendships)
    end_time = time.time()
    print(f"Quadratic runtime: {end_time - start_time} seconds")
