# map.py

import pygame

# Tile type constants
DIRT = 0
WALLS = 1

# Example tilemap data
tilemap_data = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


class Tile:
    """A class representing a single tile in the tilemap."""
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface):
        """Draws the tile on the given surface."""
        surface.blit(self.image, self.rect.topleft)

class TileMap:
    """A class to manage the tilemap, including loading and rendering."""
    def __init__(self, tile_size, tilemap_data, tile_images):
        self.tile_size = tile_size
        self.tilemap_data = tilemap_data
        self.tile_images = tile_images
        self.tiles = []

        self.load_map()

    def load_map(self):
        """Loads the tilemap based on the tilemap data."""
        for row_index, row in enumerate(self.tilemap_data):
            for col_index, tile_type in enumerate(row):
                x = col_index * self.tile_size
                y = row_index * self.tile_size
                tile_image = self.tile_images[tile_type]
                tile = Tile(tile_image, x, y)
                self.tiles.append(tile)

    def draw(self, surface):
        """Draws all the tiles on the given surface."""
        for tile in self.tiles:
            tile.draw(surface)

def load_tile_images():
    """Loads and returns a dictionary of tile images."""
    try:
        tile_images = {
            DIRT: pygame.image.load("assets/images/map/tiles/Tilled_Dirt.png").convert_alpha(),
            WALLS: pygame.image.load("assets/images/map/walls/Wooden_House_Walls_Tilset.png").convert_alpha(),
        }
    except pygame.error as e:
        print(f"Failed to load tile images: {e}")
        raise SystemExit(e)
    return tile_images

def create_tile_map():
    """Creates and returns a TileMap object."""
    tile_size = 32  # Size of each tile
    tile_images = load_tile_images()
    tilemap = TileMap(tile_size, tilemap_data, tile_images)
    return tilemap

