# Node used in the A* algorithm
class Node:
    def __init__(self, cell, parent=None, g=0, h=0):
        self.cell = cell
        self.parent = parent
        self.g = g  # Cost from start to this node
        self.h = h  # Heuristic cost to goal
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f
