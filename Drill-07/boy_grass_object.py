from pico2d import *
import random


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 599
        self.frame = random.randint(0, 7)
        self.image = load_image('ball21x21.png')
        self.speed = random.randint(5, 15)

    def update(self):
        self.frame = (self.frame + 1) % 1
        if not self.y <= 70:
            self.y -= self.speed

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 25, 25, self.x, self.y)


class Big_Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 599
        self.frame = random.randint(0, 7)
        self.image = load_image('ball41x41.png')
        self.speed = random.randint(5, 15)

    def update(self):
        self.frame = (self.frame + 1) % 1
        if not self.y <= 70:
            self.y -= self.speed

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 41, 41, self.x, self.y)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code

open_canvas()

cnt = random.randint(0, 20)
team = [Boy() for i in range(11)]
grass = Grass()
small_balls = [Ball() for i in range(cnt)]
big_balls = [Big_Ball() for i in range(20-cnt)]

running = True
# game main loop code

while running:
    handle_events()

    for bird in team:
        bird.update()
    for ball in small_balls:
        ball.update()
    for b_ball in big_balls:
        b_ball.update()

    clear_canvas()
    grass.draw()
    for bird in team:
        bird.draw()

    for ball in small_balls:
        ball.draw()
    for b_ball in big_balls:
        b_ball.draw()



    update_canvas()

    delay(0.05)
# finalization code

close_canvas()
