import random

from src.utils import print_grid_with_path, print_path, print_path_with_open
random.seed(42)

from src.algorithms.a_star import a_star
from src.grid.grid import Grid



if __name__ == "__main__":
    terrain_types = ['W', 'G', 'M', 'T']
    terrain_weights = [0.1, 0.4, 0.25, 0.15]  

    terrain_map = [
        [random.choices(terrain_types, terrain_weights)[0] for _ in range(50)]
        for _ in range(50)
    ]

    grid = Grid(terrain_map)
    start = (0, 0)
    goal = (49, 47)

    path, cost, opened_nodes = a_star(grid, start, goal)
    #print_grid_with_path(grid, path, opened_nodes)
    print_path(grid, path)

    print('')
    
    print_path_with_open(grid, path, opened_nodes)
    print(f"\nTotal cost: {cost:.2f}")
    print(f"Path length: {len(path) if path else 0}")
