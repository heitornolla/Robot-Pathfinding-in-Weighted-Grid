import random
def generate_terrain_map(width, height, terrain_types, terrain_weights, seed):
    random.seed(seed)
    terrain_map = [
        [random.choices(terrain_types, terrain_weights)[0] for _ in range(width)]
        for _ in range(height)
    ]
    return terrain_map

def reconstruct_path(node):
    path = []
    while node:
        path.append((node.cell.x, node.cell.y))
        node = node.parent
    path.reverse()
    return path

def print_path_with_open(grid, path, open_coords):
    path_set = set(path)
    open_coords = set(open_coords)

    for y in range(grid.height):
        row = ''
        for x in range(grid.width):
            coord = (x, y)
            if coord in path_set:
                row += '🟩'  # Path
            elif coord in open_coords:
                row += '🟪'  # Opened node
            else:
                terrain = grid.get_cell(x, y).terrain
                symbols = {
                    'G': '🟢',  # Grass
                    'W': '🔵',  # Water
                    'M': '🟤',  # Mud
                    'T': '🟥',  # Traffic
                }
                row += symbols[terrain]
        print(row)


def print_path(grid, path):
    for y in range(grid.height):
        row = ''
        for x in range(grid.width):
            if (x, y) in path:
                row += '🟩'  # Path cell
            else:
                terrain = grid.get_cell(x, y).terrain
                symbols = {'G': '🟢', 'W': '🔵', 'M': '🟤', 'T': '🟥'}
                row += symbols[terrain]
        print(row)
