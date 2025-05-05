# Heuristic: Manhattan distance × min terrain cost
def heuristic(cell, goal_cell):
    dx = abs(cell.x - goal_cell.x)
    dy = abs(cell.y - goal_cell.y)
    return (dx + dy)
