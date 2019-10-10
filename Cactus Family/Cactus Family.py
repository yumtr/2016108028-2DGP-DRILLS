# coding=utf-8
from pico2d import *

MAP_WIDTH = 900
MAP_HEIGHT = 900

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
        self.y = 350
        self.old_x = 0
        self.old_y = 0
        self.obj = 0
        self.speed = 20
        self.rect = self.x - 50, self.y + 50, self.x + 50, self.y - 50

    def set_pos(self, ix, iy):
        self.x = ix
        self.y = iy

    def draw_image(self):
        self.obj.clip_draw(self.frame * 100, 0 * 1, 100, 100, self.x, self.y)

        self.frame = (self.frame + 1) % 20

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
        if event.type == SDL_KEYDOWN:
            print('key downed')
            if self.xdir == self.ST_X_NONE and self.ydir == self.ST_Y_NONE:
                if event.key == SDLK_d:
                    self.xdir = self.ST_X_FORWARD
                    self.old_x = self.x + 100
                elif event.key == SDLK_a:
                    self.xdir = self.ST_X_BAKWARD
                    self.old_x = self.x - 100
                elif event.key == SDLK_w:
                    if self.ydir in (self.ST_Y_NONE, self.ST_X_NONE):
                        self.ydir = self.ST_Y_UP
                        self.old_y = self.y + 100
                elif event.key == SDLK_s:
                    if self.ydir in (self.ST_Y_NONE, self.ST_X_NONE):
                        self.ydir = self.ST_Y_DOWN
                        self.old_y = self.y - 100
            if event.key == SDLK_g:
                self.set_pos((MAP_WIDTH / 2) + 50, MAP_HEIGHT / 2)
        # elif event.type == SDL_KEYUP:
        #     print('key up')
        #     if event.key == SDLK_d:
        #         if self.xdir == self.ST_X_FORWARD:
        #             self.xdir = self.ST_X_NONE
        #     elif event.key == SDLK_a:
        #         if self.xdir == self.ST_X_BAKWARD:
        #             self.xdir = self.ST_X_NONE
        #     elif event.key == SDLK_w:
        #         if self.ydir == self.ST_Y_UP:
        #             self.ydir = self.ST_Y_NONE
        #     elif event.key == SDLK_s:
        #         if self.ydir == self.ST_Y_DOWN:
        #             self.ydir = self.ST_Y_NONE

    def render(self):
        self.draw_image()

    def update(self):
        self.move()
        self.rect = self.x - 50, self.y + 50, self.x + 50, self.y - 50


def exit():
    global running
    close_canvas()
    running = False
    pass


def handle_events():
    global running
    global dir
    global dir_y
    global rect
    events = get_events()
    for event in events:
        print('선인장', rect)
        print('돌', test.rect)
        if event.type == SDL_QUIT:
            exit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                exit()
            else:
                test.handle_Stone(event)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1
            else:
                test.handle_Stone(event)


def collision():
    global rect
    global x, y

    if y == test.y and test.xdir != test.ST_X_NONE:
        # 오른쪽 충돌
        if rect[2] >= test.rect[0] and rect[0] < test.rect[2] and test.xdir == test.ST_X_BAKWARD:
            x -= test.speed
        # 왼쪽 충돌
        elif rect[0] <= test.rect[2] and rect[2] > test.rect[0] and test.xdir == test.ST_X_FORWARD:
            x += test.speed
    if x == test.x and test.ydir != test.ST_Y_NONE:
        # 위 충돌
        if rect[1] >= test.rect[3] and rect[3] < test.rect[1] and test.ydir == test.ST_Y_DOWN:
            y -= test.speed
        # 아래 충돌
        elif rect[3] <= test.rect[1] and rect[1] > test.rect[3] and test.ydir == test.ST_Y_UP:
            y += test.speed



test = Stone()

open_canvas(MAP_WIDTH, MAP_HEIGHT)
test.obj = load_image('stone.png')
Map_Test = load_image('Map_1.png')
# cactus = load_image('Cactus test.png')
stone = load_image('Cactus test.png')

running = True
x = 200
y = 350
rect = x - 50, y + 50, x + 50, y - 50

frame_stone = 0
dir = 0
dir_y = 0


def render():
    global frame_stone
    Map_Test.draw(MAP_WIDTH // 2, MAP_HEIGHT // 2)
    test.render()
    stone.clip_draw(frame_stone * 100, 0 * 1, 100, 100, x, y)
    frame_stone = (frame_stone + 1) % 8


def update():
    global rect
    test.update()
    handle_events()
    update_canvas()
    collision()
    rect = x - 50, y + 50, x + 50, y - 50


while running:
    clear_canvas()
    render()
    update()
    x += dir * 10
    y += dir_y * 10
    delay(0.05)
