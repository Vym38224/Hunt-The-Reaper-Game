import pygame
import random
import buttons
from players import *

# Načtení IMG 
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
human_attack = 0

run_game = 0

attack_x = 1
attack_1x = -1* attack_x

scelet_speed = 3
scelet_boss_speed = 3

attack_speed = 7
fmag_distance = 5
wmag_distance = 8
human_distance = 5

# Nastavení scelet_hp = 0 na začátku hry
scelet_hp = 0
str_scelet_hp = str(scelet_hp)
try:
    f_scelet_hp = open("players_hp/scelet_hp.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_scelet_hp.write(str_scelet_hp)
scelet_hp1 = 0
str_scelet_hp1 = str(scelet_hp1)
try:
    f_scelet_hp1 = open("players_hp/scelet_hp1.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_scelet_hp1.write(str_scelet_hp1)
scelet_hp2 = 0
str_scelet_hp2 = str(scelet_hp2)
try:
    f_scelet_hp2 = open("players_hp/scelet_hp2.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_scelet_hp2.write(str_scelet_hp2)
scelet_hp3 = 0
str_scelet_hp3 = str(scelet_hp3)
try:
    f_scelet_hp3 = open("players_hp/scelet_hp3.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_scelet_hp3.write(str_scelet_hp3)
scelet_hp4 = 0
str_scelet_hp4 = str(scelet_hp4)
try:
    f_scelet_hp4 = open("players_hp/scelet_hp4.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_scelet_hp4.write(str_scelet_hp4)
scelet_hp5 = 0
str_scelet_hp5 = str(scelet_hp5)
try:
    f_scelet_hp5 = open("players_hp/scelet_hp5.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_scelet_hp5.write(str_scelet_hp5)
scelet_hp6 = 0
str_scelet_hp6 = str(scelet_hp6)
try:
    f_scelet_hp6 = open("players_hp/scelet_hp6.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_scelet_hp6.write(str_scelet_hp6)
scelet_hp7 = 0
str_scelet_hp7 = str(scelet_hp7)
try:
    f_scelet_hp7 = open("players_hp/scelet_hp7.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_scelet_hp7.write(str_scelet_hp7)

# Nastavení enemy_scelet = 0 na začátku hry
enemy_scelet = 0
str_enemy_scelet = str(enemy_scelet)
try:
    f_enemy_scelet = open("players/enemy_scelet.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_scelet.write(str_enemy_scelet)
enemy_scelet1 = 0
str_enemy_scelet1 = str(enemy_scelet1)
try:
    f_enemy_scelet1 = open("players/enemy_scelet1.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_scelet1.write(str_enemy_scelet1)
enemy_scelet2 = 0
str_enemy_scelet2 = str(enemy_scelet2)
try:
    f_enemy_scelet2 = open("players/enemy_scelet2.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_scelet2.write(str_enemy_scelet2)
enemy_scelet3 = 0
str_enemy_scelet3 = str(enemy_scelet3)
try:
    f_enemy_scelet3 = open("players/enemy_scelet3.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_scelet3.write(str_enemy_scelet3)
enemy_scelet4 = 0
str_enemy_scelet4 = str(enemy_scelet4)
try:
    f_enemy_scelet4 = open("players/enemy_scelet4.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_scelet4.write(str_enemy_scelet4)
enemy_scelet5 = 0
str_enemy_scelet5 = str(enemy_scelet5)
try:
    f_enemy_scelet5 = open("players/enemy_scelet5.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_scelet5.write(str_enemy_scelet5)
enemy_scelet6 = 0
str_enemy_scelet6 = str(enemy_scelet6)
try:
    f_enemy_scelet6 = open("players/enemy_scelet6.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_scelet6.write(str_enemy_scelet6)
enemy_scelet7 = 0
str_enemy_scelet7 = str(enemy_scelet7)
try:
    f_enemy_scelet7 = open("players/enemy_scelet7.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_scelet7.write(str_enemy_scelet7)


# Random pohyb skeletonů
scelet_x = random.choice ([-1,1])
scelet_y = random.choice([-1,1])
scelet1_x = random.choice ([-1,1])
scelet1_y = random.choice([-1,1])
scelet2_x = random.choice ([-1,1])
scelet2_y = random.choice([-1,1])
scelet3_x = random.choice ([-1,1])
scelet3_y = random.choice([-1,1])
scelet4_x = random.choice ([-1,1])
scelet4_y = random.choice([-1,1])
scelet5_x = random.choice ([-1,1])
scelet5_y = random.choice([-1,1])
scelet6_x = random.choice ([-1,1])
scelet6_y = random.choice([-1,1])
scelet7_x = random.choice ([-1,1])
scelet7_y = random.choice([-1,1])
scelet_boss_x = random.choice ([-1,1])
scelet_boss_y = random.choice([-1,1])

#-----------------------------------------------------------------------------------------------#
### HRÁČ V POLI ###
#-----------------------------------------------------------------------------------------------#

# Human
player_human = int()
player_human_str=str(player_human)
try:
    f_player_human = open("players/player_human.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_player_human.read(player_human)
human_hp = (player0.hp)
if player_human > 0:
    str_human_hp = str(human_hp)
    try:
        f2 = open("players_hp/human_hp.txt", "r")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")
    text = f2.read(human_hp)
   

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
    f4 = open("players_hp/scelet_hp1.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f4.read(scelet1_hp)

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
    f5 = open("players_hp/scelet_hp2.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f5.read(scelet2_hp)

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
    f6 = open("players_hp/scelet_hp3.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f6.read(scelet3_hp)

# Skeleton 4
enemy_scelet4= int()
enemy_scelet4_str=str(enemy_scelet4)
try:
    f_enemy_scelet4 = open("players/enemy_scelet4.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_scelet4.read(enemy_scelet4)
scelet4_hp = (enemy0.hp)
str_scelet4_hp = str(scelet4_hp)
try:
    f3 = open("players_hp/scelet_hp4.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(scelet4_hp)

# Skeleton 5
enemy_scelet5= int()
enemy_scelet5_str=str(enemy_scelet5)
try:
    f_enemy_scelet5 = open("players/enemy_scelet5.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_scelet5.read(enemy_scelet5)
scelet5_hp = (enemy0.hp)
str_scelet5_hp = str(scelet5_hp)
try:
    f3 = open("players_hp/scelet_hp5.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(scelet5_hp)

# Skeleton 6
enemy_scelet6= int()
enemy_scelet6_str=str(enemy_scelet6)
try:
    f_enemy_scelet6 = open("players/enemy_scelet6.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_scelet6.read(enemy_scelet6)
scelet6_hp = (enemy0.hp)
str_scelet6_hp = str(scelet6_hp)
try:
    f3 = open("players_hp/scelet_hp6.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(scelet6_hp)

# Skeleton 7
enemy_scelet7= int()
enemy_scelet7_str=str(enemy_scelet7)
try:
    f_enemy_scelet7 = open("players/enemy_scelet7.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_scelet7.read(enemy_scelet7)
scelet7_hp = (enemy0.hp)
str_scelet7_hp = str(scelet7_hp)
try:
    f3 = open("players_hp/scelet_hp7.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(scelet7_hp)

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
    f3 = open("players_hp/scelet_boss_hp.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(enemy_scelet_boss_hp)

#-----------------------------------------------------------------------------------------------#
### BACKGROUND, OBRÁZKY, TEXTY ###
#-----------------------------------------------------------------------------------------------#
# BACKGROUND
background_img = loadify(background.img)
background_img_rect = background_img.get_rect()

#-----------------------------------------------------------------------------------------------#

# OBRÁZKY

# Buttons
start_img = pygame.image.load("img/start_btn.png").convert_alpha()
start_button = buttons.Button(940,0,start_img,0.8)
exit_img = pygame.image.load("img/exit_btn.png").convert_alpha()
exit_button = buttons.Button(1070,0,exit_img,0.8)

# Human
human_portret = loadify("img/human_portret.png")
human_portret_rect = human_portret.get_rect()
human_portret_rect.center = (35, 35)

human_image = loadify(player0.img)
human_rect = human_image.get_rect()
human_rect.center = (width//2, height//2)

human2_image = loadify(player0.img2)
human2_rect = human2_image.get_rect()
human2_rect.center = (width//2, height//2)

human_attack_image = loadify(player0.img_attack)
human_attack_rect = human_attack_image.get_rect()
human_attack_rect.center = (0,0)

human_attack2_image = loadify(player0.img_attack2)
human_attack2_rect = human_attack2_image.get_rect()
human_attack2_rect.center = (0,0)

human_move_image = loadify("img/human_move.png")
human_move_image_rect = human_move_image.get_rect()

human_move_image2 = loadify("img/human_move2.png")
human_move_image2_rect = human_move_image2.get_rect()

name0_text = pygame.font.SysFont("Moncerat", 20)
name0_text = name0_text.render(player0.name, True, white)
name0_text_rect = name0_text.get_rect()
name0_text_rect.center = (600,425)

# Firemag
fzard_portret = loadify("img/fmag_portret.png")
fzard_portret_rect = fzard_portret.get_rect()
fzard_portret_rect.center = (105, 35)

fzard_portret_lock = loadify("img/fmag_portret_lock.png")
fzard_portret_lock_rect = fzard_portret_lock.get_rect()
fzard_portret_lock_rect.center = (105, 35)

fzard_image = loadify(player1.img)
fzard_rect = fzard_image.get_rect()
fzard_rect.center = (width//2, height//2)

fzard2_image = loadify(player1.img2)
fzard2_rect = fzard2_image.get_rect()
fzard2_rect.center = (width//2, height//2)

fzard_move_image = loadify("img/firemag_move.png")
fzard_move_image_rect = fzard_move_image.get_rect()

fzard_move_image2 = loadify("img/firemag_move2.png")
fzard_move_image2_rect = fzard_move_image2.get_rect()

fball_image = loadify(player1.img_attack)
fball_rect = fball_image.get_rect()

fball2_image = loadify(player1.img_attack2)
fball2_rect = fball2_image.get_rect()

name1_text = pygame.font.SysFont("Moncerat", 20)
name1_text = name1_text.render(player1.name, True, white)
name1_text_rect = name1_text.get_rect()
name1_text_rect.center = (600,440)

# Watermag
wzard_portret = loadify("img/wzard_portret.png")
wzard_portret_rect = wzard_portret.get_rect()
wzard_portret_rect.center = (175, 35)

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

wzard_move_image = loadify("img/watermag_move.png")
wzard_move_image_rect = wzard_move_image.get_rect()

wzard_move_image2 = loadify("img/watermag_move2.png")
wzard_move_image2_rect = wzard_move_image2.get_rect()

name2_text = pygame.font.SysFont("Moncerat", 20)
name2_text = name2_text.render(player2.name, True, white)
name2_text_rect = name2_text.get_rect()
name2_text_rect.center = (600,435)

# Portal
portal_image = loadify("img/portal.png")
portal_image_rect = portal_image.get_rect()
portal_image_rect.center = (width//2 + 500, height//2 - 200)

# Sceleton
if scelet_hp > 0:
    scelet_image = loadify(enemy0.img)
    scelet_rect = scelet_image.get_rect()
    scelet_rect.center = (width//2 + 500, height//2 - 200)

    e_name_text = pygame.font.SysFont("Moncerat", 20)
    e_name_text = e_name_text.render(enemy0.name, True, red)
    e_name_text_rect = e_name_text.get_rect()
    e_name_text_rect.center = (992,435)

# Sceleton 1
if scelet1_hp > 0 :
    scelet1_image = loadify(enemy0.img)
    scelet1_rect = scelet1_image.get_rect()
    scelet1_rect.center = (width//2 - 100, height//2 - 200)

    e1_name_text = pygame.font.SysFont("Moncerat", 20)
    e1_name_text = e1_name_text.render(enemy0.name, True, red)
    e1_name_text_rect = e1_name_text.get_rect()
    e1_name_text_rect.center = (992,435)

# Sceleton 2
if scelet2_hp > 0 :
    scelet2_image = loadify(enemy0.img)
    scelet2_rect = scelet2_image.get_rect()
    scelet2_rect.center = (width//2 + 100, height//2 - 200)

    e2_name_text = pygame.font.SysFont("Moncerat", 20)
    e2_name_text = e2_name_text.render(enemy0.name, True, red)
    e2_name_text_rect = e2_name_text.get_rect()
    e2_name_text_rect.center = (992,435)

# Sceleton 3
if scelet3_hp > 0 :
    scelet3_image = loadify(enemy0.img)
    scelet3_rect = scelet3_image.get_rect()
    scelet3_rect.center = (width//2 - 300, height//2 - 200)

    e3_name_text = pygame.font.SysFont("Moncerat", 20)
    e3_name_text = e3_name_text.render(enemy0.name, True, red)
    e3_name_text_rect = e3_name_text.get_rect()
    e3_name_text_rect.center = (992,435)

# Sceleton 4
if scelet4_hp > 0 :
    scelet4_image = loadify(enemy0.img)
    scelet4_rect = scelet4_image.get_rect()
    scelet4_rect.center = (width//2 + 300, height//2 - 200)

    e4_name_text = pygame.font.SysFont("Moncerat", 20)
    e4_name_text = e4_name_text.render(enemy0.name, True, red)
    e4_name_text_rect = e4_name_text.get_rect()
    e4_name_text_rect.center = (992,435)

# Sceleton 5
if scelet5_hp > 0 :
    scelet5_image = loadify(enemy0.img)
    scelet5_rect = scelet5_image.get_rect()
    scelet5_rect.center = (width//2 - 100, height//2 - 200)

    e5_name_text = pygame.font.SysFont("Moncerat", 20)
    e5_name_text = e5_name_text.render(enemy0.name, True, red)
    e5_name_text_rect = e5_name_text.get_rect()
    e5_name_text_rect.center = (992,435)

# Sceleton 6
if scelet6_hp > 0 :
    scelet6_image = loadify(enemy0.img)
    scelet6_rect = scelet6_image.get_rect()
    scelet6_rect.center = (width//2, height//2 - 200)

    e6_name_text = pygame.font.SysFont("Moncerat", 20)
    e6_name_text = e6_name_text.render(enemy0.name, True, red)
    e6_name_text_rect = e6_name_text.get_rect()
    e6_name_text_rect.center = (992,435)

# Sceleton 7
if scelet7_hp > 0 :
    scelet7_image = loadify(enemy0.img)
    scelet7_rect = scelet7_image.get_rect()
    scelet7_rect.center = (width//2 + 250, height//2 - 200)

    e7_name_text = pygame.font.SysFont("Moncerat", 20)
    e7_name_text = e7_name_text.render(enemy0.name, True, red)
    e7_name_text_rect = e7_name_text.get_rect()
    e7_name_text_rect.center = (992,435)

# Sceleton BOSS
if enemy_scelet_boss_hp > 0:
    scelet_boss_image = loadify(enemy1.img)
    scelet_boss_rect = scelet_boss_image.get_rect()
    scelet_boss_rect.center = (width//2 + 500, height//2 - 200)

    eboss_name_text = pygame.font.SysFont("Moncerat", 20)
    eboss_name_text = eboss_name_text.render(enemy1.name, True, red)
    eboss_name_text_rect = eboss_name_text.get_rect()
    eboss_name_text_rect.center = (900,435)

#-----------------------------------------------------------------------------------------------#
# TEXTY 
custom1_font = pygame.font.SysFont("Helvetica", 64)
custom1_text = custom1_font.render("WELCOME TO THE GAME", True, yellow)
custom1_text_rect = custom1_text.get_rect()
custom1_text_rect.center = (width//2, height//2 + 300)

#-----------------------------------------------------------------------------------------------#
#### HLAVNÍ CYKLUS ####
#-----------------------------------------------------------------------------------------------#

lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

#-----------------------------------------------------------------------------------------------#
### OBRÁZKY BLIT ###
#-----------------------------------------------------------------------------------------------#

# Bg
    screen.blit(background_img, background_img_rect)

# Portréty
    if enemy_scelet_boss_hp <= 0:
        screen.blit(fzard_portret, fzard_portret_rect)
    if enemy_scelet_boss_hp > 0: 
            screen.blit(fzard_portret_lock, fzard_portret_lock_rect)
    if scelet_hp7 < 0 and scelet_hp6 < 0 and scelet_hp5 < 0 and scelet4_hp < 0:
        screen.blit(wzard_portret, wzard_portret_rect)
    screen.blit(human_portret, human_portret_rect)

# Portal
    if enemy_scelet > 0 or enemy_scelet1 > 0 or enemy_scelet2 > 0 or enemy_scelet3 > 0 or enemy_scelet4 > 0 or enemy_scelet5 > 0 or enemy_scelet6 > 0 or enemy_scelet7 > 0:
        if scelet_hp > 0 or scelet1_hp > 0 or scelet2_hp > 0 or scelet3_hp > 0 or scelet4_hp > 0 or scelet5_hp > 0 or scelet6_hp > 0 or scelet7_hp > 0:
            screen.blit(portal_image,portal_image_rect)
# Text bez enemy
    if enemy_scelet == 0:     
        screen.blit(custom1_text, custom1_text_rect)
# Buttons
    if start_button.draw(screen):
        run_game = 1
    if exit_button.draw(screen):
        lets_continue = False
    
# HP bosse
    custom2_font = pygame.font.SysFont("Helvetica", 44)
    custom3_font = pygame.font.SysFont("Helvetica", 44)
    custom4_font = pygame.font.SysFont("Helvetica", 44)
    if enemy_scelet_boss > 0 and enemy_scelet_boss_hp >= 100:
        custom2_text = custom2_font.render("BOSS HP: " + f"{enemy_scelet_boss_hp}", True, green)
        custom2_text_rect = custom2_text.get_rect()
        custom2_text_rect.center = (width//2, height//2 + 350)
        screen.blit(custom2_text, custom2_text_rect)
    if enemy_scelet_boss > 0 and enemy_scelet_boss_hp <= 99 and enemy_scelet_boss_hp >= 50:
        custom3_text = custom3_font.render("BOSS HP: " + f"{enemy_scelet_boss_hp}", True, yellow)
        custom3_text_rect = custom3_text.get_rect()
        custom3_text_rect.center = (width//2, height//2 + 350)
        screen.blit(custom3_text, custom3_text_rect)
    if enemy_scelet_boss > 0 and enemy_scelet_boss_hp <= 49 and enemy_scelet_boss_hp > 0:
        custom4_text = custom4_font.render("BOSS HP: " + f"{enemy_scelet_boss_hp}", True, red)
        custom4_text_rect = custom4_text.get_rect()
        custom4_text_rect.center = (width//2, height//2 + 350)
        screen.blit(custom4_text, custom4_text_rect)


#-----------------------------------------------------------------------------------------------#
### POSTAVY ###
#-----------------------------------------------------------------------------------------------#
    keys = pygame.key.get_pressed()
# Načtení Humana do pole
    if keys [pygame.K_1]:
        player_human += 1
        player_human_str = str(player_human)
        try:
            f_human = open("players/player_human.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_human.write(player_human_str)
        f_human.close()
        if player_fmag > 0:
            player_fmag -= 10
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

# Načtení Fmága do pole
    if keys [pygame.K_2]:
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
        
        if player_human > 0:
            player_human -= 10
            player_human_str = str(player_human)
            try:
                f_human = open("players/player_human.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f_human.write(player_human_str)
            f_human.close()

# Načtení Wmága do pole
    if keys [pygame.K_3]:
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
        
        if player_human > 0:
            player_human -= 10
            player_human_str = str(player_human)
            try:
                f_human = open("players/player_human.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f_human.write(player_human_str)
            f_human.close()

# Načte příšery
    if run_game == 1:

# Skeleton 
        enemy_scelet += 1
        enemy_scelet_str = str(enemy_scelet)
        try:
            f_enemy_scelet = open("players/enemy_scelet.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_enemy_scelet.write(enemy_scelet_str)
        f_enemy_scelet.close()

# Skeleton 1 + 2 + 3
    if scelet_hp <= 0:         
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

# Skeleton 4 + 5 + 6 + 7
    if scelet_hp <= 0 and scelet1_hp <= 0 and scelet2_hp <= 0 and scelet3_hp <= 0:
        enemy_scelet4 += 1
        enemy_scelet4_str = str(enemy_scelet4)
        try:
            f_enemy_scelet4 = open("players/enemy_scelet4.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_enemy_scelet4.write(enemy_scelet4_str)
        f_enemy_scelet4.close()
    
        enemy_scelet5 += 1
        enemy_scelet5_str = str(enemy_scelet5)
        try:
            f_enemy_scelet5 = open("players/enemy_scelet5.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_enemy_scelet5.write(enemy_scelet5_str)
        f_enemy_scelet5.close()

        enemy_scelet6 += 1
        enemy_scelet6_str = str(enemy_scelet6)
        try:
            f_enemy_scelet6 = open("players/enemy_scelet6.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_enemy_scelet6.write(enemy_scelet6_str)
        f_enemy_scelet6.close()

        enemy_scelet7 += 1
        enemy_scelet7_str = str(enemy_scelet7)
        try:
            f_enemy_scelet7 = open("players/enemy_scelet7.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_enemy_scelet7.write(enemy_scelet7_str)
        f_enemy_scelet7.close()
        

    # Skeleton BOSS
    if scelet_hp <= 0 and scelet1_hp <= 0 and scelet2_hp <= 0 and scelet3_hp <= 0 and scelet4_hp <= 0 and scelet5_hp <= 0 and scelet6_hp <= 0 and scelet7_hp <= 0:
        enemy_scelet_boss += 1
        enemy_scelet_boss_str = str(enemy_scelet_boss)
        try:
            f_enemy_scelet_boss  = open("players/enemy_scelet_boss.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_enemy_scelet_boss.write(enemy_scelet_boss_str)
        f_enemy_scelet_boss.close()
    if enemy_scelet_boss_hp <= 0:
        pass

     # Human
    if player_human > 0:
        if human_hp > 0:
            hp0_text = pygame.font.SysFont("Moncerat", 18)
        if human_hp >= 600:
            hp0_text = hp0_text.render("HP: " + f"{human_hp}", True, green)
        if human_hp >= 350 and human_hp <= 599:
            hp0_text = hp0_text.render("HP: " + f"{human_hp}", True, yellow)
        if human_hp <= 349 and human_hp > 0:
            hp0_text = hp0_text.render("HP: " + f"{human_hp}", True, red)
        if human_hp < 0:
            player_human -= 100000000
            player_human_str = str(player_human)
            try:
                f_human = open("players/player_human.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f_human.write(player_human_str)
            f_human.close()
        hp0_text_rect = hp0_text.get_rect()
        hp0_text_rect.center = (human_rect.x + 50, human_rect.y + 110)
        keys = pygame.key.get_pressed()
        if keys [pygame.K_w] and human_rect.top > 0 and human2_rect.top > 0:
            human_move_image_rect.y = human_move_image_rect.y - human_distance
            human_move_image2_rect.y = human_move_image2_rect.y - human_distance
            human_rect.y = human_rect.y - human_distance
            human2_rect.y = human2_rect.y - human_distance
            name0_text_rect.y = name0_text_rect.y - human_distance  
            hp0_text_rect.y = hp0_text_rect.y - human_distance
        elif keys [pygame.K_s] and human_rect.bottom < height - 120 and human2_rect.bottom < height - 120:
            human_move_image_rect.y = human_move_image_rect.y + human_distance
            human_move_image2_rect.y = human_move_image2_rect.y + human_distance
            human_rect.y = human_rect.y + human_distance
            human2_rect.y = human2_rect.y + human_distance
            name0_text_rect.y = name0_text_rect.y + human_distance
            hp0_text_rect.y = hp0_text_rect.y + human_distance
        elif keys [pygame.K_a] and human_rect.left > 0 and human2_rect.left > 0:
            human_move_image_rect.x = human_move_image_rect.x - human_distance
            human_move_image2_rect.x = human_move_image2_rect.x - human_distance
            human_rect.x = human_rect.x - human_distance
            human2_rect.x = human2_rect.x - human_distance
            name0_text_rect.x = name0_text_rect.x - human_distance
            hp0_text_rect.x = hp0_text_rect.x - human_distance  
            mirror = 1
        elif keys [pygame.K_d] and human_rect.right > 0 and human2_rect.right < width:
            human_move_image_rect.x = human_move_image_rect.x + human_distance
            human_move_image2_rect.x = human_move_image2_rect.x + human_distance
            human_rect.x = human_rect.x + human_distance
            human2_rect.x = human2_rect.x + human_distance
            name0_text_rect.x = name0_text_rect.x + human_distance
            hp0_text_rect.x = hp0_text_rect.x + human_distance
            mirror = 0 

        elif keys [pygame.K_SPACE] and mirror == 1:
            human_attack = 1
        elif keys [pygame.K_SPACE] and mirror == 0:
            human_attack = 2
   
        if human_attack == 1 and keys [pygame.K_SPACE]:
                human_attack2_rect.center = (human2_rect.x - 25 ,human2_rect.y + 45)
                screen.blit(human_attack2_image,human_attack2_rect)
            
        if human_attack == 2 and keys [pygame.K_SPACE]:           
                human_attack_rect.center = (human_rect.x + 125 ,human_rect.y + 45)
                screen.blit(human_attack_image,human_attack_rect)
            
        if mirror == 0:
            if keys [pygame.K_d] or keys [pygame.K_w] or keys [pygame.K_s]:
                human_move_image_rect.center = (human_rect.x + 40 ,human_rect.y  + 45)
                screen.blit(human_move_image,human_move_image_rect)
                screen.blit(name0_text,name0_text_rect)
                screen.blit(hp0_text,hp0_text_rect)
            else:
                screen.blit(human_image,human_rect)
                screen.blit(name0_text,name0_text_rect)
                screen.blit(hp0_text,hp0_text_rect)

        if mirror == 1:
            if keys [pygame.K_a] or keys [pygame.K_w] or keys [pygame.K_s]: 
                human_move_image2_rect.center = (human2_rect.x + 60,human2_rect.y + 45)
                screen.blit(human_move_image2,human_move_image2_rect)                
                screen.blit(name0_text,name0_text_rect)
                screen.blit(hp0_text,hp0_text_rect)
            else:
                screen.blit(human2_image,human2_rect)
                screen.blit(name0_text,name0_text_rect)
                screen.blit(hp0_text,hp0_text_rect)
        
    # Firemag
    if player_fmag > 0 and enemy_scelet_boss_hp <= 0:
        if fmag_hp > 0:
            hp1_text = pygame.font.SysFont("Moncerat", 18)
        if fmag_hp >= 200:
            hp1_text = hp1_text.render("HP: " + f"{fmag_hp}", True, green)
        if fmag_hp >= 100 and fmag_hp < 200:
            hp1_text = hp1_text.render("HP: " + f"{fmag_hp}", True, yellow)
        if fmag_hp <= 99 and fmag_hp > 0:
            hp1_text = hp1_text.render("HP: " + f"{fmag_hp}", True, red)
        if fmag_hp < 0:
            player_fmag -= 100000000
            player_fmag_str = str(player_fmag)
            try:
                f_fmag = open("players/player_fmag.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f_fmag.write(player_fmag_str)
            f_fmag.close()
        hp1_text_rect = hp1_text.get_rect()
        hp1_text_rect.center = (fzard_rect.x + 60, fzard_rect.y + 135)
        keys = pygame.key.get_pressed()
        if keys [pygame.K_w] and fzard_rect.top > 0 and fzard2_rect.top > 0:
            fzard_rect.y = fzard_rect.y - fmag_distance
            fzard2_rect.y = fzard2_rect.y - fmag_distance
            name1_text_rect.y = name1_text_rect.y - fmag_distance 
            hp1_text_rect.y = hp1_text_rect.y - fmag_distance
        elif keys [pygame.K_s] and fzard_rect.bottom < height - 120 and fzard2_rect.bottom < height - 120:
            fzard_rect.y = fzard_rect.y + fmag_distance
            fzard2_rect.y = fzard2_rect.y + fmag_distance
            name1_text_rect.y = name1_text_rect.y + fmag_distance
            hp1_text_rect.y = hp1_text_rect.y + fmag_distance
        elif keys [pygame.K_a] and fzard_rect.left > 0 and fzard2_rect.left > 0:
            fzard_rect.x = fzard_rect.x - fmag_distance
            fzard2_rect.x = fzard2_rect.x - fmag_distance
            name1_text_rect.x = name1_text_rect.x - fmag_distance
            hp1_text_rect.x = hp1_text_rect.x - fmag_distance   
            mirror = 1
        elif keys [pygame.K_d] and fzard_rect.right > 0 and fzard2_rect.right < width:
            fzard_rect.x = fzard_rect.x +fmag_distance
            fzard2_rect.x = fzard2_rect.x + fmag_distance
            name1_text_rect.x = name1_text_rect.x + fmag_distance
            hp1_text_rect.x = hp1_text_rect.x + fmag_distance
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

        if fball_rect.right > 0 or fball2_rect.right < width or fball_rect.left > 0 or fball2_rect.left < width:
             fire_attack == 0
    
        if mirror == 0:
            if keys [pygame.K_d] or keys [pygame.K_w] or keys [pygame.K_s]:
                fzard_move_image_rect.center = (fzard_rect.x + 65,fzard_rect.y  + 60)
                screen.blit(fzard_move_image,fzard_move_image_rect)
                screen.blit(name1_text,name1_text_rect)
                screen.blit(hp1_text,hp1_text_rect)
            else:
                screen.blit(fzard_image,fzard_rect)
                screen.blit(name1_text,name1_text_rect)
                screen.blit(hp1_text,hp1_text_rect)

        if mirror == 1:
            if keys [pygame.K_a] or keys [pygame.K_w] or keys [pygame.K_s]: 
                fzard_move_image2_rect.center = (fzard2_rect.x + 65 ,fzard2_rect.y + 60)
                screen.blit(fzard_move_image2,fzard_move_image2_rect)                
                screen.blit(name1_text,name1_text_rect)
                screen.blit(hp1_text,hp1_text_rect)
            else:
                screen.blit(fzard2_image,fzard2_rect)
                screen.blit(name1_text,name1_text_rect)
                screen.blit(hp1_text,hp1_text_rect)

    # Water mag
    if player_wmag > 0:
        if wmag_hp > 0:
            hp2_text = pygame.font.SysFont("Moncerat", 18)
        if wmag_hp >= 75:
            hp2_text = hp2_text.render("HP: " + f"{wmag_hp}", True, green)
        if wmag_hp <= 74 and wmag_hp >= 40:
            hp2_text = hp2_text.render("HP: " + f"{wmag_hp}", True, yellow)
        if wmag_hp <= 39 and wmag_hp > 0:
            hp2_text = hp2_text.render("HP: " + f"{wmag_hp}", True, red)
        if wmag_hp < 0:
            player_wmag -= 100000000
            player_wmag_str = str(player_wmag)
            try:
                f_wmag = open("players/player_wmag.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f_wmag.write(player_wmag_str)
            f_wmag.close()
        hp2_text_rect = hp2_text.get_rect()
        hp2_text_rect.center = (wzard_rect.x + 65, wzard_rect.y + 130)  
        keys = pygame.key.get_pressed()
        if keys [pygame.K_w] and wzard_rect.top > 0 and wzard2_rect.top > 0:
            wzard_move_image_rect.y = wzard_move_image_rect.y - wmag_distance
            wzard_move_image2_rect.y = wzard_move_image2_rect.y - wmag_distance
            wzard_rect.y = wzard_rect.y - wmag_distance
            wzard2_rect.y = wzard2_rect.y - wmag_distance
            name2_text_rect.y = name2_text_rect.y - wmag_distance
            hp2_text_rect.y = hp2_text_rect.y - wmag_distance
        elif keys [pygame.K_s] and wzard_rect.bottom < height - 120 and wzard2_rect.bottom < height - 120:
            wzard_move_image_rect.y = wzard_move_image_rect.y + wmag_distance
            wzard_move_image2_rect.y = wzard_move_image2_rect.y + wmag_distance
            wzard_rect.y = wzard_rect.y + wmag_distance
            wzard2_rect.y = wzard2_rect.y + wmag_distance
            name2_text_rect.y = name2_text_rect.y + wmag_distance
            hp2_text_rect.y = hp2_text_rect.y + wmag_distance
        elif keys [pygame.K_a] and wzard_rect.left > 0 and wzard2_rect.left > 0:                    
            wzard_move_image_rect.x = wzard_move_image_rect.x - wmag_distance
            wzard_rect.x = wzard_rect.x - wmag_distance
            wzard2_rect.x = wzard2_rect.x - wmag_distance
            name2_text_rect.x = name2_text_rect.x - wmag_distance
            hp2_text_rect.x = hp2_text_rect.x - wmag_distance
            mirror = 1
        elif keys [pygame.K_d] and wzard_rect.right > 0 and wzard2_rect.right < width:
            wzard_move_image_rect.x = wzard_move_image_rect.x + wmag_distance
            wzard_rect.x = wzard_rect.x + wmag_distance
            wzard2_rect.x = wzard2_rect.x + wmag_distance
            name2_text_rect.x = name2_text_rect.x + wmag_distance
            hp2_text_rect.x = hp2_text_rect.x + wmag_distance
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

        if wzard_attack_rect.right > 0 or wzard_attack2_rect.right < width or wzard_attack_rect.left > 0 or wzard_attack2_rect.left < width:
             wire_attack == 0
              
        
        if mirror == 0:
            if keys [pygame.K_d] or keys [pygame.K_w] or keys [pygame.K_s]:
                wzard_move_image_rect.center = (wzard_rect.x + 55 ,wzard_rect.y  + 60)
                screen.blit(wzard_move_image,wzard_move_image_rect)
                screen.blit(name2_text,name2_text_rect)
                screen.blit(hp2_text,hp2_text_rect)
            else:
                screen.blit(wzard_image,wzard_rect)
                screen.blit(name2_text,name2_text_rect)
                screen.blit(hp2_text,hp2_text_rect)

        if mirror == 1:
            if keys [pygame.K_a] or keys [pygame.K_w] or keys [pygame.K_s]: 
                wzard_move_image2_rect.center = (wzard2_rect.x + 80 ,wzard2_rect.y + 60)
                screen.blit(wzard_move_image2,wzard_move_image2_rect)                
                screen.blit(name2_text,name2_text_rect)
                screen.blit(hp2_text,hp2_text_rect)
            else:
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
        if scelet_rect.left < 100 or scelet_rect.left > width - 120:
            scelet_x = -1 * scelet_x
        elif scelet_rect.top < 75 or scelet_rect.bottom > height - 120:
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
        if scelet1_rect.left < 100 or scelet1_rect.left > width - 120:
            scelet1_x = -1 * scelet1_x
        elif scelet1_rect.top < 75 or scelet1_rect.bottom > height - 120:
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
        if scelet2_rect.left < 100 or scelet2_rect.left > width - 120:
            scelet2_x = -1 * scelet2_x
        elif scelet2_rect.top < 75 or scelet2_rect.bottom > height - 120:
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
        if scelet3_rect.left < 100 or scelet3_rect.left > width - 120:
            scelet3_x = -1 * scelet3_x
        elif scelet3_rect.top < 75 or scelet3_rect.bottom > height - 120:
            scelet3_y = -1 * scelet3_y
        if scelet3_rect.left < 130: 
            scelet3_image = loadify(enemy0.img2)          
        if scelet3_rect.left >= 1000: 
            scelet3_image = loadify(enemy0.img)

    # Skeleton 4
    if enemy_scelet4 > 0:
        hp4_text4 = pygame.font.SysFont("Moncerat", 18)
        if scelet4_hp > 0:      
            hp4_text4 = hp4_text4.render("HP: " + f"{scelet4_hp}", True, white)
            hp4_text4_rect = hp4_text4.get_rect()
            hp4_text4_rect.center = (scelet4_rect.x + 30, scelet4_rect.y + 125)
            screen.blit(hp4_text4,hp4_text4_rect)
        e4_name_text_rect.center = (scelet4_rect.x + 30, scelet4_rect.y + 110)
        if scelet4_hp > 0:
            screen.blit(scelet4_image,scelet4_rect)
            screen.blit(e4_name_text,e4_name_text_rect)
        scelet4_rect.x += scelet4_x * scelet_speed
        scelet4_rect.y += scelet4_y * scelet_speed
        if scelet4_rect.left < 100 or scelet4_rect.left > width - 120:
            scelet4_x = -1 * scelet4_x
        elif scelet4_rect.top < 75 or scelet4_rect.bottom > height - 120:
            scelet4_y = -1 * scelet4_y
        if scelet4_rect.left < 130: 
            scelet4_image = loadify(enemy0.img2)        
        if scelet4_rect.left >= 1000: 
            scelet4_image = loadify(enemy0.img)

    # Skeleton 5
    if enemy_scelet5 > 0:
        hp5_text5 = pygame.font.SysFont("Moncerat", 18)
        if scelet5_hp > 0:      
            hp5_text5 = hp5_text5.render("HP: " + f"{scelet5_hp}", True, white)
            hp5_text5_rect = hp5_text5.get_rect()
            hp5_text5_rect.center = (scelet5_rect.x + 30, scelet5_rect.y + 125)
            screen.blit(hp5_text5,hp5_text5_rect)
        e5_name_text_rect.center = (scelet5_rect.x + 30, scelet5_rect.y + 110)
        if scelet5_hp > 0:
            screen.blit(scelet5_image,scelet5_rect)
            screen.blit(e5_name_text,e5_name_text_rect)
        scelet5_rect.x += scelet5_x * scelet_speed
        scelet5_rect.y += scelet5_y * scelet_speed
        if scelet5_rect.left < 100 or scelet5_rect.left > width - 120:
            scelet5_x = -1 * scelet5_x
        elif scelet5_rect.top < 75 or scelet5_rect.bottom > height - 120:
            scelet5_y = -1 * scelet5_y
        if scelet5_rect.left < 130: 
            scelet5_image = loadify(enemy0.img2)              
        if scelet5_rect.left >= 1000: 
            scelet5_image = loadify(enemy0.img)

 # Skeleton 6
    if enemy_scelet6 > 0:
        hp6_text6 = pygame.font.SysFont("Moncerat", 18)
        if scelet6_hp > 0:      
            hp6_text6 = hp6_text6.render("HP: " + f"{scelet6_hp}", True, white)
            hp6_text6_rect = hp6_text6.get_rect()
            hp6_text6_rect.center = (scelet6_rect.x + 30, scelet6_rect.y + 125)
            screen.blit(hp6_text6,hp6_text6_rect)
        e6_name_text_rect.center = (scelet6_rect.x + 30, scelet6_rect.y + 110)
        if scelet6_hp > 0:
            screen.blit(scelet6_image,scelet6_rect)
            screen.blit(e6_name_text,e6_name_text_rect)
        scelet6_rect.x += scelet6_x * scelet_speed
        scelet6_rect.y += scelet6_y * scelet_speed
        if scelet6_rect.left < 100 or scelet6_rect.left > width - 120:
            scelet6_x = -1 * scelet6_x
        elif scelet6_rect.top < 75 or scelet6_rect.bottom > height - 120:
            scelet6_y = -1 * scelet6_y
        if scelet6_rect.left < 130: 
            scelet6_image = loadify(enemy0.img2)              
        if scelet6_rect.left >= 1000: 
            scelet6_image = loadify(enemy0.img)

# Skeleton 7
    if enemy_scelet7 > 0:
        hp7_text7 = pygame.font.SysFont("Moncerat", 18)
        if scelet7_hp > 0:      
            hp7_text7 = hp7_text7.render("HP: " + f"{scelet7_hp}", True, white)
            hp7_text7_rect = hp7_text7.get_rect()
            hp7_text7_rect.center = (scelet7_rect.x + 30, scelet7_rect.y + 125)
            screen.blit(hp7_text7,hp7_text7_rect)
        e7_name_text_rect.center = (scelet7_rect.x + 30, scelet7_rect.y + 110)
        if scelet7_hp > 0:
            screen.blit(scelet7_image,scelet7_rect)
            screen.blit(e7_name_text,e7_name_text_rect)
        scelet7_rect.x += scelet7_x * scelet_speed
        scelet7_rect.y += scelet7_y * scelet_speed
        if scelet7_rect.left < 100 or scelet7_rect.left > width - 120:
            scelet7_x = -1 * scelet7_x
        elif scelet7_rect.top < 75 or scelet7_rect.bottom > height - 120:
            scelet7_y = -1 * scelet7_y
        if scelet7_rect.left < 130: 
            scelet7_image = loadify(enemy0.img2)              
        if scelet7_rect.left >= 1000: 
            scelet7_image = loadify(enemy0.img)

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
        if scelet_boss_rect.left < 100 or scelet_boss_rect.left > width - 120:
            scelet_boss_x = -1 * scelet_boss_x
        elif scelet_boss_rect.top < 75 or scelet_boss_rect.bottom > height - 120:
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

# scelet --> human
    if scelet_rect.colliderect(human_rect) or scelet_rect.colliderect(human2_rect):
        if player_human > 0 and scelet_hp > 0 and enemy_scelet > 0:
            human_hp -= 1
            str_human_hp = str(human_hp)
            try:
                f1 = open("players_hp/human_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f1.write(str_human_hp)
            f1.close()

 # scelet1 --> human
    if scelet1_rect.colliderect(human_rect) or scelet1_rect.colliderect(human2_rect) :
        if player_human > 0 and scelet1_hp > 0 and enemy_scelet1 > 0:
            human_hp -= 1
            str_human_hp = str(human_hp)
            try:
                f1 = open("players_hp/human_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f1.write(str_human_hp)
            f1.close()

# scelet2 --> human
    if scelet2_rect.colliderect(human_rect) or scelet2_rect.colliderect(human2_rect) :
        if player_human > 0 and scelet2_hp > 0 and enemy_scelet2 > 0:
            human_hp -= 1
            str_human_hp = str(human_hp)
            try:
                f1 = open("players_hp/human_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f1.write(str_human_hp)
            f1.close()

# scelet3 --> human
    if scelet3_rect.colliderect(human_rect) or scelet3_rect.colliderect(human2_rect) :
        if player_human > 0 and scelet3_hp > 0 and enemy_scelet3 > 0:
            human_hp -= 1
            str_human_hp = str(human_hp)
            try:
                f1 = open("players_hp/human_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f1.write(str_human_hp)
            f1.close()

# scelet4 --> human
    if scelet4_rect.colliderect(human_rect) or scelet4_rect.colliderect(human2_rect) :
        if player_human > 0 and scelet4_hp > 0 and enemy_scelet4 > 0:
            human_hp -= 1
            str_human_hp = str(human_hp)
            try:
                f1 = open("players_hp/human_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f1.write(str_human_hp)
            f1.close()

# scelet5 --> human
    if scelet5_rect.colliderect(human_rect) or scelet5_rect.colliderect(human2_rect) :
        if player_human > 0 and scelet5_hp > 0 and enemy_scelet5 > 0:
            human_hp -= 1
            str_human_hp = str(human_hp)
            try:
                f1 = open("players_hp/human_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f1.write(str_human_hp)
            f1.close()

# scelet6 --> human
    if scelet6_rect.colliderect(human_rect) or scelet6_rect.colliderect(human2_rect):
        if player_human > 0 and scelet6_hp > 0 and enemy_scelet6 > 0:
            human_hp -= 1
            str_human_hp = str(human_hp)
            try:
                f1 = open("players_hp/human_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f1.write(str_human_hp)
            f1.close()

# scelet7 --> human
    if scelet7_rect.colliderect(human_rect) or scelet7_rect.colliderect(human2_rect):
        if player_human > 0 and scelet7_hp > 0 and enemy_scelet7 > 0:
            human_hp -= 1
            str_human_hp = str(human_hp)
            try:
                f1 = open("players_hp/human_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f1.write(str_human_hp)
            f1.close()

# sceletboss --> human
    if scelet_boss_rect.colliderect(human_rect) or scelet_boss_rect.colliderect(human2_rect) and human_attack == 1 and keys [pygame.K_SPACE]:
        if player_human > 0 and enemy_scelet_boss_hp > 0 and enemy_scelet_boss > 0:
            human_hp -= 2
            str_human_hp = str(human_hp)
            try:
                f1 = open("players_hp/human_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f1.write(str_human_hp)
            f1.close()
#-----------------------------------------------------------------------------------------------#
# scelet --> firemag
    if scelet_rect.colliderect(fzard_rect) or scelet_rect.colliderect(fzard2_rect):
        if player_fmag > 0 and scelet_hp > 0 and enemy_scelet > 0:
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
        if player_fmag > 0 and scelet1_hp > 0 and enemy_scelet1 > 0:
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
        if player_fmag > 0 and scelet2_hp > 0 and enemy_scelet2 > 0:
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
        if player_fmag > 0 and scelet3_hp > 0 and enemy_scelet3 > 0:
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
        if player_fmag > 0 and enemy_scelet_boss_hp > 0 and enemy_scelet_boss > 0:
            fmag_hp -= 2
            str_fmag_hp = str(fmag_hp)
            try:
                f1 = open("players_hp/fmag_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f1.write(str_fmag_hp)
            f1.close()
#-----------------------------------------------------------------------------------------------#
# scelet --> watermag
    if scelet_rect.colliderect(wzard_rect) or scelet_rect.colliderect(wzard2_rect):
        if player_wmag > 0 and scelet_hp > 0 and enemy_scelet > 0:
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
        if player_wmag > 0 and scelet1_hp > 0 and enemy_scelet1 > 0:
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
        if player_wmag > 0 and scelet2_hp > 0 and enemy_scelet2 > 0:
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
        if player_wmag > 0 and scelet3_hp > 0 and enemy_scelet3 > 0:
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
        if player_wmag > 0 and enemy_scelet_boss_hp > 0 and enemy_scelet_boss > 0:
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

# human_attack --> scelet
    if human_attack_rect.colliderect(scelet_rect) or human_attack2_rect.colliderect(scelet_rect) :
        if enemy_scelet > 0 and keys [pygame.K_SPACE]:
            scelet_hp -= 1
            str_scelet_hp = str(scelet_hp)
            try:
                f3 = open("players_hp/scelet_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_scelet_hp)
            f3.close()

# human_attack--> scelet1
    if human_attack_rect.colliderect(scelet1_rect) or human_attack2_rect.colliderect(scelet1_rect):
        if enemy_scelet1 > 0 and keys [pygame.K_SPACE]:
            scelet1_hp -= 1
            str_scelet1_hp = str(scelet1_hp)
            try:
                f3 = open("players_hp/scelet1_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_scelet1_hp)
            f3.close()

# human_attack--> scelet2
    if human_attack_rect.colliderect(scelet2_rect) or human_attack2_rect.colliderect(scelet2_rect):
        if enemy_scelet2 > 0 and keys [pygame.K_SPACE]:
            scelet2_hp -= 1
            str_scelet2_hp = str(scelet2_hp)
            try:
                f3 = open("players_hp/scelet2_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_scelet2_hp)
            f3.close()

# human_attack --> scelet3
    if human_attack_rect.colliderect(scelet3_rect) or human_attack2_rect.colliderect(scelet3_rect):
        if enemy_scelet3 > 0 and keys [pygame.K_SPACE]:
            scelet3_hp -= 1
            str_scelet3_hp = str(scelet3_hp)
            try:
                f3 = open("players_hp/scelet3_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_scelet3_hp)
            f3.close()

# human_attack --> scelet4
    if human_attack_rect.colliderect(scelet4_rect) or human_attack2_rect.colliderect(scelet4_rect):
        if enemy_scelet4 > 0 and keys [pygame.K_SPACE]:
            scelet4_hp -= 1
            str_scelet4_hp = str(scelet4_hp)
            try:
                f3 = open("players_hp/scelet4_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_scelet4_hp)
            f3.close()

# human_attack --> scelet5
    if human_attack_rect.colliderect(scelet5_rect) or human_attack2_rect.colliderect(scelet5_rect):
        if enemy_scelet5 > 0 and keys [pygame.K_SPACE]:
            scelet5_hp -= 1
            str_scelet5_hp = str(scelet5_hp)
            try:
                f3 = open("players_hp/scelet5_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_scelet5_hp)
            f3.close()
        
# human_attack --> scelet6
    if human_attack_rect.colliderect(scelet6_rect) or human_attack2_rect.colliderect(scelet6_rect):
        if enemy_scelet6 > 0 and keys [pygame.K_SPACE]:
            scelet6_hp -= 10
            str_scelet6_hp = str(scelet6_hp)
            try:
                f3 = open("players_hp/scelet6_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_scelet6_hp)
            f3.close()

# human_attack --> scelet7
    if human_attack_rect.colliderect(scelet7_rect) or human_attack2_rect.colliderect(scelet7_rect):
        if enemy_scelet7 > 0 and keys [pygame.K_SPACE]:
            scelet7_hp -= 10
            str_scelet7_hp = str(scelet7_hp)
            try:
                f3 = open("players_hp/scelet7_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_scelet7_hp)
            f3.close()

# human_attack --> sceletboss
    if human_attack_rect.colliderect(scelet_boss_rect) or human_attack2_rect.colliderect(scelet_boss_rect):
        if enemy_scelet_boss > 0 and keys [pygame.K_SPACE]:
            enemy_scelet_boss_hp -= 1
            str_enemy_scelet_boss_hp = str(enemy_scelet_boss_hp)
            try:
                f3 = open("players_hp/scelet_boss_hp.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f3.write(str_enemy_scelet_boss_hp)
            f3.close()

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


#-----------------------------------------------------------------------------------------------#
# OBRAZCE
#-----------------------------------------------------------------------------------------------#

    pygame.draw.line(screen, black, (1,1),(1200,1), 3)
    pygame.draw.line(screen, black, (1,70),(1200,70), 3)

    pygame.draw.line(screen, black, (1,1),(1,70), 3)
    pygame.draw.line(screen, black, (1198,1),(1198,70), 3)

    pygame.draw.line(screen, black, (70,70),(70,0), 3)
    pygame.draw.line(screen, black, (140,70),(140,0), 3)
    pygame.draw.line(screen, black, (210,70),(210,0), 3)
    pygame.draw.line(screen, black, (280,70),(280,0), 3)
    pygame.draw.line(screen, black, (350,70),(350,0), 3)
    pygame.draw.line(screen, black, (1069,70),(1069,0), 3)



    pygame.display.update()
    clock.tick_busy_loop(fps)

# Ukončení hry
pygame.quit()