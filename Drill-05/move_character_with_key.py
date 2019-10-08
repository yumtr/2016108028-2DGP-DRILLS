from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 800, 600

def handle_events():
    global running
    global C_x, C_y
    global p1, p2
    global x,y, i, is_right

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                i = 0
                p1 = (x, y)
                p2 = event.x, event.y
                if p2[0] - p1[0] < 0:
                    is_right = True
                else:
                    is_right = False
        elif event.type == SDL_MOUSEMOTION:
            C_x, C_y = event.x + 18, KPU_HEIGHT - 1 - event.y - 20
    pass

def Move(p1, p2):
    global x, y
    global i
    if i < 100:
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        i = i + 3





open_canvas(KPU_WIDTH, KPU_HEIGHT)
KPU = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_curser = load_image('hand_arrow.png')

running = True
x = 400
y = 300
frame = 0
dir = 1
C_x, C_y = 0, 0
i = 0
p1, p2 = (x, y), (x, y)
is_right = True
while running:
    clear_canvas()
    KPU.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand_curser.draw(C_x, C_y)

    Move(p1, p2)
    if is_right == True:
        character.clip_draw(frame * 100, 0 * 1, 100, 100, x, KPU_HEIGHT - 1 - y)
    else:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, KPU_HEIGHT - 1 - y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

    delay(0.05)

close_canvas()

