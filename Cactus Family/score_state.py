import game_framework
from pico2d import *
import Cactus_Family
import json

MAP_WIDTH, MAP_HEIGHT = 900, 800
name = "ScoreState"
image = None
text = None
score_data = []
NO_SCORE = 10000
select_sound = None
clear_score_sound = None


def load_score_data():
    global score_data
    with open('json_files\\max_score_data.json', 'r') as f:
        score_data = json.load(f)
    # print(score_data[0]['map_1'])


def reset_score():
    reset_num = [NO_SCORE for i in range(4)]
    with open('json_files\\max_score_data.json', 'w') as f:
        json.dump(reset_num, f)


def enter():
    global image, text, select_sound, clear_score_sound
    text = load_font('font\\CookieRun Bold.ttf', 50)
    image = load_image('image_file\\score_state.png')
    load_score_data()
    select_sound = load_wav('sound_effect\\pause_sound.wav')
    select_sound.set_volume(100)
    clear_score_sound = load_wav('sound_effect\\clear_score_sound.wav')
    clear_score_sound.set_volume(100)


def exit():
    global image
    del image


def update():
    pass


def draw():
    clear_canvas()
    image.draw(450, 400)
    for i in range(4):
        if score_data[i] == NO_SCORE:
            score_data[i] = 'No Score'
        text.draw(180, 500 - (i * 100), '스테이지 ' + str(i + 1) + ' - ' + str(score_data[i]), color=(255, 255, 255))
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_r:
                    reset_score()
                    game_framework.pop_state()
                    clear_score_sound.play()
                else:
                    game_framework.pop_state()
                    select_sound.play()


def pause(): pass


def resume(): pass
