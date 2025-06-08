def reconstruct_path(node):
    path = []
    while node:
        path.append((node.cell.x, node.cell.y))
        node = node.parent
    path.reverse()
    return path

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


def print_path_with_open(grid, path, opened_set):
    path_set = set(path)
    opened_set = set(opened_set)

    for y in range(grid.height):
        row = ''
        for x in range(grid.width):
            coord = (x, y)
            if coord in path_set:
                row += '🟩'  # Path
            elif coord in opened_set:
                row += '🟨'  # Opened node
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
                row += '🟪'  # Path cell
            else:
                terrain = grid.get_cell(x, y).terrain
                symbols = {'G': '🟢', 'W': '🔵', 'M': '🟤', 'T': '🟥'}
                row += symbols[terrain]
        print(row)
