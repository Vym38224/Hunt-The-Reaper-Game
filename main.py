import pygame
from players import *

def loadify(imgname):
    return pygame.image.load(imgname).convert_alpha()

# Inicializace
pygame.init()

width = 1200
height = 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hra")

# Barvičky 
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
dark_green = (0, 100, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
grey = (130,130,130)
    
# Nastavení
fps = 60
clock = pygame.time.Clock()
mirror = 0
fire_attack = 0
wire_attack = 0
attack_x = 1
attack_1x = -1* attack_x
attack_speed = 8
distance = 9
mag = 1
fmag = 0
wmag = 1

 
#### BACKGROUND, OBRÁZKY, TEXTY ####
# BG
background_img = loadify(background.img)
background_img_rect = background_img.get_rect()

# IMG
# Firemag
fzard_image = loadify(player1.img)
fzard_rect = fzard_image.get_rect()
fzard_rect.center = (width//2, height//2)

fzard2_image = loadify(player1.img2)
fzard2_rect = fzard2_image.get_rect()
fzard2_rect.center = (width//2, height//2)

fball_image = loadify(player1.img_attack)
fball_rect = fball_image.get_rect()

fball2_image = loadify(player1.img_attack2)
fball2_rect = fball2_image.get_rect()

name1_text = pygame.font.SysFont("Moncerat", 20)
name1_text = name1_text.render(player1.name, True, white)
name1_text_rect = name1_text.get_rect()
name1_text_rect.center = (600,440)

lvl1_text = pygame.font.SysFont("Moncerat", 16)
lvl1_text = lvl1_text.render("lvl " + str(player1.level), True, yellow)
lvl1_text_rect = lvl1_text.get_rect()
lvl1_text_rect.center = (600,450)




# Watermag
wzard_image = loadify(player2.img)
wzard_rect = wzard_image.get_rect()
wzard_rect.center = (width//2, height//2)

wzard2_image = loadify(player2.img2)
wzard2_rect = wzard_image.get_rect()
wzard2_rect.center = (width//2 , height//2 )

wzard_attack_image = loadify(player2.img_attack)
wzard_attack_rect = wzard_attack_image.get_rect()

wzard_attack2_image = loadify(player2.img_attack2)
wzard_attack2_rect = wzard_attack2_image.get_rect()

name2_text = pygame.font.SysFont("Moncerat", 20)
name2_text = name2_text.render(player2.name, True, white)
name2_text_rect = name2_text.get_rect()
name2_text_rect.center = (592,435)

lvl2_text = pygame.font.SysFont("Moncerat", 16)
lvl2_text = lvl2_text.render("lvl " + str(player2.level), True, yellow)
lvl2_text_rect = lvl2_text.get_rect()
lvl2_text_rect.center = (588,445)



#### HLAVNÍ CYKLUS ####
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    screen.blit(background_img, background_img_rect)

    # Firemag
    if mag == 1 and fmag == 1:
        keys = pygame.key.get_pressed()
        if keys [pygame.K_w] and fzard_rect.top > 0 and fzard2_rect.top > 0:
            fzard_rect.y = fzard_rect.y - distance
            fzard2_rect.y = fzard2_rect.y - distance
            name1_text_rect.y = name1_text_rect.y - distance  
            lvl1_text_rect.y = lvl1_text_rect.y - distance
        elif keys [pygame.K_s] and fzard_rect.bottom < height - 120 and fzard2_rect.bottom < height - 120:
            fzard_rect.y = fzard_rect.y + distance
            fzard2_rect.y = fzard2_rect.y + distance
            name1_text_rect.y = name1_text_rect.y + distance
            lvl1_text_rect.y = lvl1_text_rect.y + distance
        elif keys [pygame.K_a] and fzard_rect.left > 0 and fzard2_rect.left > 0:
            fzard_rect.x = fzard_rect.x - distance
            fzard2_rect.x = fzard2_rect.x - distance
            name1_text_rect.x = name1_text_rect.x - distance
            lvl1_text_rect.x = lvl1_text_rect.x - distance    
            mirror = 1
        elif keys [pygame.K_d] and fzard_rect.right > 0 and fzard2_rect.right < width:
            fzard_rect.x = fzard_rect.x + distance
            fzard2_rect.x = fzard2_rect.x + distance
            name1_text_rect.x = name1_text_rect.x + distance
            lvl1_text_rect.x = lvl1_text_rect.x + distance
            mirror = 0 

        elif keys [pygame.K_SPACE]:
            if mirror == 1:
                fball2_rect.center = (fzard2_rect.x + 20,fzard2_rect.y + 35)
                fire_attack = 1
            if mirror == 0:
                fball_rect.center = (fzard_rect.x + 100,fzard_rect.y + 35)
                fire_attack = 2
        
        elif fire_attack == 1:
            screen.blit(fball2_image,fball2_rect)
            fball2_rect.x += attack_1x * attack_speed
        elif fire_attack == 2:
            screen.blit(fball_image,fball_rect)
            fball_rect.x += attack_x * attack_speed         
        
        if mirror == 0:
            screen.blit(fzard_image,fzard_rect)
            screen.blit(name1_text,name1_text_rect)
            screen.blit(lvl1_text,lvl1_text_rect)
        if mirror == 1:
            screen.blit(fzard2_image,fzard2_rect)
            screen.blit(name1_text,name1_text_rect)
            screen.blit(lvl1_text,lvl1_text_rect)


    # Water mag
    if mag == 1 and wmag == 1:
        keys = pygame.key.get_pressed()
        if keys [pygame.K_w] and wzard_rect.top > 0 and wzard2_rect.top > 0:
            wzard_rect.y = wzard_rect.y - distance
            wzard2_rect.y = wzard2_rect.y - distance
            name2_text_rect.y = name2_text_rect.y - distance  
            lvl2_text_rect.y = lvl2_text_rect.y - distance
        elif keys [pygame.K_s] and wzard_rect.bottom < height - 120 and wzard2_rect.bottom < height - 120:
            wzard_rect.y = wzard_rect.y + distance
            wzard2_rect.y = wzard2_rect.y + distance
            name2_text_rect.y = name2_text_rect.y + distance
            lvl2_text_rect.y = lvl2_text_rect.y + distance
        elif keys [pygame.K_a] and wzard_rect.left > 0 and wzard2_rect.left > 0:
            wzard_rect.x = wzard_rect.x - distance
            wzard2_rect.x = wzard2_rect.x - distance
            name2_text_rect.x = name2_text_rect.x - distance
            lvl2_text_rect.x = lvl2_text_rect.x - distance
            mirror = 1
        elif keys [pygame.K_d] and wzard_rect.right > 0 and wzard2_rect.right < width:
            wzard_rect.x = wzard_rect.x + distance
            wzard2_rect.x = wzard2_rect.x + distance
            name2_text_rect.x = name2_text_rect.x + distance
            lvl2_text_rect.x = lvl2_text_rect.x + distance
            mirror = 0       
              
        elif keys [pygame.K_SPACE]:
            if mirror == 1:
                wzard_attack2_rect.center = (wzard2_rect.x + 20,wzard2_rect.y + 35)
                wire_attack = 1
            if mirror == 0:
                wzard_attack_rect.center = (wzard_rect.x + 100,wzard_rect.y + 35)
                wire_attack = 2
        
        elif wire_attack == 1:
            screen.blit(wzard_attack2_image,wzard_attack2_rect)
            wzard_attack2_rect.x += attack_1x * attack_speed
        elif wire_attack == 2:
            screen.blit(wzard_attack_image,wzard_attack_rect)
            wzard_attack_rect.x += attack_x * attack_speed         
        
        if mirror == 0:
            screen.blit(wzard_image,wzard_rect)
            screen.blit(name2_text,name2_text_rect)
            screen.blit(lvl2_text,lvl2_text_rect)
        if mirror == 1:
            screen.blit(wzard2_image,wzard2_rect)
            screen.blit(name2_text,name2_text_rect)
            screen.blit(lvl2_text,lvl2_text_rect)
            
    
    pygame.display.update()
    clock.tick_busy_loop(fps)

# Ukončení hry
pygame.quit()

