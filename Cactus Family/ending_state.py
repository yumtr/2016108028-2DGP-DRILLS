import game_framework
import title_state
from pico2d import *

name = "EndingState"
image = None


def enter():
    global image
    image = load_image('image_file\\ending.png')


def exit():
    global image
    del image


def update():
    pass


def draw():
    clear_canvas()
    image.draw(450, 400)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(title_state)


def pause(): pass


def resume(): pass
