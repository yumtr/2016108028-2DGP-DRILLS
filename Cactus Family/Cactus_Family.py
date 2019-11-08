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

LEFT_COLLISION, TOP_COLLISION, RIGHT_COLLISION, BOTTOM_COLLISION = range(4)
ST_X_NONE, ST_X_FORWARD, ST_X_BAKWARD, ST_Y_NONE, ST_Y_UP, ST_Y_DOWN = range(6)


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
        self.cac_count = 6
        self.block_count = 30
        self.cac_pos = [(4, 3), (6, 7), (5, 7), (4, 7), (3, 7), (2, 7)]
        self.clear_pos = []
        self.stone_pos = [4, 5]
        self.block_pos = [(8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (7, 9), (6, 9), (5, 9),
                          (4, 9), (3, 9), (2, 9), (1, 9), (0, 8), (0, 7), (0, 6), (0, 5), (0, 4), (0, 3), (0, 2),
                          (0, 1), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

    def easy_stage(self):
        self.map_image = 'image_file\\Map_easy.png'
        self.cac_count = 3
        self.block_count = 18
        self.cac_pos = [(6, 3), (5, 6), (3, 6)]
        self.clear_pos = [(3, 3), (3, 4), (2, 4)]
        self.stone_pos = [4, 5]
        self.block_pos = [(7, 3), (8, 4), (8, 5), (7, 6), (6, 7), (5, 8), (4, 9), (3, 8), (2, 7),
                          (1, 6), (0, 5), (0, 4), (1, 3), (2, 2), (3, 1), (4, 2), (5, 1), (6, 2)]

    def normal_stage(self):
        self.map_image = 'image_file\\Map_normal.png'
        self.cac_count = 4
        self.block_count = 21
        self.cac_pos = [(2, 2), (6, 3), (2, 6), (2, 7)]
        self.clear_pos = [(4, 4), (3, 4), (3, 5), (2, 4)]
        self.stone_pos = [4, 5]
        self.block_pos = [(8, 4), (4, 0), (3, 0), (0, 3), (1, 4), (0, 5), (0, 6),
                          (3, 9), (2, 9), (7, 3), (7, 5), (7, 6), (6, 7), (5, 8),
                          (4, 8), (0, 8), (1, 7), (1, 2), (2, 1), (5, 1), (6, 2)]

    def hard_stage(self):
        self.map_image = 'image_file\\Map_hard.png'
        self.cac_count = 6
        self.block_count = 22
        self.cac_pos = [(6, 4), (5, 8), (4, 2), (4, 4), (1, 3), (1, 5)]
        self.clear_pos = [(5, 4), (5, 5), (4, 3), (4, 4), (3, 4), (2, 4)]
        self.stone_pos = [4, 5]
        self.block_pos = [(7, 2), (7, 3), (7, 4), (6, 5), (7, 6), (7, 7), (6, 8), (5, 9), (4, 9), (3, 9), (2, 8),
                          (1, 7), (1, 6), (0, 5), (1, 4), (0, 3), (1, 2), (2, 1), (3, 1), (4, 0), (5, 0), (6, 1)]

    def setting_stage(self):
        self.map = load_image(self.map_image)
        player.set_position(self.stone_pos)
        for i in range(self.cac_count):
            cac.append(Cactus())
            cac[i].__init__()
            cac[i].set_position(self.cac_pos[i])
        for i in range(self.block_count):
            block.append(Block())
            block[i].__init__()
            block[i].set_position(self.block_pos[i])
        # 선인장 그룹 초기화해주고 다시만들어줌
        setting_group()

    def check_stage_clear(self):
        cac_array = []
        for i in range(self.cac_count):
            cac_array.append((cac[i].get_pos()))
        self.clear_pos.sort()
        cac_array.sort()

        if self.clear_pos == cac_array:
            global clear
            clear = True

    def draw_stage(self):
        self.map.draw(MAP_WIDTH // 2, MAP_HEIGHT // 2)


def setting_group():
    cactus_group.all_cactus.clear()
    cactus_group.single_cactus.clear()
    cactus_group.merge_cactus_groups.clear()
    for i in range(game_stage.cac_count):
        cactus_group.all_cactus.append(i)
        cactus_group.single_cactus.append(i)


def is_player_collision_to_cac_group(group):
    for i in group:
        if cac[i].collision_to_cactus(player):
            return True


# 두 그룹 충돌 검사
def groups_collision_check(first_group, second_group):
    for i in first_group:
        for j in second_group:
            if cac[i].collision_to_cactus(cac[j]):
                return True


class Group:
    def __init__(self):
        self.all_cactus = []  # 합쳐진 선인장들의 그룹들
        self.merge_cactus_groups = []  # 충돌한 선인장들의 그룹
        self.single_cactus = []

    # 싱글선인장에서 선인장끼리 붙어지면 그룹에 한번 넣음
    def make_cactus_group(self, coll_cac):
        self.single_cactus.remove(coll_cac)
        self.merge_cactus_groups.append([coll_cac])

        # 합쳐진 선인장그룹들 끼리 비교해서 병합함

    def group_checking(self):
        for i in range(len(self.merge_cactus_groups)):
            for j in range(len(self.merge_cactus_groups)):
                if not i == j:
                    if groups_collision_check(self.merge_cactus_groups[i], self.merge_cactus_groups[j]):
                        self.merge_cactus_groups[i].extend(self.merge_cactus_groups[j])
                        self.merge_cactus_groups[i].sort()
                        del self.merge_cactus_groups[j]
                        return

    def print_g(self):
        # print('모든 선인장', self.all_cactus)
        print('전체 그룹', self.merge_cactus_groups)
        print('그룹에 안속함', self.single_cactus)

    def update(self):
        for i in self.all_cactus:  # 충돌이 발생할때 한번만 부름
            if cac[i].is_collision:
                self.make_cactus_group(i)  # 그룹을 만든다
                self.all_cactus.remove(i)  # 충돌된 선인장을 전체 리스트에서 제거한다.
                self.print_g()  # 출력
        self.group_checking()  # 항상 그룹끼리 체크해줌


class Block:
    def __init__(self):
        self.x, self.y = 400, 300
        self.rect = self.x - 50, self.y + 50, self.x + 50, self.y - 50
        self.collision_judgment = True

    def set_position(self, pos):
        self.x = pos[1] * 100
        self.y = pos[0] * 100

    # 플레이어랑 벽하고 충돌
    def collision_stone_to_block(self):
        if self.rect[0] + player.speed == player.rect[2] and self.y == player.y:
            player.x_dir = ST_X_NONE
            player.x -= player.speed
        elif self.rect[2] - player.speed == player.rect[0] and self.y == player.y:
            player.x_dir = ST_X_NONE
            player.x += player.speed
        elif self.rect[1] - player.speed == player.rect[3] and self.x == player.x:
            player.y_dir = ST_Y_NONE
            player.y += player.speed
        elif self.rect[3] + player.speed == player.rect[1] and self.x == player.x:
            player.y_dir = ST_Y_NONE
            player.y -= player.speed

    # 싱글 선인장이랑 벽하고 충돌
    def collision_single_cactus_to_block(self, ano):
        if self.rect[0] + ano.speed == ano.rect[2] and self.y == ano.y:
            player.x_dir = ST_X_NONE
            player.x -= player.speed
            ano.x_dir = ST_X_NONE
            ano.x -= ano.speed
        elif self.rect[2] - ano.speed == ano.rect[0] and self.y == ano.y:
            player.x_dir = ST_X_NONE
            player.x += player.speed
            ano.x_dir = ST_X_NONE
            ano.x += ano.speed

        elif self.rect[1] - ano.speed == ano.rect[3] and self.x == ano.x:
            player.y_dir = ST_Y_NONE
            player.y += player.speed
            ano.y_dir = ST_Y_NONE
            ano.y += ano.speed

        elif self.rect[3] + ano.speed == ano.rect[1] and self.x == ano.x:
            player.y_dir = ST_Y_NONE
            player.y -= player.speed
            ano.y_dir = ST_Y_NONE
            ano.y -= ano.speed

    # 그룹 선인장이랑 벽하고 충돌
    def collision_group_cactus_to_block(self, group):
        if is_player_collision_to_cac_group(group):
            for i in group:
                if self.rect[0] == cac[i].rect[2] and self.y == cac[i].y:
                    # player.forward_access = False
                    player.move_judge(ST_X_FORWARD)
                    return False
                elif self.rect[2] == cac[i].rect[0] and self.y == cac[i].y:
                    # player.bakward_access = False
                    player.move_judge(ST_X_BAKWARD)
                    return False
                if self.rect[1] == cac[i].rect[3] and self.x == cac[i].x:
                    # player.down_access = False
                    player.move_judge(ST_Y_DOWN)
                    return False
                if self.rect[3] == cac[i].rect[1] and self.x == cac[i].x:
                    # player.up_access = False
                    player.move_judge(ST_Y_UP)
                    return False
        else:
            return True

    def update(self):
        self.rect = [self.x - 50, self.y + 50, self.x + 50, self.y - 50]
        self.collision_stone_to_block()

        for i in cactus_group.single_cactus:
            self.collision_single_cactus_to_block(cac[i])

        self.collision_judgment = True
        for i in range(len(cactus_group.merge_cactus_groups)):
            if self.collision_group_cactus_to_block(cactus_group.merge_cactus_groups[i]):
                self.collision_judgment = True
            else:
                self.collision_judgment = False
        if self.collision_judgment:  # 아무 충돌도없다는 거니까 아무대나 움직일수있게
            player.forward_access = True
            player.bakward_access = True
            player.up_access = True
            player.down_access = True

    def render(self):
        if debug_mode:
            draw_rectangle(self.rect[0], self.rect[1], self.rect[2], self.rect[3])
        pass


class Stone:
    def __init__(self):
        self.x_dir, self.y_dir = ST_X_NONE, ST_Y_NONE
        self.frame = 0
        self.obj = load_image('image_file\\stone_sprites.png')
        self.x, self.y = 400, 300
        self.old_x, self.old_y = 0, 0
        self.speed = 20
        self.rect = self.x - 50, self.y + 50, self.x + 50, self.y - 50
        self.anime_cnt = 0
        self.forward_access = True
        self.bakward_access = True
        self.up_access = True
        self.down_access = True

    # 내 move_type 방향에 선인장이있어야 move_type = False 설정
    def move_judge(self, move_type):
        for i in range(game_stage.cac_count):
            if move_type == ST_X_FORWARD and self.rect[2] == cac[i].rect[0] and self.y == cac[i].y:
                self.forward_access = False
            elif move_type == ST_X_BAKWARD and self.rect[0] == cac[i].rect[2] and self.y == cac[i].y:
                self.bakward_access = False
            elif move_type == ST_Y_UP and self.rect[1] == cac[i].rect[3] and self.x == cac[i].x:
                self.up_access = False
            elif move_type == ST_Y_DOWN and self.rect[3] == cac[i].rect[1] and self.x == cac[i].x:
                self.down_access = False
            pass

    def set_image(self, filename):
        self.obj = load_image(filename)

    def set_position(self, pos):
        self.x = pos[1] * 100
        self.y = pos[0] * 100

    def get_pos(self):
        return self.y / 100, self.x / 100

    def draw_image(self, count, x_size, y_size, low):
        self.obj.clip_draw(self.frame * x_size, low * x_size, x_size, y_size, self.x, self.y)
        self.frame = (self.frame + 1) % count

    def move(self):
        if self.x_dir == ST_X_FORWARD:
            self.x += self.speed
            if self.x >= self.old_x:
                self.x_dir = ST_X_NONE
        elif self.x_dir == ST_X_BAKWARD:
            self.x -= self.speed
            if self.x <= self.old_x:
                self.x_dir = ST_X_NONE
        elif self.y_dir == ST_Y_UP:
            self.y += self.speed
            if self.y >= self.old_y:
                self.y_dir = ST_Y_NONE
        elif self.y_dir == ST_Y_DOWN:
            self.y -= self.speed
            if self.y <= self.old_y:
                self.y_dir = ST_Y_NONE

    def handle_Stone(self, event):
        if event.type == SDL_KEYDOWN and self.x_dir == ST_X_NONE and self.y_dir == ST_Y_NONE:
            if self.x_dir == ST_X_NONE and self.y_dir == ST_Y_NONE:
                if event.key == SDLK_d and self.rect[2] < MAP_WIDTH - 50 and self.forward_access:
                    self.x_dir = ST_X_FORWARD
                    # 임시 테스트 쭉이동하도록 + 1000
                    self.old_x = self.x + 100
                elif event.key == SDLK_a and 50 < self.rect[0] and self.bakward_access:
                    self.x_dir = ST_X_BAKWARD
                    self.old_x = self.x - 100
                elif event.key == SDLK_w and self.rect[1] < MAP_WIDTH - 150 and self.up_access:
                    self.y_dir = ST_Y_UP
                    self.old_y = self.y + 100
                elif event.key == SDLK_s and 50 < self.rect[3] and self.down_access:
                    self.y_dir = ST_Y_DOWN
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
        super().__init__()
        self.x_dir, self.y_dir = ST_X_NONE, ST_Y_NONE
        self.obj = load_image('image_file\\Cactus_sprite.png')
        self.x, self.y = 0, 0
        self.old_x, self.old_y = 0, 0
        self.frame = 0
        self.speed = 20
        self.rect = [self.x - 50, self.y + 50, self.x + 50, self.y - 50]
        self.is_collision = False
        self.is_movable = True

    def random_pos(self):
        self.x = random.randint(1, 8) * 100
        self.y = random.randint(1, 7) * 100

    def set_collision_state(self, ano):
        if self.rect[0] == ano.rect[2] and self.y == ano.y:
            self.is_collision = True
            ano.is_collision = True
        elif self.rect[1] == ano.rect[3] and self.x == ano.x:
            self.is_collision = True
            ano.is_collision = True

    def collision_to_cactus(self, ano):
        if self.rect[0] == ano.rect[2] and self.y == ano.y or \
                self.rect[2] == ano.rect[0] and self.y == ano.y or \
                self.rect[1] == ano.rect[3] and self.x == ano.x or \
                self.rect[3] == ano.rect[1] and self.x == ano.x:
            return True
        else:
            return False

    def move_cactus(self, move_type, cac_num):
        if self.is_collision:
            for i in range(len(cactus_group.merge_cactus_groups)):
                if cac_num in cactus_group.merge_cactus_groups[i]:
                    if move_type == ST_X_FORWARD:
                        for j in cactus_group.merge_cactus_groups[i]:
                            cac[j].x_dir = ST_X_FORWARD
                            cac[j].old_x = cac[j].x + 100
                    elif move_type == ST_X_BAKWARD:
                        for j in cactus_group.merge_cactus_groups[i]:
                            cac[j].x_dir = ST_X_BAKWARD
                            cac[j].old_x = cac[j].x - 100
                    elif move_type == ST_Y_UP:
                        for j in cactus_group.merge_cactus_groups[i]:
                            cac[j].y_dir = ST_Y_UP
                            cac[j].old_y = cac[j].y + 100
                    elif move_type == ST_Y_DOWN:
                        for j in cactus_group.merge_cactus_groups[i]:
                            cac[j].y_dir = ST_Y_DOWN
                            cac[j].old_y = cac[j].y - 100
        else:
            if move_type == ST_X_FORWARD:
                self.x_dir = move_type
                self.old_x = self.x + 100
            elif move_type == ST_X_BAKWARD:
                self.x_dir = move_type
                self.old_x = self.x - 100
            elif move_type == ST_Y_UP:
                self.y_dir = move_type
                self.old_y = self.y + 100
            elif move_type == ST_Y_DOWN:
                self.y_dir = move_type
                self.old_y = self.y - 100

    def collision_to_player(self, cac_num):
        if self.y == player.y and self.x_dir == ST_X_NONE:
            if self.rect[0] <= player.rect[2] and self.rect[2] > player.rect[0]:
                if player.x_dir == ST_X_BAKWARD:
                    self.move_cactus(ST_X_BAKWARD, cac_num)
                elif player.x_dir == ST_X_FORWARD:
                    self.move_cactus(ST_X_FORWARD, cac_num)
        elif self.x == player.x and self.y_dir == ST_Y_NONE:
            if self.rect[3] <= player.rect[1] and self.rect[1] > player.rect[3]:
                if player.y_dir == ST_Y_DOWN:
                    self.move_cactus(ST_Y_DOWN, cac_num)
                elif player.y_dir == ST_Y_UP:
                    self.move_cactus(ST_Y_UP, cac_num)

    def update(self):
        self.move()
        self.rect = [self.x - 50, self.y + 50, self.x + 50, self.y - 50]

    def render(self):
        if self.is_collision:
            self.draw_image(8, 100, 100, 0)
        else:
            self.draw_image(8, 100, 100, 1)
        if debug_mode:
            draw_rectangle(self.rect[0], self.rect[1], self.rect[2], self.rect[3])


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
        cac[i].update()
        cac[i].collision_to_player(i)
        for j in range(game_stage.cac_count):
            if not i == j:
                cac[i].set_collision_state(cac[j])
    # 벽 업데이트
    for i in range(game_stage.block_count):
        block[i].update()

    game_stage.check_stage_clear()
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
