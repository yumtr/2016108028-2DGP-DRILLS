from pico2d import *
import game_framework
import Cactus_Family
import class_Stage
import ending_state

MAP_WIDTH = 900
MAP_HEIGHT = 800
image = None
star = [None, None, None, None]
score = 1
clear_time = 0.0
score_text = []


def enter():
    global image, star, score_text, score
    score_text = load_font('font\\CookieRun Bold.ttf')
    image = load_image('image_file\\Clear.png')
    star[0] = load_image('image_file\\star_0.png')
    star[1] = load_image('image_file\\star_1.png')
    star[2] = load_image('image_file\\star_2.png')
    star[3] = load_image('image_file\\star_3.png')
    score = Cactus_Family.game_stage.star_rank


def exit():
    # global image
    # del image
    pass


def update():
    global clear_time
    if clear_time > 50.0:
        clear_time = 0
        resume()
    delay(0.01)
    clear_time += 0.05


def draw():
    clear_canvas()
    Cactus_Family.draw()
    image.draw(450, 400)
    star[score].draw(450, 400)
    score_text.draw(MAP_WIDTH / 2 - 95, MAP_HEIGHT / 2 - 10, '최종 움직인 횟수 : ' + str(Cactus_Family.player.move_count), color=(255, 255, 255))
    update_canvas()


def pause():
    pass


def resume():
    class_Stage.next_level()
    if class_Stage.now_stage == class_Stage.MAX_LEVEL:
        game_framework.change_state(ending_state)
    else:
        game_framework.pop_state()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and clear_time > 0.5:
            resume()
