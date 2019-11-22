import game_framework
import Cactus_Family
from pico2d import *

name = "TitleState"
image = None
menu_image = None
arrow = None
arrow_position = 250
menu_num = 1


def choose_menu():
    if menu_num == 1:
        game_framework.change_state(Cactus_Family)
    elif menu_num == 2:
        game_framework.quit()
    elif menu_num == 3:
        # game_framework.quit()
        pass


def move_arrow(y_pos):
    global arrow_position, menu_num
    if y_pos == 0 and menu_num > 1:
        arrow_position += 100
        menu_num -= 1
    elif y_pos == 1 and menu_num < 2:
        arrow_position -= 100
        menu_num += 1


def enter():
    global image, menu_image, arrow
    image = load_image('image_file\\title.png')
    menu_image = load_image('image_file\\menu.png')
    arrow = load_image('image_file\\arrow.png')


def exit():
    global image, menu_image, arrow
    del image, menu_image, arrow


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key in (SDLK_UP, SDLK_w):
                move_arrow(0)
            elif event.key in (SDLK_DOWN, SDLK_s):
                move_arrow(1)
            elif event.key in (SDLK_RETURN, SDLK_SPACE):
                choose_menu()
        elif event.type == SDL_QUIT:
            game_framework.quit()

def draw():
    clear_canvas()
    image.draw(450, 400)
    menu_image.draw(450, 150)
    arrow.draw(235, arrow_position)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
