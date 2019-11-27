import game_framework
import world_build_state
import world_build_state as start_state
import game_world
from pico2d import *

name = "ScoreState"
image = None
font = None

def enter():
    global image, font
    image = load_image('title.png')
    font = load_font('ENCR10B.TTF', 20)


def exit():
    global image
    del (image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(start_state)


def draw():
    clear_canvas()
    for i in range(min(10, len(game_world.ranking))):
        font.draw(700, 700-i * 20, str(game_world.ranking[i]))
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
