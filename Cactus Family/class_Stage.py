from pico2d import *
from class_Block import Block
from class_Cactus import Cactus
import Cactus_Family
import game_framework
import stage_clear_state
import ending_state
import json

MAP_WIDTH, MAP_HEIGHT = 900, 800
NO_SCORE = 10000
LEFT_COLLISION, TOP_COLLISION, RIGHT_COLLISION, BOTTOM_COLLISION = range(4)
ST_X_NONE, ST_X_FORWARD, ST_X_BAKWARD, ST_Y_NONE, ST_Y_UP, ST_Y_DOWN = range(6)

clear = False
now_stage = 1
cac = []
block = []
map_stage = []
map_amount = None


def load_map_data():
    global map_stage, map_amount
    with open('stage_data.json', 'r') as f:
        map_data = json.load(f)
    map_amount = len(map_data)
    print('맵갯수', map_amount)
    for data in map_data:
        map_stage.append(
            Stage(data['map_image'], data['cac_pos'], data['stone_pos'], data['block_pos'], data['clear_pos'],
                  data['star_standard']))


def next_level():
    game_stage = Cactus_Family.get_game_stage()
    global now_stage, clear
    game_stage.set_stage_score()
    print(game_stage.max_map_score[now_stage - 1], now_stage)
    now_stage += 1
    print(now_stage, ' hi ', map_amount)
    if now_stage == map_amount:
        with open('max_score_data.json', 'w') as f:
            json.dump(game_stage.max_map_score, f)
        game_framework.push_state(ending_state)
        game_stage.bgm.pause()
    else:
        change_stage(now_stage)
    clear = False


def change_stage(level):
    game_stage = Cactus_Family.get_game_stage()
    game_stage.start_sound.play()
    game_stage.set_map_data(level)
    game_stage.setting_stage()


def handle_Stage(event):
    game_stage = Cactus_Family.get_game_stage()
    global now_stage, cac
    if event.type == SDL_KEYDOWN:
        if event.key == SDLK_r:
            game_stage.restart_sound.play()
            change_stage(now_stage)
        if Cactus_Family.debug_mode:
            if event.key == SDLK_1:
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
                change_stage(0)
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


def get_cactus():
    return cac


def get_block():
    return block


class Stage:
    global now_stage

    def __init__(self, map_image='hi', cac_pos=None, stone_pos=None, block_pos=None, clear_pos=None,
                 star_standard=None):
        if clear_pos is None:
            clear_pos = []
        if star_standard is None:
            star_standard = []
        if cac_pos is None:
            cac_pos = []
        if block_pos is None:
            block_pos = []
        if stone_pos is None:
            stone_pos = []
        self.text = load_font('font\\CookieRun Bold.ttf')
        self.map_image = map_image
        self.cac_pos = cac_pos
        self.block_pos = block_pos
        self.stone_pos = stone_pos
        self.clear_pos = clear_pos
        self.star_standard = star_standard
        self.cac_count = len(self.cac_pos)
        self.block_count = len(self.block_pos)
        self.map = 0
        self.star_rank = 0
        self.max_map_score = [NO_SCORE for i in range(4)]
        self.player = Cactus_Family.get_stone()
        self.start_sound = load_wav('sound_effect\\stage_start.wav')
        self.start_sound.set_volume(100)
        self.restart_sound = load_wav('sound_effect\\restart.wav')
        self.restart_sound.set_volume(100)
        self.bgm = load_music('sound_effect\\game_bgm.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def print_score(self):
        global map_amount
        for i in range(map_amount - 1):
            self.text.draw(MAP_WIDTH / 2 - 200, MAP_HEIGHT / 3 - (50 * i),
                           '스테이지 - ' + str(i + 1) + ' 이동횟수 : ' + str(self.max_map_score[i]), color=(255, 255, 255))

    def set_stage_score(self):
        if now_stage != map_amount and self.max_map_score[now_stage - 1] > self.player.move_count:
            self.max_map_score[now_stage - 1] = self.player.move_count

    def set_map_data(self, level):
        self.map_image = map_stage[level].map_image
        print('맵이름', map_stage[level].map_image)
        for i in range(len(map_stage[level].cac_pos)):
            map_stage[level].cac_pos[i] = list(map(int, map_stage[level].cac_pos[i]))
        self.cac_pos = map_stage[level].cac_pos
        print('선인장', self.cac_pos)
        for i in range(len(map_stage[level].clear_pos)):
            map_stage[level].clear_pos[i] = list(map(int, map_stage[level].clear_pos[i]))
        self.clear_pos = map_stage[level].clear_pos
        print('클리어', self.clear_pos)
        self.stone_pos = list(map(int, map_stage[level].stone_pos))
        print('돌', self.stone_pos)
        for i in range(len(map_stage[level].block_pos)):
            map_stage[level].block_pos[i] = list(map(int, map_stage[level].block_pos[i]))
        self.block_pos = map_stage[level].block_pos
        print('블럭', self.block_pos)
        self.star_standard = list(map(int, map_stage[level].star_standard))
        print('등급', self.star_standard)
        self.cac_count = map_stage[level].cac_count
        print('선인장 수', map_stage[level].cac_count)
        self.block_count = map_stage[level].block_count
        print('블럭 수', map_stage[level].block_count)

    def setting_stage(self):
        cac.clear()
        block.clear()
        self.map = load_image(self.map_image)
        self.player.__init__(self.stone_pos)
        for i in range(self.cac_count):
            cac.append(Cactus(self.cac_pos[i]))
        for i in range(self.block_count):
            block.append(Block())
            block[i].__init__(self.block_pos[i])
        # 선인장 그룹 초기화해주고 다시만들어줌
        setting_group()

    def check_stage_clear(self):
        cac_array = []
        for i in range(self.cac_count):
            cac_array.append(cac[i].get_pos())
        self.clear_pos.sort()
        cac_array.sort()

        if self.clear_pos == cac_array:
            if self.player.move_count < self.star_standard[0]:
                self.star_rank = 3
            elif self.player.move_count < self.star_standard[1]:
                self.star_rank = 2
            elif self.player.move_count < self.star_standard[2]:
                self.star_rank = 1
            else:
                self.star_rank = 0
            game_framework.push_state(stage_clear_state)

    def draw_stage(self):
        global now_stage
        self.map.draw(MAP_WIDTH // 2, MAP_HEIGHT // 2)
        self.text.draw(45, MAP_HEIGHT - 25, '스테이지 - ' + str(now_stage), color=(255, 255, 255))
        if self.max_map_score[now_stage - 1] != NO_SCORE:
            self.text.draw(45, 20, '최고점수 : ' + str(self.max_map_score[now_stage - 1]), color=(255, 255, 255))
        else:
            self.text.draw(45, 20, '점수없음', color=(255, 255, 255))
