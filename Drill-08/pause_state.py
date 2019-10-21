from pico2d import *
import game_framework
import main_state


image = None
is_draw = False

def timer():
    global is_draw
    delay(0.1)
    is_draw = not is_draw

def enter():
    global image
    image = load_image('pause2.png')


def exit():
    global image
    del image


def update():
    pass


def draw():
    clear_canvas()
    main_state.boy.draw()
    main_state.grass.draw()
    timer()
    if is_draw:
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
