from Grid import Grid
from Node import Node
import numpy as np
import pygame
from queue import PriorityQueue


class Astar:

    def calcH(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)

    def reconstructPath(self, came_from, current):
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
            current.make_path()
        print(path)
        return path

    def algorithm(self, grid, start, end):
        count = 0
        open_set = PriorityQueue()
        open_set.put((0, count, start))
        came_from = {}
        g_score = {Node: float("inf") for row in grid for Node in row}
        g_score[start] = 0
        f_score = {Node: float("inf") for row in grid for Node in row}
        f_score[start] = self.calcH(start.get_pos(), end.get_pos())

        open_set_hash = {start}

        while not open_set.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            current = open_set.get()[2]
            open_set_hash.remove(current)

            if current == end:
                self.reconstructPath(came_from, end)
                end.make_end()
                return True
                return self.reconstructPath(came_from, end)

            for neighbor in current.neighbors:
                temp_g_score = g_score[current] + 1
                if temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + self.calcH(neighbor.get_pos(), end.get_pos())

                    if neighbor not in open_set_hash:
                        count += 1
                        open_set.put((f_score[neighbor], count, neighbor))
                        open_set_hash.add(neighbor)
                        neighbor.make_open()
            if current != start:
                current.make_closed()
        return False;

    def make_grid(self, sizeX, sizeY):
        grid = []
        gap = 64
        for i in range(sizeX):
            grid.append([])
            for j in range(sizeY):
                node = Node(i, j, gap, sizeX, sizeY)
                grid[i].append(node)
        return grid
