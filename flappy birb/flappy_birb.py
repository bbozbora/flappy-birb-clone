import pygame
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((288,512))
pygame.display.set_caption("asdadsasd")
clock = pygame.time.Clock()
game_active = True

sky_surf = pygame.image.load("sprites/background-day.png").convert_alpha()
base_surf = pygame.image.load("sprites/base.png").convert_alpha()
base1_rect = base_surf.get_rect(topleft = (0,400))
base2_rect = base_surf.get_rect(topleft = (336,400))

pipebot_surf = pygame.image.load("sprites/pipe-green.png").convert_alpha()
pipetop_surf = pygame.transform.flip(pipebot_surf,0 ,1)

gameover_surf = pygame.image.load("sprites/gameover.png").convert_alpha()

pipe_scale = 160
first_pipe_x = 500

pipe1top_rect = pipetop_surf.get_rect(bottomright = (first_pipe_x+pipe_scale*0,randint(50,250)))
pipe1bot_rect = pipebot_surf.get_rect(topright = (first_pipe_x+pipe_scale*0,pipe1top_rect.bottom + 100))

########

pipe2top_rect = pipetop_surf.get_rect(bottomright = (first_pipe_x+pipe_scale*1,randint(50,250)))
pipe2bot_rect = pipebot_surf.get_rect(topright = (first_pipe_x+pipe_scale*1,pipe2top_rect.bottom + 100))

########

pipe3top_rect = pipetop_surf.get_rect(bottomright = (first_pipe_x+pipe_scale*2,randint(50,250)))
pipe3bot_rect = pipebot_surf.get_rect(topright = (first_pipe_x+pipe_scale*2,pipe3top_rect.bottom + 100))


birb_surf = pygame.image.load("sprites/yellowbird-upflap.png").convert_alpha()
birb_rect = birb_surf.get_rect(midbottom = (90,300))

s0 = pygame.image.load("sprites/0.png").convert_alpha()
s1 = pygame.image.load("sprites/1.png").convert_alpha()
s2 = pygame.image.load("sprites/2.png").convert_alpha()
s3 = pygame.image.load("sprites/3.png").convert_alpha()
s4 = pygame.image.load("sprites/4.png").convert_alpha()
s5 = pygame.image.load("sprites/5.png").convert_alpha()
s6 = pygame.image.load("sprites/6.png").convert_alpha()
s7 = pygame.image.load("sprites/7.png").convert_alpha()
s8 = pygame.image.load("sprites/8.png").convert_alpha()
s9 = pygame.image.load("sprites/9.png").convert_alpha()

score_surf_list = [s0,s1,s2,s3,s4,s5,s6,s7,s8,s9]
temp_list=[s0]
score_total_width=0
score_x_coord=132

birb_gravity = 0
birb_jump = 0

score = 0
invis_point_rect = pygame.Rect((first_pipe_x, 0), (1, 512))

        

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()        

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    birb_jump = 7
                    birb_gravity = 0
                    print("asd")
    
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  
                    score=0
                    temp_list=[s0]
                    invis_point_rect = pygame.Rect((first_pipe_x, 0), (1, 512))
                    game_active = True
                    pipe1top_rect = pipetop_surf.get_rect(bottomright = (first_pipe_x+pipe_scale*0,randint(50,250)))
                    pipe1bot_rect = pipebot_surf.get_rect(topright = (first_pipe_x+pipe_scale*0,pipe1top_rect.bottom + 100))

                    ########

                    pipe2top_rect = pipetop_surf.get_rect(bottomright = (first_pipe_x+pipe_scale*1,randint(50,250)))
                    pipe2bot_rect = pipebot_surf.get_rect(topright = (first_pipe_x+pipe_scale*1,pipe2top_rect.bottom + 100))

                    ########

                    pipe3top_rect = pipetop_surf.get_rect(bottomright = (first_pipe_x+pipe_scale*2,randint(50,250)))
                    pipe3bot_rect = pipebot_surf.get_rect(topright = (first_pipe_x+pipe_scale*2,pipe3top_rect.bottom + 100))


    if game_active:

        pipe1top_rect.x -=2
        pipe1bot_rect.x -=2
        pipe2top_rect.x -=2
        pipe2bot_rect.x -=2
        pipe3top_rect.x -=2
        pipe3bot_rect.x -=2
        base1_rect.x -=2
        base2_rect.x -=2
        invis_point_rect.x -=2

        if pipe1top_rect.right <= 0: 
            pipe1top_rect.x += pipe_scale*3
            pipe1bot_rect.x += pipe_scale*3

            pipe1top_rect.bottom = randint(50,250)
            pipe1bot_rect.top = pipe1top_rect.bottom + 100
        
        if pipe2top_rect.right <= 0: 
            pipe2top_rect.x += pipe_scale*3
            pipe2bot_rect.x += pipe_scale*3

            pipe2top_rect.bottom = randint(50,250)
            pipe2bot_rect.top = pipe2top_rect.bottom + 100

        if pipe3top_rect.right <= 0: 
            pipe3top_rect.x += pipe_scale*3
            pipe3bot_rect.x += pipe_scale*3

            pipe3top_rect.bottom = randint(50,250)
            pipe3bot_rect.top = pipe3top_rect.bottom + 100

        if base1_rect.right <= 0:
            base1_rect.left += 672

        if base2_rect.right <= 0:
            base2_rect.left += 672

        a=1.1
        a=a**2

        birb_gravity += a/4 
        birb_rect.y += birb_gravity

        if birb_rect.bottom >= 400:  
            birb_gravity = 0 ########## game over
            birb_rect.bottom = 400
            
        if birb_jump > 0:
            birb_jump -= 1/4                #bunu yok et
            birb_rect.y -= birb_jump
            

        if birb_rect.colliderect(pipe1top_rect) or birb_rect.colliderect(pipe1bot_rect) or birb_rect.colliderect(pipe2top_rect) or birb_rect.colliderect(pipe2bot_rect) or birb_rect.colliderect(pipe3top_rect) or birb_rect.colliderect(pipe3bot_rect):
            game_active = False
            
              

        if birb_rect.colliderect(invis_point_rect):
            score += 1
            invis_point_rect.x += pipe_scale
            
            temp_list=[]

            for i in range(1,len(str(score))+1):                 
                temp_list.append(score_surf_list[int(str(score)[i-1])]) #fill the temp_list DONT FORGET TO EMPTY THE LIST AFTER!!!!!!!!!!!
                #print(int(str(score)[i-1]))
                
            #print(temp_list)
            #print("a")

            for i in temp_list:
                score_total_width += pygame.Surface.get_width(i)

            score_x_coord=int(144-score_total_width/2)
            score_total_width=0
            

        
        #print("birb gravity "+str(birb_gravity))
        #print("birb jump "+str(birb_jump))


        screen.blit(sky_surf,(0,0))   
        screen.blit(birb_surf,birb_rect)

        screen.blit(pipetop_surf,pipe1top_rect)
        screen.blit(pipebot_surf,pipe1bot_rect)
        screen.blit(pipetop_surf,pipe2top_rect)
        screen.blit(pipebot_surf,pipe2bot_rect)
        screen.blit(pipetop_surf,pipe3top_rect)
        screen.blit(pipebot_surf,pipe3bot_rect)

        screen.blit(base_surf,base1_rect)
        screen.blit(base_surf,base2_rect)


        
        

        a=-1
        b=-2

        for i in temp_list:
            
            a+=1
            b+=1
            c=1
            if a==0:
                c=0
            x= score_x_coord + pygame.Surface.get_width(temp_list[b]) * c
            screen.blit(i,(x,100))
            
        

    
    else:
        screen.blit(gameover_surf,(48,200))

    pygame.display.update()
    clock.tick(60)
