import heapq

from src.grid.node import Node
from src.heuristic import heuristic


def a_star(grid, start_coords, goal_coords):
    start_cell = grid.get_cell(*start_coords)
    goal_cell = grid.get_cell(*goal_coords)

    open_set = []
    heapq.heappush(open_set, Node(start_cell, g=0, h=heuristic(start_cell, goal_cell)))
    came_from = {}
    g_scores = { (start_cell.x, start_cell.y): 0 }
    opened_nodes = set()

    time_step = 0

    while open_set:
        current_node = heapq.heappop(open_set)
        current_cell = current_node.cell
        current_coords = (current_cell.x, current_cell.y)
        opened_nodes.add(current_coords)

        if current_coords == (goal_cell.x, goal_cell.y):
            path = []
            while current_node:
                path.append((current_node.cell.x, current_node.cell.y))
                current_node = current_node.parent
            return path[::-1], g_scores[goal_cell.x, goal_cell.y], opened_nodes

        for neighbor in grid.get_neighbors(current_cell):
            neighbor_coords = (neighbor.x, neighbor.y)
            tentative_g = g_scores[current_coords] + neighbor.cost

            if neighbor_coords not in g_scores or tentative_g < g_scores[neighbor_coords]:
                g_scores[neighbor_coords] = tentative_g
                new_node = Node(
                    cell=neighbor,
                    parent=current_node,
                    g=tentative_g,
                    h=heuristic(neighbor, goal_cell)
                )
                heapq.heappush(open_set, new_node)
                
        
        time_step+=1


    return None, float('inf'), opened_nodes
