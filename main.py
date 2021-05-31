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


def random_living():
    global rows
    global cols
    global grid
    global random_cells
    global amount
    if random_cells.get():
        available = list()
        for i in range(rows):
            for j in range(cols):
                available.append((i, j))
        random.shuffle(available)  # randomise list
        for i in range(amount):
            cell_pos = available.pop()
            cell = grid[cell_pos[0]][cell_pos[1]]
            if not cell.alive():
                cell.update(1)
                i += 1
    else:
        for i in grid:
            for j in i:
                j.update(0)


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
    global c1

    startButton.destroy()
    c1.destroy()

   # update()


w = 400
cols = 20
rows = 20
timer = 300  # in ms
amount = 30
random_cells = BooleanVar()

canvas = Canvas(root, width=w, height=w)
canvas.pack()
grid = make_grid()

startButton = Button(root, text="Start Simulation", padx=30, pady=20, command=start_sim)
startButton.pack()

c1 = Checkbutton(root, text='Randomise Cells', variable=random_cells, onvalue=True, offvalue=False,
                 command=random_living)
c1.pack()

root.mainloop()
