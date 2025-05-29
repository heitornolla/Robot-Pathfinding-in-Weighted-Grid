from collections import deque
from src.grid.node import Node


def breadth_first_search(grid, start_coords, goal_coords):
    start_cell = grid.get_cell(*start_coords)
    goal_cell = grid.get_cell(*goal_coords)

    queue = deque([Node(start_cell, g=0)])
    visited = set()
    opened_nodes = set()

    while queue:
        current_node = queue.popleft()
        current_cell = current_node.cell
        current_coords = (current_cell.x, current_cell.y)
        opened_nodes.add(current_coords)

        if current_coords == (goal_cell.x, goal_cell.y):
            path = []
            total_cost = 0
            while current_node:
                path.append((current_node.cell.x, current_node.cell.y))
                total_cost += current_node.cell.compute_cost()
                current_node = current_node.parent
            return path[::-1], total_cost, opened_nodes

        if current_coords in visited:
            continue
        visited.add(current_coords)

        for neighbor in grid.get_neighbors(current_cell):
            neighbor_coords = (neighbor.x, neighbor.y)
            if neighbor_coords not in visited:
                queue.append(Node(cell=neighbor, parent=current_node))

    return [], float("inf"), opened_nodes
