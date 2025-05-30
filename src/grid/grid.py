from typing import List
from src.grid.cell import Cell


class Grid:
    """
    Grid representation with terrain-based cells.
    """
    def __init__(self, terrain_map: List[List[str]]):
        self.width = len(terrain_map[0])
        self.height = len(terrain_map[1])
        self.cells = [
            [Cell(x, y, terrain_map[y][x]) for x in range(self.width)]
            for y in range(self.height)
        ]


    def get_cell(self, x: int, y: int) -> Cell:
        return self.cells[y][x]


    def get_neighbors(self, cell: Cell) -> List[Cell]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = cell.x + dx, cell.y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbors.append(self.get_cell(nx, ny))
        return neighbors
    
    def __repr__(self):
        grid_to_string = f"{self.width} x {self.height} grid"

        return grid_to_string
