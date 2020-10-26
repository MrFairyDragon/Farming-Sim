import pygame


class Node:

    def __init__(self, row, col, width, total_rows, total_columns):
        self.row = row
        self.col = col
        self.state = "reset"
        self.x = row * width
        self.y = col * width
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        self.total_columns = total_columns

    def get_pos(self):
        return self.row, self.col

    def isClosed(self):
        return self.state == "closed"

    def is_open(self):
        return self.state == "open"

    def is_wall(self):
        return self.state == "wall"

    def is_start(self):
        return self.state == "start"

    def is_end(self):
        return self.state == "end"

    def reset(self):
        self.state == "reset"

    def make_open(self):
        self.state = "open"

    def make_closed(self):
        self.state = "closed"

    def make_wall(self):
        self.state = "wall"

    def make_end(self):
        self.state = "end"

    def make_path(self):
        self.state = "path"

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_wall(): #Down
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_wall(): #Up
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_columns - 1 and not grid[self.row][self.col + 1].is_wall(): #Right
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_wall(): #Left
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False

