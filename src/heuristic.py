def heuristic(cell, goal_cell):
    """Manhattan distance heuristic"""
    dx = abs(cell.x - goal_cell.x)
    dy = abs(cell.y - goal_cell.y)
    return (dx + dy)
