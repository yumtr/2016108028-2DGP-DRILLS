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
size_x = 0
size_y = 0
pop_speed = 5
clear_sound = None


def enter():
    global image, star, score_text, score, size_x, size_y, pop_speed, clear_time, clear_sound
    score_text = load_font('font\\CookieRun Bold.ttf', 20)
    image = load_image('image_file\\Clear.png')
    star[0] = load_image('image_file\\star_0.png')
    star[1] = load_image('image_file\\star_1.png')
    star[2] = load_image('image_file\\star_2.png')
    star[3] = load_image('image_file\\star_3.png')
    score = Cactus_Family.game_stage.star_rank
    size_x = 0
    size_y = 0
    pop_speed = 5
    clear_time = 0.0
    clear_sound = load_wav('sound_effect\\00002991.wav')
    clear_sound.set_volume(100)
    clear_sound.play()


def exit():
    global clear_sound
    # del image
    clear_sound.set_volume(0)


def update():
    global clear_time, size_x, size_y, pop_speed
    if size_x < 450:
        size_x += 450 / 5 / pop_speed
    if size_y < 356:
        size_y += 356 / 5 / pop_speed
    if clear_time > 50.0:
        clear_time = 0
        resume()
    delay(0.01)
    clear_time += 0.05
    if pop_speed != 1:
        pop_speed -= 1


def draw():
    clear_canvas()
    Cactus_Family.draw()
    image.draw(450, 400, size_x, size_y)
    star[score].draw(450, 400, size_x, size_y)
    if clear_time > 0.3:
        score_text.draw(MAP_WIDTH / 2 - 90, MAP_HEIGHT / 2 - 10, '최종 움직인 횟수 : ' + str(Cactus_Family.player.move_count), color=(255, 255, 255))
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
