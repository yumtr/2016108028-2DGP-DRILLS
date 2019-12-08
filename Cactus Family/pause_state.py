from pico2d import *
import game_framework
import Cactus_Family

image = None
select_sound = None
size_x = 0
size_y = 0
pop_speed = 5
pop_up = None


def enter():
    global image, select_sound, size_x, size_y, pop_speed, pop_up
    image = load_image('image_file\\manual.png')
    select_sound = load_wav('sound_effect\\pause_sound.wav')
    select_sound.set_volume(100)
    select_sound.play()
    size_x = 0
    size_y = 0
    pop_speed = 5
    pop_up = True


def exit():
    pass


def update():
    global size_x, size_y, pop_speed
    if pop_up:
        if size_x < 450:
            size_x += 450 / 3 / pop_speed
        if size_y < 356:
            size_y += 356 / 3 / pop_speed

        if pop_speed != 1:
            pop_speed -= 1
    else:
        print(pop_speed)
        if size_x > 0:
            size_x -= 450 / 3 / pop_speed
        if size_y > 0:
            size_y -= 356 / 3 / pop_speed
        if pop_speed != 1:
            pop_speed -= 1
        if size_x <= 0:
            resume()


def draw():
    clear_canvas()
    Cactus_Family.draw()
    image.draw(450, 400, size_x, size_y)
    update_canvas()


def pause():
    pass


def resume():
    game_framework.pop_state()


def handle_events():
    global pop_up, pop_speed
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            select_sound.play()
            pop_up = False
            pop_speed = 5
