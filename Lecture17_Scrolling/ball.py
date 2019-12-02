import random
from pico2d import *
import game_world
import game_framework
import main_state

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1800), random.randint(0, 1100)
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.bg = None

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def set_background(self, bg):
        self.bg = bg

    def draw(self):
        cx, cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        Ball.image.clip_draw(0, 0, 21, 21, cx, cy)


    def update(self):
        pass


    def set_background(self, bg):
        self.bg = bg

# fill here
# class BigBall
