from pico2d import *
import game_framework
import main_state


image = None


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del image


def update():
    pass


def draw():
    clear_canvas()
    image.draw(400, 300)
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
