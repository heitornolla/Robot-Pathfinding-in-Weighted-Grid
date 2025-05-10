from src.grid.cell import Cell

def heuristic(cell, goal_cell):
    """Manhattan distance heuristic * water_cost"""

    water_cost = Cell(0, 0, "W").compute_cost()

    dx = abs(cell.x - goal_cell.x)
    dy = abs(cell.y - goal_cell.y)
    return (dx + dy) * water_cost
