import heapq
from src.grid.node import Node
from src.heuristic import heuristic


def greedy_best_first(grid, start_coords, goal_coords):
    start_cell = grid.get_cell(*start_coords)
    goal_cell = grid.get_cell(*goal_coords)

    open_set = []
    heapq.heappush(open_set, Node(start_cell, g=0, h=heuristic(start_cell, goal_cell)))
    came_from = {}
    opened_nodes = set()
    visited = set()

    time_step = 0

    while open_set:
        current_node = heapq.heappop(open_set)
        current_cell = current_node.cell
        current_coords = (current_cell.x, current_cell.y)
        opened_nodes.add(current_coords)

        time_step += 1

        if current_coords == (goal_cell.x, goal_cell.y):
            path = []
            while current_node:
                path.append((current_node.cell.x, current_node.cell.y))
                current_node = current_node.parent

            total_cost = sum(grid.get_cell(x, y).compute_cost(time_step) for (x, y) in path)
            return path[::-1], total_cost, opened_nodes


        if current_coords in visited:
            continue
        visited.add(current_coords)

        for neighbor in grid.get_neighbors(current_cell):
            if (neighbor.x, neighbor.y) in visited:
                continue

            new_node = Node(
                cell=neighbor,
                parent=current_node,
                g=0,  # ignored
                h=heuristic(neighbor, goal_cell)
            )
            heapq.heappush(open_set, new_node)

    total_cost = sum(grid.get_cell(x, y).get_cost(0) for (x, y) in path)
    return None, float('inf'), opened_nodes
