from pico2d import *
import random
import Cactus_Family
import class_Stage

MAP_WIDTH, MAP_HEIGHT = 900, 800
LEFT_COLLISION, TOP_COLLISION, RIGHT_COLLISION, BOTTOM_COLLISION = range(4)
ST_X_NONE, ST_X_FORWARD, ST_X_BAKWARD, ST_Y_NONE, ST_Y_UP, ST_Y_DOWN = range(6)


class Cactus:
    def __init__(self, pos=None):
        if pos is None:
            pos = [4, 3]
        self.x = pos[1] * 100
        self.y = pos[0] * 100
        self.x_dir, self.y_dir = ST_X_NONE, ST_Y_NONE
        self.obj = load_image('image_file\\Cactus_sprite.png')
        self.old_x, self.old_y = 0, 0
        self.frame = 0
        self.speed = 20
        self.rect = [self.x - 50, self.y + 50, self.x + 50, self.y - 50]
        self.is_collision = False
        self.is_movable = True
        self.move_sound_cnt = 0
        self.move_sound = [load_wav('sound_effect\\cac_move (1).wav'),
                           load_wav('sound_effect\\cac_move (2).wav'),
                           load_wav('sound_effect\\cac_move (3).wav'),
                           load_wav('sound_effect\\cac_move (4).wav'),
                           load_wav('sound_effect\\cac_move (5).wav'),
                           load_wav('sound_effect\\cac_move (6).wav')]
        for i in range(5):
            self.move_sound[i].set_volume(100)

    def is_block_around(self, move_type):
        for block in class_Stage.get_block():
            if move_type == ST_X_FORWARD and self.rect[2] == block.rect[0] and self.y == block.y:
                # print('넌 앞으로 못가')
                return False
            elif move_type == ST_X_BAKWARD and self.rect[0] == block.rect[2] and self.y == block.y:
                # print('넌 뒤로 못가')
                return False
            elif move_type == ST_Y_UP and self.rect[1] == block.rect[3] and self.x == block.x:
                # print('넌 위로 못가')
                return False
            elif move_type == ST_Y_DOWN and self.rect[3] == block.rect[1] and self.x == block.x:
                # print('넌 밑으로 못가')
                return False
        return True

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

    def draw_image(self, count, x_size, y_size, low):
        self.obj.clip_draw(self.frame * x_size, low * x_size, x_size, y_size, self.x, self.y)
        self.frame = (self.frame + 1) % count

    def get_pos(self):
        return [self.y / 100, self.x / 100]

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

    def move_sound_setting(self):
        self.move_sound_cnt = random.randint(0, 5)
        self.move_sound[self.move_sound_cnt].play()

    def move_cactus(self, move_type, cac_num):
        if self.is_collision:
            for i in range(len(Cactus_Family.cactus_group.merge_cactus_groups)):
                if cac_num in Cactus_Family.cactus_group.merge_cactus_groups[i]:
                    if move_type == ST_X_FORWARD:
                        self.move_sound_setting()
                        for j in Cactus_Family.cactus_group.merge_cactus_groups[i]:
                            Cactus_Family.cac[j].x_dir = ST_X_FORWARD
                            Cactus_Family.cac[j].old_x = Cactus_Family.cac[j].x + 100
                    elif move_type == ST_X_BAKWARD:
                        self.move_sound_setting()
                        for j in Cactus_Family.cactus_group.merge_cactus_groups[i]:
                            Cactus_Family.cac[j].x_dir = ST_X_BAKWARD
                            Cactus_Family.cac[j].old_x = Cactus_Family.cac[j].x - 100
                    elif move_type == ST_Y_UP:
                        self.move_sound_setting()
                        for j in Cactus_Family.cactus_group.merge_cactus_groups[i]:
                            Cactus_Family.cac[j].y_dir = ST_Y_UP
                            Cactus_Family.cac[j].old_y = Cactus_Family.cac[j].y + 100
                    elif move_type == ST_Y_DOWN:
                        self.move_sound_setting()
                        for j in Cactus_Family.cactus_group.merge_cactus_groups[i]:
                            Cactus_Family.cac[j].y_dir = ST_Y_DOWN
                            Cactus_Family.cac[j].old_y = Cactus_Family.cac[j].y - 100
        else:
            if move_type == ST_X_FORWARD:
                self.x_dir = move_type
                self.old_x = self.x + 100
                self.move_sound_setting()
            elif move_type == ST_X_BAKWARD:
                self.x_dir = move_type
                self.old_x = self.x - 100
                self.move_sound_setting()
            elif move_type == ST_Y_UP:
                self.y_dir = move_type
                self.old_y = self.y + 100
                self.move_sound_setting()
            elif move_type == ST_Y_DOWN:
                self.y_dir = move_type
                self.old_y = self.y - 100
                self.move_sound_setting()

    def collision_to_player(self, cac_num):
        if self.y == Cactus_Family.player.y and self.x_dir == ST_X_NONE:
            if self.rect[0] <= Cactus_Family.player.rect[2] and self.rect[2] > Cactus_Family.player.rect[0]:
                if Cactus_Family.player.x_dir == ST_X_BAKWARD:
                    self.move_cactus(ST_X_BAKWARD, cac_num)
                elif Cactus_Family.player.x_dir == ST_X_FORWARD:
                    self.move_cactus(ST_X_FORWARD, cac_num)
        elif self.x == Cactus_Family.player.x and self.y_dir == ST_Y_NONE:
            if self.rect[3] <= Cactus_Family.player.rect[1] and self.rect[1] > Cactus_Family.player.rect[3]:
                if Cactus_Family.player.y_dir == ST_Y_DOWN:
                    self.move_cactus(ST_Y_DOWN, cac_num)
                elif Cactus_Family.player.y_dir == ST_Y_UP:
                    self.move_cactus(ST_Y_UP, cac_num)

    def update(self):
        self.move()
        self.rect = [self.x - 50, self.y + 50, self.x + 50, self.y - 50]

    def render(self):
        if self.is_collision:
            self.draw_image(8, 100, 100, 0)
        else:
            self.draw_image(8, 100, 100, 1)
        if Cactus_Family.debug_mode:
            draw_rectangle(self.rect[0], self.rect[1], self.rect[2], self.rect[3])
