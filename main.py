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

#-----------------------------------------------------------------------------------------------#   
### NASTAVENÍ ###
#-----------------------------------------------------------------------------------------------#

fps = 60
clock = pygame.time.Clock()
mirror = 0
fire_attack = 0
wire_attack = 0

attack_x = 1
attack_1x = -1* attack_x

scelet_speed = 3
scelet_boss_speed = 4
attack_speed = 8
distance = 9

# Random pohyb skeletonů
scelet_x = random.choice ([-1,1])
scelet_y = random.choice([-1,1])
scelet1_x = random.choice ([-1,1])
scelet1_y = random.choice([-1,1])
scelet2_x = random.choice ([-1,1])
scelet2_y = random.choice([-1,1])
scelet3_x = random.choice ([-1,1])
scelet3_y = random.choice([-1,1])
scelet_boss_x = random.choice ([-1,1])
scelet_boss_y = random.choice([-1,1])

#-----------------------------------------------------------------------------------------------#
### HRÁČ V POLI ###
#-----------------------------------------------------------------------------------------------#

# Firemag
player_fmag = int()
player_fmag_str=str(player_fmag)
try:
    f_fmag = open("players/player_fmag.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_fmag.read(player_fmag)
fmag_hp = (player1.hp)
if player_fmag > 0:
    str_fmag_hp = str(fmag_hp)
    try:
        f1 = open("players_hp/fmag_hp.txt", "r")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")
    text = f1.read(fmag_hp)
    f1.close()

# Watermag
player_wmag = int()
player_wmag_str=str(player_wmag)
try:
    f_player_wmag = open("players/player_wmag.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_player_wmag.read(player_wmag)
wmag_hp = (player2.hp)
if player_wmag > 0:
    str_wmag_hp = str(wmag_hp)
    try:
        f2 = open("players_hp/wmag_hp.txt", "r")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")
    text = f2.read(wmag_hp)
    f2.close()

#-----------------------------------------------------------------------------------------------#
### NEPŘÍTEL V POLI ###
#-----------------------------------------------------------------------------------------------#

# Skeleton 
enemy_scelet= int()
enemy_scelet_str=str(enemy_scelet)
try:
    f_enemy_scelet = open("players/enemy_scelet.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_scelet.read(enemy_scelet)
scelet_hp = (enemy0.hp)
str_scelet_hp = str(scelet_hp)
try:
    f3 = open("players_hp/scelet_hp.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(scelet_hp)
f3.close()

# Skeleton 1
enemy_scelet1= int()
enemy_scelet1_str=str(enemy_scelet1)
try:
    f_enemy_scelet1 = open("players/enemy_scelet1.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_scelet1.read(enemy_scelet1)
scelet1_hp = (enemy0.hp)
str_scelet1_hp = str(scelet1_hp)
try:
    f4 = open("players_hp/scelet1_hp.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f4.read(scelet1_hp)
f4.close()

# Skeleton 2
enemy_scelet2= int()
enemy_scelet2_str=str(enemy_scelet2)
try:
    f_enemy_scelet2 = open("players/enemy_scelet2.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_scelet2.read(enemy_scelet2)
scelet2_hp = (enemy0.hp)
str_scelet2_hp = str(scelet2_hp)
try:
    f5 = open("players_hp/scelet2_hp.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f5.read(scelet2_hp)
f5.close()

# Skeleton 3
enemy_scelet3= int()
enemy_scelet3_str=str(enemy_scelet3)
try:
    f_enemy_scelet3 = open("players/enemy_scelet3.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_scelet3.read(enemy_scelet3)
scelet3_hp = (enemy0.hp)
str_scelet3_hp = str(scelet3_hp)
try:
    f6 = open("players_hp/scelet3_hp.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f6.read(scelet3_hp)
f6.close()

# Skeleton BOSS
enemy_scelet_boss= int()
enemy_scelet_boss_str=str(enemy_scelet_boss)
try:
    f_enemy_scelet_boss = open("players/enemy_scelet_boss.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_scelet_boss.read(enemy_scelet_boss)
enemy_scelet_boss_hp = (enemy1.hp)
str_enemy_scelet_boss_hp = str(enemy_scelet_boss_hp)
try:
    f6 = open("players_hp/scelet_boss_hp.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f6.read(enemy_scelet_boss_hp)
f6.close()

#-----------------------------------------------------------------------------------------------#
### BACKGROUND, OBRÁZKY, TEXTY ###
#-----------------------------------------------------------------------------------------------#
# BG
background_img = loadify(background.img)
background_img_rect = background_img.get_rect()

#-----------------------------------------------------------------------------------------------#

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
if scelet_hp > 0 or scelet1_hp > 0 or scelet2_hp > 0 or scelet3_hp > 0:
    portal_image = loadify("img/portal.png")
    portal_image_rect = portal_image.get_rect()
    portal_image_rect.center = (width//2 + 500, height//2 - 250)

# Sceleton
if scelet_hp > 0:
    scelet_image = loadify(enemy0.img)
    scelet_rect = scelet_image.get_rect()
    scelet_rect.center = (width//2 + 500, height//2 - 250)

    e_name_text = pygame.font.SysFont("Moncerat", 20)
    e_name_text = e_name_text.render(enemy0.name, True, red)
    e_name_text_rect = e_name_text.get_rect()
    e_name_text_rect.center = (992,435)

# Sceleton 1
if scelet1_hp > 0:
    scelet1_image = loadify(enemy0.img)
    scelet1_rect = scelet1_image.get_rect()
    scelet1_rect.center = (width//2 - 100, height//2 - 250)

    e1_name_text = pygame.font.SysFont("Moncerat", 20)
    e1_name_text = e1_name_text.render(enemy0.name, True, red)
    e1_name_text_rect = e1_name_text.get_rect()
    e1_name_text_rect.center = (392,435)

# Sceleton 2
if scelet2_hp > 0:
    scelet2_image = loadify(enemy0.img)
    scelet2_rect = scelet2_image.get_rect()
    scelet2_rect.center = (width//2 + 100, height//2 - 250)

    e2_name_text = pygame.font.SysFont("Moncerat", 20)
    e2_name_text = e2_name_text.render(enemy0.name, True, red)
    e2_name_text_rect = e2_name_text.get_rect()
    e2_name_text_rect.center = (592,435)

# Sceleton 3
if scelet3_hp > 0:
    scelet3_image = loadify(enemy0.img)
    scelet3_rect = scelet3_image.get_rect()
    scelet3_rect.center = (width//2 - 300, height//2 - 250)

    e3_name_text = pygame.font.SysFont("Moncerat", 20)
    e3_name_text = e3_name_text.render(enemy0.name, True, red)
    e3_name_text_rect = e3_name_text.get_rect()
    e3_name_text_rect.center = (192,435)

# Sceleton BOSS
if enemy_scelet_boss_hp > 0:
    scelet_boss_image = loadify(enemy1.img)
    scelet_boss_rect = scelet_boss_image.get_rect()
    scelet_boss_rect.center = (width//2 + 500, height//2 - 250)

    eboss_name_text = pygame.font.SysFont("Moncerat", 20)
    eboss_name_text = eboss_name_text.render(enemy1.name, True, red)
    eboss_name_text_rect = eboss_name_text.get_rect()
    eboss_name_text_rect.center = (992,435)

#-----------------------------------------------------------------------------------------------#

# TEXTY 
custom_font = pygame.font.SysFont("Moncerat", 44)
custom_text = custom_font.render("press f to FIGHT!", True, yellow)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (width//2, height//2 - 350)

#-----------------------------------------------------------------------------------------------#
#### HLAVNÍ CYKLUS ####
#-----------------------------------------------------------------------------------------------#

lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

#-----------------------------------------------------------------------------------------------#
### BRÁZKY BLIT ###
#-----------------------------------------------------------------------------------------------#

# Bg
    screen.blit(background_img, background_img_rect)
# Portal
    if enemy_scelet > 0 and scelet_hp > 0 or scelet1_hp > 0 or scelet2_hp > 0 or scelet3_hp > 0:
        screen.blit(portal_image,portal_image_rect)
# Text bez enemy
    if enemy_scelet == 0:
        screen.blit(custom_text, custom_text_rect)

#-----------------------------------------------------------------------------------------------#
### POSTAVY ###
#-----------------------------------------------------------------------------------------------#

# Načtení Fmága do pole
    keys = pygame.key.get_pressed()
    if keys [pygame.K_1]:
        player_fmag += 1
        player_fmag_str = str(player_fmag)
        try:
            f_fmag = open("players/player_fmag.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_fmag.write(player_fmag_str)
        f_fmag.close()
        if player_wmag > 0:
            player_wmag -= 10
            player_wmag_str = str(player_wmag)
            try:
                f_wmag = open("players/player_wmag.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f_wmag.write(player_wmag_str)
            f_wmag.close()

# Načtení Wmága do pole
    if keys [pygame.K_2]:
        player_wmag += 1
        player_wmag_str = str(player_wmag)
        try:
            f_wmag = open("players/player_wmag.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_wmag.write(player_wmag_str)
        f_wmag.close()
        if player_fmag > 0:
            player_fmag -= 10
            player_fmag_str = str(player_fmag)
            try:
                f_fmag = open("players/player_fmag.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f_fmag.write(player_fmag_str)
            f_fmag.close()

# Načte příšery
    if keys [pygame.K_f]:
        enemy_scelet += 1
        enemy_scelet_str = str(enemy_scelet)
        try:
            f_enemy_scelet = open("players/enemy_scelet.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_enemy_scelet.write(enemy_scelet_str)
        f_enemy_scelet.close()

    if scelet_hp <= 0:         
        enemy_scelet += 1
        enemy_scelet_str = str(enemy_scelet)
        try:
            f_enemy_scelet = open("players/enemy_scelet.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_enemy_scelet.write(enemy_scelet_str)
        f_enemy_scelet.close()


        enemy_scelet1 += 1
        enemy_scelet1_str = str(enemy_scelet1)
        try:
            f_enemy_scelet1 = open("players/enemy_scelet1.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_enemy_scelet1.write(enemy_scelet1_str)
        f_enemy_scelet1.close()
    
        enemy_scelet2 += 1
        enemy_scelet2_str = str(enemy_scelet2)
        try:
            f_enemy_scelet2 = open("players/enemy_scelet2.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_enemy_scelet2.write(enemy_scelet2_str)
        f_enemy_scelet2.close()

        enemy_scelet3 += 1
        enemy_scelet3_str = str(enemy_scelet3)
        try:
            f_enemy_scelet3 = open("players/enemy_scelet3.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_enemy_scelet3.write(enemy_scelet3_str)
        f_enemy_scelet3.close()

    if scelet_hp <= 0 and scelet1_hp <= 0 and scelet2_hp <= 0 and scelet3_hp <= 0:
        enemy_scelet_boss += 1
        enemy_scelet_boss_str = str(enemy_scelet_boss)
        try:
            f_enemy_scelet_boss  = open("players/enemy_scelet_boss.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_enemy_scelet_boss.write(enemy_scelet_boss_str)
        f_enemy_scelet_boss.close()
         

    # Firemag
    if player_fmag > 0:
        hp1_text = pygame.font.SysFont("Moncerat", 18)
        if fmag_hp >= 150:
            hp1_text = hp1_text.render("HP: " + f"{fmag_hp}", True, green)
        if fmag_hp >= 100 and fmag_hp < 150:
            hp1_text = hp1_text.render("HP: " + f"{fmag_hp}", True, yellow)
        if fmag_hp >= 0 and fmag_hp < 100:
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
        if wmag_hp >= 75:
            hp2_text = hp2_text.render("HP: " + f"{wmag_hp}", True, green)
        if wmag_hp >= 40 and wmag_hp < 75:
            hp2_text = hp2_text.render("HP: " + f"{wmag_hp}", True, yellow)
        if wmag_hp >= 0 and wmag_hp < 40:
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
        
    # Skeleton
    if enemy_scelet > 0:
        hp3_text = pygame.font.SysFont("Moncerat", 18)
        if scelet_hp > 0:      
            hp3_text = hp3_text.render("HP: " + f"{scelet_hp}", True, white)
            hp3_text_rect = hp3_text.get_rect()
            hp3_text_rect.center = (scelet_rect.x + 30, scelet_rect.y + 125)
            screen.blit(hp3_text,hp3_text_rect)
        e_name_text_rect.center = (scelet_rect.x + 30, scelet_rect.y + 110)
        if scelet_hp > 0:
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

    # Skeleton 1
    if enemy_scelet1 > 0:
        hp3_text1 = pygame.font.SysFont("Moncerat", 18)
        if scelet1_hp > 0:      
            hp3_text1 = hp3_text1.render("HP: " + f"{scelet1_hp}", True, white)
            hp3_text1_rect = hp3_text1.get_rect()
            hp3_text1_rect.center = (scelet1_rect.x + 30, scelet1_rect.y + 125)
            screen.blit(hp3_text1,hp3_text1_rect)
        e1_name_text_rect.center = (scelet1_rect.x + 30, scelet1_rect.y + 110)
        if scelet1_hp > 0:
            screen.blit(scelet1_image,scelet1_rect)
            screen.blit(e1_name_text,e1_name_text_rect)
        scelet1_rect.x += scelet1_x * scelet_speed
        scelet1_rect.y += scelet1_y * scelet_speed
        if scelet1_rect.left < 120 or scelet1_rect.left > width - 120:
            scelet1_x = -1 * scelet1_x
        elif scelet1_rect.top < 25 or scelet1_rect.bottom > height - 120:
            scelet1_y = -1 * scelet1_y

        if scelet1_rect.left < 130: 
            scelet1_image = loadify(enemy0.img2)
                          
        if scelet1_rect.left >= 1000: 
            scelet1_image = loadify(enemy0.img)

    # Skeleton 2
    if enemy_scelet2 > 0:
        hp3_text2 = pygame.font.SysFont("Moncerat", 18)
        if scelet2_hp > 0:      
            hp3_text2 = hp3_text2.render("HP: " + f"{scelet2_hp}", True, white)
            hp3_text2_rect = hp3_text2.get_rect()
            hp3_text2_rect.center = (scelet2_rect.x + 30, scelet2_rect.y + 125)
            screen.blit(hp3_text2,hp3_text2_rect)
        e2_name_text_rect.center = (scelet2_rect.x + 30, scelet2_rect.y + 110)
        if scelet2_hp > 0:
            screen.blit(scelet2_image,scelet2_rect)
            screen.blit(e2_name_text,e2_name_text_rect)
        scelet2_rect.x += scelet2_x * scelet_speed
        scelet2_rect.y += scelet2_y * scelet_speed
        if scelet2_rect.left < 120 or scelet2_rect.left > width - 120:
            scelet2_x = -1 * scelet2_x
        elif scelet2_rect.top < 25 or scelet2_rect.bottom > height - 120:
            scelet2_y = -1 * scelet2_y

        if scelet2_rect.left < 130: 
            scelet2_image = loadify(enemy0.img2)
                           
        if scelet2_rect.left >= 1000: 
            scelet2_image = loadify(enemy0.img)

    # Skeleton 3
    if enemy_scelet3 > 0:
        hp3_text3 = pygame.font.SysFont("Moncerat", 18)
        if scelet3_hp > 0:      
            hp3_text3 = hp3_text3.render("HP: " + f"{scelet3_hp}", True, white)
            hp3_text3_rect = hp3_text3.get_rect()
            hp3_text3_rect.center = (scelet3_rect.x + 30, scelet3_rect.y + 125)
            screen.blit(hp3_text3,hp3_text3_rect)
        e3_name_text_rect.center = (scelet3_rect.x + 30, scelet3_rect.y + 110)
        if scelet3_hp > 0:
            screen.blit(scelet3_image,scelet3_rect)
            screen.blit(e3_name_text,e3_name_text_rect)
        scelet3_rect.x += scelet3_x * scelet_speed
        scelet3_rect.y += scelet3_y * scelet_speed
        if scelet3_rect.left < 120 or scelet3_rect.left > width - 120:
            scelet3_x = -1 * scelet3_x
        elif scelet3_rect.top < 25 or scelet3_rect.bottom > height - 120:
            scelet3_y = -1 * scelet3_y

        if scelet3_rect.left < 130: 
            scelet3_image = loadify(enemy0.img2)
                
        if scelet3_rect.left >= 1000: 
            scelet3_image = loadify(enemy0.img)

    # Skeleton BOSS
    if enemy_scelet_boss > 0:
        hpboss_text = pygame.font.SysFont("Moncerat", 18)
        if enemy_scelet_boss_hp > 0:      
            hpboss_text = hpboss_text.render("HP: " + f"{enemy_scelet_boss_hp}", True, white)
            hpboss_text_rect = hpboss_text.get_rect()
            hpboss_text_rect.center = (scelet_boss_rect.x + 35, scelet_boss_rect.y + 185)
            screen.blit(hpboss_text,hpboss_text_rect)
        eboss_name_text_rect.center = (scelet_boss_rect.x + 35, scelet_boss_rect.y + 170)
        if enemy_scelet_boss_hp > 0:
            screen.blit(scelet_boss_image,scelet_boss_rect)
            screen.blit(eboss_name_text,eboss_name_text_rect)
        scelet_boss_rect.x += scelet_boss_x * scelet_boss_speed
        scelet_boss_rect.y += scelet_boss_y * scelet_boss_speed
        if scelet_boss_rect.left < 120 or scelet_boss_rect.left > width - 120:
            scelet_boss_x = -1 * scelet_boss_x
        elif scelet_boss_rect.top < 25 or scelet_boss_rect.bottom > height - 120:
            scelet_boss_y = -1 * scelet_boss_y

        if scelet_boss_rect.left < 130: 
            scelet_boss_image = loadify(enemy1.img2)
            
            
        if scelet_rect.left >= 1000: 
            scelet_boss_image = loadify(enemy1.img)
    
#-----------------------------------------------------------------------------------------------#    
### KONTROLA KOLIZE ###
#-----------------------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------------------#
# Enemy a Player
#-----------------------------------------------------------------------------------------------#

# scelet --> firemag
    if scelet_rect.colliderect(fzard_rect) or scelet_rect.colliderect(fzard2_rect):
        if player_fmag > 0 and scelet_hp > 0:
            fmag_hp -= 1
            str_fmag_hp = str(fmag_hp)
            try:
                f1 = open("players_hp/fmag_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f1.write(str_fmag_hp)
            f1.close()

 # scelet1 --> firemag
    if scelet1_rect.colliderect(fzard_rect) or scelet1_rect.colliderect(fzard2_rect):
        if player_fmag > 0 and scelet1_hp > 0:
            fmag_hp -= 1
            str_fmag_hp = str(fmag_hp)
            try:
                f1 = open("players_hp/fmag_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f1.write(str_fmag_hp)
            f1.close()

# scelet2 --> firemag
    if scelet2_rect.colliderect(fzard_rect) or scelet2_rect.colliderect(fzard2_rect):
        if player_fmag > 0 and scelet2_hp > 0:
            fmag_hp -= 1
            str_fmag_hp = str(fmag_hp)
            try:
                f1 = open("players_hp/fmag_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f1.write(str_fmag_hp)
            f1.close()

# scelet3 --> firemag
    if scelet3_rect.colliderect(fzard_rect) or scelet3_rect.colliderect(fzard2_rect):
        if player_fmag > 0 and scelet3_hp > 0:
            fmag_hp -= 1
            str_fmag_hp = str(fmag_hp)
            try:
                f1 = open("players_hp/fmag_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f1.write(str_fmag_hp)
            f1.close()

# sceletboss --> firemag
    if scelet_boss_rect.colliderect(fzard_rect) or scelet_boss_rect.colliderect(fzard2_rect):
        if player_fmag > 0 and enemy_scelet_boss_hp > 0:
            fmag_hp -= 2
            str_fmag_hp = str(fmag_hp)
            try:
                f1 = open("players_hp/fmag_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f1.write(str_fmag_hp)
            f1.close()

# scelet --> watermag
    if scelet_rect.colliderect(wzard_rect) or scelet_rect.colliderect(wzard2_rect):
        if player_wmag > 0 and scelet_hp > 0:
            wmag_hp -= 1
            str_wmag_hp = str(wmag_hp)
            try:
                f2 = open("players_hp/wmag_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f2.write(str_wmag_hp)
            f2.close()

# scelet1 --> watermag
    if scelet1_rect.colliderect(wzard_rect) or scelet1_rect.colliderect(wzard2_rect):
        if player_wmag > 0 and scelet1_hp > 0:
            wmag_hp -= 1
            str_wmag_hp = str(wmag_hp)
            try:
                f2 = open("players_hp/wmag_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f2.write(str_wmag_hp)
            f2.close()

# scelet2 --> watermag
    if scelet2_rect.colliderect(wzard_rect) or scelet2_rect.colliderect(wzard2_rect):
        if player_wmag > 0 and scelet2_hp > 0:
            wmag_hp -= 1
            str_wmag_hp = str(wmag_hp)
            try:
                f2 = open("players_hp/wmag_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f2.write(str_wmag_hp)
            f2.close()

# scelet3 --> watermag
    if scelet3_rect.colliderect(wzard_rect) or scelet3_rect.colliderect(wzard2_rect):
        if player_wmag > 0 and scelet3_hp > 0:
            wmag_hp -= 1
            str_wmag_hp = str(wmag_hp)
            try:
                f2 = open("players_hp/wmag_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f2.write(str_wmag_hp)
            f2.close()

# sceletboss --> watermag
    if scelet_boss_rect.colliderect(wzard_rect) or scelet_boss_rect.colliderect(wzard2_rect):
        if player_wmag > 0 and enemy_scelet_boss_hp > 0:
            wmag_hp -= 2
            str_wmag_hp = str(wmag_hp)
            try:
                f2 = open("players_hp/wmag_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f2.write(str_wmag_hp)
            f2.close()

#-----------------------------------------------------------------------------------------------#
# Attack a Enemy
#-----------------------------------------------------------------------------------------------#

# fireball --> scelet
    if fball_rect.colliderect(scelet_rect) or fball2_rect.colliderect(scelet_rect):
        if enemy_scelet > 0:
            scelet_hp -= 1
            str_scelet_hp = str(scelet_hp)
            try:
                f3 = open("players_hp/scelet_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_scelet_hp)
            f3.close()

# fireball --> scelet1
    if fball_rect.colliderect(scelet1_rect) or fball2_rect.colliderect(scelet1_rect):
        if enemy_scelet1 > 0:
            scelet1_hp -= 1
            str_scelet1_hp = str(scelet1_hp)
            try:
                f3 = open("players_hp/scelet1_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_scelet1_hp)
            f3.close()

# fireball --> scelet2
    if fball_rect.colliderect(scelet2_rect) or fball2_rect.colliderect(scelet2_rect):
        if enemy_scelet2 > 0:
            scelet2_hp -= 1
            str_scelet2_hp = str(scelet2_hp)
            try:
                f3 = open("players_hp/scelet2_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_scelet2_hp)
            f3.close()

# fireball --> scelet3
    if fball_rect.colliderect(scelet3_rect) or fball2_rect.colliderect(scelet3_rect):
        if enemy_scelet3 > 0:
            scelet3_hp -= 1
            str_scelet3_hp = str(scelet3_hp)
            try:
                f3 = open("players_hp/scelet3_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_scelet3_hp)
            f3.close()

# fireball --> sceletboss
    if fball_rect.colliderect(scelet_boss_rect) or fball2_rect.colliderect(scelet_boss_rect):
        if enemy_scelet_boss > 0:
            enemy_scelet_boss_hp -= 1
            str_enemy_scelet_boss_hp = str(enemy_scelet_boss_hp)
            try:
                f3 = open("players_hp/scelet_boss_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_enemy_scelet_boss_hp)
            f3.close()
#-----------------------------------------------------------------------------------------------#
# waterball --> scelet
    if wzard_attack_rect.colliderect(scelet_rect) or wzard_attack2_rect.colliderect(scelet_rect):
        if enemy_scelet > 0:
            scelet_hp -= 1
            str_scelet_hp = str(scelet_hp)
            try:
                f3 = open("players_hp/scelet_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_scelet_hp)
            f3.close()

# waterball --> scelet1
    if wzard_attack_rect.colliderect(scelet1_rect) or wzard_attack2_rect.colliderect(scelet1_rect):
        if enemy_scelet1 > 0:
            scelet1_hp -= 1
            str_scelet1_hp = str(scelet1_hp)
            try:
                f3 = open("players_hp/scelet1_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_scelet1_hp)
            f3.close()

# waterball --> scelet2
    if wzard_attack_rect.colliderect(scelet2_rect) or wzard_attack2_rect.colliderect(scelet2_rect):
        if enemy_scelet2 > 0:
            scelet2_hp -= 1
            str_scelet2_hp = str(scelet2_hp)
            try:
                f3 = open("players_hp/scelet2_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_scelet2_hp)
            f3.close()

# waterball --> scelet3
    if wzard_attack_rect.colliderect(scelet3_rect) or wzard_attack2_rect.colliderect(scelet3_rect):
        if enemy_scelet3 > 0:
            scelet3_hp -= 1
            str_scelet3_hp = str(scelet3_hp)
            try:
                f3 = open("players_hp/scelet3_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_scelet3_hp)
            f3.close()
        
# waterball --> sceletboss
    if wzard_attack_rect.colliderect(scelet_boss_rect) or wzard_attack2_rect.colliderect(scelet_boss_rect):
        if enemy_scelet_boss > 0:
            enemy_scelet_boss_hp -= 1
            str_enemy_scelet_boss_hp = str(enemy_scelet_boss_hp)
            try:
                f3 = open("players_hp/scelet_boss_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_enemy_scelet_boss_hp)
            f3.close()

    pygame.display.update()
    clock.tick_busy_loop(fps)

# Ukončení hry
pygame.quit()

