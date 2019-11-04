# coding=utf-8
from pico2d import *
import random
import game_framework
import pause_state
import stage_clear_state

MAP_WIDTH = 900
MAP_HEIGHT = 800
debug_mode = False
clear = False
now_stage = 1

player = None
cac = None
block = None
game_stage = None
cactus_group = None


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
        self.cac_count = 6
        self.block_count = 22
        self.cac_pos = [(6, 4), (5, 8), (4, 2), (4, 4), (1, 3), (1, 5)]
        self.clear_pos = [(5, 4), (5, 5), (4, 3), (4, 4), (3, 4), (2, 4)]
        self.stone_pos = [4, 5]
        self.block_pos = [(7, 2), (7, 3), (7, 4), (6, 5), (7, 6), (7, 7), (6, 8), (5, 9), (4, 9), (3, 9), (2, 8),
                          (1, 7), (1, 6), (0, 5), (1, 4), (0, 3), (1, 2), (2, 1), (3, 1), (4, 0), (5, 0), (6, 1)]

    def setting_stage(self, stone, cac_o, block_o):
        self.map = load_image(self.map_image)
        stone.set_pos(self.stone_pos)
        for i in range(self.cac_count):
            cac_o.append(Cactus())
            cac_o[i].__init__()
            cac_o[i].set_pos(self.cac_pos[i])
        for i in range(self.block_count):
            block_o.append(Block())
            block_o[i].__init__()
            block_o[i].set_pos(self.block_pos[i])
        # 선인장 그룹 초기화해주고 다시만들어줌
        setting_group()

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


def setting_group():
    cactus_group.all_cactus.clear()
    cactus_group.collision_cactus_group.clear()
    cactus_group.single_cactus.clear()
    cactus_group.merge_cactus_groups.clear()
    for i in range(game_stage.cac_count):
        cactus_group.all_cactus.append(i)
        cactus_group.single_cactus.append(i)


class Group:
    def __init__(self):
        self.all_cactus = []
        # 합쳐진 선인장들의 그룹들
        self.merge_cactus_groups = []
        # 충돌한 선인장들의 그룹
        self.collision_cactus_group = []
        # 합쳐지지않은 개별 선인장들
        self.single_cactus = []

    # def make_group(self):
    #     for j in range(game_stage.cac_count):
    #         if cac[j].isColl and j not in self.collision_cactus_group:
    #             self.collision_cactus_group.append(j)
    #             self.collision_cactus_group.sort()
    #         if j not in self.single_cactus:
    #             self.single_cactus.append(j)
    #
    #     for i in range(len(self.collision_cactus_group)):
    #         self.single_cactus.remove(self.collision_cactus_group[i])

    # 싱글선인장에서 선인장끼리 붙이치면 새로운 그룹만듬 그리고 합쳐진 그룹들에 넣음
    # 충돌됬을때 한번만 실행해야함
    def make_cactus_group(self):
        # 모든 싱글 선인장에서 충돌이면 선인장그룹에 넣음
        for i in self.single_cactus:
            if cac[i].isColl:
                self.collision_cactus_group.append(i)
                self.single_cactus.remove(i)
        if len(self.collision_cactus_group) > 1:
            self.merge_cactus_groups.append(self.collision_cactus_group)
            self.collision_cactus_group = []
            print('안녕 나는 사람이야')

    def check_collision_groups(self, num):
        for i in range(len(self.merge_cactus_groups)):
            if not i == num:
                for k in self.merge_cactus_groups[num]:
                    my_group = self.merge_cactus_groups[num][k]
                    for j in self.merge_cactus_groups[i]:
                        # 내 그룹 선인장과 다른 선인장들 비교해서 i값도 같이 리턴
                        return cac[my_group].collision_to_cactus2(cac[self.merge_cactus_groups[i][j]]), i

    # 합쳐진 선인장그룹들 끼리 비교해서 병합함
    def group_checking(self):
        for i in range(len(self.merge_cactus_groups)):  # 전체 합쳐진 선인장 그룹 중에서
            # i번째 합쳐진 선인장 그룹이 다른 그룹과 충돌 되있다면
            if self.check_collision_groups(i)[0]:
                print('그룹끼리의 은밀한 만남이 시작된다')
                return_coll = self.check_collision_groups(i)[1]
                # 충돌된 그룹에 있는 요소들을 내꺼에 추가
                self.merge_cactus_groups[i].extend(self.merge_cactus_groups[return_coll])
                # 다 추가한뒤 해당 합쳐진 선인장그룹 제거
                del self.merge_cactus_groups[return_coll]

    def print_g(self):
        # print('모든 선인장', self.all_cactus)
        print('전체 그룹', self.merge_cactus_groups)
        # print('우린그룹', self.collision_cactus_group)
        print('그룹에 안속함', self.single_cactus)

    def update(self):
        for i in self.all_cactus:
            if cac[i].isColl:
                self.make_cactus_group()
                self.all_cactus.remove(i)
                if len(self.merge_cactus_groups) > 1:
                    self.group_checking()


class Block:
    def __init__(self):
        self.x, self.y = 400, 300
        self.rect = self.x - 50, self.y + 50, self.x + 50, self.y - 50
        self.hi = 0

    def set_pos(self, pos):
        self.x = pos[1] * 100
        self.y = pos[0] * 100

    def collision_to_block(self, ano):
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

    # 싱글 선인장
    def collision_single_cactus_to_block(self, ano, stone):
        if not ano.isColl:
            if self.rect[0] + ano.speed == ano.rect[2] and self.y == ano.y:
                stone.xdir = stone.ST_X_NONE
                stone.x -= stone.speed
                ano.xdir = ano.ST_X_NONE
                ano.x -= ano.speed
            elif self.rect[2] - ano.speed == ano.rect[0] and self.y == ano.y:
                stone.xdir = stone.ST_X_NONE
                stone.x += stone.speed
                ano.xdir = ano.ST_X_NONE
                ano.x += ano.speed

            elif self.rect[1] - ano.speed == ano.rect[3] and self.x == ano.x:
                stone.ydir = stone.ST_Y_NONE
                stone.y += stone.speed
                ano.ydir = ano.ST_Y_NONE
                ano.y += ano.speed

            elif self.rect[3] + ano.speed == ano.rect[1] and self.x == ano.x:
                stone.ydir = stone.ST_Y_NONE
                stone.y -= stone.speed
                ano.ydir = ano.ST_Y_NONE
                ano.y -= ano.speed

    # 그룹 선인장
    def collision_cactus_group_to_block(self, ano, stone):
        if self.rect[0] + ano.speed == ano.rect[2] and self.y == ano.y:
            stone.xdir = stone.ST_X_NONE
            stone.x -= stone.speed
            for i in cactus_group.collision_cactus_group:
                cac[i].xdir = cac[i].ST_X_NONE
                cac[i].x -= cac[i].speed
        elif self.rect[2] - ano.speed == ano.rect[0] and self.y == ano.y:
            stone.xdir = stone.ST_X_NONE
            stone.x += stone.speed
            for i in cactus_group.collision_cactus_group:
                cac[i].xdir = cac[i].ST_X_NONE
                cac[i].x += cac[i].speed
        elif self.rect[1] - ano.speed == ano.rect[3] and self.x == ano.x:
            stone.ydir = stone.ST_Y_NONE
            stone.y += stone.speed
            for i in cactus_group.collision_cactus_group:
                cac[i].ydir = cac[i].ST_Y_NONE
                cac[i].y += cac[i].speed
        elif self.rect[3] + ano.speed == ano.rect[1] and self.x == ano.x:
            stone.ydir = stone.ST_Y_NONE
            stone.y -= stone.speed
            for i in cactus_group.collision_cactus_group:
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
        self.frame = 0
        self.obj = load_image('stone_sprites.png')
        self.x, self.y = 400, 300
        self.old_x, self.old_y = 0, 0
        self.speed = 20
        self.rect = self.x - 50, self.y + 50, self.x + 50, self.y - 50
        self.isMovable = True
        self.anime_cnt = 0

    def set_image(self, filename):
        self.obj = load_image(filename)

    def set_pos(self, pos):
        self.x = pos[1] * 100
        self.y = pos[0] * 100

    def get_pos(self):
        return self.y / 100, self.x / 100

    def draw_image(self, count, x_size, y_size, low):
        self.obj.clip_draw(self.frame * x_size, low * x_size, x_size, y_size, self.x, self.y)
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

    def update(self):
        self.move()
        self.rect = [self.x - 50, self.y + 50, self.x + 50, self.y - 50]

    def render(self):
        self.anime_cnt += 1
        if 46 > self.anime_cnt > 30:
            self.draw_image(15, 100, 100, 0)
            if self.anime_cnt == 45:
                self.anime_cnt = 0
        else:
            self.draw_image(15, 100, 100, 1)
        if debug_mode:
            draw_rectangle(self.rect[0], self.rect[1], self.rect[2], self.rect[3])


class Cactus(Stone):
    def __init__(self):
        self.xdir, self.ydir = self.ST_X_NONE, self.ST_Y_NONE
        self.obj = load_image('Cactus_sprite.png')
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

    def collision_to_cactus(self, ano):
        # 왼쪽 닫았다 나랑 닫은놈 충돌 True
        if self.rect[0] == ano.rect[2] and self.y == ano.y:
            self.isColl = True
            ano.isColl = True
        # 위쪽 닫았다
        elif self.rect[1] == ano.rect[3] and self.x == ano.x:
            self.isColl = True
            ano.isColl = True

    def collision_to_cactus2(self, ano):
        # 왼쪽 닫았다 나랑 닫은놈 충돌 True
        if self.rect[0] == ano.rect[2] and self.y == ano.y:
            return True
        # 위쪽 닫았다
        elif self.rect[1] == ano.rect[3] and self.x == ano.x:
            return True
        else:
            return False

    def collision(self, self_num):
        if self.rect[3] == player.rect[3] and player.rect[1] == self.rect[1] \
                and player.xdir != player.ST_X_NONE and self.xdir == self.ST_X_NONE:
            # 오른쪽 충돌
            if self.rect[2] >= player.rect[0] and self.rect[0] < player.rect[2] and player.xdir == player.ST_X_BAKWARD:
                if self.isColl:
                    print('안녕 나는 충돌이야')
                    for i in range(len(cactus_group.merge_cactus_groups)):
                        for j in cactus_group.merge_cactus_groups[i]:
                            if self_num in cactus_group.merge_cactus_groups[i]:
                                cac[j].xdir = cac[j].ST_X_BAKWARD
                                cac[j].old_x = cac[j].x - 100
                else:
                    self.xdir = self.ST_X_BAKWARD
                    self.old_x = self.x - 100

            # 왼쪽 충돌
            elif self.rect[0] <= player.rect[2] and self.rect[2] > player.rect[0] \
                    and player.xdir == player.ST_X_FORWARD and self.xdir == self.ST_X_NONE:
                if self.isColl:
                    for i in range(len(cactus_group.merge_cactus_groups)):
                        for j in cactus_group.merge_cactus_groups[i]:
                            if self_num in cactus_group.merge_cactus_groups[i]:
                                cac[j].xdir = cac[j].ST_X_FORWARD
                                cac[j].old_x = cac[j].x + 100
                else:
                    self.xdir = self.ST_X_FORWARD
                    self.old_x = self.x + 100
        elif self.rect[0] == player.rect[0] and player.rect[2] == self.rect[2] \
                and player.ydir != player.ST_Y_NONE and self.ydir == self.ST_Y_NONE:
            # 위 충돌
            if self.rect[1] >= player.rect[3] and self.rect[3] < player.rect[1] and player.ydir == player.ST_Y_DOWN:
                if self.isColl:
                    for i in range(len(cactus_group.merge_cactus_groups)):
                        for j in cactus_group.merge_cactus_groups[i]:
                            if self_num in cactus_group.merge_cactus_groups[i]:
                                cac[j].ydir = cac[j].ST_Y_DOWN
                                cac[j].old_y = cac[j].y - 100
                else:
                    self.ydir = self.ST_Y_DOWN
                    self.old_y = self.y - 100
            # 아래 충돌
            elif self.rect[3] <= player.rect[1] and self.rect[1] > player.rect[3] \
                    and player.ydir == player.ST_Y_UP and self.ydir == self.ST_Y_NONE:
                if self.isColl:
                    for i in range(len(cactus_group.merge_cactus_groups)):
                        for j in cactus_group.merge_cactus_groups[i]:
                            if self_num in cactus_group.merge_cactus_groups[i]:
                                cac[j].ydir = cac[j].ST_Y_UP
                                cac[j].old_y = cac[j].y + 100
                else:
                    self.ydir = self.ST_Y_UP
                    self.old_y = self.y + 100

    def render(self):
        if self.isColl:
            self.draw_image(8, 100, 100, 0)
        else:
            self.draw_image(8, 100, 100, 1)
        if debug_mode:
            draw_rectangle(self.rect[0], self.rect[1], self.rect[2], self.rect[3])

    def update(self):
        self.move()
        self.rect = [self.x - 50, self.y + 50, self.x + 50, self.y - 50]


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
    game_stage.setting_stage(player, cac, block)


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
                # print(player.x, player.y)
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
    game_stage.setting_stage(player, cac, block)


def exit():
    global player, cac, block, game_stage, cactus_group
    del player
    del cac
    del block
    del game_stage
    del cactus_group
    close_canvas()


def pause():
    pass


def resume():
    pass


def update():
    if clear:
        game_framework.push_state(stage_clear_state)
    player.update()
    # 전체 선인장
    for i in range(game_stage.cac_count):
        cac[i].collision(i)
        cac[i].update()
        for j in range(game_stage.cac_count):
            if not i == j:
                cac[i].collision_to_cactus(cac[j])
            # TODO 충돌 손봐줘야해오오오옹로ㅓㅇ로ㅓ알노ㅓㅏ
    # 그룹된 선인장
    for i in cactus_group.collision_cactus_group:
        # cac[i].collision(i)
        # cac[i].set_image('Cactus group.png')
        for j in range(game_stage.block_count):
            block[j].collision_cactus_group_to_block(cac[i], player)

    # 그룹안된 선인장
    for i in cactus_group.single_cactus:
        # cac[i].collision(i)
        for j in range(game_stage.block_count):
            block[j].collision_single_cactus_to_block(cac[i], player)

    for i in range(game_stage.block_count):
        block[i].collision_to_block(player)
        block[i].update()

    cactus_group.update()
    game_stage.stage_clear(cac)
    handle_events()
    update_canvas()


def draw():
    global clear
    game_stage.draw_stage()
    player.render()
    for i in range(game_stage.cac_count):
        cac[i].render()
    delay(0.03)
