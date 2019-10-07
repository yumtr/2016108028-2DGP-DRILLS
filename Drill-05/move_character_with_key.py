from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 800, 600

def handle_events():
    global running
    global dir
    global C_x, C_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
        elif event.type == SDL_MOUSEMOTION:
            C_x, C_y = event.x + 18, KPU_HEIGHT - 1 - event.y - 20
    pass

def Move():
    global dir
    if x > 800:
        dir -= 2
    elif x < 0:
        dir += 2

open_canvas(KPU_WIDTH, KPU_HEIGHT)
KPU = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_curser = load_image('hand_arrow.png')
running = True
x = 800 // 2
frame = 0
dir = 1
C_x, C_y = 0,0


while running:
    clear_canvas()
    KPU.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand_curser.draw(C_x, C_y)
    if dir < 0:
        character.clip_draw(frame * 100, 0 * 1, 100, 100, x, 90)
    else:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, 90)
    update_canvas()

    handle_events()
    Move()
    frame = (frame + 1) % 8
    x += dir * 10
    delay(0.05)

close_canvas()

