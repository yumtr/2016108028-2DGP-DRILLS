from pico2d import *
import game_framework
import Cactus_Family

image = None
clear_time = 0.0

def enter():
    global image
    image = load_image('Clear.png')


def exit():
    # global image
    # del image
    pass


def update():
    global clear_time
    if clear_time > 1.0:
        clear_time = 0
        resume()
    delay(0.01)
    clear_time += 0.05


def draw():
    clear_canvas()
    Cactus_Family.draw()
    image.draw(450, 400)
    update_canvas()


def pause():
    pass


def resume():
    Cactus_Family.next_level()
    game_framework.pop_state()


def handle_events():
    events = get_events()
    for event in events:
        pass
