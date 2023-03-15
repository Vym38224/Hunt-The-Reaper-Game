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
distance = 9
clock = pygame.time.Clock()
mirror = 0
fire_attack = 0
click_x = 0
click_y = 0
fball_x = 1
fball_1x = -1* fball_x
fball_speed = 9

 
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
fzard2_rect = fzard_image.get_rect()
fzard2_rect.center = (width//2, height//2)

fball_image = loadify(player1.img_attack)
fball_rect = fzard_image.get_rect()

fball2_image = loadify(player1.img_attack2)
fball2_rect = fzard_image.get_rect()

# Watermag
wzard_image = loadify(player2.img)
wzard_rect = wzard_image.get_rect()
wzard_rect.center = (width//2, height//2)

wzard2_image = loadify(player2.img2)
wzard2_rect = wzard_image.get_rect()
wzard2_rect.center = (width//2, height//2)

wzard_attack_image = loadify(player2.img_attack)
wzard_attack_rect = wzard_attack_image.get_rect()

wzard_attack2_image = loadify(player2.img_attack2)
wzard_attack2_rect = wzard_attack2_image.get_rect()

# TXT
name_text = pygame.font.SysFont("Moncerat", 20)
name_text = name_text.render(player1.name, True, white)
name_text_rect = name_text.get_rect()
name_text_rect.center = (600,440)

lvl_text = pygame.font.SysFont("Moncerat", 16)
lvl_text = lvl_text.render("lvl " + str(player1.level), True, yellow)
lvl_text_rect = lvl_text.get_rect()
lvl_text_rect.center = (600,450)


#### HLAVNÍ CYKLUS ####
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

        screen.blit(background_img, background_img_rect)
        
        keys = pygame.key.get_pressed()
        if keys [pygame.K_w]:
            fzard_rect.y = fzard_rect.y - distance
            fzard2_rect.y = fzard2_rect.y - distance
            name_text_rect.y = name_text_rect.y - distance  
            lvl_text_rect.y = lvl_text_rect.y - distance
        elif keys [pygame.K_s]:
            fzard_rect.y = fzard_rect.y + distance
            fzard2_rect.y = fzard2_rect.y + distance
            name_text_rect.y = name_text_rect.y + distance
            lvl_text_rect.y = lvl_text_rect.y + distance
        elif keys [pygame.K_a]:
            fzard_rect.x = fzard_rect.x - distance
            fzard2_rect.x = fzard2_rect.x - distance
            name_text_rect.x = name_text_rect.x - distance
            lvl_text_rect.x = lvl_text_rect.x - distance
            fzard2_rect.center = (fzard_rect.x + 60,fzard_rect.y + 60)
            mirror = 1
            fire_attack = 0
        elif keys [pygame.K_d]:
            fzard_rect.x = fzard_rect.x + distance
            fzard2_rect.x = fzard2_rect.x + distance
            name_text_rect.x = name_text_rect.x + distance
            lvl_text_rect.x = lvl_text_rect.x + distance
            mirror = 0
            fire_attack = 0
        elif keys [pygame.K_SPACE]:
            fball_rect.center = (fzard_rect.x + 150,fzard_rect.y + 80)
            fball2_rect.center = (fzard_rect.x + 60,fzard_rect.y + 80)
            fire_attack += 1

        if fire_attack >= 1 and mirror == 1: 
            screen.blit(fball2_image,fball2_rect)
            fball2_rect.x += fball_1x * fball_speed
        
        if fire_attack >= 1 and mirror == 0:            
            screen.blit(fball_image,fball_rect)
            fball_rect.x += fball_x * fball_speed
        
    if mirror == 0:
        screen.blit(fzard_image,fzard_rect)
        screen.blit(name_text,name_text_rect)
        screen.blit(lvl_text,lvl_text_rect)
    if mirror == 1:
        screen.blit(fzard2_image,fzard2_rect)
        screen.blit(name_text,name_text_rect)
        screen.blit(lvl_text,lvl_text_rect)

    pygame.display.update()
    clock.tick_busy_loop(60)

# Ukončení hry
pygame.quit()

