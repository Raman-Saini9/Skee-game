import pygame

pygame.init()
screen = pygame.display.set_mode((600,700))
pygame.display.set_caption("Snow Rider")
#Loading necessary images
background_1 = pygame.image.load("resources\\bg_1.png")
background_2 = pygame.image.load("resources\\bg_2.png")
snow_1 = pygame.image.load("resources\\snow1.png")
snow_2 = pygame.image.load("resources\\snow2.png")
filler_snow = pygame.image.load("resources\\fill_snow.png")
moon = pygame.image.load("resources\\moon.png")
player_move = pygame.image.load("resources\\player_move.png")
player_jump = pygame.image.load("resources\\player_jump.png")
obstacle = pygame.image.load("resources\\stone.png")


pygame.display.set_icon(player_jump)

#loading fonts
game_over_font= pygame.font.Font('freesansbold.ttf',64)
score_font= pygame.font.Font('freesansbold.ttf',32)
instruction_font= pygame.font.Font('freesansbold.ttf',16)

score_value = 0

def game_over():
    game_over_text = game_over_font.render("GAME OVER!",True,(255,255,255))
    screen.blit(game_over_text,(100,350))


def score():
    score_text = score_font.render("Score: "+ str(score_value),True,(255,255,255))
    screen.blit(score_text, (420,12))

def instruction():
    inst_text = instruction_font.render("Hit Space Bar to play again!",True,(255,255,255))
    screen.blit(inst_text,(200,450))

#Preset Values
b1_x = 0
b2_x = 601
s1_x = 1
s2_x = 601
fs_x = 1201
player_x = 12    
player_y = 550
jump_state = 'ready'
jump_condition = 'up'
obstacle_x = 601
collision = False
game_on = True
running = True

#Main Game Loop
while running:

    screen.blit(background_1,(b1_x,0))
    screen.blit(background_2,(b2_x,0))
    screen.blit(moon , (300,12))
    screen.blit(snow_1 , (s1_x,0))
    screen.blit(snow_2 , (s2_x,0))
    screen.blit(filler_snow,(fs_x ,560) )
    screen.blit(obstacle, (obstacle_x,582))

    #Properly quiting game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Jump Key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_x == 12 :
                jump_state = 'jump'
                
                #Restarting the game to play again
                if game_on == False:
                    score_value = 0
                    game_on = True
                
    
    #if already jumping               
    if jump_state ==  'jump':
        
        #if player on ground level
        if player_y >= 550:
            jump_condition = 'up'
        
        #if player at highest level
        elif player_y <= 350:
            jump_condition = 'down'
        
        if jump_condition == 'up':
            screen.blit(player_jump, (player_x,player_y))
            player_y -= 10
        
        elif jump_condition == 'down':
            screen.blit(player_jump, (player_x,player_y))
            player_y += 10
            
            #Player ready to jump
            if player_y == 550:
                jump_state = 'ready'
    
    #if ready to jump
    elif jump_state == 'ready':
        screen.blit(player_move , (player_x, player_y))
    
    #Check for collision
    if obstacle_x >= 32 and obstacle_x <= 52 :
        if player_y <= 550 and player_y >= 530:
            collision = True
        else:
            collision = False
                  
    x_change = 10

    # if Collision or not
    if collision == True:
        game_over()
        instruction()
        game_on = False
        #stopping all movement 
        b1_x -= 0
        b2_x -= 0
        s1_x -= 0
        s2_x -= 0
        fs_x -= 0
        obstacle_x -= 0
    
    elif collision == False:
        #Changing co-ordinates
        b1_x -= 1
        b2_x -= 1
        s1_x -= x_change
        s2_x -= x_change
        fs_x -= x_change
        obstacle_x -= x_change
    
    #obstacle movement , score increment
    if obstacle_x < -31:
        obstacle_x = 601
        score_value += 1
    
    #Background movement
    if b1_x == -601:
        b1_x = 601
    if b2_x == -601:
        b2_x = 601

    #Snow movement
    if s1_x <= -601:
        s1_x = 601
    if s2_x <= -601:
        s2_x = 601
    if fs_x <= -601:
        fs_x = 601
      
    score()
    
    pygame.display.update()

