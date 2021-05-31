class Cell:

    def __init__(self, canvas, label, alive=0):
        self._label = label
        self._canvas = canvas
        self._alive = alive % 2
        self.update(alive)

    def change_colour(self, colour):
        self._canvas.itemconfig(self._label, fill=colour)

    def alive(self):
        return self._alive

    def living_neighbours(self, grid, x, y):
        count = 0
        for i in range(x - 1, x + 2, 1):
            if i >= len(grid[0]) or i < 0:
                continue
            for j in range(y - 1, y + 2, 1):
                if j >= len(grid) or j < 0:
                    continue
                count += grid[i][j].alive()
        count -= self._alive
        return count

    def update(self, alive):
        self._alive = alive % 2
        if self._alive == 0:
            self.change_colour("white")
        else:
            self.change_colour("black")





