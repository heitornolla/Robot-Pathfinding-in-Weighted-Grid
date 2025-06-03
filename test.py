import random
random.seed(42)

from src.algorithms.a_star import a_star
from src.algorithms.bfs import breadth_first_search
from src.algorithms.dfs import depth_first_search
from src.algorithms.greedy_best_first import greedy_best_first

from src.grid.grid import Grid
from src.utils import print_path_with_open


terrain_types = ['W', 'G', 'M', 'T']
terrain_weights = [0.25, 0.25, 0.25, 0.25]  

terrain_map = [
    [random.choices(terrain_types, terrain_weights)[0] for _ in range(50)]
    for _ in range(50)
]

grid = Grid(terrain_map)
start = (0, 0)
goal = (49, 49)


def test_algorithms(grid, start, goal):
    algorithms = {
        "A*": a_star,
        "Greedy Best-First": greedy_best_first,
        "Breadth-First Search": breadth_first_search,
        "Depth-First Search": depth_first_search
    }

    results = {}
    for name, algo in algorithms.items():
        path, cost, opened = algo(grid, start, goal)
        results[name] = {
            "path_length": len(path),
            "cost": cost,
            "nodes_opened": len(opened)
        }
    return results


if __name__ == "__main__":
    results = test_algorithms(grid, start, goal)

    for name, data in results.items():
        print(f"{name}: Cost={data['cost']:.2f}, Opened={data['nodes_opened']}")
