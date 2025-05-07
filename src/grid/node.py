# Node used in the A* algorithm
from typing import Optional
from grid.cell import Cell


class Node:    
    """
    Node class used in pathfinding algorithms.
    """
    def __init__(self, cell: Cell, parent: Optional['Node'] = None, g: float = 0, h: float = 0):
        self.cell = cell
        self.parent = parent
        self.g = g  # Cost from start to this node
        self.h = h  # Heuristic cost to goal
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f
