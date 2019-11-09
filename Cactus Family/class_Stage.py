from pico2d import *
# import class_Stone
# import class_Cactus
import class_Block
import class_Cactus
import Cactus_Family

MAP_WIDTH = 900
MAP_HEIGHT = 800
LEFT_COLLISION, TOP_COLLISION, RIGHT_COLLISION, BOTTOM_COLLISION = range(4)
ST_X_NONE, ST_X_FORWARD, ST_X_BAKWARD, ST_Y_NONE, ST_Y_UP, ST_Y_DOWN = range(6)

<<<<<<< HEAD
clear = False
now_stage = 1

cac = []
block = []


def next_level():
    global now_stage, clear
    now_stage += 1
    change_stage(now_stage)
    clear = False


def change_stage(level):
    if level == 1:
        Cactus_Family.game_stage.easy_stage()
    elif level == 2:
        Cactus_Family.game_stage.normal_stage()
    elif level == 3:
        Cactus_Family.game_stage.hard_stage()
    elif level == 4:
        Cactus_Family.game_stage.level_4()
    elif level == 't':
        Cactus_Family.game_stage.test_stage()
    else:
        Cactus_Family.game_stage.test_stage()
    Cactus_Family.game_stage.setting_stage()


def handle_Stage(event):
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
            for i in range(Cactus_Family.game_stage.cac_count):
                cac[i].random_pos()

=======
>>>>>>> parent of 19c180e... 스테이지 하나 더 추가

def setting_group():
    Cactus_Family.cactus_group.all_cactus.clear()
    Cactus_Family.cactus_group.single_cactus.clear()
    Cactus_Family.cactus_group.merge_cactus_groups.clear()
    for i in range(Cactus_Family.game_stage.cac_count):
        Cactus_Family.cactus_group.all_cactus.append(i)
        Cactus_Family.cactus_group.single_cactus.append(i)


class Stage:
    def __init__(self):
        self.cac_pos = []
        self.block_pos = []
        self.stone_pos = []
        self.clear_pos = []
        self.cac_count = 0
        self.block_count = 0
        self.map_image = 'hi'
        self.map = 0

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

    def easy_stage(self):
        self.map_image = 'image_file\\Map_easy.png'
        self.cac_pos = [(6, 3), (5, 6), (3, 6)]
        self.clear_pos = [(3, 3), (3, 4), (2, 4)]
        self.stone_pos = [4, 5]
        self.block_pos = [(7, 3), (8, 4), (8, 5), (7, 6), (6, 7), (5, 8), (4, 9), (3, 8), (2, 7),
                          (1, 6), (0, 5), (0, 4), (1, 3), (2, 2), (3, 1), (4, 2), (5, 1), (6, 2)]
        self.cac_count = len(self.cac_pos)
        self.block_count = len(self.block_pos)

    def normal_stage(self):
        self.map_image = 'image_file\\Map_normal.png'
        self.cac_pos = [(2, 2), (6, 3), (2, 6), (2, 7)]
        self.clear_pos = [(4, 4), (3, 4), (3, 5), (2, 4)]
        self.stone_pos = [4, 5]
        self.block_pos = [(8, 4), (4, 0), (3, 0), (0, 3), (1, 4), (0, 5), (0, 6),
                          (3, 9), (2, 9), (7, 3), (7, 5), (7, 6), (6, 7), (5, 8),
                          (4, 8), (0, 8), (1, 7), (1, 2), (2, 1), (5, 1), (6, 2)]
        self.cac_count = len(self.cac_pos)
        self.block_count = len(self.block_pos)

    def hard_stage(self):
        self.map_image = 'image_file\\Map_hard.png'
        self.cac_pos = [(6, 4), (5, 8), (4, 2), (4, 4), (1, 3), (1, 5)]
        self.clear_pos = [(5, 4), (5, 5), (4, 3), (4, 4), (3, 4), (2, 4)]
        self.stone_pos = [4, 5]
        self.block_pos = [(7, 2), (7, 3), (7, 4), (6, 5), (7, 6), (7, 7), (6, 8), (5, 9), (4, 9), (3, 9), (2, 8),
                          (1, 7), (1, 6), (0, 5), (1, 4), (0, 3), (1, 2), (2, 1), (3, 1), (4, 0), (5, 0), (6, 1)]
        self.cac_count = len(self.cac_pos)
        self.block_count = len(self.block_pos)

    def setting_stage(self):
        self.map = load_image(self.map_image)
        Cactus_Family.player.__init__(self.stone_pos)
        for i in range(self.cac_count):
<<<<<<< HEAD
            cac.append(Cactus())
            cac[i].__init__(self.cac_pos[i])
        for i in range(self.block_count):
            block.append(Block())
            block[i].__init__(self.block_pos[i])
=======
            Cactus_Family.cac.append(class_Cactus.Cactus())
            Cactus_Family.cac[i].__init__()
            Cactus_Family.cac[i].set_position(self.cac_pos[i])
        for i in range(self.block_count):
            Cactus_Family.block.append(class_Block.Block())
            Cactus_Family.block[i].__init__()
            Cactus_Family.block[i].set_position(self.block_pos[i])
>>>>>>> parent of 19c180e... 스테이지 하나 더 추가
        # 선인장 그룹 초기화해주고 다시만들어줌
        setting_group()

    def check_stage_clear(self):
        cac_array = []
        for i in range(self.cac_count):
            cac_array.append((Cactus_Family.cac[i].get_pos()))
        self.clear_pos.sort()
        cac_array.sort()

        if self.clear_pos == cac_array:
            Cactus_Family.clear = True

    def draw_stage(self):
        self.map.draw(MAP_WIDTH // 2, MAP_HEIGHT // 2)
