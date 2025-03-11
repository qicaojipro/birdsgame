import pygame
import random
from time import sleep
pygame.init()
pygame.mixer.init()
##########定义##########
goal=0
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
frame=0
map_kuan=284
map_gao=512
FPS=60
pipes=[[150,4]]
bird=[40,map_gao//2-50]
G=0.1
V=0
font=pygame.font.Font(None,24)
gameScreen=pygame.display.set_mode((map_kuan ,map_gao ))
time=pygame.time.Clock()
background=pygame.image.load("something/background.png")
bird_wing_up=bird_wing_up2=pygame.image.load("something/bird_wing_up.png ")
bird_wing_down=bird_wing_down2=pygame.image.load("something/bird_wing_down.png ")
guandao=pygame.image.load("something/pipe_body.png")
guandao2=pygame.image.load("something/pipe_end.png")
sound=pygame.mixer.Sound("something/birdssound.wav")
############函数############
def draw_pipes():
    for w in range(len(pipes)):
        for m in range(pipes[w][1]):
            gameScreen.blit(guandao,(pipes[w][0],m*32))
        for m in range(pipes[w][1]+6,16):
            gameScreen.blit(guandao,(pipes[w][0],m*32))
        gameScreen.blit(guandao2, (pipes[w][0],((pipes)[w][1]) * 32))
        gameScreen.blit(guandao2, (pipes[w][0], ((pipes)[w][1] +5) * 32))
        pipes[w][0]-=1
def game_while():
    global V,goal
    global G
    global bird_wing_down
    global bird_wing_up
    while True:
        if len(pipes)<4:
            x=pipes[-1][0]+200
            long=random.randrange(1,9)
            pipes.append([x,long])
        if pipes[0][0]<-100:
            pipes.pop(0)
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    sound.set_volume(0.5)
                    sound.play()
                    if event.type==pygame.KEYUP:
                        sound.stop()
                    bird[1]-=30
                    V=0
            if event.type==pygame.QUIT:
                pygame.quit()
                return
        if pipes[0][0]-30==bird[0] :### < pipes[0][0] +32:
            goal += 1

        V+=G
        bird[1]+=V
        bird_wing_up=pygame.transform.rotate(bird_wing_up2,-90*(V/15))
        bird_wing_down = pygame.transform.rotate(bird_wing_down2, -90 * (V / 15))
        gameScreen.blit(background,(0,0))
        draw_pipes()
        birdwrite(bird[0],bird[1])
        goal_text=font.render(f"Score:{goal}",True,RED)
        goal_rect=goal_text.get_rect(topright=(map_kuan-20,20))
        gameScreen.blit(goal_text,goal_rect)
        pygame.display.update()
        if not safe():
            sleep(3)
            reset()
        time.tick(FPS)
def birdwrite(x,y):
    global frame,goal
    if 0<=frame<=30:
        gameScreen.blit(bird_wing_down,(x,y))
        frame+=1
    elif 30 < frame <= 60:
        gameScreen.blit(bird_wing_up, (x, y))
        frame += 1
        if frame==60:
            frame=0
def safe():
    global goal
    if bird[1]>map_gao-35:

        return False
    if bird[1]<0:

        return False
    if pipes[0][0]-30<bird[0]<pipes[0][0]+79:
        if bird[1]<(pipes[0][1]+1)*32 or bird[1]>(pipes[0][1]+4)*32:
            print("暴毙了")
            return False
    return True
def reset():
    global frame,map_kuan,map_gao,FPS,pipes,bird,map_kuan,G,V,goal
    frame = 0
    goal=0
    map_kuan = 284
    map_gao = 512
    FPS = 60
    pipes.clear()
    bird.clear()
    pipes = [[150, 4]]
    bird = [40, map_gao // 2 - 50]
    G = 0.1
    V = 0
pygame.display.set_caption("我是好鸟")
game_while()
