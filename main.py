from tkinter import *
from time import *
import random
from Cell import *

root = Tk()
grid = None


def make_grid():
    global cols
    global rows
    global w
    global canvas
    grid_ = [[0]*cols for i in range(rows)]  # make 2x2 matrix
    size_x = w / cols
    size_y = w / rows
    for i in range(rows):
        for j in range(cols):
            label = canvas.create_rectangle((i * size_x, j * size_y,
                                             i * size_x + w/cols, j * size_y + w/rows), fill='white')
            grid_[i][j] = Cell(canvas, label, random.randint(0, 1))
    return grid_


def update():
    global root
    global grid
    global cols
    global rows
    global timer

    lifeGrid = [[0]*cols for i in range(rows)]  # make 2x2 matrix for updating grid

    for i in range(rows):
        for j in range(cols):
            cell = grid[i][j]
            neighbours = cell.living_neighbours(grid, i, j)
            alive = cell.alive()
            if (not alive) and (neighbours == 3):
                lifeGrid[i][j] = 1  # bring cell to life
            elif alive and (neighbours < 2 or neighbours > 3):
                lifeGrid[i][j] = 0  # kill cell
            else:
                lifeGrid[i][j] = alive

    for i in range(rows):
        for j in range(cols):
            cell = grid[i][j]
            cell.update(lifeGrid[i][j])

    root.after(timer, update)


def start_sim():
    global canvas
    global grid
    global startButton
    startButton.destroy()
    grid = make_grid()

    update()


w = 800
cols = 30
rows = 30
timer = 300  # in ms

canvas = Canvas(root, width=w, height=w)


startButton = Button(root, text="Start Simulation", padx=30,pady=20, command=start_sim)
startButton.pack()
canvas.pack()

root.mainloop()
