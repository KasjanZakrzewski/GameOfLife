import tkinter as tk
import random as Randy

# Colors 
BACKGROUND = "#000000"
DEAD = "#555555"
ALIVE = "#B5A8FF"

# Paramiters
WIDTH = 1200
HEIGHT = 600
SPACE_SIZE = 10

COLUMNS = int(WIDTH/SPACE_SIZE)
ROWS = int(HEIGHT/SPACE_SIZE)

class Cell:
    def __init__(self, x, y):
        self.neighbours = []
        self.next_state = False
        # self.x = x
        # self.y = y
        if Randy.randint(0,1) == 1:
            self.alive = True
            self.rectangle = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=ALIVE)
        else:
            self.alive = False
            self.rectangle = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=DEAD)     

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
        if self.alive != self.next_state:
            if self.next_state:
                canvas.itemconfig(self.rectangle, fill=ALIVE)
            else:
                canvas.itemconfig(self.rectangle, fill=DEAD)

        self.alive = self.next_state


def neighbours(h, w, world):
    for j in range(h):
        for i in range(w):
            pomI = i - 1
            pomJ = j - 1
            for k in range(3):
                for l in range(3):
                    if pomI >= 0 and pomI < w and pomJ >= 0 and pomJ < h:
                        if pomI != i or pomJ != j:
                            world[j][i].add_neighbour(world[pomJ][pomI])
                    pomI += 1
                pomI = i - 1
                pomJ += 1

def step():
    # for j in range(ROWS):
    #     for i in range(COLUMNS):
    #         print(world[j][i].sigh(), end=" ")
    #     print("")
    # print("==========")

    for j in range(ROWS):
        for i in range(COLUMNS):
            world[j][i].still_standing()

    for j in range(ROWS):
        for i in range(COLUMNS):
            world[j][i].update()
    
    root.after(250, step)

root = tk.Tk() 
canvas = tk.Canvas(root, bg=BACKGROUND, height=HEIGHT, width=WIDTH) 
canvas.pack()

world = [[Cell(x*SPACE_SIZE,y*SPACE_SIZE) for x in range(COLUMNS)] for y in range(ROWS)] 
canvas.update()

neighbours(ROWS, COLUMNS, world)

step()
root.mainloop()