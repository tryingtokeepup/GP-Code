import math
import random
import time
from datetime import datetime

# programmer tells us, make sure this animals array is always .... 7 elements long/big/ in-it
animals = ["Giraffe", "Lion", "Dude", "AwesomePossum",
           "Doggy", "Cat", "Cuddlefish"]
numbers = [n for n in range(1, 100)]
# print(numbers)
#########################
# What runtime is this?
#########################

# Return the name of all the animals above

# O(10000000) => O(constant)
# O(50)       => O(constant)
# O(1000^1000000000) => this is really really really really really bad


def getAnimals():
    return animals     # O(constant)


def getCoolNumber(numbers):
    print("9 is the coolest number")  # is a constant time operation

# this concept is redunkulosly difficult, don't worry if you don't get it right now
# we already know how many operations the function will take before we run it!
#

#########################
# RUNTIME ANALYSIS
#########################
# Return the number of animals
# dynamic => we don't know beforehand how many times the function will run!


def getNumAnimals():
    num_animals = 0
    for animal in animals:
        num_animals += 1  # linear time, 0(n) time complexity
    return num_animals


# Returns each animal with all of its letter lowercased

def getLowercaseAnimals():
    copy_of_animals = animals
    animal_index = 0
    for animal in copy_of_animals:
        # as long as you include the counter, we can keep track of what's going on
        copy_of_animals[animal_index] = copy_of_animals[animal_index].lower()
        animal_index += 1
    return copy_of_animals


def hasAnimal(animal_name):
    for animal in animals:
        if animal == animal_name:
            return True
    return False  # this is implicit, right? remember this :D


def findAnimal(animal_name):
    animal_index = 0
    for animal in animals:  # O(n)
        if animal == animal_name:  # O(constant time)
            print(f"Found the {animal_name}! ")
            return animal_index

        animal_index += 1
    return -1  # basically false

# NESTED LOOP


def printAnimalPairs():  # this is a O(n) + O(n)  =  O(n^2) love you jerrick
    for animal1 in animals:  # O(n)
        for animal2 in animals:  # O(n)
            print(animal1 + " - " + animal2)  # O(1)

# make one more, but triples!


def printAnimalTriples():  # this is a O(n) + O(n) + O(n) = O(n^3)
    for animal1 in animals:  # O(n)
        for animal2 in animals:  # O(n)
            for animal3 in animals:  # O(n)
                print(animal1 + " - " + animal2 + " - " + animal3)

# print(getAnimals())

# print(getNumAnimals())


# print(getLowercaseAnimals())
# print(hasAnimal("Cat"))
# print(findAnimal("Cat"))
start_time = time.time()
print(printAnimalTriples())

end_time = time.time()
print(f"runtime: {end_time - start_time} seconds")
