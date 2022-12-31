import pygame

WALL_COLOR = (153, 125, 14)
PLAT_COLOR = (227, 50, 50)

LEVEL_OBJECTS = {
    "walls" : (
        ( (0, 50), (20, 40) ),
        ( (70, 50), (25, 20) ),
        ( (105, 70), (25, 20) )
    ),
    "plats" : (
        ((40, 50), (10, 2)),
        ((95, 50), (10, 2))
    )
}

class LevelObject:

    def __init__(self, size_tuple = (0, 0), position_tuple = (0, 0), rgb_tuple = (0, 0, 0)): 

        self._width, self._height = size_tuple
        self._x, self._y = position_tuple
        self._red, self._green, self._blue = rgb_tuple

    def draw(self, target):
        pygame.draw.rect(
            target, 
            pygame.Color(self._red, self._blue, self._green), 
            pygame.Rect(self._x, self._y, self._width, self._height)
        )

    def set_color(self, rgb_tuple):
        self._red, self._green, self._blue = rgb_tuple


def get_level_objects():

    all_objects = []

    for wall in LEVEL_OBJECTS["walls"]:
        all_objects.append( LevelObject(*wall, WALL_COLOR) )
    for plat in LEVEL_OBJECTS["plats"]:
        all_objects.append( LevelObject(*plat, PLAT_COLOR) )

    return all_objects
