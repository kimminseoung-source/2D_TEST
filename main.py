# LEC 11 
# 시작 시 화면 바닥부분에 랜덤한 20개 풍선 x 좌표 랜덤
# 풍선이 위로 올라감, 상승 속도는 풍선마다 다름
# 풍선이 화면 맨위에 도달하면 화면 밖으로 사라지지 않고 그 자리에서 위아래로 출렁

# 클래스를 만들고, 객체들을 생성하는 방식

# 커밋을 적절하게 할 것


from pico2d import * 
import random

class ball:
    pass

def reset_world():
    pass

def handle_event():
    global running
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running =False
        elif event.type == SDL_KEYDOWN and event.key() == SDLK_ESCAPE:
            running = False


def update_world():
    pass

def render_world():
    pass


open_canvas()

reset_world()

while running:
    handle_event()
    update_world()
    render_world()
    delay(0.5)

close_canvas()
