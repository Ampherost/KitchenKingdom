class GameMap:
    def __init__(self, map_data):
        self.map_data = map_data  # Could be a 2D list of tiles
        self.tile_width = 64
        self.tile_height = 32

    def render(self, screen):
        for row in range(len(self.map_data)):
            for col in range(len(self.map_data[row])):
                tile = self.map_data[row][col]
                x, y = self.iso_coords(col, row)
                screen.blit(tile.image, (x, y))

    def iso_coords(self, x, y):
        screen_x = (x - y) * (self.tile_width / 2)
        screen_y = (x + y) * (self.tile_height / 2)
        return screen_x, screen_y
