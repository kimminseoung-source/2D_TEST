# LEC 11 
# 시작 시 화면 바닥부분에 랜덤한 20개 풍선 x 좌표 랜덤
# 풍선이 위로 올라감, 상승 속도는 풍선마다 다름
# 풍선이 화면 맨위에 도달하면 화면 밖으로 사라지지 않고 그 자리에서 위아래로 출렁

# 1. 랜덤한 풍선 20개 생성
# 1-1 풍선 화면이 띄우기, 
# 2. 풍선이 위로 향함, 속도는 다르게
# 3. 풍선이 위에 도달하면 그자리에서 둥둥 머물기


# 클래스를 만들고, 객체들을 생성하는 방식

# 커밋을 적절하게 할 것


from pico2d import * 
import random

class Ball:
    def __init__(self):
        self.image = load_image('ball.png')
        self.x, self.y = random.randint(100, 700), 0

    def draw(self):
        self.image.clip_draw(0,0,41,41,self.x, self.y)
        pass

    def update(self):
        self.y += random.randint(5,30)
        pass
    
   



def reset_world():
    global running
    global world

    running = True


    world = []
    
    ball = Ball()
    balls = [Ball() for i in range (0,20)]
    world+=balls
    

def handle_event():
    global running
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running =False
        elif event.type == SDL_KEYDOWN and event.key() == SDLK_ESCAPE:
            running = False


def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()

    for o in world:
        o.draw()

    update_canvas()

    pass


open_canvas()

reset_world()

while running:
    handle_event()
    update_world()
    render_world()
    delay(0.5)



close_canvas()


