from src.grid.terrains.terrains import TerrainType


class Cell:
    def __init__(self, x, y, terrain):
        self.x = x
        self.y = y
        self.terrain = terrain
        self.cost = self.compute_cost()


    def compute_cost(self, time_step=0):
        if self.terrain == TerrainType.WATER:
            return 1
        elif self.terrain == TerrainType.GRASS:
            return 1.2
        elif self.terrain == TerrainType.MUD:
            return 2
        elif self.terrain == TerrainType.TRAFFIC:
            return 1 + time_step * 0.1
