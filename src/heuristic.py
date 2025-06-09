from src.grid.cell import Cell

def heuristic(cell, goal_cell):
    """Manhattan distance heuristic * water_cost"""

    water_cost = Cell(0, 0, "W").compute_cost()
    mud_cost = Cell(0, 0, "M").compute_cost() # inadmissible heuristic example

    dx = abs(cell.x - goal_cell.x)
    dy = abs(cell.y - goal_cell.y)
    return (dx + dy) * water_cost
