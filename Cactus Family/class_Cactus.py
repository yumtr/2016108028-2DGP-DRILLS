from pico2d import *
import random
from class_Stone import Stone
import Cactus_Family

MAP_WIDTH = 900
MAP_HEIGHT = 800
LEFT_COLLISION, TOP_COLLISION, RIGHT_COLLISION, BOTTOM_COLLISION = range(4)
ST_X_NONE, ST_X_FORWARD, ST_X_BAKWARD, ST_Y_NONE, ST_Y_UP, ST_Y_DOWN = range(6)


class Cactus(Stone):
    def __init__(self, pos=[4, 3]):
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
            for i in range(len(Cactus_Family.cactus_group.merge_cactus_groups)):
                if cac_num in Cactus_Family.cactus_group.merge_cactus_groups[i]:
                    if move_type == ST_X_FORWARD:
                        for j in Cactus_Family.cactus_group.merge_cactus_groups[i]:
                            Cactus_Family.cac[j].x_dir = ST_X_FORWARD
                            Cactus_Family.cac[j].old_x = Cactus_Family.cac[j].x + 100
                    elif move_type == ST_X_BAKWARD:
                        for j in Cactus_Family.cactus_group.merge_cactus_groups[i]:
                            Cactus_Family.cac[j].x_dir = ST_X_BAKWARD
                            Cactus_Family.cac[j].old_x = Cactus_Family.cac[j].x - 100
                    elif move_type == ST_Y_UP:
                        for j in Cactus_Family.cactus_group.merge_cactus_groups[i]:
                            Cactus_Family.cac[j].y_dir = ST_Y_UP
                            Cactus_Family.cac[j].old_y = Cactus_Family.cac[j].y + 100
                    elif move_type == ST_Y_DOWN:
                        for j in Cactus_Family.cactus_group.merge_cactus_groups[i]:
                            Cactus_Family.cac[j].y_dir = ST_Y_DOWN
                            Cactus_Family.cac[j].old_y = Cactus_Family.cac[j].y - 100
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
