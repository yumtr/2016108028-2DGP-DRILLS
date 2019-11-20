from pico2d import *
from class_Block import Block
from class_Cactus import Cactus
import Cactus_Family
import game_framework
import stage_clear_state
import ending_state

MAX_LEVEL = 5
MAP_WIDTH = 900
MAP_HEIGHT = 800
LEFT_COLLISION, TOP_COLLISION, RIGHT_COLLISION, BOTTOM_COLLISION = range(4)
ST_X_NONE, ST_X_FORWARD, ST_X_BAKWARD, ST_Y_NONE, ST_Y_UP, ST_Y_DOWN = range(6)

clear = False
now_stage = 1

cac = []
block = []


def next_level():
    game_stage = Cactus_Family.get_game_stage()
    global now_stage, clear
    game_stage.set_stage_score()
    print(game_stage.map_score[now_stage], now_stage)
    now_stage += 1
    change_stage(now_stage)
    clear = False


def change_stage(level):
    game_stage = Cactus_Family.get_game_stage()
    if level == 1:
        game_stage.level_1()
    elif level == 2:
        game_stage.level_2()
    elif level == 3:
        game_stage.level_3()
    elif level == 4:
        game_stage.level_4()
    elif level == 't':
        game_stage.test_stage()
    else:
        game_stage.test_stage()
    game_stage.setting_stage()


# game_framework.push_state(ending_state)


def handle_Stage(event):
    game_stage = Cactus_Family.get_game_stage()
    global now_stage, cac
    if event.type == SDL_KEYDOWN:
        if event.key == SDLK_r:
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
        elif event.key == SDLK_4:
            now_stage = 4
            change_stage(now_stage)
        elif event.key == SDLK_t:
            change_stage('t')
            for i in range(game_stage.cac_count):
                cac[i].random_pos()


def setting_group():
    game_stage = Cactus_Family.get_game_stage()
    cactus_group = Cactus_Family.get_cactus_group()
    cactus_group.all_cactus.clear()
    cactus_group.single_cactus.clear()
    cactus_group.merge_cactus_groups.clear()
    for i in range(game_stage.cac_count):
        cactus_group.all_cactus.append(i)
        cactus_group.single_cactus.append(i)


class Stage:
    global cac, now_stage

    def __init__(self):
        self.text = load_font('font\\CookieRun Bold.ttf')
        self.cac_pos = []
        self.block_pos = []
        self.stone_pos = []
        self.clear_pos = []
        self.cac_count = 0
        self.block_count = 0
        self.map_image = 'hi'
        self.map = 0
        self.score = 0
        self.map_score = [0, 0, 0, 0, 0, 0]
        self.player = Cactus_Family.get_stone()

    def print_score(self):
        for i in range(MAX_LEVEL - 1):
            self.text.draw(MAP_WIDTH / 2, MAP_HEIGHT / 3 - (50 * i), str(i + 1) + '스테이지 기록 ' + str(self.map_score[i + 1]), color=(255, 255, 255))

    def set_stage_score(self):
        if now_stage != MAX_LEVEL:
            self.map_score[now_stage] = self.player.move_count

    def test_stage(self):
        self.map_image = 'image_file\\Map_test.png'
        self.clear_pos = []
        self.cac_pos = [(4, 3), (6, 7), (5, 7), (4, 7), (3, 7), (2, 7)]
        self.stone_pos = [4, 5]
        self.block_pos = [(8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (7, 9), (6, 9), (5, 9),
                          (4, 9), (3, 9), (2, 9), (1, 9), (0, 8), (0, 7), (0, 6), (0, 5), (0, 4), (0, 3), (0, 2),
                          (0, 1), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
        self.cac_count = len(self.cac_pos)
        self.block_count = len(self.block_pos)

    def level_1(self):
        self.map_image = 'image_file\\Map_easy.png'
        self.cac_pos = [(6, 3), (5, 6), (3, 6)]
        self.clear_pos = [(3, 3), (3, 4), (2, 4)]
        self.stone_pos = [4, 5]
        self.block_pos = [(7, 3), (8, 4), (8, 5), (7, 6), (6, 7), (5, 8), (4, 9), (3, 8), (2, 7),
                          (1, 6), (0, 5), (0, 4), (1, 3), (2, 2), (3, 1), (4, 2), (5, 1), (6, 2)]
        self.cac_count = len(self.cac_pos)
        self.block_count = len(self.block_pos)

    def level_2(self):
        self.map_image = 'image_file\\Map_normal.png'
        self.cac_pos = [(2, 2), (6, 3), (2, 6), (2, 7)]
        self.clear_pos = [(4, 4), (3, 4), (3, 5), (2, 4)]
        self.stone_pos = [4, 5]
        self.block_pos = [(8, 4), (4, 0), (3, 0), (0, 3), (1, 4), (0, 5), (0, 6),
                          (3, 9), (2, 9), (7, 3), (7, 5), (7, 6), (6, 7), (5, 8),
                          (4, 8), (0, 8), (1, 7), (1, 2), (2, 1), (5, 1), (6, 2)]
        self.cac_count = len(self.cac_pos)
        self.block_count = len(self.block_pos)

    def level_3(self):
        self.map_image = 'image_file\\Map_hard.png'
        self.cac_pos = [(6, 4), (5, 8), (4, 2), (4, 4), (1, 3), (1, 5)]
        self.clear_pos = [(5, 4), (5, 5), (4, 3), (4, 4), (3, 4), (2, 4)]
        self.stone_pos = [4, 5]
        self.block_pos = [(7, 2), (7, 3), (7, 4), (6, 5), (7, 6), (7, 7), (6, 8), (5, 9), (4, 9), (3, 9), (2, 8),
                          (1, 7), (1, 6), (0, 5), (1, 4), (0, 3), (1, 2), (2, 1), (3, 1), (4, 0), (5, 0), (6, 1)]
        self.cac_count = len(self.cac_pos)
        self.block_count = len(self.block_pos)

    def level_4(self):
        self.map_image = 'image_file\\Map_4.png'
        self.cac_pos = [(7, 7), (6, 4), (5, 5), (6, 7), (4, 2), (3, 3), (2, 6), (1, 6)]
        self.clear_pos = [(5, 6), (4, 4), (4, 5), (4, 6), (3, 2), (3, 3), (3, 4), (2, 4)]
        self.stone_pos = [4, 5]
        self.block_pos = [(8, 2), (8, 7), (7, 1), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8), (6, 1), (6, 9), (5, 0),
                          (5, 8), (4, 0), (4, 9), (3, 0), (3, 9), (2, 1), (2, 8), (1, 2), (1, 7), (0, 3), (0, 4),
                          (0, 5), (0, 6)]
        self.cac_count = len(self.cac_pos)
        self.block_count = len(self.block_pos)

    def setting_stage(self):
        self.map = load_image(self.map_image)
        self.player.__init__(self.stone_pos)
        for i in range(self.cac_count):
            cac.append(Cactus())
            cac[i].__init__(self.cac_pos[i])
        for i in range(self.block_count):
            block.append(Block())
            block[i].__init__(self.block_pos[i])
        # 선인장 그룹 초기화해주고 다시만들어줌
        setting_group()

    def check_stage_clear(self):
        cac_array = []
        for i in range(self.cac_count):
            cac_array.append((cac[i].get_pos()))
        self.clear_pos.sort()
        cac_array.sort()

        if self.clear_pos == cac_array:
            game_framework.push_state(stage_clear_state)

    def draw_stage(self):
        global now_stage
        self.map.draw(MAP_WIDTH // 2, MAP_HEIGHT // 2)
        self.text.draw(10, MAP_HEIGHT - 25, '스테이지 ' + str(now_stage), color=(255, 255, 255))
        self.text.draw(10, MAP_HEIGHT - 50, '성적 ' + str(self.map_score[now_stage]), color=(255, 255, 255))

