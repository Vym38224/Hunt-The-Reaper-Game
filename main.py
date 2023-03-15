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
fps_bg = pygame.Surface((25,25))
fps_bg.fill((255,255,255))
fps_font = pygame.font.SysFont("Arial", 20)

mirror = 0
fire_attack = 0
click_x = 0
click_y = 0
fball_x = 1
fball_1x = -1* fball_x
fball_speed = 9

 
# Background + Obrázky
background_img = loadify("img/background.png")
background_img_rect = background_img.get_rect()

fzard_image = loadify(player1.img)
fzard_rect = fzard_image.get_rect()
fzard_rect.center = (width//2, height//2)
fzard2_image = loadify("img/firemag2.png")
fzard2_rect = fzard_image.get_rect()
fzard2_rect.center = (width//2, height//2)

fball_image = loadify("img/fireball.png")
fball_rect = fzard_image.get_rect()
fball2_image = loadify("img/fireball2.png")
fball2_rect = fzard_image.get_rect()


# Hlavní cyklus
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
        elif keys [pygame.K_s]:
            fzard_rect.y = fzard_rect.y + distance
            fzard2_rect.y = fzard2_rect.y + distance
        elif keys [pygame.K_a]:
            fzard_rect.x = fzard_rect.x - distance
            fzard2_rect.x = fzard2_rect.x - distance
            fzard2_rect.center = (fzard_rect.x + 60,fzard_rect.y + 60)
            mirror = 1
            fire_attack = 0
        elif keys [pygame.K_d]:
            fzard_rect.x = fzard_rect.x + distance
            fzard2_rect.x = fzard2_rect.x + distance
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
    if mirror == 1:
        screen.blit(fzard2_image,fzard2_rect)

    pygame.display.update()
    clock.tick_busy_loop(144)

# Ukončení hry
pygame.quit()

