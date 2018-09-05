import pygame,sys,random
from pygame.locals import *

#colors (R,G,B) 
red=(255,0,0)
green=(127,255,0)
blue=(135,206,250)
black=(0,0,0)
white=(255,255,255)
yellow=(255,255,0)

pygame.init()   #initialize
window=pygame.display.set_mode((600,600))   #window 800x600
pygame.display.set_caption('Crappy Bird')
clock=pygame.time.Clock()
fps=60

birdY=260

pipe1_len=random.randint(70,400)
pipe1_x=300
pipe1_y=0

pipe2_len=random.randint(70,400)
pipe2_x=450
pipe2_y=0

pipe3_len=random.randint(70,400)
pipe3_x=600
pipe3_y=0

pipe4_len=random.randint(70,400)
pipe4_x=750
pipe4_y=0

top_pipe1_y = top_pipe2_y = top_pipe3_y = top_pipe4_y = 0
score=0

fontobj=pygame.font.SysFont('freesansbold.ttf',50)
scorefont=pygame.font.Font('freesansbold.ttf',64)

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                birdY-=50
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_SPACE:
                birdY+=0
                
    if pipe1_x==0:
        pipe1_x=600
        pipe1_len=random.randint(70,400)
    if pipe2_x==0:
        pipe2_x=600
        pipe2_len=random.randint(70,400)
    if pipe3_x==0:
        pipe3_x=600
        pipe3_len=random.randint(70,400)
    if pipe4_x==0:
        pipe4_x=600
        pipe4_len=random.randint(70,400)

    top_pipe1_len=450-pipe1_len
    top_pipe2_len=450-pipe2_len
    top_pipe3_len=450-pipe3_len
    top_pipe4_len=450-pipe4_len
    
    birdY+=2.5
    bird=pygame.Rect(100,birdY,40,40)

    pipe1=pygame.Rect(pipe1_x,pipe1_y,50,pipe1_len)
    pipe1_x-=1
    pipe1.bottom=600
    top_pipe1=pygame.Rect(pipe1_x,top_pipe1_y,50,top_pipe1_len)
        
    pipe2=pygame.Rect(pipe2_x,pipe2_y,50,pipe2_len)
    pipe2_x-=1
    pipe2.bottom=600
    top_pipe2=pygame.Rect(pipe2_x,top_pipe2_y,50,top_pipe2_len)
    
    pipe3=pygame.Rect(pipe3_x,pipe3_y,50,pipe3_len)
    pipe3_x-=1
    pipe3.bottom=600
    top_pipe3=pygame.Rect(pipe3_x,top_pipe3_y,50,top_pipe3_len)
    
    pipe4=pygame.Rect(pipe4_x,pipe4_y,50,pipe4_len)
    pipe4_x-=1
    pipe4.bottom=600
    top_pipe4=pygame.Rect(pipe4_x,top_pipe4_y,50,top_pipe4_len)
 
    pipes=[pipe1,top_pipe1,pipe2,top_pipe2,pipe3,top_pipe3,pipe4,top_pipe3]
    bottompipes=[pipe1,pipe2,pipe3,pipe4]

    for i in pipes:
        if bird.colliderect(i) or birdY==560:
            pygame.time.delay(1000)
            window.fill(blue)
            textover=fontobj.render('GAME OVER',True,white,blue)    #game over
            textoverrect=textover.get_rect()
            textoverrect.centerx=300
            textoverrect.centery=300
            window.blit(textover,textoverrect)
            pygame.display.update()
            pygame.time.delay(1000)
            pygame.quit()
            sys.exit()
    for i in bottompipes:
        if i.centerx==100:
            score+=1
           
    scoretext=scorefont.render(str(score),True,red,blue)
    scorerect=scoretext.get_rect()
    scorerect.centerx=300
    scorerect.centery=75
    
    window.fill(blue)
    window.fill(green,pipe1)
    window.fill(green,pipe2)
    window.fill(green,pipe3)
    window.fill(green,pipe4)
    window.fill(green,top_pipe1)
    window.fill(green,top_pipe2)
    window.fill(green,top_pipe3)
    window.fill(green,top_pipe4)
    window.fill(yellow,bird)
    window.blit(scoretext,scorerect)
    
    pygame.display.update()
    clock.tick(fps)
