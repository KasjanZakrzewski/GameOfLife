import random as Randy
import time

class Cell:
    def __init__(self):
        self.neighbours = []
        self.next_state = False
        if Randy.randint(0,1) == 1:
            self.alive = True
        else:
            self.alive = False
        
    def sigh(self):
        if self.alive:
            return "+"
        else:
            return "."

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def still_standing(self):
        standing = 0
        for neighbour in self.neighbours:
            if neighbour.alive:
                standing += 1

        if self.alive:
            if standing in [2, 3]:
                self.next_state = True 
            else:
                self.next_state = False
        else:
            if standing == 3:
                self.next_state = True 
            else:
                self.next_state = False

        return standing
    
    def update(self):
        self.alive = self.next_state



def neighbours(h, w, world):
    for i in range(h):
        for j in range(w):
            pomI = i - 1
            pomJ = j - 1
            for k in range(3):
                for l in range(3):
                    if pomI >= 0 and pomI < h and pomJ >= 0 and pomJ < w:
                        if pomI != i or pomJ != j:
                            world[j][i].add_neighbour(world[pomJ][pomI])
                    pomI += 1
                pomI = i - 1
                pomJ += 1


w = 11
h = 11
t = 12

read = False

world = [[Cell() for x in range(h)] for y in range(w)] 

if read:
    file = open('Plik2.txt', 'r')
    i = 0
    j = 0 
    for line in file.readlines():
        for char in line:
            if char != "\n":
                if char == "+":
                    world[j][i].alive = True
                else:
                    world[j][i].alive = False
            j += 1
        j = 0
        i += 1

neighbours(h, w, world)


for k in range(t):
    for i in range(h):
        for j in range(w):
            print(world[j][i].sigh(), end=" ")
        print("")

    print("==========")

    for i in range(h):
        for j in range(w):
            world[j][i].still_standing()

    for i in range(h):
        for j in range(w):
            world[j][i].update()
    
    time.sleep(1) 


# spr sąsiadów
# for row in world:
#     for cell in row:
#         for neighbour in cell.neighbours:
#             print(neighbour.sigh(), end=" ")
#         print(cell.still_standing(), end=" ")
#         print("")