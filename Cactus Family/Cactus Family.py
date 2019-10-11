# coding=utf-8
from pico2d import *

MAP_WIDTH = 900
MAP_HEIGHT = 800


class Player():
    ST_X_NONE, ST_X_FORWARD, ST_X_BAKWARD = 0, 1, 2
    ST_Y_NONE, ST_Y_UP, ST_Y_DOWN = 3, 4, 5
    HIGH_SPEED = 30
    LOW_SPEED = 10
    pass


class Stone(Player):
    def __init__(self):
        self.xdir = self.ST_X_NONE
        self.ydir = self.ST_Y_NONE
        self.frame = 0
        self.x = 400
        self.y = 300
        self.old_x = 0
        self.old_y = 0
        self.obj = 0
        self.speed = 20
        self.rect = self.x - 50, self.y + 50, self.x + 50, self.y - 50

    def set_image(self, filename):
        self.obj = load_image(filename)

    def set_pos(self, ix, iy):
        self.x = ix
        self.y = iy

    def draw_image(self, count, x_size, y_size):
        self.obj.clip_draw(self.frame * x_size, 0 * 1, x_size, y_size, self.x, self.y)
        self.frame = (self.frame + 1) % count

    def move(self):
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
        # if 0 < test.y < MAP_HEIGHT and 0 < test.x - 50 < MAP_WIDTH:
        if event.type == SDL_KEYDOWN:
            if self.xdir == self.ST_X_NONE and self.ydir == self.ST_Y_NONE:
                if event.key == SDLK_d and test.rect[2] < MAP_WIDTH - 50:
                    self.xdir = self.ST_X_FORWARD
                    self.old_x = self.x + 100
                elif event.key == SDLK_a and 50 < test.rect[0]:
                    self.xdir = self.ST_X_BAKWARD
                    self.old_x = self.x - 100
                elif event.key == SDLK_w and test.rect[1] < MAP_WIDTH - 150:
                    self.ydir = self.ST_Y_UP
                    self.old_y = self.y + 100
                elif event.key == SDLK_s and 50 < test.rect[3]:
                    self.ydir = self.ST_Y_DOWN
                    self.old_y = self.y - 100
                if event.key == SDLK_g:
                    self.set_pos((MAP_WIDTH / 2) + 50, MAP_HEIGHT / 2)

    def render(self):
        self.draw_image(20, 100, 100)

    def update(self):
        self.move()
        self.rect = self.x - 50, self.y + 50, self.x + 50, self.y - 50


class Cactus(Stone):
    def __init__(self):
        self.set_pos(400, 200)
        self.frame = 0
        self.speed = 25
        self.state = 0
        self.rect = self.x - 50, self.y + 50, self.x + 50, self.y - 50

    def collision(self, test):
        if self.y == test.y and test.xdir != test.ST_X_NONE:
            # 오른쪽 충돌
            if self.rect[2] >= test.rect[0] and self.rect[0] < test.rect[2] and test.xdir == test.ST_X_BAKWARD:
                self.x -= self.speed
            # 왼쪽 충돌
            elif self.rect[0] <= test.rect[2] and self.rect[2] > test.rect[0] and test.xdir == test.ST_X_FORWARD:
                self.x += self.speed
        elif self.x == test.x and test.ydir != test.ST_Y_NONE:
            # 위 충돌
            if self.rect[1] >= test.rect[3] and self.rect[3] < test.rect[1] and test.ydir == test.ST_Y_DOWN:
                self.y -= self.speed
            # 아래 충돌
            elif self.rect[3] <= test.rect[1] and self.rect[1] > test.rect[3] and test.ydir == test.ST_Y_UP:
                self.y += self.speed

    def collision2(self, ano):

        # 좌우
        if self.y == ano.y:
            if self.rect[2] == ano.rect[0]:
                print("나나나나나")
                self.x = ano.x - 100
            elif self.rect[0] == ano.rect[2]:
                print("dsdsd")
                self.x = ano.x + 100
        # 상하
        elif self.x == ano.x:
            if self.rect[1] == ano.rect[3]:
                self.y = ano.y - 100
            elif self.rect[3] == ano.rect[1]:
                self.y = ano.y + 100

    def render(self):
        self.draw_image(8, 100, 100)

    def update(self):
        self.rect = self.x - 50, self.y + 50, self.x + 50, self.y - 50


def exit():
    global running
    close_canvas()
    running = False
    pass


def handle_events():
    global running
    global rect
    events = get_events()
    for event in events:

        if event.type == SDL_QUIT:
            exit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                exit()
            elif event.key == SDLK_q:
                for i in 0, 2, 1:
                    cac[i].set_pos((i * 200) + 200, (i * 200) + 200)
            else:
                test.handle_Stone(event)
        elif event.type == SDL_KEYUP:
            test.handle_Stone(event)


open_canvas(MAP_WIDTH, MAP_HEIGHT)
test = Stone()
test.set_image('stone.png')
cac = [Cactus(), Cactus(), Cactus()]
for i in 0, 2, 1:
    cac[i].set_image('Cactus test.png')
Map_Test = load_image('Map_1.png')
running = True
cac[1].set_pos(600, 200)
cac[2].set_pos(200, 600)


def render():
    Map_Test.draw(MAP_WIDTH // 2, MAP_HEIGHT // 2)
    test.render()
    for i in 0, 2, 1:
        cac[i].render()


def update():
    test.update()
    for i in 0, 2, 1:
        cac[i].update()
        cac[i].collision(test)
        cac[0].collision2(cac[i])
        cac[1].collision2(cac[i])
        cac[2].collision2(cac[i])

    handle_events()
    update_canvas()


while running:
    clear_canvas()
    render()
    update()
    delay(0.05)
