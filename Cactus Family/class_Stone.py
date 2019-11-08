from pico2d import *
import Cactus_Family

MAP_WIDTH = 900
MAP_HEIGHT = 800
LEFT_COLLISION, TOP_COLLISION, RIGHT_COLLISION, BOTTOM_COLLISION = range(4)
ST_X_NONE, ST_X_FORWARD, ST_X_BAKWARD, ST_Y_NONE, ST_Y_UP, ST_Y_DOWN = range(6)


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
        for i in range(Cactus_Family.game_stage.cac_count):
            if move_type == ST_X_FORWARD and self.rect[2] == Cactus_Family.cac[i].rect[0] \
                    and self.y == Cactus_Family.cac[i].y:
                self.forward_access = False
            elif move_type == ST_X_BAKWARD and self.rect[0] == Cactus_Family.cac[i].rect[2] \
                    and self.y == Cactus_Family.cac[i].y:
                self.bakward_access = False
            elif move_type == ST_Y_UP and self.rect[1] == Cactus_Family.cac[i].rect[3] \
                    and self.x == Cactus_Family.cac[i].x:
                self.up_access = False
            elif move_type == ST_Y_DOWN and self.rect[3] == Cactus_Family.cac[i].rect[1] \
                    and self.x == Cactus_Family.cac[i].x:
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
        if Cactus_Family.debug_mode:
            draw_rectangle(self.rect[0], self.rect[1], self.rect[2], self.rect[3])
