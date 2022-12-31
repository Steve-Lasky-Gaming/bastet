import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 720, 480
SCREEN_COLOR = (162, 103, 105)
WALL_COLOR = (213, 185, 178)
PLAT_COLOR = (109, 46, 70)

GROUND_LEVEL = 128
WALL_WIDTH = 64

LEVEL_OBJECTS = {
    # object_name, (width, height), (x_pos, y_pos)
    "walls" : (
        ( "left_wall", (WALL_WIDTH, SCREEN_HEIGHT - GROUND_LEVEL), (0, GROUND_LEVEL) ),
        ( "center_wall", (WALL_WIDTH, SCREEN_HEIGHT - GROUND_LEVEL), ((SCREEN_WIDTH - 2 * WALL_WIDTH)  / 2, GROUND_LEVEL) ),
        ( "right_wall", (WALL_WIDTH, SCREEN_HEIGHT - GROUND_LEVEL), (SCREEN_WIDTH - WALL_WIDTH, GROUND_LEVEL) )
    ),
    "plats" : (
        ("left_plat", (64, 64), (0.25 * SCREEN_WIDTH, GROUND_LEVEL + 128)),
        ("right_plat", (64, 64), (0.75 * SCREEN_WIDTH, GROUND_LEVEL + 128))
    )
}

class LevelObject:

    def __init__(self, obj_name, size_tuple = (0, 0), position_tuple = (0, 0), rgb_tuple = (0, 0, 0)): 

        self._name = obj_name
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
