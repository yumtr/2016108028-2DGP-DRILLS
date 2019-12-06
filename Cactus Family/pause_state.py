from pico2d import *
import game_framework
import Cactus_Family

image = None


def enter():
    global image
    image = load_image('image_file\\manual.png')


def exit():
    global image
    del image


def update():
    pass


def draw():
    clear_canvas()
    Cactus_Family.draw()
    image.draw(450, 400)
    update_canvas()


def pause():
    pass


def resume():
    game_framework.pop_state()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            resume()
