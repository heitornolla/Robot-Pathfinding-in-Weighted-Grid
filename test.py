import random

from src.utils import print_path_with_open
random.seed(42)

from src.algorithms.a_star import a_star
from src.algorithms.greedy_best_first import greedy_best_first
from src.grid.grid import Grid


# Explain on 5x5 grid, demonstrate on 20x20 and 50x50
# Showcase open nodes while debugging the code

# Add more heuristics to show differences - BFS, DFS, overestimation
if __name__ == "__main__":
    terrain_types = ['W', 'G', 'M', 'T']
    terrain_weights = [0.1, 0.4, 0.25, 0.15]  

    terrain_map = [
        [random.choices(terrain_types, terrain_weights)[0] for _ in range(30)]
        for _ in range(30)
    ]

    grid = Grid(terrain_map)
    start = (0, 0)
    goal = (26, 16)

    path, cost, opened_nodes = a_star(grid, start, goal)

    print('')
    
    print_path_with_open(grid, path, opened_nodes)
    print(f"\nTotal cost: {cost:.2f}")
    print(f"Path length: {len(path) if path else 0}")
    print(f"Opened {len(opened_nodes)} nodes during the search.")

    path, cost, opened_nodes = greedy_best_first(grid, start, goal)

    print('')
    
    print_path_with_open(grid, path, opened_nodes)
    print(f"\nTotal cost: {cost:.2f}")
    print(f"Path length: {len(path) if path else 0}")
    print(f"Opened {len(opened_nodes)} nodes during the search.")
