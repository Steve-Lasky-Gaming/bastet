#!/usr/bin/env python3

import pygame
import sys
import threading
import time

level_data = {
    "width" : 200,
    "height" : 100,
    "objects" :
        [
            {"type" : "wall",  "x" :   0, "y" : 50, "w" : 20, "h" : 40},
            {"type" : "hplat", "x" :  40, "y" : 50, "w" : 10, "h" :  2},
            {"type" : "wall",  "x" :  70, "y" : 50, "w" : 25, "h" : 20},
            {"type" : "vplat", "x" :  95, "y" : 50, "w" : 10, "h" :  2},
            {"type" : "wall",  "x" : 105, "y" : 70, "w" : 25, "h" : 20},
        ]
}

render_lock = threading.Lock()
shutdown = False

screen = None

def render_thread_proc():
    while not shutdown:
        screen.fill(pygame.Color(50, 35, 20))

        with render_lock:
            # everything is a box for the moment
            for obj in level_data["objects"]:
                if obj["type"] == "wall":
                    pygame.draw.rect(screen, pygame.Color(153, 125, 14),
                            pygame.Rect(obj["x"], obj["y"], obj["w"], obj["h"]))
                elif obj["type"] == "hplat":
                    pygame.draw.rect(screen, pygame.Color(227, 50, 50),
                            pygame.Rect(obj["x"], obj["y"], obj["w"], obj["h"]))
                elif obj["type"] == "vplat":
                    pygame.draw.rect(screen, pygame.Color(78, 176, 245),
                            pygame.Rect(obj["x"], obj["y"], obj["w"], obj["h"]))

        pygame.display.flip()

def main():
    global screen
    global shutdown

    pygame.init()
    screen = pygame.display.set_mode((320, 240))

    render_thread = threading.Thread(target=render_thread_proc)
    render_thread.start()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with render_lock:
                    shutdown = True
                render_thread.join()
                sys.exit(0)
        time.sleep(1./60)

main()
