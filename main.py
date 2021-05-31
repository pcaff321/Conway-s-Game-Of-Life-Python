from tkinter import *
from time import *
import random
from Cell import *

root = Tk()
grid = None
drawing = True


def clicked(event, cell):
    global drawing
    if drawing:
        cell.update(not cell.alive())


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
                                             i * size_x + w/cols, j * size_y + w/rows), fill='white',
                                            tag='cell' + str(i) + str(j))
            cell = Cell(canvas, label)
            grid_[i][j] = cell
            canvas.tag_bind('cell' + str(i) + str(j), "<Button-1>", lambda event, c=cell: clicked(event, c))
    return grid_


def random_living(amount):
    global rows
    global cols
    global grid
    amount = amount % (rows * cols)
    i = 0
    while i < amount:
        x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
        cell = grid[x][y]
        if not cell.alive():
            cell.update(1)
            i += 1


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

    update()


w = 400
cols = 20
rows = 20
timer = 500  # in ms

canvas = Canvas(root, width=w, height=w)
canvas.pack()
grid = make_grid()

startButton = Button(root, text="Start Simulation", padx=30,pady=20, command=start_sim)
startButton.pack()

root.mainloop()
