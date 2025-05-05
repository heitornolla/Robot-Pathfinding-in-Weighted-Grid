from src.grid.cell import Cell


class Grid:
    def __init__(self, terrain_map):
        self.width = len(terrain_map[0])
        self.height = len(terrain_map[1])
        self.cells = [
            [Cell(x, y, terrain_map[y][x]) for x in range(self.width)]
            for y in range(self.height)
        ]


    def get_cell(self, x, y):
        return self.cells[y][x]


    def get_neighbors(self, cell):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = cell.x + dx, cell.y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbors.append(self.get_cell(nx, ny))
        return neighbors
