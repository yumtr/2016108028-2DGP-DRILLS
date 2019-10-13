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
                if event.key == SDLK_d and self.rect[2] < MAP_WIDTH - 50:
                    self.xdir = self.ST_X_FORWARD
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
                if event.key == SDLK_g:
                    self.set_pos((MAP_WIDTH / 2) + 50, MAP_HEIGHT / 2)

    def render(self):
        self.draw_image(20, 100, 100)
        # draw_rectangle(self.rect[0], self.rect[1], self.rect[2], self.rect[3])

    def update(self):
        self.move()
        self.rect = [self.x - 50, self.y + 50, self.x + 50, self.y - 50]


class Cactus(Stone):
    global player

    def __init__(self, px, py):
        self.xdir = self.ST_X_NONE
        self.ydir = self.ST_Y_NONE
        self.set_pos(px, py)
        self.old_x = 0
        self.old_y = 0
        self.frame = 0
        self.speed = 25
        self.left = 50
        self.top = 50
        self.right = 50
        self.bottom = 50
        self.rect = [self.x - self.left, self.y + self.top, self.x + self.right, self.y - self.bottom]
        self.state = 0
        self.left_col = False
        self.top_col = False
        self.right_col = False
        self.bottom_col = False
        self.isMerge = False
        self.isParents = False
        self.nx = 0
        self.ny = 0
        self.P = 0

    def Set_NewPos(self, ano):
        if 1:
            self.old_x = self.x
            self.old_y = self.y
            self.nx = self.old_x
            self.ny = self.old_y

            print('뭘봐')
            print(self.old_x, self.nx, self.x)

            if self.old_x < ano.x:
                self.nx = ano.x - self.old_x
            else:
                self.nx = self.old_x - ano.x
            if self.old_y < ano.y:
                self.ny = ano.y - self.old_y
            else:
                self.ny = self.old_y - ano.y
            self.isMerge = True

    def New_coll(self, ano):
        if self.isMerge:
            self.x = ano.x - self.nx
            self.y = ano.y - self.ny

        if not self.isParents:
            if self.rect[1] == ano.rect[1] and self.rect[3] == ano.rect[3]:
                # 오른쪽 닫았다
                if self.rect[2] == ano.rect[0]:
                    self.Set_NewPos(ano)
                    print('오른쪽')
                # 왼쪽 닫았다
                if self.rect[0] == ano.rect[2]:
                    if not ano.isParents:
                        self.isParents = True
                    elif ano.isParents:
                        self.Set_NewPos(ano)
                    print('왼쪽')
            elif self.rect[0] == ano.rect[0] and self.rect[2] == ano.rect[2]:
                # 위쪽 닫았다
                if self.rect[1] == ano.rect[3] and not self.top_col:
                    self.top_col = True
                    self.old_y = self.y + 100
                # 아래쪽 닫았다
                if self.rect[3] == ano.rect[1] and not self.bottom_col:
                    self.bottom_col = True
                    self.old_y = self.y - 100

        # if self.xdir == self.ST_X_NONE and self.ydir == self.ST_Y_NONE:
        #     if self.right_col:
        #         self.xdir = ano.xdir
        #         self.ydir = ano.ydir
        #         print('좌 붙음')
        #     if self.left_col:
        #         self.xdir = ano.xdir
        #         self.ydir = ano.ydir
        #         print('우 붙음')

            # if self.top_col:
            #     #print('하 붙음')
            #
            # if self.bottom_col:
            #     #print('하 붙음')

    def collision(self):
        if self.rect[3] == player.rect[3] and player.rect[1] == self.rect[1] and player.xdir != player.ST_X_NONE:
            # 오른쪽 충돌
            if self.rect[2] >= player.rect[0] and self.rect[0] < player.rect[2] and player.xdir == player.ST_X_BAKWARD:
                if self.isMerge:

                self.xdir = self.ST_X_BAKWARD
                #self.x -= self.speed
                self.old_x = self.x
                print('col 0')
            # 왼쪽 충돌
            elif self.rect[0] <= player.rect[2] and self.rect[2] > player.rect[0] and player.xdir == player.ST_X_FORWARD:
                self.xdir = self.ST_X_FORWARD
                #self.x += self.speed
                self.old_x = self.x
                print('col 1')
            else:
                self.xdir = self.ST_X_NONE
        elif self.rect[0] == player.rect[0] and player.rect[2] == self.rect[2] and player.ydir != player.ST_Y_NONE:
            # 위 충돌
            if self.rect[1] >= player.rect[3] and self.rect[3] < player.rect[1] and player.ydir == player.ST_Y_DOWN:
                self.ydir = self.ST_Y_DOWN
                #self.y -= self.speed
                self.old_y = self.y
                print('col 2')
            # 아래 충돌
            elif self.rect[3] <= player.rect[1] and self.rect[1] > player.rect[3] and player.ydir == player.ST_Y_UP:
                self.ydir = self.ST_Y_UP
                #self.y += self.speed
                self.old_y = self.y
                print('col 3')
            else:
                self.ydir = self.ST_X_NONE

    def collision2(self, ano):
        # 좌우
        if self.rect[3] == ano.rect[3] and ano.rect[1] == self.rect[1]:
            if self.rect[2] == ano.rect[0] and ano.state:
                # self.x = ano.x - (ano.left + ano.right)
                self.right += ano.right + ano.left
                ano.state = 0
                print('1')
            elif self.rect[0] == ano.rect[2] and not ano.state:
                # self.x = ano.x + (ano.left + ano.right)
                self.left += ano.right + ano.left
                ano.state = 1
                print('2')
        # 상하
        elif self.rect[0] == ano.rect[0] and ano.rect[2] == self.rect[2]:
            if self.rect[1] == ano.rect[3]:
                # self.y = ano.y - (ano.top + ano.bottom)
                self.top += ano.top + ano.bottom
                print('3')
            elif self.rect[3] == ano.rect[1]:
                # self.y = ano.y + (ano.top + ano.bottom)
                self.bottom += ano.top + ano.bottom
                print('4')

    def render(self):
        self.draw_image(8, 100, 100)

    def update(self):
        self.move()
        # if self.isMerge:
        #     print(self.old_x, self.nx, self.x)
        #     self.rect = [self.nx - 50, self.ny + 50, self.nx + 50, self.ny - 50]
        # else:
        self.rect = [self.x - self.left, self.y + self.top, self.x + self.right, self.y - self.bottom]


def exit():
    global running
    close_canvas()
    running = False
    pass


def handle_events():
    global running, cac_count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            exit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                exit()
            elif event.key == SDLK_q:
                for i in range(0, cac_count):
                    cac[i].__init__((i * 100) + 200, (i * 100) + 200)
                    cac[i].state = 0
            elif event.key == SDLK_e:
                print(player.rect)
                for i in range(0, cac_count):
                    print(cac[i].rect)
            else:
                player.handle_Stone(event)
        elif event.type == SDL_KEYUP:
            player.handle_Stone(event)


cac_count = 2

open_canvas(MAP_WIDTH, MAP_HEIGHT)
player = Stone()
player.set_image('stone.png')
cac = []
for i in range(cac_count):
    cac.append(Cactus((i * 100) + 100, (i * 100) + 100))
    cac[i].set_image('Cactus test.png')
Map_Test = load_image('Map_1.png')
running = True
BGM = load_music('SweetPoop .mp3')


def render():
    Map_Test.draw(MAP_WIDTH // 2, MAP_HEIGHT // 2)
    player.render()

    for i in range(0, cac_count):
        draw_rectangle(cac[i].rect[0], cac[i].rect[1], cac[i].rect[2], cac[i].rect[3])
        cac[i].render()


def update():
    player.update()
    for i in range(cac_count):
        cac[i].update()
        cac[i].collision()
        for j in range(cac_count):
            if not i == j:
                cac[i].New_coll(cac[j])

    handle_events()
    update_canvas()


while running:
    clear_canvas()
    render()
    update()
    delay(0.05)
