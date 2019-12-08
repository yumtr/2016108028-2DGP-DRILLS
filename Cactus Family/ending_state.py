import game_framework
import title_state
from pico2d import *
import Cactus_Family

name = "EndingState"
image = None
ending_bgm = None
score_data = None


def load_score_data():
    global score_data
    with open('json_files\\max_score_data.json', 'r') as f:
        score_data = json.load(f)
    # print(score_data[0]['map_1'])


def enter():
    global image, ending_bgm
    image = load_image('image_file\\ending.png')
    ending_bgm = load_music('sound_effect\\ending_bgm.mp3')
    ending_bgm.set_volume(64)
    ending_bgm.repeat_play()


def exit():
    global image, ending_bgm
    ending_bgm.pause()
    del image


def update():
    pass


def draw():
    clear_canvas()
    image.draw(450, 400)
    Cactus_Family.game_stage.print_score()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_KEYDOWN:
                game_framework.change_state(title_state)




def pause(): pass


def resume(): pass
