import pygame
import sys
import threading
import time

from level import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_COLOR, get_level_objects



def render_thread_proc(level_objects, screen, render_lock, shutdown):
    while not shutdown:
        screen.fill(SCREEN_COLOR)
        with render_lock:
            for obj in level_objects:
                obj.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":

    screen = None
    render_lock = threading.Lock()
    shutdown = False

    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    level_objects = get_level_objects()

    render_thread = threading.Thread(target = lambda : render_thread_proc(level_objects, screen, render_lock, shutdown))
    render_thread.start()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with render_lock:
                    shutdown = True
                render_thread.join()
                sys.exit(0)
        time.sleep(1./60)

