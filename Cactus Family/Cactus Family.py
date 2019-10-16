# coding=utf-8
from pico2d import *
import random

MAP_WIDTH = 900
MAP_HEIGHT = 800
debug_mode = True


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

    def easy_stage(self):
        self.map_image = 'Map_1.png'
        self.cac_count = 4
        self.block_count = 21
        self.cac_pos = [(2, 2), (6, 3), (2, 6), (2, 7)]
        self.clear_pos = [(4, 4), (3, 4), (3, 5), (2, 4)]
        self.stone_pos = [4, 5]
        self.block_pos = [(8, 4), (4, 0), (3, 0), (0, 3), (0, 4), (0, 5), (0, 6),
                          (3, 9), (2, 9), (7, 3), (7, 5), (7, 6), (6, 7), (5, 8),
                          (4, 8), (1, 8), (1, 7), (1, 2), (2, 1), (5, 1), (6, 2)]

    def normal_stage(self):
        self.map_image = 'Map_2.png'
        self.cac_count = 4
        self.block_count = 21
        self.cac_pos = [(2, 2), (6, 3), (2, 6), (2, 7)]
        self.clear_pos = [(4, 4), (3, 4), (3, 5), (2, 4)]
        self.stone_pos = [4, 5]
        self.block_pos = [(8, 4), (4, 0), (3, 0), (0, 3), (0, 4), (0, 5), (0, 6),
                          (3, 9), (2, 9), (7, 3), (7, 5), (7, 6), (6, 7), (5, 8),
                          (4, 8), (1, 8), (1, 7), (1, 2), (2, 1), (5, 1), (6, 2)]

    def setting_stage(self, stone, cac, block):
        self.map = load_image(self.map_image)
        stone.set_pos(self.stone_pos)
        for i in range(self.cac_count):
            cac.append(Cactus())
            cac[i].__init__()
            cac[i].set_image('Cactus test.png')
            cac[i].set_pos(self.cac_pos[i])
        for i in range(self.block_count):
            block.append(Block())
            block[i].__init__()
            block[i].set_pos(self.block_pos[i])

    def stage_clear(self, cac):
        cac_array = []
        for i in range(self.cac_count):
            cac_array.append((cac[i].get_pos()))
        self.clear_pos.sort()
        cac_array.sort()
        if self.clear_pos == cac_array:
            print('클리어')

    def draw_stage(self):
        self.map.draw(MAP_WIDTH // 2, MAP_HEIGHT // 2)


class Group:
    def __init__(self):
        self.array = []

    def partition(self):
        pass

    def print_g(self):
        print(self.array)


class Block:
    def __init__(self):
        self.x, self.y = 400, 300
        self.rect = self.x - 50, self.y + 50, self.x + 50, self.y - 50
        pass

    def set_pos(self, pos):
        self.x = pos[1] * 100
        self.y = pos[0] * 100

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
        self.xdir = self.ST_X_NONE
        self.ydir = self.ST_Y_NONE
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

    def 벽하고충돌(self, type):
        # for i in range(block_count):
        #     print(block_count)
        #     if block[i].rect[0] == self.rect[2] and block[i].y == self.y and type == 0:
        #         print('넌 못지나간다')
        #         return False
        #     elif block[i].rect[2] == self.rect[0] and block[i].y == self.y and type == 1:
        #         print('넌 못지나간다2')
        #         return False
        #     elif block[i].rect[1] == self.rect[3] and block[i].x == self.x and type == 2:
        #         print('넌 못지나간다3')
        #         return False
        #     elif block[i].rect[3] == self.rect[1] and block[i].x == self.x and type == 3:
        #         print('넌 못지나간다4')
        #         return False
        #     else:
        #         print('넌 지나간다', type, i)
        #         return True
        return True
        pass

    def handle_Stone(self, event):
        if event.type == SDL_KEYDOWN:
            if self.xdir == self.ST_X_NONE and self.ydir == self.ST_Y_NONE:
                if event.key == SDLK_d and self.벽하고충돌(0) and self.rect[2] < MAP_WIDTH - 50:
                    self.xdir = self.ST_X_FORWARD
                    self.old_x = self.x + 100
                elif event.key == SDLK_a and self.벽하고충돌(1) and 50 < self.rect[0]:
                    self.xdir = self.ST_X_BAKWARD
                    self.old_x = self.x - 100
                elif event.key == SDLK_w and self.벽하고충돌(2) and self.rect[1] < MAP_WIDTH - 150:
                    self.ydir = self.ST_Y_UP
                    self.old_y = self.y + 100
                elif event.key == SDLK_s and self.벽하고충돌(3) and 50 < self.rect[3]:
                    self.ydir = self.ST_Y_DOWN
                    self.old_y = self.y - 100

    def update(self):
        self.move()
        self.rect = [self.x - 50, self.y + 50, self.x + 50, self.y - 50]

    def render(self):
        self.draw_image(20, 100, 100)


class Cactus(Stone):
    def __init__(self):
        self.xdir = self.ST_X_NONE
        self.ydir = self.ST_Y_NONE
        self.x = random.randint(1, 8) * 100
        self.y = random.randint(1, 7) * 100
        self.old_x, self.old_y = 0, 0
        self.frame = 0
        self.speed = 20
        self.rect = [self.x - 50, self.y + 50, self.x + 50, self.y - 50]
        self.isColl = False
        self.isMovable = True

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
                # TODO 그룹에 속해있지않은데 이미 그룹에 누가 있다면
                else:
                    self.xdir = self.ST_X_BAKWARD
                    self.old_x = self.x - 25
                # print('col 0')
            # 왼쪽 충돌
            elif self.rect[0] <= player.rect[2] and self.rect[2] > player.rect[
                0] and player.xdir == player.ST_X_FORWARD:
                if self.isColl:
                    for i in cg.array:
                        cac[i].xdir = cac[i].ST_X_FORWARD
                        cac[i].old_x = cac[i].x + 25
                else:
                    self.xdir = self.ST_X_FORWARD
                    self.old_x = self.x + 25
                # print('col 1')

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
                # print('col 2')
            # 아래 충돌
            elif self.rect[3] <= player.rect[1] and self.rect[1] > player.rect[3] and player.ydir == player.ST_Y_UP:
                if self.isColl:
                    for i in cg.array:
                        cac[i].ydir = cac[i].ST_Y_UP
                        cac[i].old_y = cac[i].y + 25
                else:
                    self.ydir = self.ST_Y_UP
                    self.old_y = self.y + 25
                # print('col 3')

    def handle_cactus(self, event):
        pass

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


def handle_events():
    global debug_mode
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            exit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                exit()
            elif event.key == SDLK_p:
                for i in range(game_stage.cac_count):
                    cac[i].__init__()
                    cg.array.clear()
            elif event.key == SDLK_e:
                print(player.rect)
                for i in range(cac_count):
                    print(cac[i].rect)
            elif event.key == SDLK_1:
                game_stage.easy_stage()
                game_stage.setting_stage(player, cac, block)
                cg.array.clear()
            elif event.key == SDLK_2:
                game_stage.normal_stage()
                game_stage.setting_stage(player, cac, block)
                cg.array.clear()
            elif event.key == SDLK_3:
                cg.array.clear()
            elif event.key == SDLK_i:
                debug_mode = not debug_mode
            else:
                player.handle_Stone(event)
                for i in range(game_stage.cac_count):
                    cac[i].handle_cactus(event)
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


def make_group():
    for j in range(game_stage.cac_count):
        if cac[j].isColl and j not in cg.array:
            cg.array.append(j)
            cg.print_g()


def render():
    game_stage.draw_stage()
    player.render()

    for i in range(game_stage.cac_count):
        cac[i].render()


def update():
    player.update()
    for i in range(game_stage.cac_count):
        cac[i].update()
        cac[i].collision()
        for j in range(game_stage.cac_count):
            if not i == j:
                cac[i].New_coll(cac[j])
    for i in range(game_stage.block_count):
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
