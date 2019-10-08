from pico2d import *


def handle_events():
    global running
    global dir
    global dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
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
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


open_canvas()
grass = load_image('grass.png')
character = load_image('Cactus test.png')
stone = load_image('stone.png')

running = True
x = 400 // 2
y = 90

print(rect)

frame = 0
frame_stone = 0
dir = 0
dir_y = 0

while running:
    clear_canvas()
    grass.draw(400, 30)

    # if dir > 0:
    #   character.clip_draw(frame * 100, 100 * 1, 100, 100, x, 90)
    # else:
    #   character.clip_draw(frame * 100, 0 * 1, 100, 100, x, 90)
    character.clip_draw(frame * 100, 0 * 1, 100, 100, 400, 90)
    stone.clip_draw(frame_stone * 100, 0 * 1, 100, 100, x, y)

    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    frame_stone = (frame_stone + 1) % 20

    x += dir * 10
    y += dir_y * 10
    delay(0.05)

close_canvas()
