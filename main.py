import pygame
import random
from players import *

# načtení IMG 
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
green = (124, 252, 0)
    
# Nastavení
fps = 60
clock = pygame.time.Clock()
#---------------------------#
# Hráč v poli
player_fmag = int()
player_fmag_str=str(player_fmag)
try:
    f_fmag = open("player_fmag.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_fmag.read(player_fmag)
f_fmag.close()

player_wmag = int()
player_wmag_str=str(player_wmag)
try:
    f_player_wmag = open("player_wmag.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_player_wmag.read(player_wmag)

#---------------------------#
# Nepřítel v poli
enemy = int()
enemy_str=str(enemy)
try:
    f_enemies = open("enemies.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemies.read(enemy)

#---------------------------#
mirror = 0
fire_attack = 0
wire_attack = 0

attack_x = 1
attack_1x = -1* attack_x

scelet_x = random.choice ([-1,1])
scelet_y = random.choice([-1,1])

scelet_speed = 3
attack_speed = 8
distance = 9

fmag_hp = (player1.hp)
if player_fmag > 0:
    str_fmag_hp = str(fmag_hp)
    try:
        f1 = open("fmag_hp.txt", "r")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")
    text = f1.read(fmag_hp)
    f1.close()

wmag_hp = (player2.hp)
if player_wmag > 0:
    str_wmag_hp = str(wmag_hp)
    try:
        f2 = open("wmag_hp.txt", "r")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")
    text = f2.read(wmag_hp)
    f2.close()

scelet_hp = (enemy0.hp)
if enemy == 1:
    str_scelet_hp = str(scelet_hp)
    try:
        f3 = open("scelet_hp.txt", "r")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")
    text = f3.read(scelet_hp)
    f3.close()


 
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



# Portal
if enemy >= 1:
    portal_image = loadify("img/portal.png")
    portal_image_rect = portal_image.get_rect()
    portal_image_rect.center = (width//2 + 500, height//2 - 250)

# Sceleton
scelet_image = loadify(enemy0.img)
scelet_rect = scelet_image.get_rect()
scelet_rect.center = (width//2 + 500, height//2 - 250)

e_name_text = pygame.font.SysFont("Moncerat", 20)
e_name_text = e_name_text.render(enemy0.name, True, red)
e_name_text_rect = e_name_text.get_rect()
e_name_text_rect.center = (992,435)


#### HLAVNÍ CYKLUS ####


lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False


### OBJEKTY ###

# bg
    screen.blit(background_img, background_img_rect)
# Portal
    if enemy >= 1:
        screen.blit(portal_image,portal_image_rect)


### POSTAVY ###
    keys = pygame.key.get_pressed()
    if keys [pygame.K_1]:
        player_fmag += 1
        player_fmag_str = str(player_fmag)
        try:
            f_fmag = open("player_fmag.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_fmag.write(player_fmag_str)
        f_fmag.close()
        if player_wmag > 0:
            player_wmag -= 10
            player_wmag_str = str(player_wmag)
            try:
                f_wmag = open("player_wmag.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f_wmag.write(player_wmag_str)
            f_wmag.close()

    keys = pygame.key.get_pressed()
    if keys [pygame.K_2]:
        player_wmag += 1
        player_wmag_str = str(player_wmag)
        try:
            f_wmag = open("player_wmag.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_wmag.write(player_wmag_str)
        f_wmag.close()
        if player_fmag > 0:
            player_fmag -= 10
            player_fmag_str = str(player_fmag)
            try:
                f_fmag = open("player_fmag.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f_fmag.write(player_fmag_str)
            f_fmag.close()



    # Firemag
    if player_fmag > 0:
        hp1_text = pygame.font.SysFont("Moncerat", 18)
        if fmag_hp >= 250:
            hp1_text = hp1_text.render("HP: " + f"{fmag_hp}", True, green)
        if fmag_hp >= 125 and fmag_hp < 250:
            hp1_text = hp1_text.render("HP: " + f"{fmag_hp}", True, yellow)
        if fmag_hp >= 0 and fmag_hp < 125:
            hp1_text = hp1_text.render("HP: " + f"{fmag_hp}", True, red)
        if fmag_hp < 0:
            hp1_text = hp1_text.render("HP (seš mrtvej sračko): " + f"{fmag_hp}", True, red)
        hp1_text_rect = hp1_text.get_rect()
        hp1_text_rect.center = (fzard_rect.x + 60, fzard_rect.y + 135)
        keys = pygame.key.get_pressed()
        if keys [pygame.K_w] and fzard_rect.top > 0 and fzard2_rect.top > 0:
            fzard_rect.y = fzard_rect.y - distance
            fzard2_rect.y = fzard2_rect.y - distance
            name1_text_rect.y = name1_text_rect.y - distance  
            hp1_text_rect.y = hp1_text_rect.y - distance
        elif keys [pygame.K_s] and fzard_rect.bottom < height - 120 and fzard2_rect.bottom < height - 120:
            fzard_rect.y = fzard_rect.y + distance
            fzard2_rect.y = fzard2_rect.y + distance
            name1_text_rect.y = name1_text_rect.y + distance
            hp1_text_rect.y = hp1_text_rect.y + distance
        elif keys [pygame.K_a] and fzard_rect.left > 0 and fzard2_rect.left > 0:
            fzard_rect.x = fzard_rect.x - distance
            fzard2_rect.x = fzard2_rect.x - distance
            name1_text_rect.x = name1_text_rect.x - distance
            hp1_text_rect.x = hp1_text_rect.x - distance    
            mirror = 1
        elif keys [pygame.K_d] and fzard_rect.right > 0 and fzard2_rect.right < width:
            fzard_rect.x = fzard_rect.x + distance
            fzard2_rect.x = fzard2_rect.x + distance
            name1_text_rect.x = name1_text_rect.x + distance
            hp1_text_rect.x = hp1_text_rect.x + distance
            mirror = 0 

        elif keys [pygame.K_SPACE] and mirror == 1:
            fball2_rect.center = (fzard2_rect.x + 20,fzard2_rect.y + 35)
            fire_attack = 1
        elif keys [pygame.K_SPACE] and mirror == 0:
            fball_rect.center = (fzard_rect.x + 100,fzard_rect.y + 35)
            fire_attack = 2
            
        if fire_attack == 1:
            screen.blit(fball2_image,fball2_rect)
            fball2_rect.x += attack_1x * attack_speed
        if fire_attack == 2:
            screen.blit(fball_image,fball_rect)
            fball_rect.x += attack_x * attack_speed 
    
        if mirror == 0:
            screen.blit(fzard_image,fzard_rect)
            screen.blit(name1_text,name1_text_rect)
            screen.blit(hp1_text,hp1_text_rect)
        if mirror == 1:
            screen.blit(fzard2_image,fzard2_rect)
            screen.blit(name1_text,name1_text_rect)
            screen.blit(hp1_text,hp1_text_rect)

    # Water mag
    if player_wmag > 0:
        hp2_text = pygame.font.SysFont("Moncerat", 18)
        if wmag_hp >= 150:
            hp2_text = hp2_text.render("HP: " + f"{wmag_hp}", True, green)
        if wmag_hp >= 50 and wmag_hp < 150:
            hp2_text = hp2_text.render("HP: " + f"{wmag_hp}", True, yellow)
        if wmag_hp >= 0 and wmag_hp < 50:
            hp2_text = hp2_text.render("HP: " + f"{wmag_hp}", True, red)
        if wmag_hp < 0:
            hp2_text = hp2_text.render("HP (seš mrtvej sračko): " + f"{wmag_hp}", True, red)
        hp2_text_rect = hp2_text.get_rect()
        hp2_text_rect.center = (wzard_rect.x + 60, wzard_rect.y + 130)
        keys = pygame.key.get_pressed()
        if keys [pygame.K_w] and wzard_rect.top > 0 and wzard2_rect.top > 0:
            wzard_rect.y = wzard_rect.y - distance
            wzard2_rect.y = wzard2_rect.y - distance
            name2_text_rect.y = name2_text_rect.y - distance  
            hp2_text_rect.y = hp2_text_rect.y - distance
        elif keys [pygame.K_s] and wzard_rect.bottom < height - 120 and wzard2_rect.bottom < height - 120:
            wzard_rect.y = wzard_rect.y + distance
            wzard2_rect.y = wzard2_rect.y + distance
            name2_text_rect.y = name2_text_rect.y + distance
            hp2_text_rect.y = hp2_text_rect.y + distance
        elif keys [pygame.K_a] and wzard_rect.left > 0 and wzard2_rect.left > 0:
            wzard_rect.x = wzard_rect.x - distance
            wzard2_rect.x = wzard2_rect.x - distance
            name2_text_rect.x = name2_text_rect.x - distance
            hp2_text_rect.x = hp2_text_rect.x - distance
            mirror = 1
        elif keys [pygame.K_d] and wzard_rect.right > 0 and wzard2_rect.right < width:
            wzard_rect.x = wzard_rect.x + distance
            wzard2_rect.x = wzard2_rect.x + distance
            name2_text_rect.x = name2_text_rect.x + distance
            hp2_text_rect.x = hp2_text_rect.x + distance
            mirror = 0       
              
        elif keys [pygame.K_SPACE] and mirror == 1:
            wzard_attack2_rect.center = (wzard2_rect.x + 10,wzard2_rect.y + 70)
            wire_attack = 1
        elif keys [pygame.K_SPACE] and mirror == 0:
            wzard_attack_rect.center = (wzard_rect.x + 125,wzard_rect.y + 70)
            wire_attack = 2
        
        if wire_attack == 1:
            screen.blit(wzard_attack2_image,wzard_attack2_rect)
            wzard_attack2_rect.x += attack_1x * attack_speed
        if wire_attack == 2:
            screen.blit(wzard_attack_image,wzard_attack_rect)
            wzard_attack_rect.x += attack_x * attack_speed         
        
        if mirror == 0:
            screen.blit(wzard_image,wzard_rect)
            screen.blit(name2_text,name2_text_rect)
            screen.blit(hp2_text,hp2_text_rect)
        if mirror == 1:
            screen.blit(wzard2_image,wzard2_rect)
            screen.blit(name2_text,name2_text_rect)
            screen.blit(hp2_text,hp2_text_rect)
        
    # Sceleton
    if enemy == 1:
        hp3_text = pygame.font.SysFont("Moncerat", 18)
        if scelet_hp > 0:      
            hp3_text = hp3_text.render("HP: " + f"{scelet_hp}", True, white)
            hp3_text_rect = hp3_text.get_rect()
            hp3_text_rect.center = (scelet_rect.x + 30, scelet_rect.y + 125)
            screen.blit(hp3_text,hp3_text_rect)
        if scelet_hp <= 0:
            scelet = 0
        e_name_text_rect.center = (scelet_rect.x + 30, scelet_rect.y + 110)
        screen.blit(scelet_image,scelet_rect)
        screen.blit(e_name_text,e_name_text_rect)
        scelet_rect.x += scelet_x * scelet_speed
        scelet_rect.y += scelet_y * scelet_speed
        if scelet_rect.left < 120 or scelet_rect.left > width - 120:
            scelet_x = -1 * scelet_x
        elif scelet_rect.top < 25 or scelet_rect.bottom > height - 120:
            scelet_y = -1 * scelet_y

        if scelet_rect.left < 130: 
            scelet_image = loadify(enemy0.img2)
                
            
        if scelet_rect.left >= 1000: 
            scelet_image = loadify(enemy0.img)
    
    
            
        

### KONTROLA KOLIZE ###


    if fball_rect.colliderect(scelet_rect) or fball2_rect.colliderect(scelet_rect):
        if scelet == 1:
            scelet_hp -= 1
            str_scelet_hp = str(scelet_hp)
            try:
                f3 = open("scelet_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_scelet_hp)
            f3.close()

    if wzard_attack_rect.colliderect(scelet_rect) or wzard_attack2_rect.colliderect(scelet_rect):
        if scelet == 1:
            scelet_hp -= 1
            str_scelet_hp = str(scelet_hp)
            try:
                f3 = open("scelet_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_scelet_hp)
            f3.close()

        if scelet_hp <= 0:
            scelet = 0
    
    if scelet_rect.colliderect(fzard_rect) or scelet_rect.colliderect(fzard2_rect):
        if player == 1:
            fmag_hp -= 1
            str_fmag_hp = str(fmag_hp)
            try:
                f1 = open("fmag_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f1.write(str_fmag_hp)
            f1.close()

    if scelet_rect.colliderect(wzard_rect) or scelet_rect.colliderect(wzard2_rect):
        if player == 2:
            wmag_hp -= 1
            str_wmag_hp = str(wmag_hp)
            try:
                f2 = open("wmag_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f2.write(str_wmag_hp)
            f2.close()

    


    pygame.display.update()
    clock.tick_busy_loop(fps)

# Ukončení hry
pygame.quit()

