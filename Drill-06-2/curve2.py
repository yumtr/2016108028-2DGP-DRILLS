import random
from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 800, 600




def move_point(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    global x, y, i
    speed = 5
    if i < 1000:
        i = i + speed
        if 0 < i < 100:
            t = i / 100
            x = ((-t ** 3 + 2 * t ** 2 - t) * p10[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p2[0] + (t ** 3 - t ** 2) * p3[0]) / 2
            y = ((-t ** 3 + 2 * t ** 2 - t) * p10[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p2[1] + (t ** 3 - t ** 2) * p3[1]) / 2
        elif 100 < i < 200:
            t = (i - 100) / 100
            x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
            y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        elif 200 < i < 300:
            t = (i - 200) / 100
            x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p5[0]) / 2
            y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p5[1]) / 2
        elif 300 < i < 400:
            t = (i - 300) / 100
            x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p5[0] + (t ** 3 - t ** 2) * p6[0]) / 2
            y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p5[1] + (t ** 3 - t ** 2) * p6[1]) / 2
        elif 400 < i < 500:
            t = (i - 400) / 100
            x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p6[0] + (t ** 3 - t ** 2) * p7[0]) / 2
            y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p6[1] + (t ** 3 - t ** 2) * p7[1]) / 2
        elif 500 < i < 600:
            t = (i - 500) / 100
            x = ((-t ** 3 + 2 * t ** 2 - t) * p5[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p7[0] + (t ** 3 - t ** 2) * p8[0]) / 2
            y = ((-t ** 3 + 2 * t ** 2 - t) * p5[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p7[1] + (t ** 3 - t ** 2) * p8[1]) / 2
        elif 600 < i < 700:
            t = (i - 600) / 100
            x = ((-t ** 3 + 2 * t ** 2 - t) * p6[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p8[0] + (t ** 3 - t ** 2) * p9[0]) / 2
            y = ((-t ** 3 + 2 * t ** 2 - t) * p6[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p8[1] + (t ** 3 - t ** 2) * p9[1]) / 2
        elif 700 < i < 800:
            t = (i - 700) / 100
            x = ((-t ** 3 + 2 * t ** 2 - t) * p7[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p9[0] + (t ** 3 - t ** 2) * p10[0]) / 2
            y = ((-t ** 3 + 2 * t ** 2 - t) * p7[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p9[1] + (t ** 3 - t ** 2) * p10[1]) / 2
        elif 800 < i < 900:
            t = (i - 800) / 100
            x = ((-t ** 3 + 2 * t ** 2 - t) * p8[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p10[0] + (t ** 3 - t ** 2) * p1[0]) / 2
            y = ((-t ** 3 + 2 * t ** 2 - t) * p8[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p10[1] + (t ** 3 - t ** 2) * p1[1]) / 2
        elif 900 < i < 1000:
            t = (i - 900) / 100
            x = ((-t ** 3 + 2 * t ** 2 - t) * p9[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p1[0] + (t ** 3 - t ** 2) * p2[0]) / 2
            y = ((-t ** 3 + 2 * t ** 2 - t) * p9[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p1[1] + (t ** 3 - t ** 2) * p2[1]) / 2
    else:
        i = 3


running = True
open_canvas(KPU_WIDTH, KPU_HEIGHT)
KPU = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

x = 400
y = 300
frame = 0
rand_x = 0
rand_y = 0
i = 1
is_right = True

p1 = (random.randint(1, 7) * 100, random.randint(1, 5) * 100)
p2 = (random.randint(1, 7) * 100, random.randint(1, 5) * 100)
p3 = (random.randint(1, 7) * 100, random.randint(1, 5) * 100)
p4 = (random.randint(1, 7) * 100, random.randint(1, 5) * 100)
p5 = (random.randint(1, 7) * 100, random.randint(1, 5) * 100)
p6 = (random.randint(1, 7) * 100, random.randint(1, 5) * 100)
p7 = (random.randint(1, 7) * 100, random.randint(1, 5) * 100)
p8 = (random.randint(1, 7) * 100, random.randint(1, 5) * 100)
p9 = (random.randint(1, 7) * 100, random.randint(1, 5) * 100)
p0 = (random.randint(1, 7) * 100, random.randint(1, 5) * 100)

while running:
    clear_canvas()
    KPU.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    move_point((p1[0], p1[1]),
               (p2[0], p2[1]),
               (p3[0], p3[1]),
               (p4[0], p4[1]),
               (p5[0], p5[1]),
               (p6[0], p6[1]),
               (p7[0], p7[1]),
               (p8[0], p8[1]),
               (p9[0], p9[1]),
               (p0[0], p0[1]),)
    if is_right:
        character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    update_canvas()

    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()
