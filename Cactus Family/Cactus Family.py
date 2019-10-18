# coding=utf-8
from pico2d import *
import random
import threading

MAP_WIDTH = 900
MAP_HEIGHT = 800
debug_mode = False

clear = False
now_stage = 1


class Clear_Scene:
    def __init__(self):
        self.scene = load_image('Clear.png')
        self.count = 0
        self.timer = 0

    def Win(self):
        global clear
        if self.count == 0:
            self.timer = threading.Timer(1, self.Win)
            self.timer.start()
        self.count += 1

        if self.count == 15:
            self.timer.cancel()
            self.count = 0
            print(self.count)
            clear = False
            global now_stage
            now_stage += 1
            change_stage(now_stage)
        else:
            self.draw_scene()

    def draw_scene(self):
        self.scene.draw(MAP_WIDTH // 2, MAP_HEIGHT // 2)


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
        self.map_image = 'Map_test.png'
        self.cac_count = 6
        self.block_count = 30
        self.cac_pos = [(4, 3), (6, 7), (5, 7), (4, 7), (3, 7), (2, 7)]
        self.clear_pos = []
        self.stone_pos = [4, 5]
        self.block_pos = [(8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (7, 9), (6, 9), (5, 9),
                          (4, 9), (3, 9), (2, 9), (1, 9), (0, 8), (0, 7), (0, 6), (0, 5), (0, 4), (0, 3), (0, 2),
                          (0, 1), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

    def easy_stage(self):
        self.map_image = 'Map_easy.png'
        self.cac_count = 3
        self.block_count = 18
        self.cac_pos = [(6, 3), (5, 6), (3, 6)]
        self.clear_pos = [(3, 3), (3, 4), (2, 4)]
        self.stone_pos = [4, 5]
        self.block_pos = [(7, 3), (8, 4), (8, 5), (7, 6), (6, 7), (5, 8), (4, 9), (3, 8), (2, 7),
                          (1, 6), (0, 5), (0, 4), (1, 3), (2, 2), (3, 1), (4, 2), (5, 1), (6, 2)]

    def normal_stage(self):
        self.map_image = 'Map_normal.png'
        self.cac_count = 4
        self.block_count = 21
        self.cac_pos = [(2, 2), (6, 3), (2, 6), (2, 7)]
        self.clear_pos = [(4, 4), (3, 4), (3, 5), (2, 4)]
        self.stone_pos = [4, 5]
        self.block_pos = [(8, 4), (4, 0), (3, 0), (0, 3), (1, 4), (0, 5), (0, 6),
                          (3, 9), (2, 9), (7, 3), (7, 5), (7, 6), (6, 7), (5, 8),
                          (4, 8), (0, 8), (1, 7), (1, 2), (2, 1), (5, 1), (6, 2)]

    def hard_stage(self):
        self.map_image = 'Map_hard.png'
        self.cac_count = 4
        self.block_count = 21
        self.cac_pos = [(2, 2), (6, 3), (2, 6), (2, 7)]
        self.clear_pos = [(4, 4), (3, 4), (3, 5), (2, 4)]
        self.stone_pos = [4, 5]
        self.block_pos = [(8, 4), (4, 0), (3, 0), (0, 3), (0, 4), (0, 5), (0, 6),
                          (3, 9), (2, 9), (7, 3), (7, 5), (7, 6), (6, 7), (5, 8),
                          (4, 8), (1, 8), (1, 7), (1, 2), (2, 1), (5, 1), (6, 2)]

    def setting_stage(self, stone, cac_o, block_o):
        self.map = load_image(self.map_image)
        stone.set_pos(self.stone_pos)
        for i in range(self.cac_count):
            cac_o.append(Cactus())
            cac_o[i].__init__()
            cac_o[i].set_image('Cactus test.png')
            cac_o[i].set_pos(self.cac_pos[i])
        for i in range(self.block_count):
            block_o.append(Block())
            block_o[i].__init__()
            block_o[i].set_pos(self.block_pos[i])

    def stage_clear(self, cac_o):
        cac_array = []
        for i in range(self.cac_count):
            cac_array.append((cac_o[i].get_pos()))
        self.clear_pos.sort()
        cac_array.sort()
        if self.clear_pos == cac_array:
            global clear
            clear = True

    def draw_stage(self):
        self.map.draw(MAP_WIDTH // 2, MAP_HEIGHT // 2)


class Group:
    def __init__(self):
        self.array = []
        self.not_group = []

    def partition(self):
        pass

    def print_g(self):
        print('우린그룹', self.array)
        print('그룹에 안속함', self.not_group)


class Block:
    def __init__(self):
        self.x, self.y = 400, 300
        self.rect = self.x - 50, self.y + 50, self.x + 50, self.y - 50

    def set_pos(self, pos):
        self.x = pos[1] * 100
        self.y = pos[0] * 100

    def col2block(self, ano):
        if self.rect[0] + ano.speed == ano.rect[2] and self.y == ano.y:
            ano.xdir = ano.ST_X_NONE
            ano.x -= ano.speed
        elif self.rect[2] - ano.speed == ano.rect[0] and self.y == ano.y:
            ano.xdir = ano.ST_X_NONE
            ano.x += ano.speed
        elif self.rect[1] - ano.speed == ano.rect[3] and self.x == ano.x:
            ano.ydir = ano.ST_Y_NONE
            ano.y += ano.speed
        elif self.rect[3] + ano.speed == ano.rect[1] and self.x == ano.x:
            ano.ydir = ano.ST_Y_NONE
            ano.y -= ano.speed

    def col2blockPlayer(self, ano):
        if not ano.isColl:
            if self.rect[0] + ano.speed == ano.rect[2] and self.y == ano.y:
                player.xdir = player.ST_X_NONE
                player.x -= player.speed + 20
                ano.xdir = ano.ST_X_NONE
                ano.x -= ano.speed
            elif self.rect[2] - ano.speed == ano.rect[0] and self.y == ano.y:
                player.xdir = player.ST_X_NONE
                player.x += player.speed + 20
                ano.xdir = ano.ST_X_NONE
                ano.x += ano.speed

            elif self.rect[1] - ano.speed == ano.rect[3] and self.x == ano.x:
                player.ydir = player.ST_Y_NONE
                player.y += player.speed + 20
                ano.ydir = ano.ST_Y_NONE
                ano.y += ano.speed

            elif self.rect[3] + ano.speed == ano.rect[1] and self.x == ano.x:
                player.ydir = player.ST_Y_NONE
                player.y -= player.speed + 20
                ano.ydir = ano.ST_Y_NONE
                ano.y -= ano.speed

    def cg2blockPlayer(self, ano):
        if self.rect[0] + ano.speed == ano.rect[2] and self.y == ano.y:
            player.xdir = player.ST_X_NONE
            player.x -= (player.speed + 20)
            for i in cg.array:
                cac[i].xdir = cac[i].ST_X_NONE
                cac[i].x -= cac[i].speed
        elif self.rect[2] - ano.speed == ano.rect[0] and self.y == ano.y:
            player.xdir = player.ST_X_NONE
            player.x += (player.speed + 20)
            for i in cg.array:
                cac[i].xdir = cac[i].ST_X_NONE
                cac[i].x += cac[i].speed
        elif self.rect[1] - ano.speed == ano.rect[3] and self.x == ano.x:
            player.ydir = player.ST_Y_NONE
            player.y += (player.speed + 20)
            for i in cg.array:
                cac[i].ydir = cac[i].ST_Y_NONE
                cac[i].y += cac[i].speed
        elif self.rect[3] + ano.speed == ano.rect[1] and self.x == ano.x:
            player.ydir = player.ST_Y_NONE
            player.y -= (player.speed + 20)
            for i in cg.array:
                cac[i].ydir = cac[i].ST_Y_NONE
                cac[i].y -= cac[i].speed

    def update(self):
        self.rect = [self.x - 50, self.y + 50, self.x + 50, self.y - 50]
        if debug_mode:
            draw_rectangle(self.rect[0], self.rect[1], self.rect[2], self.rect[3])


class Player:
    def __init__(self):
        pass

    ST_X_NONE, ST_X_FORWARD, ST_X_BAKWARD = 0, 1, 2
    ST_Y_NONE, ST_Y_UP, ST_Y_DOWN = 3, 4, 5
    HIGH_SPEED = 30
    LOW_SPEED = 10
    pass


class Stone(Player):
    def __init__(self):
        self.xdir, self.ydir = self.ST_X_NONE, self.ST_Y_NONE
        self.frame, self.obj = 0, 0
        self.x, self.y = 400, 300
        self.old_x, self.old_y = 0, 0
        self.speed = 20
        self.rect = self.x - 50, self.y + 50, self.x + 50, self.y - 50
        self.isMovable = True

    def set_image(self, filename):
        self.obj = load_image(filename)

    def set_pos(self, pos):
        self.x = pos[1] * 100
        self.y = pos[0] * 100

    def get_pos(self):
        return self.y / 100, self.x / 100

    def draw_image(self, count, x_size, y_size):
        self.obj.clip_draw(self.frame * x_size, 0 * 1, x_size, y_size, self.x, self.y)
        self.frame = (self.frame + 1) % count

    def move(self):
        if self.isMovable:
            if self.xdir == self.ST_X_FORWARD:
                self.x += self.speed
                if self.x >= self.old_x:
                    self.xdir = self.ST_X_NONE
            elif self.xdir == self.ST_X_BAKWARD:
                self.x -= self.speed
                if self.x <= self.old_x:
                    self.xdir = self.ST_X_NONE
            if self.ydir == self.ST_Y_UP:
                self.y += self.speed
                if self.y >= self.old_y:
                    self.ydir = self.ST_Y_NONE
            elif self.ydir == self.ST_Y_DOWN:
                self.y -= self.speed
                if self.y <= self.old_y:
                    self.ydir = self.ST_Y_NONE
        else:
            print('못움직임')

    def handle_Stone(self, event):
        if event.type == SDL_KEYDOWN and self.xdir == self.ST_X_NONE and self.ydir == self.ST_Y_NONE:
            if self.xdir == self.ST_X_NONE and self.ydir == self.ST_Y_NONE:
                if event.key == SDLK_d and self.rect[2] < MAP_WIDTH - 50:
                    self.xdir = self.ST_X_FORWARD
                    # 임시 테스트 쭉이동하도록 + 1000
                    self.old_x = self.x + 100
                elif event.key == SDLK_a and 50 < self.rect[0]:
                    self.xdir = self.ST_X_BAKWARD
                    self.old_x = self.x - 100
                elif event.key == SDLK_w and self.rect[1] < MAP_WIDTH - 150:
                    self.ydir = self.ST_Y_UP
                    self.old_y = self.y + 100
                elif event.key == SDLK_s and 50 < self.rect[3]:
                    self.ydir = self.ST_Y_DOWN
                    self.old_y = self.y - 100
        elif event.type == SDL_KEYUP:
            # 임시 테스트 쭉이동 ㅇㅇ
            # if self.xdir == self.ST_X_NONE and self.ydir == self.ST_Y_NONE:
            #     if event.key == SDLK_d:
            #         self.old_x = self.x - (self.x % 100) + 100
            #     elif event.key == SDLK_a:
            #         self.old_x = self.x - (self.x % 100)
            #     elif event.key == SDLK_w:
            #         self.old_y = self.y - (self.y % 100) + 100
            #     elif event.key == SDLK_s:
            #         self.old_y = self.y - (self.y % 100)
            pass

    def update(self):
        self.move()
        self.rect = [self.x - 50, self.y + 50, self.x + 50, self.y - 50]

    def render(self):
        self.draw_image(20, 100, 100)
        if debug_mode:
            draw_rectangle(self.rect[0], self.rect[1], self.rect[2], self.rect[3])


class Cactus(Stone):
    def __init__(self):
        self.xdir, self.ydir = self.ST_X_NONE, self.ST_Y_NONE
        self.x, self.y = 0, 0
        self.old_x, self.old_y = 0, 0
        self.frame = 0
        self.speed = 20
        self.rect = [self.x - 50, self.y + 50, self.x + 50, self.y - 50]
        self.isColl = False
        self.isMovable = True

    def random_pos(self):
        self.x = random.randint(1, 8) * 100
        self.y = random.randint(1, 7) * 100

    def check_col(self, ano):
        if self.rect[0] == ano.rect[2] and self.y == ano.y:
            return True
        elif self.rect[1] == ano.rect[3] and self.x == ano.x:
            return True
        else:
            return False

    def New_coll(self, ano):
        if 1:
            # 왼쪽 닫았다
            if self.rect[0] == ano.rect[2] and self.y == ano.y:
                self.isColl = True
                ano.isColl = True
            # 위쪽 닫았다
            elif self.rect[1] == ano.rect[3] and self.x == ano.x:
                self.isColl = True
                ano.isColl = True

    def collision(self):
        if self.rect[3] == player.rect[3] and player.rect[1] == self.rect[1] and player.xdir != player.ST_X_NONE:
            # 오른쪽 충돌
            if self.rect[2] >= player.rect[0] and self.rect[0] < player.rect[2] and player.xdir == player.ST_X_BAKWARD:
                if self.isColl:
                    for i in cg.array:
                        cac[i].xdir = cac[i].ST_X_BAKWARD
                        cac[i].old_x = cac[i].x - 25
                else:
                    self.xdir = self.ST_X_BAKWARD
                    self.old_x = self.x - 25
            # 왼쪽 충돌
            elif self.rect[0] <= player.rect[2] and \
                    self.rect[2] > player.rect[0] and player.xdir == player.ST_X_FORWARD:
                if self.isColl:
                    for i in cg.array:
                        cac[i].xdir = cac[i].ST_X_FORWARD
                        cac[i].old_x = cac[i].x + 25
                else:
                    self.xdir = self.ST_X_FORWARD
                    self.old_x = self.x + 25
        elif self.rect[0] == player.rect[0] and player.rect[2] == self.rect[2] and player.ydir != player.ST_Y_NONE:
            # 위 충돌
            if self.rect[1] >= player.rect[3] and self.rect[3] < player.rect[1] and player.ydir == player.ST_Y_DOWN:
                if self.isColl:
                    for i in cg.array:
                        cac[i].ydir = cac[i].ST_Y_DOWN
                        cac[i].old_y = cac[i].y - 25
                else:
                    self.ydir = self.ST_Y_DOWN
                    self.old_y = self.y - 25
            # 아래 충돌
            elif self.rect[3] <= player.rect[1] and self.rect[1] > player.rect[3] and player.ydir == player.ST_Y_UP:
                if self.isColl:
                    for i in cg.array:
                        cac[i].ydir = cac[i].ST_Y_UP
                        cac[i].old_y = cac[i].y + 25
                else:
                    self.ydir = self.ST_Y_UP
                    self.old_y = self.y + 25

    def render(self):
        self.draw_image(8, 100, 100)
        if debug_mode:
            draw_rectangle(self.rect[0], self.rect[1], self.rect[2], self.rect[3])

    def update(self):
        self.move()
        self.rect = [self.x - 50, self.y + 50, self.x + 50, self.y - 50]


def exit():
    global running
    close_canvas()
    running = False


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
    game_stage.setting_stage(player, cac, block)
    cg.array.clear()
    cg.not_group.clear()


def handle_events():
    global debug_mode, now_stage
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            exit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                exit()
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
                cg.print_g()
            else:
                player.handle_Stone(event)
        elif event.type == SDL_KEYUP:
            player.handle_Stone(event)


open_canvas(MAP_WIDTH, MAP_HEIGHT)
running = True
player = Stone()
player.set_image('stone.png')
cac = []
block = []
game_stage = Stage()
game_stage.easy_stage()
game_stage.setting_stage(player, cac, block)

cg = Group()
scene = Clear_Scene()


def make_group():
    for j in range(game_stage.cac_count):
        if cac[j].isColl and j not in cg.array:
            cg.array.append(j)
            cg.array.sort()
        if j not in cg.not_group:
            cg.not_group.append(j)

    for i in range(len(cg.array)):
        cg.not_group.remove(cg.array[i])


def render():
    global clear
    game_stage.draw_stage()
    player.render()
    for i in range(game_stage.cac_count):
        cac[i].render()
    if clear:
        scene.Win()


def update():
    player.update()
    # 전체 선인장
    for i in range(game_stage.cac_count):
        cac[i].update()
        for j in range(game_stage.cac_count):
            if not i == j:
                cac[i].New_coll(cac[j])
            # TODO 충돌 손봐줘야해요오오오옹로ㅓㅇ로ㅓ알노ㅓㅏ
    # 그룹된 선인장
    for i in cg.array:
        cac[i].collision()
        cac[i].set_image('Cactus group.png')
        for j in range(game_stage.block_count):
            block[j].cg2blockPlayer(cac[i])

    # 그룹안된 선인장
    for i in cg.not_group:
        cac[i].collision()
        for j in range(game_stage.block_count):
            block[j].col2blockPlayer(cac[i])

    for i in range(game_stage.block_count):
        block[i].col2block(player)
        block[i].update()

    make_group()
    game_stage.stage_clear(cac)
    handle_events()
    update_canvas()


while running:

    clear_canvas()
    render()
    update()
    delay(0.05)