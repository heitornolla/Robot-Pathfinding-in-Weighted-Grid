import heapq

from src.grid.node import Node
from src.heuristic import heuristic
from src.utils import reconstruct_path

def a_star(grid, start_coords, goal_coords):
    start_cell = grid.get_cell(*start_coords)
    goal_cell = grid.get_cell(*goal_coords)

    open_heap = []
    heapq.heappush(open_heap, Node(start_cell, g=0, h=heuristic(start_cell, goal_cell)))
    g_scores = { start_coords: 0 }

    open_coords = set()
    closed_coords = set()

    time_step = 0

    while open_heap:
        current_node = heapq.heappop(open_heap)
        current_cell = current_node.cell
        current_coords = (current_cell.x, current_cell.y)

        if(current_coords in closed_coords):
            continue
        
        closed_coords.add(current_coords)

        time_step+=1

        if current_coords == goal_coords:
            path = reconstruct_path(current_node)
            return path, g_scores[goal_coords], open_coords

        for neighbor in grid.get_neighbors(current_cell):
            neighbor_coords = (neighbor.x, neighbor.y)
            if neighbor_coords in closed_coords:
                continue

            tentative_g = g_scores[current_coords] + neighbor.compute_cost(time_step)

            if neighbor_coords not in g_scores or tentative_g < g_scores[neighbor_coords]:
                g_scores[neighbor_coords] = tentative_g
                new_node = Node(
                    cell=neighbor,
                    parent=current_node,
                    g=tentative_g,
                    h=heuristic(neighbor, goal_cell)
                )
                heapq.heappush(open_heap, new_node)
                open_coords.add(neighbor_coords)
                

    return None, float('inf'), open_coords
