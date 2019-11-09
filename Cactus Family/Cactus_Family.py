# coding=utf-8
from pico2d import *
import game_framework
import pause_state
import stage_clear_state
import title_state

from class_Group import Group
from class_Stone import Stone
from class_Stage import Stage

MAP_WIDTH = 900
MAP_HEIGHT = 800
debug_mode = False
clear = False
now_stage = 1

player = None
<<<<<<< HEAD
=======
cac = None
block = None
game_stage = None
>>>>>>> parent of 19c180e... 스테이지 하나 더 추가
cactus_group = None
game_stage = None

LEFT_COLLISION, TOP_COLLISION, RIGHT_COLLISION, BOTTOM_COLLISION = range(4)
ST_X_NONE, ST_X_FORWARD, ST_X_BAKWARD, ST_Y_NONE, ST_Y_UP, ST_Y_DOWN = range(6)


def next_level():
    global now_stage, clear
    now_stage += 1
    change_stage(now_stage)
    clear = False


def change_stage(level):
    if level == 1:
        game_stage.easy_stage()
    elif level == 2:
        game_stage.normal_stage()
    elif level == 3:
        game_stage.hard_stage()
    elif level == 't':
        game_stage.test_stage()
    else:
        game_stage.test_stage()
    game_stage.setting_stage()


def handle_events():
    global debug_mode, now_stage
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_r:
                change_stage(now_stage)
            elif event.key == SDLK_1:
                now_stage = 1
                change_stage(now_stage)
            elif event.key == SDLK_2:
                now_stage = 2
                change_stage(now_stage)
            elif event.key == SDLK_3:
                now_stage = 3
                change_stage(now_stage)
            elif event.key == SDLK_t:
                change_stage('t')
                for i in range(game_stage.cac_count):
                    cac[i].random_pos()
            elif event.key == SDLK_i:
                debug_mode = not debug_mode
                cactus_group.print_g()
            elif event.key == SDLK_p:
                game_framework.push_state(pause_state)
            else:
                player.handle_Stone(event)
        elif event.type == SDL_KEYUP:
            player.handle_Stone(event)


def enter():
    global player, cac, block, game_stage, cactus_group
    player = Stone()
    cac = []
    block = []
    cactus_group = Group()
    game_stage = Stage()
    game_stage.easy_stage()
    game_stage.setting_stage()


def exit():
<<<<<<< HEAD
    global player, game_stage, cactus_group
    del player
=======
    global player, cac, block, game_stage, cactus_group
    del player
    del cac
    del block
>>>>>>> parent of 19c180e... 스테이지 하나 더 추가
    del game_stage
    del cactus_group


def pause(): pass


def resume(): pass


def update():
    # 클리어 체크
    game_stage.check_stage_clear()
    if clear:
        game_framework.push_state(stage_clear_state)
    player.update()
    # 전체 선인장
    for i in range(game_stage.cac_count):
        cac[i].update()
        cac[i].collision_to_player(i)
        for j in range(game_stage.cac_count):
            if not i == j:
                cac[i].set_collision_state(cac[j])
    # 벽 업데이트
    for i in range(game_stage.block_count):
        block[i].update()
    cactus_group.update()

    handle_events()
    update_canvas()


def draw():
    game_stage.draw_stage()
    player.render()
    # 벽 그리기
    for i in range(game_stage.block_count):
        block[i].render()
    # 선인장 그리기
    for i in range(game_stage.cac_count):
        cac[i].render()
    delay(0.03)
