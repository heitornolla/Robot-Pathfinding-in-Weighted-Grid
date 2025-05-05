from src.algorithms.a_star import a_star
from src.grid.grid import Grid




def print_grid_with_path(grid, path, opened=None):
    print("\nGrid Visualization (P = Path, O = Opened node):\n")
    for y in range(grid.height):
        row = ''
        for x in range(grid.width):
            cell = grid.get_cell(x, y)
            coord = (x, y)
            if path and coord in path:
                row += ' P '
            elif opened and coord in opened:
                row += ' O '
            else:
                row += f' {cell.terrain} '
        print(row)


terrain_map = [
    ['G', 'G', 'G', 'G', 'G', 'T', 'T', 'M', 'G', 'W', 'W', 'W', 'G', 'G', 'G', 'T', 'T', 'G', 'G', 'G'],
    ['G', 'M', 'M', 'G', 'G', 'T', 'T', 'G', 'G', 'W', 'G', 'G', 'G', 'M', 'M', 'G', 'T', 'T', 'M', 'G'],
    ['G', 'G', 'G', 'M', 'G', 'G', 'T', 'G', 'W', 'W', 'W', 'G', 'M', 'G', 'T', 'G', 'T', 'M', 'G', 'G'],
    ['M', 'M', 'G', 'G', 'T', 'G', 'T', 'M', 'G', 'G', 'G', 'M', 'G', 'G', 'G', 'G', 'G', 'T', 'M', 'G'],
    ['G', 'T', 'T', 'T', 'G', 'M', 'M', 'G', 'T', 'W', 'W', 'W', 'T', 'M', 'G', 'T', 'G', 'G', 'G', 'G'],
    ['G', 'G', 'G', 'G', 'M', 'G', 'T', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'M', 'T', 'T', 'M', 'G', 'G'],
    ['G', 'M', 'T', 'T', 'G', 'W', 'W', 'W', 'M', 'G', 'T', 'T', 'G', 'G', 'G', 'G', 'M', 'M', 'G', 'G'],
    ['T', 'T', 'G', 'G', 'G', 'G', 'G', 'G', 'T', 'M', 'M', 'G', 'G', 'T', 'T', 'M', 'G', 'G', 'G', 'G'],
    ['W', 'W', 'W', 'M', 'G', 'T', 'G', 'G', 'G', 'G', 'G', 'T', 'M', 'M', 'G', 'G', 'T', 'G', 'W', 'W'],
    ['M', 'G', 'T', 'G', 'G', 'G', 'M', 'T', 'T', 'M', 'G', 'G', 'G', 'G', 'G', 'M', 'T', 'T', 'G', 'G'],
    ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'M', 'M', 'T', 'G', 'T', 'T', 'W', 'W', 'W', 'M', 'G', 'T', 'G'],
    ['G', 'T', 'T', 'G', 'W', 'W', 'W', 'M', 'G', 'T', 'M', 'G', 'G', 'T', 'T', 'G', 'G', 'G', 'M', 'G'],
    ['G', 'G', 'M', 'M', 'G', 'G', 'T', 'T', 'G', 'G', 'G', 'G', 'M', 'G', 'T', 'M', 'G', 'W', 'W', 'G'],
    ['G', 'G', 'G', 'T', 'T', 'G', 'M', 'G', 'W', 'W', 'W', 'T', 'G', 'M', 'G', 'T', 'G', 'G', 'G', 'G'],
    ['T', 'T', 'M', 'M', 'G', 'G', 'G', 'T', 'G', 'G', 'G', 'G', 'G', 'T', 'G', 'M', 'T', 'G', 'M', 'G'],
    ['M', 'G', 'T', 'T', 'M', 'G', 'G', 'G', 'M', 'T', 'T', 'G', 'W', 'W', 'W', 'G', 'M', 'G', 'T', 'G'],
    ['G', 'G', 'G', 'G', 'G', 'T', 'T', 'M', 'G', 'G', 'G', 'T', 'M', 'G', 'G', 'G', 'T', 'G', 'G', 'G'],
    ['G', 'M', 'M', 'G', 'W', 'W', 'W', 'T', 'G', 'M', 'G', 'G', 'G', 'M', 'T', 'T', 'G', 'G', 'G', 'M'],
    ['G', 'G', 'T', 'M', 'G', 'G', 'T', 'T', 'M', 'G', 'T', 'T', 'M', 'G', 'W', 'W', 'W', 'T', 'G', 'G'],
    ['G', 'G', 'G', 'G', 'G', 'M', 'T', 'G', 'G', 'G', 'G', 'M', 'T', 'T', 'G', 'G', 'G', 'M', 'G', 'M']
]

if __name__ == "__main__":
    grid = Grid(terrain_map)
    start = (0, 0)
    goal = (19, 19)

    path, cost, opened_nodes = a_star(grid, start, goal)
    print_grid_with_path(grid, path, opened_nodes)
    print(f"\nTotal cost: {cost:.2f}")
    print(f"Path length: {len(path) if path else 0}")

