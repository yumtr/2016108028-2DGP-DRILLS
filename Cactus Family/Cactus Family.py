from pico2d import *


class Player():
    ST_X_NONE, ST_X_FORWARD, ST_X_BAKWARD = 0, 1, 2
    ST_Y_NONE, ST_Y_UP, ST_Y_DOWN = 3, 4, 5
    HIGH_SPEED = 10
    LOW_SPEED = 4
    pass


class Cactus(Player):
    def __init__(self):
        self.xdir = self.ST_X_NONE
        self.ydir = self.ST_X_NONE
        pass

    frame = 0
    x = 400
    y = 300
    obj = 0
    speed = 10

    def set_pos(self, ix, iy):
        self.x = ix
        self.y = iy

    def draw_image(self):
        self.obj.clip_draw(self.frame * 100, 0 * 1, 100, 100, self.x, self.y)
        self.frame = (self.frame + 1) % 8

    def move(self):
        if self.xdir == self.ST_X_FORWARD:
            self.x += self.speed
        elif self.xdir == self.ST_X_BAKWARD:
            self.x -= self.speed

        if self.ydir == self.ST_Y_UP:
            self.y += self.speed
        elif self.ydir == self.ST_Y_DOWN:
            self.y -= self.speed

    def handle_cactus(self, event):
        if event.type == SDL_KEYDOWN:
            print('key downed')
            if event.key == SDLK_d:
                if self.xdir in (self.ST_X_NONE, self.ST_X_BAKWARD):
                    self.x = ST_X_FORWARD
            elif event.key == SDLK_a:
                if self.xdir in (self.ST_X_NONE, self.ST_X_FORWARD):
                    self.x = ST_X_BAKWARD
            elif event.key == SDLK_w:
                if self.ydir in (self.ST_Y_NONE, self.ST_Y_DOWN):
                    self.y = ST_Y_UP
            elif event.key == SDLK_s:
                if self.ydir in (self.ST_Y_NONE, self.ST_Y_UP):
                    self.y = ST_Y_DOWN
            elif event.key == SDLK_g:
                self.set_pos(300, 400)

    def render(self):
        self.draw_image()

    def update(self):
        self.move()


def exit():
    global running
    close_canvas()
    running = False
    pass


def handle_events():
    global running
    global dir
    global dir_y

    events = get_events()
    for event in events:
        test.handle_cactus(event)
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
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


test = Cactus()

open_canvas()
test.obj = load_image('Cactus test.png')
grass = load_image('grass.png')
# cactus = load_image('Cactus test.png')
stone = load_image('stone.png')

running = True
x = 400 // 2
y = 90

frame_stone = 0
dir = 0
dir_y = 0


def render():
    global frame_stone
    grass.draw(400, 30)
    test.render()
    stone.clip_draw(frame_stone * 100, 0 * 1, 100, 100, x, y)
    frame_stone = (frame_stone + 1) % 20


def update():
    test.update()
    handle_events()
    update_canvas()


while running:
    clear_canvas()
    render()
    update()
    x += dir * 10
    y += dir_y * 10
    delay(0.05)
