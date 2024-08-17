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
pygame.display.set_caption("Hunt the reaper")

# Barvičky 
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
dark_green = (0, 100, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
orange = (255,140,0)
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
arrow_attack = 0

run_game = 0

attack_x = 1
attack_1x = -1* attack_x

ghost_speed = 4
ghost_boss_speed = 4
spider_speed = 2
spider_boss_speed = 2
scelet_speed = 2
scelet_boss_speed = 3
goblin_speed = 3
goblin_boss_speed = 3

archer_attack_speed = 15
light_attack_speed = 4
fball_speed = 9

fmag_distance = 5
light_distance = 6
human_distance = 4
archer_distance = 5

# Nastavení ghost_hp = 0 na začátku hry
ghost_hp = 0
str_ghost_hp = str(ghost_hp)
try:
    f_ghost_hp = open("players_hp/ghost_hp.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_ghost_hp.write(str_ghost_hp)
ghost_hp1 = 0
str_ghost_hp1 = str(ghost_hp1)
try:
    f_ghost_hp1 = open("players_hp/ghost_hp1.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_ghost_hp1.write(str_ghost_hp1)
ghost_hp2= 0
str_ghost_hp2 = str(ghost_hp2)
try:
    f_ghost_hp2= open("players_hp/ghost_hp2.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_ghost_hp.write(str_ghost_hp2)
ghost_hp3 = 0
str_ghost_hp3 = str(ghost_hp3)
try:
    f_ghost_hp3 = open("players_hp/ghost_hp3.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_ghost_hp.write(str_ghost_hp3)

# Nastavení goblin_hp = 0 na začátku hry
goblin_hp = 0
str_goblin_hp = str(goblin_hp)
try:
    f_goblin_hp = open("players_hp/goblin_hp.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_goblin_hp.write(str_goblin_hp)
goblin_hp1 = 0
str_goblin_hp1 = str(goblin_hp1)
try:
    f_goblin_hp1 = open("players_hp/goblin_hp1.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_goblin_hp.write(str_goblin_hp1)
goblin_hp2 = 0
str_goblin_hp2 = str(goblin_hp2)
try:
    f_goblin_hp2 = open("players_hp/goblin_hp2.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_goblin_hp2.write(str_goblin_hp2)
goblin_hp3 = 0
str_goblin_hp3 = str(goblin_hp3)
try:
    f_goblin_hp3 = open("players_hp/goblin_hp3.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_goblin_hp3.write(str_goblin_hp3)

# Nastavení spider_hp = 0 na začátku hry
spider_hp = 0
str_spider_hp = str(spider_hp)
try:
    f_spider_hp = open("players_hp/spider_hp.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_spider_hp.write(str_spider_hp)
spider_hp1 = 0
str_spider_hp1 = str(spider_hp1)
try:
    f_spider_hp1 = open("players_hp/spider_hp1.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_spider_hp.write(str_spider_hp1)
spider_hp2 = 0
str_spider_hp2 = str(spider_hp2)
try:
    f_spider_hp2 = open("players_hp/spider_hp2.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_spider_hp2.write(str_spider_hp2)
spider_hp3 = 0
str_spider_hp3 = str(spider_hp3)
try:
    f_spider_hp3 = open("players_hp/spider_hp3.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_spider_hp3.write(str_spider_hp3)

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

# Nastavení enemy_goblin = 0 na začátku hry
enemy_goblin = 0
str_enemy_goblin = str(enemy_goblin)
try:
    f_enemy_goblin = open("players/enemy_goblin.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_goblin.write(str_enemy_goblin)
enemy_goblin1 = 0
str_enemy_goblin1 = str(enemy_goblin1)
try:
    f_enemy_goblin1 = open("players/enemy_goblin1.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_goblin1.write(str_enemy_goblin1)
enemy_goblin2 = 0
str_enemy_goblin2 = str(enemy_goblin1)
try:
    f_enemy_goblin2 = open("players/enemy_goblin2.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_goblin2.write(str_enemy_goblin2)
enemy_goblin3 = 0
str_enemy_goblin3 = str(enemy_goblin3)
try:
    f_enemy_goblin3 = open("players/enemy_goblin3.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_goblin3.write(str_enemy_goblin3)

# Nastavení enemy_spider = 0 na začátku hry
enemy_spider = 0
str_enemy_spider = str(enemy_spider)
try:
    f_enemy_spider = open("players/enemy_spider.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_spider.write(str_enemy_spider)
enemy_spider1 = 0
str_enemy_spider1 = str(enemy_spider1)
try:
    f_enemy_spider1 = open("players/enemy_spider1.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_spider1.write(str_enemy_spider1)
enemy_spider2 = 0
str_enemy_spider2 = str(enemy_spider1)
try:
    f_enemy_spider2 = open("players/enemy_spider2.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_spider2.write(str_enemy_spider2)
enemy_spider3 = 0
str_enemy_spider3 = str(enemy_spider3)
try:
    f_enemy_spider3 = open("players/enemy_spider3.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_spider3.write(str_enemy_spider3)

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

# Nastavení enemy_ghost = 0 na začátku hry
enemy_ghost = 0
str_enemy_ghost = str(enemy_ghost)
try:
    f_enemy_ghost = open("players/enemy_ghost.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_ghost.write(str_enemy_ghost)
enemy_ghost1 = 0
str_enemy_ghost1 = str(enemy_ghost1)
try:
    f_enemy_ghost1 = open("players/enemy_ghost1.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_ghost1.write(str_enemy_ghost1)
enemy_ghost2 = 0
str_enemy_ghost2 = str(enemy_ghost2)
try:
    f_enemy_ghost2 = open("players/enemy_ghost2.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_ghost2.write(str_enemy_ghost2)
enemy_ghost3 = 0
str_enemy_ghost3 = str(enemy_ghost3)
try:
    f_enemy_ghost3 = open("players/enemy_ghost3.txt","w")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_ghost3.write(str_enemy_ghost3)


# Random pohyb skeletonů
ghost_x = random.choice ([-1,1])
ghost_y = random.choice([-1,1])
ghost1_x = random.choice ([-1,1])
ghost1_y = random.choice([-1,1])
ghost2_x = random.choice ([-1,1])
ghost2_y = random.choice([-1,1])
ghost3_x = random.choice ([-1,1])
ghost3_y = random.choice([-1,1])
ghost_boss_x = random.choice ([-1,1])
ghost_boss_y = random.choice([-1,1])
spider_x = random.choice ([-1,1])
spider_y = random.choice([-1,1])
spider1_x = random.choice ([-1,1])
spider1_y = random.choice([-1,1])
spider2_x = random.choice ([-1,1])
spider2_y = random.choice([-1,1])
spider3_x = random.choice ([-1,1])
spider3_y = random.choice([-1,1])
spider_boss_x = random.choice ([-1,1])
spider_boss_y = random.choice([-1,1])
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
goblin_x = random.choice ([-1,1])
goblin_y = random.choice([-1,1])
goblin1_x = random.choice ([-1,1])
goblin1_y = random.choice([-1,1])
goblin2_x = random.choice ([-1,1])
goblin2_y = random.choice([-1,1])
goblin3_x = random.choice ([-1,1])
goblin3_y = random.choice([-1,1])
goblin_boss_x = random.choice ([-1,1])
goblin_boss_y = random.choice([-1,1])

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
player_light = int()
player_light_str=str(player_light)
try:
    f_player_light = open("players/player_light.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_player_light.read(player_light)
light_hp = (player2.hp)
if player_light > 0:
    str_light_hp = str(light_hp)
    try:
        f2 = open("players_hp/light_hp.txt", "r")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")
    text = f2.read(light_hp)

# Archer
player_archer = int()
player_archer_str=str(player_archer)
try:
    f_player_archer = open("players/player_archer.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_player_archer.read(player_archer)
archer_hp = (player3.hp)
if player_archer > 0:
    str_archer_hp = str(archer_hp)
    try:
        f2 = open("players_hp/archer_hp.txt", "r")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")
    text = f2.read(archer_hp)
    
#-----------------------------------------------------------------------------------------------#
### NEPŘÍTEL V POLI ###
#-----------------------------------------------------------------------------------------------#

# Goblin
enemy_goblin = int()
enemy_goblin_str=str(enemy_goblin)
try:
    f_enemy_goblin = open("players/enemy_goblin.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_goblin.read(enemy_goblin)
goblin_hp = (enemy4.hp)
str_goblin_hp = str(goblin_hp)
try:
    f3 = open("players_hp/goblin_hp.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(goblin_hp)

# Goblin 1
enemy_goblin1= int()
enemy_goblin1_str=str(enemy_goblin1)
try:
    f_enemy_goblin1 = open("players/enemy_goblin1.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_goblin1.read(enemy_goblin1)
goblin_hp1 = (enemy4.hp)
str_goblin_hp1 = str(goblin_hp1)
try:
    f3 = open("players_hp/goblin_hp1.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(goblin_hp1)

# Goblin 2
enemy_goblin2= int()
enemy_goblin2_str=str(enemy_goblin2)
try:
    f_enemy_goblin2 = open("players/enemy_goblin2.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_goblin2.read(enemy_goblin2)
goblin_hp2 = (enemy4.hp)
str_goblin_hp2 = str(goblin_hp2)
try:
    f3 = open("players_hp/goblin_hp2.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(goblin_hp2)

# Goblin 3
enemy_goblin3= int()
enemy_goblin3_str=str(enemy_goblin3)
try:
    f_enemy_goblin3 = open("players/enemy_goblin3.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_goblin3.read(enemy_goblin3)
goblin_hp3 = (enemy4.hp)
str_goblin_hp3 = str(goblin_hp3)
try:
    f3 = open("players_hp/goblin_hp3.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(goblin_hp3)

# Goblin BOSS
enemy_goblin_boss = int()
enemy_goblin_boss_str=str(enemy_goblin_boss)
try:
    f_enemy_goblin_boss  = open("players/enemy_goblin_boss.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_goblin.read(enemy_goblin_boss)
goblin_boss_hp = (enemy5.hp)
str_goblin_hp = str(goblin_boss_hp)
try:
    f3 = open("players_hp/goblin_boss_hp.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(goblin_boss_hp)

# Spider
enemy_spider= int()
enemy_spider_str=str(enemy_spider)
try:
    f_enemy_spider = open("players/enemy_spider.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_spider.read(enemy_spider)
spider_hp = (enemy2.hp)
str_spider_hp = str(spider_hp)
try:
    f3 = open("players_hp/spider_hp.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(spider_hp)

# Spider 1
enemy_spider1= int()
enemy_spider1_str=str(enemy_spider1)
try:
    f_enemy_spider1 = open("players/enemy_spider1.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_spider1.read(enemy_spider1)
spider_hp1 = (enemy2.hp)
str_spider_hp1 = str(spider_hp1)
try:
    f3 = open("players_hp/spider_hp1.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(spider_hp1)

# Spider 2
enemy_spider2= int()
enemy_spider2_str=str(enemy_spider2)
try:
    f_enemy_spider2 = open("players/enemy_spider2.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_spider2.read(enemy_spider2)
spider_hp2 = (enemy2.hp)
str_spider_hp2 = str(spider_hp2)
try:
    f3 = open("players_hp/spider_hp2.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(spider_hp2)

# Spider 3
enemy_spider3= int()
enemy_spider3_str=str(enemy_spider3)
try:
    f_enemy_spider3 = open("players/enemy_spider3.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_spider3.read(enemy_spider3)
spider_hp3 = (enemy2.hp)
str_spider_hp3 = str(spider_hp3)
try:
    f3 = open("players_hp/spider_hp3.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(spider_hp3)

# Spider BOSS
enemy_spider_boss= int()
enemy_spiderspider_boss_str=str(enemy_spider_boss)
try:
    f_enemy_spider_boss = open("players/enemy_spider_boss.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_spider.read(enemy_spider_boss)
enemy_spider_boss_hp = (enemy3.hp)
str_enemy_spider_boss_hp = str(enemy_spider_boss_hp)
try:
    f3 = open("players_hp/spider_boss_hp.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(enemy_spider_boss_hp)

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

# Ghost
enemy_ghost= int()
enemy_ghost_str=str(enemy_ghost)
try:
    f_enemy_ghost = open("players/enemy_ghost.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_ghost.read(enemy_ghost)
ghost_hp = (enemy6.hp)
str_ghost_hp = str(ghost_hp)
try:
    f3 = open("players_hp/ghost_hp.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(ghost_hp)

# Ghost 1
enemy_ghost1= int()
enemy_ghost1_str=str(enemy_ghost1)
try:
    f_enemy_ghost1 = open("players/enemy_ghost1.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_ghost1.read(enemy_ghost1)
ghost_hp1 = (enemy6.hp)
str_ghost1_hp = str(ghost_hp1)
try:
    f3 = open("players_hp/ghost_hp1.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(ghost_hp1)

# Ghost 2
enemy_ghost2= int()
enemy_ghost2_str=str(enemy_ghost2)
try:
    f_enemy_ghost2 = open("players/enemy_ghost2.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_ghost2.read(enemy_ghost2)
ghost_hp2 = (enemy6.hp)
str_ghost_hp2 = str(ghost_hp2)
try:
    f3 = open("players_hp/ghost_hp2.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(ghost_hp2)

# Ghost 3
enemy_ghost3= int()
enemy_ghost3_str=str(enemy_ghost3)
try:
    f_enemy_ghost3 = open("players/enemy_ghost3.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_ghost3.read(enemy_ghost3)
ghost_hp3 = (enemy6.hp)
str_ghost_hp3 = str(ghost_hp3)
try:
    f3 = open("players_hp/ghost_hp3.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(ghost_hp3)

# Ghost BOSS
enemy_ghost_boss = int()
enemy_ghost_boss_str=str(enemy_ghost_boss)
try:
    f_enemy_ghost_boss  = open("players/enemy_ghost_boss.txt","r")
except FileNotFoundError:
        print("Soubor nebyl nalezen")
text = f_enemy_ghost.read(enemy_ghost_boss)
ghost_boss_hp = (enemy7.hp)
str_ghost_hp = str(ghost_boss_hp)
try:
    f3 = open("players_hp/ghost_boss_hp.txt", "r")
except FileNotFoundError:
    print("Soubor nebyl nalezen")
text = f3.read(ghost_boss_hp)

#-----------------------------------------------------------------------------------------------#
### BACKGROUND, OBRÁZKY, TEXTY ###
#-----------------------------------------------------------------------------------------------#
# BACKGROUND
home_background_img = loadify(background_home.img)
home_background_img_rect = home_background_img.get_rect()

spider_background_img = loadify(background_spider.img)
spider_background_img_rect = spider_background_img.get_rect()

skelet_background_img = loadify(background_skelet.img)
skelet_background_img_rect = skelet_background_img.get_rect()

goblin_background_img = loadify(background_goblin.img)
goblin_background_img_rect = goblin_background_img.get_rect()

ghost_background_img = loadify(background_ghost.img)
ghost_background_img_rect = ghost_background_img.get_rect()

end_background_img = loadify(background_end.img)
end_background_img_rect = end_background_img.get_rect()

win_background_img = loadify(background_win.img)
win_background_img_rect = win_background_img.get_rect()


#-----------------------------------------------------------------------------------------------#

# OBRÁZKY

# Buttons
exit_img = pygame.image.load("img/exit_btn.png").convert_alpha()
exit_button = buttons.Button(0,0,exit_img,0.8)

start_img = pygame.image.load("img/start_btn.png").convert_alpha()
start_button = buttons.Button(0,0,start_img,0.8)

# Human
human_portret = loadify("img/human_portret.png")
human_portret_rect = human_portret.get_rect()
human_portret_rect.center = (width//2 - 105, 35)

human_portret_dead = loadify("img/human_portret_dead.png")
human_portret_dead_rect = human_portret_dead.get_rect()
human_portret_dead_rect.center = (width//2 - 105, 35)

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
fzard_portret_rect.center = (width//2 + 35, 35)

fzard_portret_dead = loadify("img/fmag_portret_dead.png")
fzard_portret_dead_rect = fzard_portret_dead.get_rect()
fzard_portret_dead_rect.center = (width//2 + 35, 35)

fzard_portret_lock = loadify("img/fmag_portret_lock.png")
fzard_portret_lock_rect = fzard_portret_lock.get_rect()
fzard_portret_lock_rect.center = (width//2 + 35, 35)

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
light_portret = loadify("img/light_portret.png")
light_portret_rect = light_portret.get_rect()
light_portret_rect.center = (width//2 + 105, 35)

light_portret_dead = loadify("img/light_portret_dead.png")
light_portret_dead_rect = light_portret_dead.get_rect()
light_portret_dead_rect.center = (width//2 + 105, 35)

light_portret_lock = loadify("img/light_portret_lock.png")
light_portret_lock_rect = light_portret_lock.get_rect()
light_portret_lock_rect.center = (width//2 + 105, 35)

light_image = loadify(player2.img)
light_rect = light_image.get_rect()
light_rect.center = (width//2, height//2)

light2_image = loadify(player2.img2)
light2_rect = light_image.get_rect()
light2_rect.center = (width//2 , height//2 )

light_attack_image = loadify(player2.img_attack)
light_attack_rect = light_attack_image.get_rect()

light_attack2_image = loadify(player2.img_attack2)
light_attack2_rect = light_attack2_image.get_rect()

light_move_image = loadify("img/watermag_move.png")
light_move_image_rect = light_move_image.get_rect()

light_move_image2 = loadify("img/watermag_move2.png")
light_move_image2_rect = light_move_image2.get_rect()

name2_text = pygame.font.SysFont("Moncerat", 20)
name2_text = name2_text.render(player2.name, True, white)
name2_text_rect = name2_text.get_rect()
name2_text_rect.center = (600,430)

# Archer
archer_portret = loadify("img/archer_portret.png")
archer_portret_rect = archer_portret.get_rect()
archer_portret_rect.center = (width//2 - 35, 35)

archer_portret_dead = loadify("img/archer_portret_dead.png")
archer_portret_dead_rect = archer_portret_dead.get_rect()
archer_portret_dead_rect.center = (width//2 - 35, 35)

archer_portret_lock = loadify("img/archer_portret_lock.png")
archer_portret_lock_rect = archer_portret_lock.get_rect()
archer_portret_lock_rect.center = (width//2 - 35, 35)

archer_image = loadify(player3.img)
archer_rect = archer_image.get_rect()
archer_rect.center = (width//2, height//2)

archer2_image = loadify(player3.img2)
archer2_rect = archer_image.get_rect()
archer2_rect.center = (width//2 , height//2 )

arrow_image = loadify(player3.img_attack)
arrow_rect = arrow_image.get_rect()

arrow2_image = loadify(player3.img_attack2)
arrow2_rect = arrow2_image.get_rect()

archer_move_image = loadify("img/archer_move.png")
archer_move_image_rect = archer_move_image.get_rect()

archer_move_image2 = loadify("img/archer_move2.png")
archer_move_image2_rect = archer_move_image2.get_rect()

name3_text = pygame.font.SysFont("Moncerat", 20)
name3_text = name3_text.render(player3.name, True, white)
name3_text_rect = name3_text.get_rect()
name3_text_rect.center = (600,440)

# Skelet Portal
portal_image = loadify("img/portal.png")
portal_image_rect = portal_image.get_rect()
portal_image_rect.center = (width//2 + 500, height//2 - 200)

# Spider Portal
s_portal_image = loadify("img/spider_portal.png")
s_portal_image_rect = s_portal_image.get_rect()
s_portal_image_rect.center = (width//2 + 500, height//2 - 200)

# Goblin Portal
g_portal_image = loadify("img/goblin_portal.png")
g_portal_image_rect = g_portal_image.get_rect()
g_portal_image_rect.center = (width//2 + 500, height//2 - 200)

# Goblin Portal
gh_portal_image = loadify("img/ghost_portal.png")
gh_portal_image_rect = gh_portal_image.get_rect()
gh_portal_image_rect.center = (width//2 + 500, height//2 - 200)


# Spider
if spider_hp > 0:
    spider_image = loadify(enemy2.img)
    spider_rect = spider_image.get_rect()
    spider_rect.center = (width//2 + 500, height//2 - 200)

    e_name_text = pygame.font.SysFont("Moncerat", 20)
    e_name_text = e_name_text.render(enemy2.name, True, red)
    e_name_text_rect = e_name_text.get_rect()
    e_name_text_rect.center = (992,435)

# Spider 1
if spider_hp1 > 0:
    spider_image1 = loadify(enemy2.img)
    spider_rect1 = spider_image1.get_rect()
    spider_rect1.center = (width//2 -100, height//2 - 100)

    e11_name_text = pygame.font.SysFont("Moncerat", 20)
    e11_name_text = e11_name_text.render(enemy2.name, True, red)
    e11_name_text_rect = e11_name_text.get_rect()
    e11_name_text_rect.center = (992,435)

# Spider 2
if spider_hp2 > 0:
    spider_image2 = loadify(enemy2.img)
    spider_rect2 = spider_image2.get_rect()
    spider_rect2.center = (width//2 + 100, height//2 - 200)

    e12_name_text = pygame.font.SysFont("Moncerat", 20)
    e12_name_text = e12_name_text.render(enemy2.name, True, red)
    e12_name_text_rect = e12_name_text.get_rect()
    e12_name_text_rect.center = (992,435)

# Spider 3
if spider_hp3 > 0:
    spider_image3 = loadify(enemy2.img)
    spider_rect3 = spider_image3.get_rect()
    spider_rect3.center = (width//2 , height//2 - 200)

    e9_name_text = pygame.font.SysFont("Moncerat", 20)
    e9_name_text = e9_name_text.render(enemy2.name, True, red)
    e9_name_text_rect = e9_name_text.get_rect()
    e9_name_text_rect.center = (992,435)

# Spider BOSS
if enemy_spider_boss_hp > 0:
    spider_boss_image = loadify(enemy3.img)
    spider_boss_rect = spider_boss_image.get_rect()
    spider_boss_rect.center = (width//2 + 500, height//2 - 200)

    eboss2_name_text = pygame.font.SysFont("Moncerat", 20)
    eboss2_name_text = eboss2_name_text.render(enemy3.name, True, red)
    eboss2_name_text_rect = eboss2_name_text.get_rect()
    eboss2_name_text_rect.center = (900,435)
     
# Sceleton
if scelet_hp > 0:
    scelet_image = loadify(enemy0.img)
    scelet_rect = scelet_image.get_rect()
    scelet_rect.center = (width//2 + 500, height//2 - 200)

    e8_name_text = pygame.font.SysFont("Moncerat", 20)
    e8_name_text = e8_name_text.render(enemy0.name, True, red)
    e8_name_text_rect = e8_name_text.get_rect()
    e8_name_text_rect.center = (992,435)

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
    scelet2_rect.center = (width//2 + 100, height//2 - 100)

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

# Ghost
if ghost_hp > 0 :
    ghost_image = loadify(enemy6.img)
    ghost_rect = ghost_image.get_rect()
    ghost_rect.center = (width//2 + 300, height//2 - 100)

    egh_name_text = pygame.font.SysFont("Moncerat", 20)
    egh_name_text = egh_name_text.render(enemy6.name, True, red)
    egh_name_text_rect = egh_name_text.get_rect()
    egh_name_text_rect.center = (992,435)

# Ghost 1
if ghost_hp1 > 0 :
    ghost1_image = loadify(enemy6.img)
    ghost1_rect = ghost1_image.get_rect()
    ghost1_rect.center = (width//2 - 200, height//2 - 200)

    egh1_name_text = pygame.font.SysFont("Moncerat", 20)
    egh1_name_text = egh1_name_text.render(enemy6.name, True, red)
    egh1_name_text_rect = egh1_name_text.get_rect()
    egh1_name_text_rect.center = (992,435)

# Ghost 2
if ghost_hp2 > 0 :
    ghost2_image = loadify(enemy6.img)
    ghost2_rect = ghost2_image.get_rect()
    ghost2_rect.center = (width//2 - 300, height//2 + 200)

    egh2_name_text = pygame.font.SysFont("Moncerat", 20)
    egh2_name_text = egh2_name_text.render(enemy6.name, True, red)
    egh2_name_text_rect = egh2_name_text.get_rect()
    egh2_name_text_rect.center = (992,435)

# Ghost 3
if ghost_hp3 > 0 :
    ghost3_image = loadify(enemy6.img)
    ghost3_rect = ghost3_image.get_rect()
    ghost3_rect.center = (width//2 + 100, height//2 - 200)

    egh3_name_text = pygame.font.SysFont("Moncerat", 20)
    egh3_name_text = egh3_name_text.render(enemy6.name, True, red)
    egh3_name_text_rect = egh3_name_text.get_rect()
    egh3_name_text_rect.center = (992,435)

# Ghost BOSS
if ghost_boss_hp > 0:
    ghost_boss_image = loadify(enemy7.img)
    ghost_boss_rect = ghost_boss_image.get_rect()
    ghost_boss_rect.center = (width//2 + 400, height//2)

    ebossgh_name_text = pygame.font.SysFont("Moncerat", 20)
    ebossgh_name_text = ebossgh_name_text.render(enemy7.name, True, red)
    ebossgh_name_text_rect = ebossgh_name_text.get_rect()
    ebossgh_name_text_rect.center = (900,height//2)

# Sceleton BOSS
if enemy_scelet_boss_hp > 0:
    scelet_boss_image = loadify(enemy1.img)
    scelet_boss_rect = scelet_boss_image.get_rect()
    scelet_boss_rect.center = (width//2 + 500, height//2 - 200)

    eboss_name_text = pygame.font.SysFont("Moncerat", 20)
    eboss_name_text = eboss_name_text.render(enemy1.name, True, red)
    eboss_name_text_rect = eboss_name_text.get_rect()
    eboss_name_text_rect.center = (900,435)

# Goblin
if goblin_hp > 0:
    goblin_image = loadify(enemy4.img)
    goblin_rect = goblin_image.get_rect()
    goblin_rect.center = (width//2 + 500, height//2 - 200)

    eg_name_text = pygame.font.SysFont("Moncerat", 20)
    eg_name_text = eg_name_text.render(enemy4.name, True, red)
    eg_name_text_rect = eg_name_text.get_rect()
    eg_name_text_rect.center = (992,435)

# Goblin 1
if goblin_hp1 > 0:
    goblin_image1 = loadify(enemy4.img)
    goblin_rect1 = goblin_image1.get_rect()
    goblin_rect1.center = (width//2 + 300, height//2 - 200)

    eg1_name_text = pygame.font.SysFont("Moncerat", 20)
    eg1_name_text = eg1_name_text.render(enemy4.name, True, red)
    eg1_name_text_rect = eg1_name_text.get_rect()
    eg1_name_text_rect.center = (992,435)

# Goblin 2
if goblin_hp2 > 0:
    goblin_image2 = loadify(enemy4.img)
    goblin_rect2 = goblin_image2.get_rect()
    goblin_rect2.center = (width//2 + 100, height//2 - 100)

    eg2_name_text = pygame.font.SysFont("Moncerat", 20)
    eg2_name_text = eg2_name_text.render(enemy4.name, True, red)
    eg2_name_text_rect = eg2_name_text.get_rect()
    eg2_name_text_rect.center = (992,435)

# Goblin 3
if goblin_hp3 > 0:
    goblin_image3 = loadify(enemy4.img)
    goblin_rect3 = goblin_image3.get_rect()
    goblin_rect3.center = (width//2 - 100, height//2 - 200)

    eg3_name_text = pygame.font.SysFont("Moncerat", 20)
    eg3_name_text = eg3_name_text.render(enemy4.name, True, red)
    eg3_name_text_rect = eg3_name_text.get_rect()
    eg3_name_text_rect.center = (width//2 - 100,435)

# Goblin BOSS
if goblin_boss_hp > 0:
    goblin_boss_image = loadify(enemy5.img)
    goblin_boss_rect = goblin_boss_image.get_rect()
    goblin_boss_rect.center = (width//2 + 400, height//2)

    eboss3_name_text = pygame.font.SysFont("Moncerat", 20)
    eboss3_name_text = eboss3_name_text.render(enemy5.name, True, red)
    eboss3_name_text_rect = eboss3_name_text.get_rect()
    eboss3_name_text_rect.center = (900,height//2)

#-----------------------------------------------------------------------------------------------#
# TEXTY 
custom1_font = pygame.font.SysFont("Helvetica", 60, 1.5)
custom1_text = custom1_font.render("WELCOME TO THE GAME", True, orange)
custom1_text_rect = custom1_text.get_rect()
custom1_text_rect.center = (width//2, height//2 - 339)

custom_end_font = pygame.font.SysFont("Helvetica", 60, 1.5)
custom_end_text = custom_end_font.render("GAME OVER", True, orange)
custom_end_text_rect = custom_end_text.get_rect()
custom_end_text_rect.center = (width//2, height//2 - 339)

custom_end1_font = pygame.font.SysFont("Helvetica", 60, 1.5)
custom_end1_text = custom_end1_font.render("YOU LOSE", True, red)
custom_end1_text_rect = custom_end1_text.get_rect()
custom_end1_text_rect.center = (width//2, height//2 + 300)

custom_end2_font = pygame.font.SysFont("Helvetica", 60, 1.5)
custom_end2_text = custom_end2_font.render("YOU WIN", True, yellow)
custom_end2_text_rect = custom_end2_text.get_rect()
custom_end2_text_rect.center = (width//2, height//2 + 300)
#-----------------------------------------------------------------------------------------------#
### MUSIC ###
#-----------------------------------------------------------------------------------------------#
# BACKGOUND MUSIC
if run_game == 0:
    pygame.mixer.Channel(5).play(pygame.mixer.Sound("music/home_background_music.wav"))
    pygame.mixer.Channel(5).set_volume(0.1)

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
# Backgrounds
    if enemy_spider == 0:
        screen.blit(home_background_img, home_background_img_rect)
    if run_game == 1 or enemy_spider > 0 or enemy_spider1 > 0 or enemy_spider2 > 0 or enemy_spider3 > 0 or enemy_spider_boss > 0:
        if scelet_hp > 0 or spider_hp1 > 0 or spider_hp2 > 0 or spider_hp3 > 0 or enemy_spider_boss_hp > 0:
            screen.blit(spider_background_img, spider_background_img_rect)
    if enemy_scelet > 0 or enemy_scelet1 > 0 or enemy_scelet2 > 0 or enemy_scelet3 > 0 or enemy_scelet_boss > 0:
        if scelet_hp > 0 or scelet1_hp > 0 or scelet2_hp > 0 or scelet3_hp > 0 or enemy_scelet_boss_hp > 0:
            screen.blit(skelet_background_img, skelet_background_img_rect)
    if enemy_goblin > 0 or enemy_goblin1 > 0 or enemy_goblin2 > 0 or enemy_goblin3 > 0 or enemy_goblin_boss > 0:
        if goblin_hp > 0 or goblin_hp1 > 0 or goblin_hp2 > 0 or goblin_hp3 > 0 or goblin_boss_hp > 0:
            screen.blit(goblin_background_img, goblin_background_img_rect)
    if enemy_ghost > 0 or enemy_ghost1 > 0 or enemy_ghost2 > 0 or enemy_ghost3 > 0 or enemy_ghost_boss > 0:
        if ghost_hp > 0 or ghost_hp1 > 0 or ghost_hp2 > 0 or ghost_hp3 > 0 or ghost_boss_hp > 0:
            screen.blit(ghost_background_img, ghost_background_img_rect)
    if ghost_boss_hp <= 0:
        screen.blit(home_background_img, home_background_img_rect)
    pygame.draw.rect(screen,grey,(3,3,126,66))

    # Text  + fill bez enemy
    if enemy_spider == 0:   
        pygame.draw.rect(screen,grey,(3,3,width//2 + 627,66))  
        screen.blit(custom1_text, custom1_text_rect)
        
    if run_game == 0:
        pygame.mixer.Channel(7).stop()
        # Button start
        if start_button.draw(screen):
            run_game = 1
    
    if run_game == 1 and player_human > 0 or player_archer > 0 or player_fmag > 0 or player_light > 0:
        pygame.mixer.Channel(5).stop()
        # Button exit   
        if exit_button.draw(screen):
            import sys
            import os
            python = sys.executable
            os.execl(python, python, * sys.argv)

    if run_game == 1 and player_human < 0 or player_archer < 0 or player_fmag < 0 or player_light < 0:
        pygame.mixer.Channel(5).stop()
        # Button exit   
        if exit_button.draw(screen):
            import sys
            import os
            python = sys.executable
            os.execl(python, python, * sys.argv)

    # START FIGHT MUSIC
    if run_game == 1 and keys[pygame.K_1]:
        pygame.mixer.Channel(6).play(pygame.mixer.Sound("sounds/human_hello.wav"))
        pygame.mixer.Channel(6).set_volume(0.01)
    if run_game == 1 and keys[pygame.K_2]and enemy_spider_boss_hp <= 0 and archer_hp >0:
        pygame.mixer.Channel(6).play(pygame.mixer.Sound("sounds/archer_hello.wav"))
        pygame.mixer.Channel(6).set_volume(0.05)
    if run_game == 1 and keys[pygame.K_3] and enemy_scelet_boss_hp <= 0 and fmag_hp >0:
        pygame.mixer.Channel(6).play(pygame.mixer.Sound("sounds/fire_hello.wav"))
        pygame.mixer.Channel(6).set_volume(0.01)
    if run_game == 1 and keys[pygame.K_4] and goblin_boss_hp <= 0 and light_hp >0:
        pygame.mixer.Channel(6).play(pygame.mixer.Sound("sounds/war_hello.wav"))
        pygame.mixer.Channel(6).set_volume(0.03)
#-----------------------------------------------------------------------------------------------#
# KONEC HRY
#-----------------------------------------------------------------------------------------------#

# PROHRA
    if enemy_ghost_boss > 0 and human_hp <= 0 and archer_hp <= 0 and fmag_hp <=0 and light_hp <= 0 and run_game == 1:
            pygame.mixer.Channel(4).stop()
            pygame.mixer.Channel(6).stop()
            pygame.mixer.Channel(5).play(pygame.mixer.Sound("music/end_background_music.wav"))
            pygame.mixer.Channel(5).set_volume(0.5)
    if human_hp <= 0 and archer_hp <= 0 and fmag_hp <=0 and light_hp <= 0 and run_game == 1:
        pygame.mixer.Channel(4).stop()
        pygame.mixer.Channel(6).stop()
        screen.blit(end_background_img, end_background_img_rect)
        pygame.draw.rect(screen,grey,(3,3,width//2 + 627,66))
        screen.blit(custom_end_text, custom_end_text_rect)
        screen.blit(custom_end1_text, custom_end1_text_rect)
        enemy_ghost_boss -= 1000
        str_enemy_ghost_boss = str(enemy_ghost_boss)
        try:
            f_enemy_ghost_boss = open("players_hp/enemy_ghost_boss.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_enemy_ghost_boss.write(str_enemy_ghost_boss)
        enemy_spider -= 1000
        str_enemy_spider = str(enemy_spider)
        try:
            f_enemy_spider = open("players/enemy_spider.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_enemy_spider.write(str_enemy_spider)
        # Button exit   
        if exit_button.draw(screen):
            import sys
            import os
            python = sys.executable
            os.execl(python, python, * sys.argv)
        pygame.draw.line(screen, black, (127,70),(127,0), 3)
        
# VÝHRA
    if enemy_spider > 0 and run_game == 1 and ghost_boss_hp <= 0:
            pygame.mixer.Channel(5).stop()
            pygame.mixer.Channel(3).play(pygame.mixer.Sound("music/home_background_music.wav"))
            pygame.mixer.Channel(3).set_volume(0.05)
    if ghost_boss_hp <= 0 and run_game == 1:
        pygame.mixer.Channel(5).stop()
        screen.blit(win_background_img, win_background_img_rect)
        pygame.draw.rect(screen,grey,(3,3,width//2 + 627,66))
        screen.blit(custom_end_text, custom_end_text_rect)
        screen.blit(custom_end2_text, custom_end2_text_rect)
        pygame.draw.rect(screen,grey,(3,3,width//2 - 144,66))
        pygame.draw.rect(screen,grey,(width//2 + 143,3,325,66))
        enemy_spider -= 1000
        str_enemy_spider = str(enemy_spider)
        try:
            f_enemy_spider = open("players/enemy_spider.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_enemy_spider.write(str_enemy_spider)
        light_hp -= 10000 # war
        str_light_hp = str(light_hp)
        try:
            f1 = open("players_hp/light_hp.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f1.write(str_light_hp)
        f1.close()
        archer_hp -= 10000 # arhcer
        str_archer_hp = str(archer_hp)
        try:
            f1 = open("players_hp/archer_hp.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f1.write(str_archer_hp)
        f1.close()
        human_hp -= 10000 # human
        str_human_hp = str(human_hp)
        try:
            f1 = open("players_hp/human_hp.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f1.write(str_human_hp)
        f1.close()
        fmag_hp -= 10000 # fmag
        str_fmag_hp = str(fmag_hp)
        try:
            f1 = open("players_hp/fmag_hp.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f1.write(str_fmag_hp)
        f1.close()
        # Button exit   
        if exit_button.draw(screen):
            import sys
            import os
            python = sys.executable
            os.execl(python, python, * sys.argv)
        pygame.draw.line(screen, black, (127,70),(127,0), 3)
         
# Portréty
    if enemy_spider > 0:
        if enemy_spider_boss_hp <= 0:
            if archer_hp > 0:
                screen.blit(archer_portret, archer_portret_rect)
            if archer_hp <= 0:
                screen.blit(archer_portret_dead, archer_portret_dead_rect)
        if enemy_spider_boss_hp > 0: 
            screen.blit(archer_portret_lock, archer_portret_lock_rect)

        if enemy_scelet_boss_hp <= 0:
            if fmag_hp > 0:
                screen.blit(fzard_portret, fzard_portret_rect)
            if fmag_hp <= 0:
                screen.blit(fzard_portret_dead, fzard_portret_dead_rect)
        if enemy_scelet_boss_hp > 0: 
            screen.blit(fzard_portret_lock, fzard_portret_lock_rect)

        if goblin_boss_hp <= 0:
            if light_hp > 0:
                screen.blit(light_portret, light_portret_rect)
            if light_hp <= 0:
                screen.blit(light_portret_dead, light_portret_dead_rect)
        if goblin_boss_hp > 0: 
            screen.blit(light_portret_lock, light_portret_lock_rect)

        if human_hp > 0:                 
            screen.blit(human_portret, human_portret_rect)
        if human_hp <= 0:                 
            screen.blit(human_portret_dead, human_portret_dead_rect)

# Spider Portal
    if enemy_spider > 0 or enemy_spider1 > 0 or enemy_spider2 > 0 or enemy_spider3 > 0:
        if scelet_hp > 0 or spider_hp1 > 0 or spider_hp2 > 0 or spider_hp3 > 0:
            screen.blit(s_portal_image,s_portal_image_rect)     
# Skelet Portal
    if enemy_scelet > 0 or enemy_scelet1 > 0 or enemy_scelet2 > 0 or enemy_scelet3 > 0:
        if scelet_hp > 0 or scelet1_hp > 0 or scelet2_hp > 0 or scelet3_hp > 0:
            screen.blit(portal_image,portal_image_rect)
# Goblin Portal
    if enemy_goblin > 0 or enemy_goblin1 > 0 or enemy_goblin2 > 0 or enemy_goblin3 > 0:
        if goblin_hp > 0 or goblin_hp1 > 0 or goblin_hp2 > 0 or goblin_hp3 > 0:
            screen.blit(g_portal_image,g_portal_image_rect)
# Ghost Portal
    if enemy_ghost > 0 or enemy_ghost1 > 0 or enemy_ghost2 > 0 or enemy_ghost3 > 0:
        if ghost_hp > 0 or ghost_hp1 > 0 or ghost_hp2 > 0 or ghost_hp3 > 0:
            screen.blit(gh_portal_image,gh_portal_image_rect)
        
# HP Ghost bosse
    customgh1_font = pygame.font.SysFont("Helvetica", 44)
    customgh2_font = pygame.font.SysFont("Helvetica", 44)
    customgh3_font = pygame.font.SysFont("Helvetica", 44)
    if enemy_ghost_boss > 0 and ghost_boss_hp >= 500:
        customgh1_text = customgh1_font.render("BOSS HP: " + f"{ghost_boss_hp}", True, green)
        customgh1_text_rect = customgh1_text.get_rect()
        customgh1_text_rect.center = (width//2, height//2 + 350)
        screen.blit(customgh1_text, customgh1_text_rect)
    if enemy_ghost_boss > 0 and ghost_boss_hp <= 499 and ghost_boss_hp >= 250:
        customgh2_text = customgh2_font.render("BOSS HP: " + f"{ghost_boss_hp}", True, yellow)
        customgh2_text_rect = customgh2_text.get_rect()
        customgh2_text_rect.center = (width//2, height//2 + 350)
        screen.blit(customgh2_text, customgh2_text_rect)
    if enemy_ghost_boss > 0 and ghost_boss_hp <= 249 and ghost_boss_hp > 0:
        customgh3_text = customgh3_font.render("BOSS HP: " + f"{ghost_boss_hp}", True, red)
        customgh3_text_rect = customgh3_text.get_rect()
        customgh3_text_rect.center = (width//2, height//2 + 350)
        screen.blit(customgh3_text, customgh3_text_rect)
    
# HP Scelet bosse
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

# HP Spider bosse
    custom5_font = pygame.font.SysFont("Helvetica", 44)
    custom6_font = pygame.font.SysFont("Helvetica", 44)
    custom7_font = pygame.font.SysFont("Helvetica", 44)
    if enemy_spider_boss > 0 and enemy_spider_boss_hp >= 100:
        custom5_text = custom5_font.render("BOSS HP: " + f"{enemy_spider_boss_hp}", True, green)
        custom5_text_rect = custom5_text.get_rect()
        custom5_text_rect.center = (width//2, height//2 + 350)
        screen.blit(custom5_text, custom5_text_rect)
    if enemy_spider_boss > 0 and enemy_spider_boss_hp <= 99 and enemy_spider_boss_hp >= 50:
        custom6_text = custom6_font.render("BOSS HP: " + f"{enemy_spider_boss_hp}", True, yellow)
        custom6_text_rect = custom6_text.get_rect()
        custom6_text_rect.center = (width//2, height//2 + 350)
        screen.blit(custom6_text, custom6_text_rect)
    if enemy_spider_boss > 0 and enemy_spider_boss_hp <= 49 and enemy_spider_boss_hp > 0:
        custom7_text = custom7_font.render("BOSS HP: " + f"{enemy_spider_boss_hp}", True, red)
        custom7_text_rect = custom7_text.get_rect()
        custom7_text_rect.center = (width//2, height//2 + 350)
        screen.blit(custom7_text, custom7_text_rect)

# HP Goblin bosse
    custom8_font = pygame.font.SysFont("Helvetica", 44)
    custom9_font = pygame.font.SysFont("Helvetica", 44)
    custom10_font = pygame.font.SysFont("Helvetica", 44)
    if enemy_goblin_boss > 0 and goblin_boss_hp >= 600:
        custom8_text = custom8_font.render("BOSS HP: " + f"{goblin_boss_hp}", True, green)
        custom8_text_rect = custom8_text.get_rect()
        custom8_text_rect.center = (width//2, height//2 + 350)
        screen.blit(custom8_text, custom8_text_rect)
    if enemy_goblin_boss > 0 and goblin_boss_hp <= 599 and goblin_boss_hp >= 300:
        custom9_text = custom9_font.render("BOSS HP: " + f"{goblin_boss_hp}", True, yellow)
        custom9_text_rect = custom9_text.get_rect()
        custom9_text_rect.center = (width//2, height//2 + 350)
        screen.blit(custom9_text, custom9_text_rect)
    if enemy_goblin_boss > 0 and goblin_boss_hp <= 299 and goblin_boss_hp > 0:
        custom10_text = custom10_font.render("BOSS HP: " + f"{goblin_boss_hp}", True, red)
        custom10_text_rect = custom10_text.get_rect()
        custom10_text_rect.center = (width//2, height//2 + 350)
        screen.blit(custom10_text, custom10_text_rect)


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

        if player_light > 0:
            player_light -= 10
            player_light_str = str(player_light)
            try:
                f_light = open("players/player_light.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f_light.write(player_light_str)
            f_light.close()
        
        if player_archer > 0:
            player_archer -= 10
            player_archer_str = str(player_archer)
            try:
                f_archer = open("players/player_archer.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f_archer.write(player_archer_str)
            f_archer.close()

# Načtení Fmága do pole
    if keys [pygame.K_3]:
        player_fmag += 1
        player_fmag_str = str(player_fmag)
        try:
            f_fmag = open("players/player_fmag.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_fmag.write(player_fmag_str)
        f_fmag.close()
        if player_light > 0:
            player_light -= 10
            player_light_str = str(player_light)
            try:
                f_light = open("players/player_light.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f_light.write(player_light_str)
            f_light.close()
        
        if player_human > 0:
            player_human -= 10
            player_human_str = str(player_human)
            try:
                f_human = open("players/player_human.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f_human.write(player_human_str)
            f_human.close()
        
        if player_archer > 0:
            player_archer -= 10
            player_archer_str = str(player_archer)
            try:
                f_archer = open("players/player_archer.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f_archer.write(player_archer_str)
            f_archer.close()

# Načtení Wmága do pole
    if keys [pygame.K_4]:
        player_light += 1
        player_light_str = str(player_light)
        try:
            f_light = open("players/player_light.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_light.write(player_light_str)
        f_light.close()
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
        
        if player_archer > 0:
            player_archer -= 10
            player_archer_str = str(player_archer)
            try:
                f_archer = open("players/player_archer.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f_archer.write(player_archer_str)
            f_archer.close()

# Načtení Archera do pole
    if keys [pygame.K_2]:
        player_archer += 1
        player_archer_str = str(player_archer)
        try:
            f_archer = open("players/player_archer.txt","w")
        except FileNotFoundError:
                print("Soubor nebyl nalezen")
        text = f_archer.write(player_archer_str)
        f_archer.close()
        if player_light > 0:
            player_light -= 10
            player_light_str = str(player_light)
            try:
                f_light = open("players/player_light.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f_light.write(player_light_str)
            f_light.close()

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

    def update_enemy_count(file_path, enemy_count):
        enemy_count += 1
        enemy_count_str = str(enemy_count)
        try:
            with open(file_path, "w") as f:
                f.write(enemy_count_str)
        except FileNotFoundError:
            print("Soubor nebyl nalezen")
        return enemy_count

    # Načte příšery
    if run_game == 1:
        # Spider
        enemy_spider = update_enemy_count("players/enemy_spider.txt", enemy_spider)
    # Spider 1 + 2 + 3
    if spider_hp <= 0:
        enemy_spider1 = update_enemy_count("players/enemy_spider1.txt", enemy_spider1)
        enemy_spider2 = update_enemy_count("players/enemy_spider2.txt", enemy_spider2)
        enemy_spider3 = update_enemy_count("players/enemy_spider3.txt", enemy_spider3)
    # Spider BOSS
    if spider_hp <= 0 and spider_hp1 <= 0 and spider_hp2 <= 0 and spider_hp3 <= 0:
        enemy_spider_boss = update_enemy_count("players/enemy_spider_boss.txt", enemy_spider_boss)
        
        
    if enemy_spider_boss_hp <= 0 and run_game == 1:
        # Skeleton
        enemy_scelet = update_enemy_count("players/enemy_scelet.txt", enemy_scelet)
        # Skeleton 1 + 2 + 3
        if scelet_hp <= 0:
            enemy_scelet1 = update_enemy_count("players/enemy_scelet1.txt", enemy_scelet1)
            enemy_scelet2 = update_enemy_count("players/enemy_scelet2.txt", enemy_scelet2)
            enemy_scelet3 = update_enemy_count("players/enemy_scelet3.txt", enemy_scelet3)
        # Skeleton BOSS
        if scelet_hp <= 0 and scelet1_hp <= 0 and scelet2_hp <= 0 and scelet3_hp <= 0:
            enemy_scelet_boss = update_enemy_count("players/enemy_scelet_boss.txt", enemy_scelet_boss)


    if enemy_scelet_boss_hp <= 0 and run_game == 1:
        # Goblin
        enemy_goblin = update_enemy_count("players/enemy_goblin.txt", enemy_goblin)
        # Goblin 1 + 2 + 3
        if goblin_hp <= 0:
            enemy_goblin1 = update_enemy_count("players/enemy_goblin1.txt", enemy_goblin1)
            enemy_goblin2 = update_enemy_count("players/enemy_goblin2.txt", enemy_goblin2)
            enemy_goblin3 = update_enemy_count("players/enemy_goblin3.txt", enemy_goblin3)
        # Goblin BOSS
        if goblin_hp <= 0 and goblin_hp1 <= 0 and goblin_hp2 <= 0 and goblin_hp3 <= 0:
            enemy_goblin_boss = update_enemy_count("players/enemy_goblin_boss.txt", enemy_goblin_boss)


    if goblin_boss_hp <= 0 and run_game == 1:
        # Ghost
        enemy_ghost = update_enemy_count("players/enemy_ghost.txt", enemy_ghost)
        # Ghost 1 + 2 + 3
        if ghost_hp <= 0:
            enemy_ghost1 = update_enemy_count("players/enemy_ghost1.txt", enemy_ghost1)
            enemy_ghost2 = update_enemy_count("players/enemy_ghost2.txt", enemy_ghost2)
            enemy_ghost3 = update_enemy_count("players/enemy_ghost3.txt", enemy_ghost3)
        # Ghost BOSS
        if ghost_hp <= 0 and ghost_hp1 <= 0 and ghost_hp2 <= 0 and ghost_hp3 <= 0:
            enemy_ghost_boss = update_enemy_count("players/enemy_ghost_boss.txt", enemy_ghost_boss)
   
# Human
    if player_human > 0 and enemy_spider > 0:
        if human_hp > 0:
            hp0_text = pygame.font.SysFont("Moncerat", 18)
        if human_hp >= 600:
            hp0_text = hp0_text.render("HP: " + f"{human_hp}", True, green)
        if human_hp >= 350 and human_hp <= 599:
            hp0_text = hp0_text.render("HP: " + f"{human_hp}", True, yellow)
        if human_hp <= 349 and human_hp > 0:
            hp0_text = hp0_text.render("HP: " + f"{human_hp}", True, red)
        if human_hp <= 0:
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
        if keys [pygame.K_w] and human_rect.top > 100 and human2_rect.top > 100:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/steps.wav'))
            pygame.mixer.Channel(0).set_volume(0.2)
            human_move_image_rect.y = human_move_image_rect.y - human_distance
            human_move_image2_rect.y = human_move_image2_rect.y - human_distance
            human_rect.y = human_rect.y - human_distance
            human2_rect.y = human2_rect.y - human_distance
            name0_text_rect.y = name0_text_rect.y - human_distance  
            hp0_text_rect.y = hp0_text_rect.y - human_distance
        elif keys [pygame.K_s] and human_rect.bottom < height - 120 and human2_rect.bottom < height - 120:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/steps.wav'))
            pygame.mixer.Channel(0).set_volume(0.2)
            human_move_image_rect.y = human_move_image_rect.y + human_distance
            human_move_image2_rect.y = human_move_image2_rect.y + human_distance
            human_rect.y = human_rect.y + human_distance
            human2_rect.y = human2_rect.y + human_distance
            name0_text_rect.y = name0_text_rect.y + human_distance
            hp0_text_rect.y = hp0_text_rect.y + human_distance
        elif keys [pygame.K_a] and human_rect.left > 25 and human2_rect.left > 25:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/steps.wav'))
            pygame.mixer.Channel(0).set_volume(0.2)
            human_move_image_rect.x = human_move_image_rect.x - human_distance
            human_move_image2_rect.x = human_move_image2_rect.x - human_distance
            human_rect.x = human_rect.x - human_distance
            human2_rect.x = human2_rect.x - human_distance
            name0_text_rect.x = name0_text_rect.x - human_distance
            hp0_text_rect.x = hp0_text_rect.x - human_distance  
            mirror = 1
        elif keys [pygame.K_d] and human_rect.right > 0 and human2_rect.right < width:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/steps.wav'))
            pygame.mixer.Channel(0).set_volume(0.2)
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
                pygame.mixer.Channel(2).play(pygame.mixer.Sound('sounds/human_attack.wav'))
                pygame.mixer.Channel(2).set_volume(0.01)
                human_attack2_rect.center = (human2_rect.x - 25 ,human2_rect.y + 45)
                screen.blit(human_attack2_image,human_attack2_rect)
            
        if human_attack == 2 and keys [pygame.K_SPACE]:
                pygame.mixer.Channel(2).play(pygame.mixer.Sound('sounds/human_attack.wav'))
                pygame.mixer.Channel(2).set_volume(0.01)        
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
        if fmag_hp <= 0:
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
        if keys [pygame.K_w] and fzard_rect.top > 100 and fzard2_rect.top > 100:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/steps.wav'))
            pygame.mixer.Channel(0).set_volume(0.2)
            fzard_rect.y = fzard_rect.y - fmag_distance
            fzard2_rect.y = fzard2_rect.y - fmag_distance
            name1_text_rect.y = name1_text_rect.y - fmag_distance 
            hp1_text_rect.y = hp1_text_rect.y - fmag_distance
        elif keys [pygame.K_s] and fzard_rect.bottom < height - 120 and fzard2_rect.bottom < height - 120:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/steps.wav'))
            pygame.mixer.Channel(0).set_volume(0.2)
            fzard_rect.y = fzard_rect.y + fmag_distance
            fzard2_rect.y = fzard2_rect.y + fmag_distance
            name1_text_rect.y = name1_text_rect.y + fmag_distance
            hp1_text_rect.y = hp1_text_rect.y + fmag_distance
        elif keys [pygame.K_a] and fzard_rect.left > 25 and fzard2_rect.left > 25:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/steps.wav'))
            pygame.mixer.Channel(0).set_volume(0.2)
            fzard_rect.x = fzard_rect.x - fmag_distance
            fzard2_rect.x = fzard2_rect.x - fmag_distance
            name1_text_rect.x = name1_text_rect.x - fmag_distance
            hp1_text_rect.x = hp1_text_rect.x - fmag_distance   
            mirror = 1
        elif keys [pygame.K_d] and fzard_rect.right > 0 and fzard2_rect.right < width:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/steps.wav'))
            pygame.mixer.Channel(0).set_volume(0.2)
            fzard_rect.x = fzard_rect.x +fmag_distance
            fzard2_rect.x = fzard2_rect.x + fmag_distance
            name1_text_rect.x = name1_text_rect.x + fmag_distance
            hp1_text_rect.x = hp1_text_rect.x + fmag_distance
            mirror = 0 

        elif keys [pygame.K_SPACE] and mirror == 1:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound('sounds/fireball.wav'))
            pygame.mixer.Channel(3).set_volume(0.03)
            fball2_rect.center = (fzard2_rect.x + 20,fzard2_rect.y + 35)
            fire_attack = 1
        elif keys [pygame.K_SPACE] and mirror == 0:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound('sounds/fireball.wav'))
            pygame.mixer.Channel(3).set_volume(0.03)
            fball_rect.center = (fzard_rect.x + 100,fzard_rect.y + 35)
            fire_attack = 2
            
        if fire_attack == 1:
            screen.blit(fball2_image,fball2_rect)
            fball2_rect.x += attack_1x * fball_speed
        if fire_attack == 2:
            screen.blit(fball_image,fball_rect)
            fball_rect.x += attack_x * fball_speed 

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
    if player_light > 0 and goblin_boss_hp <= 0:
        if light_hp > 0:
            hp2_text = pygame.font.SysFont("Moncerat", 18)
        if light_hp >= 75:
            hp2_text = hp2_text.render("HP: " + f"{light_hp}", True, green)
        if light_hp <= 74 and light_hp >= 40:
            hp2_text = hp2_text.render("HP: " + f"{light_hp}", True, yellow)
        if light_hp <= 39 and light_hp > 0:
            hp2_text = hp2_text.render("HP: " + f"{light_hp}", True, red)
        if light_hp <= 0:
            player_light -= 100000000
            player_light_str = str(player_light)
            try:
                f_light = open("players/player_light.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f_light.write(player_light_str)
            f_light.close()
        hp2_text_rect = hp2_text.get_rect()
        hp2_text_rect.center = (light_rect.x + 80, light_rect.y + 120)  
        keys = pygame.key.get_pressed()
        if keys [pygame.K_w] and light_rect.top > 100 and light2_rect.top > 100:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/steps.wav'))
            pygame.mixer.Channel(0).set_volume(0.2)
            light_move_image_rect.y = light_move_image_rect.y - light_distance
            light_move_image2_rect.y = light_move_image2_rect.y - light_distance
            light_rect.y = light_rect.y - light_distance
            light2_rect.y = light2_rect.y - light_distance
            name2_text_rect.y = name2_text_rect.y - light_distance
            hp2_text_rect.y = hp2_text_rect.y - light_distance
        elif keys [pygame.K_s] and light_rect.bottom < height - 120 and light2_rect.bottom < height - 120:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/steps.wav'))
            pygame.mixer.Channel(0).set_volume(0.2)
            light_move_image_rect.y = light_move_image_rect.y + light_distance
            light_move_image2_rect.y = light_move_image2_rect.y + light_distance
            light_rect.y = light_rect.y + light_distance
            light2_rect.y = light2_rect.y + light_distance
            name2_text_rect.y = name2_text_rect.y + light_distance
            hp2_text_rect.y = hp2_text_rect.y + light_distance
        elif keys [pygame.K_a] and light_rect.left > 25 and light2_rect.left > 25:  
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/steps.wav'))
            pygame.mixer.Channel(0).set_volume(0.2)               
            light_move_image_rect.x = light_move_image_rect.x - light_distance
            light_rect.x = light_rect.x - light_distance
            light2_rect.x = light2_rect.x - light_distance
            name2_text_rect.x = name2_text_rect.x - light_distance
            hp2_text_rect.x = hp2_text_rect.x - light_distance
            mirror = 1
        elif keys [pygame.K_d] and light_rect.right > 0 and light2_rect.right < width:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/steps.wav'))
            pygame.mixer.Channel(0).set_volume(0.2)
            light_move_image_rect.x = light_move_image_rect.x + light_distance
            light_rect.x = light_rect.x + light_distance
            light2_rect.x = light2_rect.x + light_distance
            name2_text_rect.x = name2_text_rect.x + light_distance
            hp2_text_rect.x = hp2_text_rect.x + light_distance
            mirror = 0       
              
        elif keys [pygame.K_SPACE] and mirror == 1:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound('sounds/war_attack.wav'))
            pygame.mixer.Channel(3).set_volume(0.1)
            light_attack2_rect.center = (light2_rect.x + 10,light2_rect.y + 70)
            wire_attack = 1
        elif keys [pygame.K_SPACE] and mirror == 0:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound('sounds/war_attack.wav'))
            pygame.mixer.Channel(3).set_volume(0.1)
            light_attack_rect.center = (light_rect.x + 125,light_rect.y + 70)
            wire_attack = 2
        
        if wire_attack == 1:
            screen.blit(light_attack2_image,light_attack2_rect)
            light_attack2_rect.x += attack_1x * light_attack_speed
        if wire_attack == 2:
            screen.blit(light_attack_image,light_attack_rect)
            light_attack_rect.x += attack_x * light_attack_speed  

        if ghost_hp1 <= 0 and ghost_hp2 <= 0 and ghost_hp3 <= 0 :
            wire_attack == 0
              
        if mirror == 0:
            if keys [pygame.K_d] or keys [pygame.K_w] or keys [pygame.K_s]:
                light_move_image_rect.center = (light2_rect.x + 80 ,light2_rect.y + 50)
                screen.blit(light_move_image,light_move_image_rect)
                screen.blit(name2_text,name2_text_rect)
                screen.blit(hp2_text,hp2_text_rect)
            else:
                screen.blit(light_image,light_rect)
                screen.blit(name2_text,name2_text_rect)
                screen.blit(hp2_text,hp2_text_rect)

        if mirror == 1:
            if keys [pygame.K_a] or keys [pygame.K_w] or keys [pygame.K_s]: 
                light_move_image2_rect.center = (light2_rect.x + 80 ,light2_rect.y + 50)
                screen.blit(light_move_image2,light_move_image2_rect)                
                screen.blit(name2_text,name2_text_rect)
                screen.blit(hp2_text,hp2_text_rect)
            else:
                screen.blit(light2_image,light2_rect)
                screen.blit(name2_text,name2_text_rect)
                screen.blit(hp2_text,hp2_text_rect)

# Archer
    if player_archer > 0 and enemy_spider_boss_hp <= 0:  
        hp3_text = pygame.font.SysFont("Moncerat", 18)
        if archer_hp >= 125:
            hp3_text = hp3_text.render("HP: " + f"{archer_hp}", True, green)        
        if archer_hp <= 124 and archer_hp >= 80:
            hp3_text = hp3_text.render("HP: " + f"{archer_hp}", True, yellow)     
        if archer_hp <= 79 and archer_hp > 0:
            hp3_text = hp3_text.render("HP: " + f"{archer_hp}", True, red)
        if archer_hp <= 0:
            hp3_text = hp3_text.render("HP: " + f"{archer_hp}", True, red)
            player_archer -= 100000000
            player_archer_str = str(player_archer)
            try:
                f_archer = open("players/player_archer.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f_archer.write(player_archer_str)
            f_archer.close()
        hp3_text_rect = hp3_text.get_rect()
        hp3_text_rect.center = (archer_rect.x + 25, archer_rect.y + 135)
        keys = pygame.key.get_pressed()
        if keys [pygame.K_w] and archer_rect.top > 100 and archer2_rect.top > 100:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/steps.wav'))
            pygame.mixer.Channel(0).set_volume(0.2)         
            archer_move_image_rect.y = archer_move_image_rect.y - archer_distance
            archer_move_image2_rect.y = archer_move_image2_rect.y - archer_distance
            archer_rect.y = archer_rect.y - archer_distance
            archer2_rect.y = archer2_rect.y - archer_distance
            name3_text_rect.y = name3_text_rect.y - archer_distance
            hp3_text_rect.y = hp3_text_rect.y - archer_distance
        elif keys [pygame.K_s] and archer_rect.bottom < height - 120 and archer2_rect.bottom < height - 120:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/steps.wav'))
            pygame.mixer.Channel(0).set_volume(0.2)     
            archer_move_image_rect.y = archer_move_image_rect.y + archer_distance
            archer_move_image2_rect.y = archer_move_image2_rect.y + archer_distance
            archer_rect.y = archer_rect.y + archer_distance
            archer2_rect.y = archer2_rect.y + archer_distance
            name3_text_rect.y = name3_text_rect.y + archer_distance
            hp3_text_rect.y = hp3_text_rect.y + archer_distance
        elif keys [pygame.K_a] and archer_rect.left > 25 and archer2_rect.left > 25: 
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/steps.wav'))
            pygame.mixer.Channel(0).set_volume(0.2)
            archer_move_image_rect.x = archer_move_image_rect.x - archer_distance
            archer_rect.x = archer_rect.x - archer_distance
            archer2_rect.x = archer2_rect.x - archer_distance
            name3_text_rect.x = name3_text_rect.x - archer_distance
            hp3_text_rect.x = hp3_text_rect.x - archer_distance
            mirror = 1
        elif keys [pygame.K_d] and archer_rect.right > 0 and archer2_rect.right < width:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/steps.wav'))
            pygame.mixer.Channel(0).set_volume(0.2)
            archer_move_image_rect.x = archer_move_image_rect.x + archer_distance
            archer_rect.x = archer_rect.x + archer_distance
            archer2_rect.x = archer2_rect.x + archer_distance
            name3_text_rect.x = name3_text_rect.x + archer_distance
            hp3_text_rect.x = hp3_text_rect.x + archer_distance
            mirror = 0       

        elif keys [pygame.K_SPACE] and mirror == 1:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('sounds/arrow.wav'))
            pygame.mixer.Channel(1).set_volume(0.5)
            
            arrow2_rect.center = (archer2_rect.x + 30,archer2_rect.y + 55)
            arrow_attack = 1
        elif keys [pygame.K_SPACE] and mirror == 0:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('sounds/arrow.wav'))
            pygame.mixer.Channel(1).set_volume(0.5)
            
            arrow_rect.center = (archer_rect.x + 55,archer_rect.y + 55)
            arrow_attack = 2
        
        if arrow_attack == 1:
            screen.blit(arrow2_image,arrow2_rect)
            arrow2_rect.x += attack_1x * archer_attack_speed
        if arrow_attack == 2:
            screen.blit(arrow_image,arrow_rect)
            arrow_rect.x += attack_x * archer_attack_speed   

        if arrow_rect.right > 0 or arrow2_rect.right < width or arrow_rect.left > 0 or arrow2_rect.left < width:
            arrow_attack == 0
              
        if mirror == 0:
            if keys [pygame.K_d] or keys [pygame.K_w] or keys [pygame.K_s]:
                archer_move_image_rect.center = (archer_rect.x + 35 ,archer_rect.y + 50)
                screen.blit(archer_move_image,archer_move_image_rect)
                screen.blit(name3_text,name3_text_rect)
                screen.blit(hp3_text,hp3_text_rect)
            else:
                screen.blit(archer_image,archer_rect)
                screen.blit(name3_text,name3_text_rect)
                screen.blit(hp3_text,hp3_text_rect)

        if mirror == 1:
            if keys [pygame.K_a] or keys [pygame.K_w] or keys [pygame.K_s]: 
                archer_move_image2_rect.center = (archer2_rect.x +35 ,archer2_rect.y +50)
                screen.blit(archer_move_image2,archer_move_image2_rect)                
                screen.blit(name3_text,name3_text_rect)
                screen.blit(hp3_text,hp3_text_rect)
            else:
                screen.blit(archer2_image,archer2_rect)
                screen.blit(name3_text,name3_text_rect)
                screen.blit(hp3_text,hp3_text_rect)

    # Spirder
    if enemy_spider > 0:
        hp_spider_text = pygame.font.SysFont("Moncerat", 18)
        if spider_hp > 0:      
            hp_spider_text = hp_spider_text.render("HP: " + f"{spider_hp}", True, white)
            hp_spider_text_rect = hp_spider_text.get_rect()
            hp_spider_text_rect.center = (spider_rect.x + 30, spider_rect.y + 40)
            screen.blit(hp_spider_text,hp_spider_text_rect)
        e9_name_text_rect.center = (spider_rect.x + 30, spider_rect.y + 50)
        if spider_hp > 0:
            screen.blit(spider_image,spider_rect)
            screen.blit(e9_name_text,e9_name_text_rect)
        spider_rect.x += spider_x * spider_speed
        spider_rect.y += spider_y * spider_speed
        if spider_rect.left < 100 or spider_rect.left > width - 120:
            spider_x = -1 * spider_x
        elif spider_rect.top < 75 or spider_rect.bottom > height - 120:
            spider_y = -1 * spider_y
        if spider_rect.left < 130: 
            spider_image = loadify(enemy2.img2)         
        if spider_rect.left >= 1000: 
            spider_image = loadify(enemy2.img)

    # Spirder 1
    if enemy_spider1 > 0:
        hp_spider1_text = pygame.font.SysFont("Moncerat", 18)
        if spider_hp1 > 0:      
            hp_spider1_text = hp_spider1_text.render("HP: " + f"{spider_hp1}", True, white)
            hp_spider1_text_rect = hp_spider1_text.get_rect()
            hp_spider1_text_rect.center = (spider_rect1.x + 30, spider_rect1.y + 40)
            screen.blit(hp_spider1_text,hp_spider1_text_rect)
        e11_name_text_rect.center = (spider_rect1.x + 30, spider_rect1.y + 50)
        if spider_hp1 > 0:
            screen.blit(spider_image1,spider_rect1)
            screen.blit(e11_name_text,e11_name_text_rect)
        spider_rect1.x += spider1_x * spider_speed
        spider_rect1.y += spider1_y * spider_speed
        if spider_rect1.left < 100 or spider_rect1.left > width - 120:
            spider1_x = -1 * spider1_x
        elif spider_rect1.top < 75 or spider_rect1.bottom > height - 120:
            spider1_y = -1 * spider1_y
        if spider_rect1.left < 130: 
            spider_image1 = loadify(enemy2.img2)         
        if spider_rect1.left >= 1000: 
            spider_image1 = loadify(enemy2.img)

    # Spirder 2
    if enemy_spider2 > 0:
        hp_spider2_text = pygame.font.SysFont("Moncerat", 18)
        if spider_hp2 > 0:      
            hp_spider2_text = hp_spider2_text.render("HP: " + f"{spider_hp2}", True, white)
            hp_spider2_text_rect = hp_spider2_text.get_rect()
            hp_spider2_text_rect.center = (spider_rect2.x + 30, spider_rect2.y + 40)
            screen.blit(hp_spider2_text,hp_spider2_text_rect)
        e9_name_text_rect.center = (spider_rect2.x + 30, spider_rect2.y + 50)
        if spider_hp2 > 0:
            screen.blit(spider_image2,spider_rect2)
            screen.blit(e9_name_text,e9_name_text_rect)
        spider_rect2.x += spider2_x * spider_speed
        spider_rect2.y += spider2_y * spider_speed
        if spider_rect2.left < 100 or spider_rect2.left > width - 120:
            spider2_x = -1 * spider2_x
        elif spider_rect2.top < 75 or spider_rect2.bottom > height - 120:
            spider2_y = -1 * spider2_y
        if spider_rect2.left < 130: 
            spider_image2 = loadify(enemy2.img2)         
        if spider_rect2.left >= 1000: 
            spider_image2 = loadify(enemy2.img)

    # Spirder 3
    if enemy_spider3 > 0:
        hp_spider3_text = pygame.font.SysFont("Moncerat", 18)
        if spider_hp3 > 0:      
            hp_spider3_text = hp_spider3_text.render("HP: " + f"{spider_hp3}", True, white)
            hp_spider3_text_rect = hp_spider3_text.get_rect()
            hp_spider3_text_rect.center = (spider_rect3.x + 30, spider_rect3.y + 40)
            screen.blit(hp_spider3_text,hp_spider3_text_rect)
        e12_name_text_rect.center = (spider_rect3.x + 30, spider_rect3.y + 50)
        if spider_hp3 > 0:
            screen.blit(spider_image3,spider_rect3)
            screen.blit(e12_name_text,e12_name_text_rect)
        spider_rect3.x += spider3_x * spider_speed
        spider_rect3.y += spider3_y * spider_speed
        if spider_rect3.left < 100 or spider_rect3.left > width - 120:
            spider3_x = -1 * spider3_x
        elif spider_rect3.top < 75 or spider_rect3.bottom > height - 120:
            spider3_y = -1 * spider3_y
        if spider_rect3.left < 130: 
            spider_image3 = loadify(enemy2.img2)         
        if spider_rect3.left >= 1000: 
            spider_image3 = loadify(enemy2.img)

# Spider BOSS
    if enemy_spider_boss > 0:
        hpboss2_text = pygame.font.SysFont("Moncerat", 18)
        if enemy_spider_boss_hp > 0:      
            hpboss2_text = hpboss2_text.render("HP: " + f"{enemy_spider_boss_hp}", True, white)
            hpboss2_text_rect = hpboss2_text.get_rect()
            hpboss2_text_rect.center = (spider_boss_rect.x + 35, spider_boss_rect.y + 80)
            screen.blit(hpboss2_text,hpboss2_text_rect)
        eboss2_name_text_rect.center = (spider_boss_rect.x + 35, spider_boss_rect.y + 90)
        if enemy_spider_boss_hp > 0:
            screen.blit(spider_boss_image,spider_boss_rect)
            screen.blit(eboss2_name_text,eboss2_name_text_rect)
        spider_boss_rect.x += spider_boss_x * spider_boss_speed
        spider_boss_rect.y += spider_boss_y * spider_boss_speed
        if spider_boss_rect.left < 100 or spider_boss_rect.left > width - 120:
            spider_boss_x = -1 * spider_boss_x
        elif spider_boss_rect.top < 75 or spider_boss_rect.bottom > height - 120:
            spider_boss_y = -1 * spider_boss_y

        if spider_boss_rect.left < 130: 
            spider_boss_image = loadify(enemy3.img2)
            
        if spider_boss_rect.left >= 1000: 
            spider_boss_image = loadify(enemy3.img)
        if spider_boss_rect.colliderect(s_portal_image_rect) and enemy_spider_boss_hp > 0:
            pygame.mixer.Channel(7).play(pygame.mixer.Sound("sounds/spider.wav"))
            pygame.mixer.Channel(7).set_volume(0.04)
        
    # Skeleton
    if enemy_scelet > 0:
        hp3_text = pygame.font.SysFont("Moncerat", 18)
        if scelet_hp > 0:      
            hp3_text = hp3_text.render("HP: " + f"{scelet_hp}", True, white)
            hp3_text_rect = hp3_text.get_rect()
            hp3_text_rect.center = (scelet_rect.x + 30, scelet_rect.y + 125)
            screen.blit(hp3_text,hp3_text_rect)
        e8_name_text_rect.center = (scelet_rect.x + 30, scelet_rect.y + 110)
        if scelet_hp > 0:
            screen.blit(scelet_image,scelet_rect)
            screen.blit(e8_name_text,e8_name_text_rect)
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
        
        if scelet_boss_rect.colliderect(portal_image_rect) and enemy_scelet_boss_hp > 0:
            pygame.mixer.Channel(7).play(pygame.mixer.Sound("sounds/skelet.wav"))
            pygame.mixer.Channel(7).set_volume(0.1)

    # Goblin
    if enemy_goblin > 0:
        hp_goblin_text = pygame.font.SysFont("Moncerat", 18)
        if goblin_hp > 0:      
            hp_goblin_text = hp_goblin_text.render("HP: " + f"{goblin_hp}", True, white)
            hp_goblin_text_rect = hp_goblin_text.get_rect()
            hp_goblin_text_rect.center = (goblin_rect.x + 25, goblin_rect.y + 95)
            screen.blit(hp_goblin_text,hp_goblin_text_rect)
        eg_name_text_rect.center = (goblin_rect.x + 25, goblin_rect.y + 105)
        if goblin_hp > 0:
            screen.blit(goblin_image,goblin_rect)
            screen.blit(eg_name_text,eg_name_text_rect)
        goblin_rect.x += goblin_x * goblin_speed
        goblin_rect.y += goblin_y * goblin_speed
        if goblin_rect.left < 100 or goblin_rect.left > width - 120:
            goblin_x = -1 * goblin_x
        elif goblin_rect.top < 75 or goblin_rect.bottom > height - 120:
            goblin_y = -1 * goblin_y
        if goblin_rect.left < 130: 
            goblin_image = loadify(enemy4.img2)         
        if goblin_rect.left >= 1000: 
            goblin_image = loadify(enemy4.img)
    
    # Goblin 1
    if enemy_goblin1 > 0:
        hp_goblin1_text = pygame.font.SysFont("Moncerat", 18)
        if goblin_hp1 > 0:      
            hp_goblin1_text = hp_goblin1_text.render("HP: " + f"{goblin_hp1}", True, white)
            hp_goblin1_text_rect = hp_goblin1_text.get_rect()
            hp_goblin1_text_rect.center = (goblin_rect1.x + 25, goblin_rect1.y + 95)
            screen.blit(hp_goblin1_text,hp_goblin1_text_rect)
        eg1_name_text_rect.center = (goblin_rect1.x + 25, goblin_rect1.y + 105)
        if goblin_hp1 > 0:
            screen.blit(goblin_image1,goblin_rect1)
            screen.blit(eg1_name_text,eg1_name_text_rect)
        goblin_rect1.x += goblin1_x * goblin_speed
        goblin_rect1.y += goblin1_y * goblin_speed
        if goblin_rect1.left < 100 or goblin_rect1.left > width - 120:
            goblin1_x = -1 * goblin1_x
        elif goblin_rect1.top < 75 or goblin_rect1.bottom > height - 120:
            goblin1_y = -1 * goblin1_y
        if goblin_rect1.left < 130: 
            goblin_image1 = loadify(enemy4.img2)         
        if goblin_rect1.left >= 1000: 
            goblin_image1 = loadify(enemy4.img)

    # Goblin 2
    if enemy_goblin2 > 0:
        hp_goblin2_text = pygame.font.SysFont("Moncerat", 18)
        if goblin_hp2 > 0:      
            hp_goblin2_text = hp_goblin2_text.render("HP: " + f"{goblin_hp2}", True, white)
            hp_goblin2_text_rect = hp_goblin2_text.get_rect()
            hp_goblin2_text_rect.center = (goblin_rect2.x + 25, goblin_rect2.y + 95)
            screen.blit(hp_goblin2_text,hp_goblin2_text_rect)
        eg2_name_text_rect.center = (goblin_rect2.x + 25, goblin_rect2.y + 105)
        if goblin_hp2 > 0:
            screen.blit(goblin_image2,goblin_rect2)
            screen.blit(eg2_name_text,eg2_name_text_rect)
        goblin_rect2.x += goblin2_x * goblin_speed
        goblin_rect2.y += goblin2_y * goblin_speed
        if goblin_rect2.left < 100 or goblin_rect2.left > width - 120:
            goblin2_x = -1 * goblin2_x
        elif goblin_rect2.top < 75 or goblin_rect2.bottom > height - 120:
            goblin2_y = -1 * goblin2_y
        if goblin_rect2.left < 130: 
            goblin_image2 = loadify(enemy4.img2)         
        if goblin_rect2.left >= 1000: 
            goblin_image2 = loadify(enemy4.img)
    
    # Goblin 3
    if enemy_goblin3 > 0:
        hp_goblin3_text = pygame.font.SysFont("Moncerat", 18)
        if goblin_hp3 > 0:      
            hp_goblin3_text = hp_goblin3_text.render("HP: " + f"{goblin_hp3}", True, white)
            hp_goblin3_text_rect = hp_goblin3_text.get_rect()
            hp_goblin3_text_rect.center = (goblin_rect3.x + 25, goblin_rect3.y + 95)
            screen.blit(hp_goblin3_text,hp_goblin3_text_rect)
        eg3_name_text_rect.center = (goblin_rect3.x + 25, goblin_rect3.y + 105)
        if goblin_hp3 > 0:
            screen.blit(goblin_image3,goblin_rect3)
            screen.blit(eg3_name_text,eg3_name_text_rect)
        goblin_rect3.x += goblin3_x * goblin_speed
        goblin_rect3.y += goblin3_y * goblin_speed
        if goblin_rect3.left < 100 or goblin_rect3.left > width - 120:
            goblin3_x = -1 * goblin3_x
        elif goblin_rect3.top < 75 or goblin_rect3.bottom > height - 120:
            goblin3_y = -1 * goblin3_y
        if goblin_rect3.left < 130: 
            goblin_image3 = loadify(enemy4.img2)         
        if goblin_rect3.left >= 1000: 
            goblin_image3 = loadify(enemy4.img)
    
    # Goblin BOSS
    if enemy_goblin_boss > 0:
        hp_goblin_boss_text = pygame.font.SysFont("Moncerat", 18)
        if goblin_boss_hp > 0:      
            hp_goblin_boss_text = hp_goblin_boss_text.render("HP: " + f"{goblin_boss_hp}", True, white)
            hp_goblin_boss_text_rect = hp_goblin_boss_text.get_rect()
            hp_goblin_boss_text_rect.center = (goblin_boss_rect.x + 105, goblin_boss_rect.y + 255)
            screen.blit(hp_goblin_boss_text,hp_goblin_boss_text_rect)
        eboss3_name_text_rect.center = (goblin_boss_rect.x + 105, goblin_boss_rect.y + 265)
        if goblin_boss_hp > 0:
            screen.blit(goblin_boss_image,goblin_boss_rect)
            screen.blit(eboss3_name_text,eboss3_name_text_rect)
        goblin_boss_rect.x += goblin_boss_x * goblin_boss_speed
        goblin_boss_rect.y += goblin_boss_y * goblin_boss_speed
        if goblin_boss_rect.left < 100 or goblin_boss_rect.left > width - 240:
            goblin_boss_x = -1 * goblin_boss_x
        elif goblin_boss_rect.top < 75 or goblin_boss_rect.bottom > height - 160:
            goblin_boss_y = -1 * goblin_boss_y
        if goblin_boss_rect.left < 130: 
            goblin_boss_image = loadify(enemy5.img2)         
        if goblin_boss_rect.left >= 900: 
            goblin_boss_image = loadify(enemy5.img)
        
        if goblin_boss_rect.colliderect(g_portal_image_rect) and goblin_boss_hp > 0:
            pygame.mixer.Channel(7).play(pygame.mixer.Sound("sounds/goblin.wav"))
            pygame.mixer.Channel(7).set_volume(0.4)

    # Ghost
    if enemy_ghost > 0:
        hp_ghost_text = pygame.font.SysFont("Moncerat", 18)
        if ghost_hp > 0:      
            hp_ghost_text = hp_ghost_text.render("HP: " + f"{ghost_hp}", True, white)
            hp_ghost_text_rect = hp_ghost_text.get_rect()
            hp_ghost_text_rect.center = (ghost_rect.x + 30, ghost_rect.y + 80)
            screen.blit(hp_ghost_text,hp_ghost_text_rect)
        egh_name_text_rect.center = (ghost_rect.x + 30, ghost_rect.y + 90)
        if ghost_hp > 0:
            screen.blit(ghost_image,ghost_rect)
            screen.blit(egh_name_text,egh_name_text_rect)
        ghost_rect.x += ghost_x * ghost_speed
        ghost_rect.y += ghost_y * ghost_speed
        if ghost_rect.left < 100 or ghost_rect.left > width - 120:
            ghost_x = -1 * ghost_x
        elif ghost_rect.top < 75 or ghost_rect.bottom > height - 120:
            ghost_y = -1 * ghost_y
        if ghost_rect.left < 130: 
            ghost_image = loadify(enemy6.img2)        
        if ghost_rect.left >= 1000: 
            ghost_image = loadify(enemy6.img)

    # Ghost 1
    if enemy_ghost1 > 0:
        hp_ghost1_text = pygame.font.SysFont("Moncerat", 18)
        if ghost_hp1 > 0:      
            hp_ghost1_text = hp_ghost1_text.render("HP: " + f"{ghost_hp1}", True, white)
            hp_ghost1_text_rect = hp_ghost1_text.get_rect()
            hp_ghost1_text_rect.center = (ghost1_rect.x + 30, ghost1_rect.y + 80)
            screen.blit(hp_ghost1_text,hp_ghost1_text_rect)
        egh1_name_text_rect.center = (ghost1_rect.x + 30, ghost1_rect.y + 90)
        if ghost_hp1 > 0:
            screen.blit(ghost1_image,ghost1_rect)
            screen.blit(egh1_name_text,egh1_name_text_rect)
        ghost1_rect.x += ghost1_x * ghost_speed
        ghost1_rect.y += ghost1_y * ghost_speed
        if ghost1_rect.left < 100 or ghost1_rect.left > width - 120:
            ghost1_x = -1 * ghost1_x
        elif ghost1_rect.top < 75 or ghost1_rect.bottom > height - 120:
            ghost1_y = -1 * ghost1_y
        if ghost1_rect.left < 130: 
            ghost1_image = loadify(enemy6.img2)        
        if ghost1_rect.left >= 1000: 
            ghost1_image = loadify(enemy6.img)

 # Ghost 2
    if enemy_ghost2 > 0:
        hp_ghost2_text = pygame.font.SysFont("Moncerat", 18)
        if ghost_hp2 > 0:      
            hp_ghost2_text = hp_ghost2_text.render("HP: " + f"{ghost_hp2}", True, white)
            hp_ghost2_text_rect = hp_ghost2_text.get_rect()
            hp_ghost2_text_rect.center = (ghost2_rect.x + 30, ghost2_rect.y + 80)
            screen.blit(hp_ghost2_text,hp_ghost2_text_rect)
        egh2_name_text_rect.center = (ghost2_rect.x + 30, ghost2_rect.y + 90)
        if ghost_hp2 > 0:
            screen.blit(ghost2_image,ghost2_rect)
            screen.blit(egh2_name_text,egh2_name_text_rect)
        ghost2_rect.x += ghost2_x * ghost_speed
        ghost2_rect.y += ghost2_y * ghost_speed
        if ghost2_rect.left < 100 or ghost2_rect.left > width - 120:
            ghost2_x = -1 * ghost2_x
        elif ghost2_rect.top < 75 or ghost2_rect.bottom > height - 120:
            ghost2_y = -1 * ghost2_y
        if ghost2_rect.left < 130: 
            ghost2_image = loadify(enemy6.img2)        
        if ghost2_rect.left >= 1000: 
            ghost2_image = loadify(enemy6.img)

# Ghost 3
    if enemy_ghost3 > 0:
        hp_ghost3_text = pygame.font.SysFont("Moncerat", 18)
        if ghost_hp3 > 0:      
            hp_ghost3_text = hp_ghost3_text.render("HP: " + f"{ghost_hp3}", True, white)
            hp_ghost3_text_rect = hp_ghost3_text.get_rect()
            hp_ghost3_text_rect.center = (ghost3_rect.x + 30, ghost3_rect.y + 80)
            screen.blit(hp_ghost3_text,hp_ghost3_text_rect)
        egh3_name_text_rect.center = (ghost3_rect.x + 30, ghost3_rect.y + 90)
        if ghost_hp3 > 0:
            screen.blit(ghost3_image,ghost3_rect)
            screen.blit(egh3_name_text,egh3_name_text_rect)
        ghost3_rect.x += ghost3_x * ghost_speed
        ghost3_rect.y += ghost3_y * ghost_speed
        if ghost3_rect.left < 100 or ghost3_rect.left > width - 120:
            ghost3_x = -1 * ghost3_x
        elif ghost3_rect.top < 75 or ghost3_rect.bottom > height - 120:
            ghost3_y = -1 * ghost3_y
        if ghost3_rect.left < 130: 
            ghost3_image = loadify(enemy6.img2)        
        if ghost3_rect.left >= 1000: 
            ghost3_image = loadify(enemy6.img)

# Ghost BOSS
    if enemy_ghost_boss > 0:
        hp_ghost_boss_text = pygame.font.SysFont("Moncerat", 18)
        if ghost_boss_hp > 0:      
            hp_ghost_boss_text = hp_ghost_boss_text.render("HP: " + f"{ghost_boss_hp}", True, white)
            hp_ghost_boss_text_rect = hp_ghost_boss_text.get_rect()
            hp_ghost_boss_text_rect.center = (ghost_boss_rect.x + 85, ghost_boss_rect.y + 235)
            screen.blit(hp_ghost_boss_text,hp_ghost_boss_text_rect)
        eboss3_name_text_rect.center = (ghost_boss_rect.x + 85, ghost_boss_rect.y + 245)
        if ghost_boss_hp > 0:
            screen.blit(ghost_boss_image,ghost_boss_rect)
            screen.blit(eboss3_name_text,eboss3_name_text_rect)
        ghost_boss_rect.x += ghost_boss_x * ghost_boss_speed
        ghost_boss_rect.y += ghost_boss_y * ghost_boss_speed
        if ghost_boss_rect.left < 100 or ghost_boss_rect.left > width - 140:
            ghost_boss_x = -1 * ghost_boss_x
        elif ghost_boss_rect.top < 75 or ghost_boss_rect.bottom > height - 160:
            ghost_boss_y = -1 * ghost_boss_y
        if ghost_boss_rect.left < 130: 
            ghost_boss_image = loadify(enemy7.img2)         
        if ghost_boss_rect.left >= 950: 
            ghost_boss_image = loadify(enemy7.img)
        
        if ghost_boss_rect.colliderect(gh_portal_image_rect) and ghost_boss_hp > 0:
            pygame.mixer.Channel(6).play(pygame.mixer.Sound("sounds/ghost.wav"))
            pygame.mixer.Channel(6).set_volume(0.01)
    
#-----------------------------------------------------------------------------------------------#    
                            ### KONTROLA KOLIZE ###
#-----------------------------------------------------------------------------------------------#

# Kolize mezi Enemy a Player
#-----------------------------------------------------------------------------------------------#
    def handle_collision(player,attacker_rect, attacker2_rect, target_rect, target_hp, damage, player_hp, player_file, sound_channel, sound_file, volume, enemy):
        if attacker_rect.colliderect(target_rect) or attacker2_rect.colliderect(target_rect):
            if player_hp > 0 and target_hp > 0 and enemy > 0 and player > 0:
                player_hp -= damage
                str_player_hp = str(player_hp)
                try:
                    with open(player_file, "w") as f:
                        f.write(str_player_hp)
                except FileNotFoundError:
                    print("Soubor nebyl nalezen")
                pygame.mixer.Channel(sound_channel).play(pygame.mixer.Sound(sound_file))
                pygame.mixer.Channel(sound_channel).set_volume(volume)
        return player_hp

    # Define common parameters
    sound_channel = 7
    collision_params = [
        # Human collisions
        (player_human, spider_rect, spider_rect, human_rect, spider_hp, 1, "players_hp/human_hp.txt", "sounds/uh.wav", 0.1, enemy_spider),
        (player_human,spider_rect1, spider_rect1, human_rect, spider_hp1, 1, "players_hp/human_hp.txt", "sounds/uh.wav", 0.1, enemy_spider1),
        (player_human,spider_rect2, spider_rect2, human_rect, spider_hp2, 1, "players_hp/human_hp.txt", "sounds/uh.wav", 0.1, enemy_spider2),
        (player_human,spider_rect3, spider_rect3, human_rect, spider_hp3, 1, "players_hp/human_hp.txt", "sounds/uh.wav", 0.1, enemy_spider3),
        (player_human,spider_boss_rect, spider_boss_rect, human_rect, enemy_spider_boss_hp, 2, "players_hp/human_hp.txt", "sounds/uh.wav", 0.1, enemy_spider_boss),
        (player_human,scelet_rect, scelet_rect, human_rect, scelet_hp, 1, "players_hp/human_hp.txt", "sounds/uh.wav", 0.1, enemy_scelet),
        (player_human,scelet1_rect, scelet1_rect, human_rect, scelet1_hp, 1, "players_hp/human_hp.txt", "sounds/uh.wav", 0.1, enemy_scelet1),
        (player_human,scelet2_rect, scelet2_rect, human_rect, scelet2_hp, 1, "players_hp/human_hp.txt", "sounds/uh.wav", 0.1, enemy_scelet2),
        (player_human,scelet_boss_rect, scelet_boss_rect, human_rect, enemy_scelet_boss_hp, 2, "players_hp/human_hp.txt", "sounds/uh.wav", 0.1, enemy_scelet_boss),
        (player_human,goblin_rect, goblin_rect, human_rect, goblin_hp, 2, "players_hp/human_hp.txt", "sounds/uh.wav", 0.1, enemy_goblin),
        (player_human,goblin_rect1, goblin_rect1, human_rect, goblin_hp1, 2, "players_hp/human_hp.txt", "sounds/uh.wav", 0.1, enemy_goblin1),
        (player_human,goblin_rect2, goblin_rect2, human_rect, goblin_hp2, 2, "players_hp/human_hp.txt", "sounds/uh.wav", 0.1, enemy_goblin2),
        (player_human,goblin_rect3, goblin_rect3, human_rect, goblin_hp3, 2, "players_hp/human_hp.txt", "sounds/uh.wav", 0.1, enemy_goblin3),
        (player_human,goblin_boss_rect, goblin_boss_rect, human_rect, goblin_boss_hp, 2, "players_hp/human_hp.txt", "sounds/uh.wav", 0.1, enemy_goblin_boss),
        (player_human,ghost_rect, ghost_rect, human_rect, ghost_hp, 5, "players_hp/human_hp.txt", "sounds/uh.wav", 0.1, enemy_ghost),
        (player_human,ghost1_rect, ghost1_rect, human_rect, ghost_hp1, 5, "players_hp/human_hp.txt", "sounds/uh.wav", 0.1, enemy_ghost1),
        (player_human,ghost2_rect, ghost2_rect, human_rect, ghost_hp2, 5, "players_hp/human_hp.txt", "sounds/uh.wav", 0.1, enemy_ghost2),
        (player_human,ghost3_rect, ghost3_rect, human_rect, ghost_hp3, 5, "players_hp/human_hp.txt", "sounds/uh.wav", 0.1, enemy_ghost3),
        (player_human,ghost_boss_rect, ghost_boss_rect, human_rect, ghost_boss_hp, 50, "players_hp/human_hp.txt", "sounds/uh.wav", 0.1, enemy_ghost_boss),
        
        # Archer collisions
        (player_archer,scelet_rect, scelet_rect, archer_rect, scelet_hp, 1, "players_hp/archer_hp.txt", "sounds/uh.wav", 0.1, enemy_scelet),
        (player_archer,scelet1_rect, scelet1_rect, archer_rect, scelet1_hp, 1, "players_hp/archer_hp.txt", "sounds/uh.wav", 0.1, enemy_scelet1),
        (player_archer,scelet2_rect, scelet2_rect, archer_rect, scelet2_hp, 1, "players_hp/archer_hp.txt", "sounds/uh.wav", 0.1, enemy_scelet2),
        (player_archer,scelet3_rect, scelet3_rect, archer_rect, scelet3_hp, 1, "players_hp/archer_hp.txt", "sounds/uh.wav", 0.1, enemy_scelet3),
        (player_archer,scelet_boss_rect, scelet_boss_rect, archer_rect, enemy_scelet_boss_hp, 1, "players_hp/archer_hp.txt", "sounds/uh.wav", 0.1, enemy_scelet_boss),
        (player_archer,goblin_rect, goblin_rect, archer_rect, goblin_hp, 2, "players_hp/archer_hp.txt", "sounds/uh.wav", 0.1, enemy_goblin),
        (player_archer,goblin_rect1, goblin_rect1, archer_rect, goblin_hp1, 2, "players_hp/archer_hp.txt", "sounds/uh.wav", 0.1, enemy_goblin1),
        (player_archer,goblin_rect2, goblin_rect2, archer_rect, goblin_hp2, 2, "players_hp/archer_hp.txt", "sounds/uh.wav", 0.1, enemy_goblin2),
        (player_archer,goblin_rect3, goblin_rect3, archer_rect, goblin_hp3, 2, "players_hp/archer_hp.txt", "sounds/uh.wav", 0.1, enemy_goblin3),
        (player_archer,goblin_boss_rect, goblin_boss_rect, archer_rect, goblin_boss_hp, 2, "players_hp/archer_hp.txt", "sounds/uh.wav", 0.1, enemy_goblin_boss),
        (player_archer,ghost_rect, ghost_rect, archer_rect, ghost_hp, 3, "players_hp/archer_hp.txt", "sounds/uh.wav", 0.1, enemy_ghost),
        (player_archer,ghost1_rect, ghost1_rect, archer_rect, ghost_hp1, 3, "players_hp/archer_hp.txt", "sounds/uh.wav", 0.1, enemy_ghost1),
        (player_archer,ghost2_rect, ghost2_rect, archer_rect, ghost_hp2, 3, "players_hp/archer_hp.txt", "sounds/uh.wav", 0.1, enemy_ghost2),
        (player_archer,ghost3_rect, ghost3_rect, archer_rect, ghost_hp3, 3, "players_hp/archer_hp.txt", "sounds/uh.wav", 0.1, enemy_ghost3),
        (player_archer,ghost_boss_rect, ghost_boss_rect, archer_rect, ghost_boss_hp, 3, "players_hp/archer_hp.txt", "sounds/uh.wav", 0.1, enemy_ghost_boss),
        
        # Firemag collisions
        (player_fmag,goblin_rect, goblin_rect, fzard_rect, goblin_hp, 1, "players_hp/fmag_hp.txt", "sounds/uh.wav", 0.1, enemy_goblin),
        (player_fmag,goblin_rect2, goblin_rect2, fzard_rect, goblin_hp2, 1, "players_hp/fmag_hp.txt", "sounds/uh.wav", 0.1, enemy_goblin2),
        (player_fmag,goblin_rect1, goblin_rect1, fzard_rect, goblin_hp1, 1, "players_hp/fmag_hp.txt", "sounds/uh.wav", 0.1, enemy_goblin1),
        (player_fmag,goblin_rect3, goblin_rect3, fzard_rect, goblin_hp3, 1, "players_hp/fmag_hp.txt", "sounds/uh.wav", 0.1, enemy_goblin3),
        (player_fmag,goblin_boss_rect, goblin_boss_rect, fzard_rect, goblin_boss_hp, 1, "players_hp/fmag_hp.txt", "sounds/uh.wav", 0.1, enemy_goblin_boss),
        (player_fmag,ghost_rect, ghost_rect, fzard_rect, ghost_hp, 2, "players_hp/fmag_hp.txt", "sounds/uh.wav", 0.1, enemy_ghost),
        (player_fmag,ghost1_rect, ghost1_rect, fzard_rect, ghost_hp1, 2, "players_hp/fmag_hp.txt", "sounds/uh.wav", 0.1, enemy_ghost1),
        (player_fmag,ghost2_rect, ghost2_rect, fzard_rect, ghost_hp2, 2, "players_hp/fmag_hp.txt", "sounds/uh.wav", 0.1, enemy_ghost2),
        (player_fmag,ghost3_rect, ghost3_rect, fzard_rect, ghost_hp3, 2, "players_hp/fmag_hp.txt", "sounds/uh.wav", 0.1, enemy_ghost3),
        (player_fmag,ghost_boss_rect, ghost_boss_rect, fzard_rect, ghost_boss_hp, 2, "players_hp/fmag_hp.txt", "sounds/uh.wav", 0.1, enemy_ghost_boss),
        
        # Light collisions
        (player_light,ghost_rect, ghost_rect, light_rect, ghost_hp, 1, "players_hp/light_hp.txt", "sounds/wuh.wav", 0.01, enemy_ghost),
        (player_light,ghost1_rect, ghost1_rect, light_rect, ghost_hp1, 1, "players_hp/light_hp.txt", "sounds/wuh.wav", 0.01, enemy_ghost1),
        (player_light,ghost2_rect, ghost2_rect, light_rect, ghost_hp2, 1, "players_hp/light_hp.txt", "sounds/wuh.wav", 0.01, enemy_ghost2),
        (player_light,ghost3_rect, ghost3_rect, light_rect, ghost_hp3, 1, "players_hp/light_hp.txt", "sounds/wuh.wav", 0.01, enemy_ghost3),
        (player_light,ghost_boss_rect, ghost_boss_rect, light_rect, ghost_boss_hp, 1, "players_hp/light_hp.txt", "sounds/wuh.wav", 0.01, enemy_ghost_boss)
    ]
    # Iterate over collision parameters and handle collisions
    for params in collision_params:
        player, attacker_rect, attacker2_rect, target_rect, target_hp, damage, player_file, sound_file, volume, enemy = params
        if "human" in player_file:
            human_hp = handle_collision(player_human,attacker_rect, attacker2_rect, target_rect, target_hp, damage, human_hp, player_file, sound_channel, sound_file, volume, enemy)
        elif "archer" in player_file:
            archer_hp = handle_collision(player_archer,attacker_rect, attacker2_rect, target_rect, target_hp, damage, archer_hp, player_file, sound_channel, sound_file, volume, enemy)
        elif "fmag" in player_file:
            fmag_hp = handle_collision(player_fmag,attacker_rect, attacker2_rect, target_rect, target_hp, damage, fmag_hp, player_file, sound_channel, sound_file, volume, enemy)
        elif "light" in player_file:
            light_hp = handle_collision(player_light,attacker_rect, attacker2_rect, target_rect, target_hp, damage, light_hp, player_file, sound_channel, sound_file, volume, enemy)

# Kolize mezi Attack a Enemy
#-----------------------------------------------------------------------------------------------#
    def handle_collision(attack_rect, attack2_rect, entity_rect, enemy_entity, player, entity_hp, file_path, damage, keys=None, key_check=None):
        if attack_rect.colliderect(entity_rect) or attack2_rect.colliderect(entity_rect):
            if enemy_entity > 0 and player > 0 and (keys is None or keys[key_check]):
                entity_hp -= 1000 * damage
                str_entity_hp = str(entity_hp)
                try:
                    with open(file_path, "w") as f3:
                        f3.write(str_entity_hp)
                except FileNotFoundError:
                    print("Soubor nebyl nalezen")
        return entity_hp

    # Human attacks
    spider_hp = handle_collision(human_attack_rect, human_attack2_rect, spider_rect, enemy_spider, player_human, spider_hp, "players_hp/spider_hp.txt", 1, keys, pygame.K_SPACE)
    spider_hp1 = handle_collision(human_attack_rect, human_attack2_rect, spider_rect1, enemy_spider1, player_human, spider_hp1, "players_hp/spider_hp1.txt", 1, keys, pygame.K_SPACE)
    spider_hp2 = handle_collision(human_attack_rect, human_attack2_rect, spider_rect2, enemy_spider2, player_human, spider_hp2, "players_hp/spider_hp2.txt", 1, keys, pygame.K_SPACE)
    spider_hp3 = handle_collision(human_attack_rect, human_attack2_rect, spider_rect3, enemy_spider3, player_human, spider_hp3, "players_hp/spider_hp3.txt", 1, keys, pygame.K_SPACE)
    enemy_spider_boss_hp = handle_collision(human_attack_rect, human_attack2_rect, spider_boss_rect, enemy_spider_boss, player_human, enemy_spider_boss_hp, "players_hp/spider_boss_hp.txt", 1, keys, pygame.K_SPACE)
    scelet_hp = handle_collision(human_attack_rect, human_attack2_rect, scelet_rect, enemy_scelet, player_human, scelet_hp, "players_hp/scelet_hp.txt", 0.5, keys, pygame.K_SPACE)
    scelet1_hp = handle_collision(human_attack_rect, human_attack2_rect, scelet1_rect, enemy_scelet1, player_human, scelet1_hp, "players_hp/scelet1_hp.txt", 0.5, keys, pygame.K_SPACE)
    scelet2_hp = handle_collision(human_attack_rect, human_attack2_rect, scelet2_rect, enemy_scelet2, player_human, scelet2_hp, "players_hp/scelet2_hp.txt", 0.5, keys, pygame.K_SPACE)
    scelet3_hp = handle_collision(human_attack_rect, human_attack2_rect, scelet3_rect, enemy_scelet3, player_human, scelet3_hp, "players_hp/scelet3_hp.txt", 0.5, keys, pygame.K_SPACE)
    enemy_scelet_boss_hp = handle_collision(human_attack_rect, human_attack2_rect, scelet_boss_rect, enemy_scelet_boss, player_human, enemy_scelet_boss_hp, "players_hp/scelet_boss_hp.txt", 0.5, keys, pygame.K_SPACE)
    goblin_hp = handle_collision(human_attack_rect, human_attack2_rect, goblin_rect, enemy_goblin, player_human, goblin_hp, "players_hp/goblin_hp.txt", 0.25, keys, pygame.K_SPACE)
    goblin_hp1 = handle_collision(human_attack_rect, human_attack2_rect, goblin_rect1, enemy_goblin1, player_human, goblin_hp1, "players_hp/goblin_hp1.txt", 0.25, keys, pygame.K_SPACE)
    goblin_hp2 = handle_collision(human_attack_rect, human_attack2_rect, goblin_rect2, enemy_goblin2, player_human, goblin_hp2, "players_hp/goblin_hp2.txt", 0.25, keys, pygame.K_SPACE)
    goblin_hp3 = handle_collision(human_attack_rect, human_attack2_rect, goblin_rect3, enemy_goblin3, player_human, goblin_hp3, "players_hp/goblin_hp3.txt", 0.25, keys, pygame.K_SPACE)
    goblin_boss_hp = handle_collision(human_attack_rect, human_attack2_rect, goblin_boss_rect, enemy_goblin_boss, player_human, goblin_boss_hp, "players_hp/goblin_boss_hp.txt", 0.25, keys, pygame.K_SPACE)

    # Arrow collisions
    scelet_hp = handle_collision(arrow_rect, arrow2_rect, scelet_rect, enemy_scelet, player_archer, scelet_hp, "players_hp/scelet_hp.txt", 1)
    scelet1_hp = handle_collision(arrow_rect, arrow2_rect, scelet1_rect, enemy_scelet1, player_archer, scelet1_hp, "players_hp/scelet_hp1.txt", 2)
    scelet2_hp = handle_collision(arrow_rect, arrow2_rect, scelet2_rect, enemy_scelet2, player_archer, scelet2_hp, "players_hp/scelet_hp2.txt", 2)
    scelet3_hp = handle_collision(arrow_rect, arrow2_rect, scelet3_rect, enemy_scelet3, player_archer, scelet3_hp, "players_hp/scelet_hp3.txt", 2)
    enemy_scelet_boss_hp = handle_collision(arrow_rect, arrow2_rect, scelet_boss_rect, enemy_scelet_boss, player_archer, enemy_scelet_boss_hp, "players_hp/scelet_boss_hp.txt", 2)
    goblin_hp = handle_collision(arrow_rect, arrow2_rect, goblin_rect, enemy_goblin, player_archer, goblin_hp, "players_hp/goblin_hp.txt", 0.5)
    goblin_hp1 = handle_collision(arrow_rect, arrow2_rect, goblin_rect1, enemy_goblin1, player_archer, goblin_hp1, "players_hp/goblin_hp1.txt", 0.5)
    goblin_hp2 = handle_collision(arrow_rect, arrow2_rect, goblin_rect2, enemy_goblin2, player_archer, goblin_hp2, "players_hp/goblin_hp2.txt", 0.5)
    goblin_hp3 = handle_collision(arrow_rect, arrow2_rect, goblin_rect3, enemy_goblin3, player_archer, goblin_hp3, "players_hp/goblin_hp3.txt", 0.5)
    goblin_boss_hp = handle_collision(arrow_rect, arrow2_rect, goblin_boss_rect, enemy_goblin_boss, player_archer, goblin_boss_hp, "players_hp/goblin_boss_hp.txt", 0.5)
    ghost_hp = handle_collision(arrow_rect, arrow2_rect, ghost_rect, enemy_ghost, player_archer, ghost_hp, "players_hp/ghost_hp.txt", 0.25)
    ghost_hp1 = handle_collision(arrow_rect, arrow2_rect, ghost1_rect, enemy_ghost1, player_archer, ghost_hp1, "players_hp/ghost_hp1.txt", 0.25)
    ghost_hp2 = handle_collision(arrow_rect, arrow2_rect, ghost2_rect, enemy_ghost2, player_archer, ghost_hp2, "players_hp/ghost_hp2.txt", 0.25)
    ghost_hp3 = handle_collision(arrow_rect, arrow2_rect, ghost3_rect, enemy_ghost3, player_archer, ghost_hp3, "players_hp/ghost_hp3.txt", 0.25)
    ghost_boss_hp = handle_collision(arrow_rect, arrow2_rect, ghost_boss_rect, enemy_ghost_boss, player_archer, ghost_boss_hp, "players_hp/ghost_boss_hp.txt", 0.5)

    # Fireball collisions
    goblin_hp = handle_collision(fball_rect, fball2_rect, goblin_rect, enemy_goblin, player_fmag, goblin_hp, "players_hp/goblin_hp.txt", 1)
    goblin_hp1 = handle_collision(fball_rect, fball2_rect, goblin_rect1, enemy_goblin1, player_fmag, goblin_hp1, "players_hp/goblin_hp1.txt", 1)
    goblin_hp2 = handle_collision(fball_rect, fball2_rect, goblin_rect2, enemy_goblin2, player_fmag, goblin_hp2, "players_hp/goblin_hp2.txt", 1)
    goblin_hp3 = handle_collision(fball_rect, fball2_rect, goblin_rect3, enemy_goblin3, player_fmag, goblin_hp3, "players_hp/goblin_hp3.txt", 1)
    goblin_boss_hp = handle_collision(fball_rect, fball2_rect, goblin_boss_rect, enemy_goblin_boss, player_fmag, goblin_boss_hp, "players_hp/goblin_boss_hp.txt", 2)
    ghost_hp = handle_collision(fball_rect, fball2_rect, ghost_rect, enemy_ghost, player_fmag, ghost_hp, "players_hp/ghost_hp.txt", 0.5)
    ghost_hp1 = handle_collision(fball_rect, fball2_rect, ghost1_rect, enemy_ghost1, player_fmag, ghost_hp1, "players_hp/ghost_hp1.txt", 0.5)
    ghost_hp2 = handle_collision(fball_rect, fball2_rect, ghost2_rect, enemy_ghost2, player_fmag, ghost_hp2, "players_hp/ghost_hp2.txt", 0.5)
    ghost_hp3 = handle_collision(fball_rect, fball2_rect, ghost3_rect, enemy_ghost3, player_fmag, ghost_hp3, "players_hp/ghost_hp3.txt", 0.5)
    ghost_boss_hp = handle_collision(fball_rect, fball2_rect, ghost_boss_rect, enemy_ghost_boss, player_fmag, ghost_boss_hp, "players_hp/ghost_boss_hp.txt", 1)

    # Ligh collisions
    ghost_hp = handle_collision(light_attack_rect, light_attack2_rect, ghost_rect, enemy_ghost, player_light, ghost_hp, "players_hp/ghost_hp.txt", 1)
    ghost_hp1 = handle_collision(light_attack_rect, light_attack2_rect, ghost1_rect, enemy_ghost1, player_light, ghost_hp1, "players_hp/ghost_hp1.txt", 1)
    ghost_hp2 = handle_collision(light_attack_rect, light_attack2_rect, ghost2_rect, enemy_ghost2, player_light, ghost_hp2, "players_hp/ghost_hp2.txt", 1)
    ghost_hp3 = handle_collision(light_attack_rect, light_attack2_rect, ghost3_rect, enemy_ghost3, player_light, ghost_hp3, "players_hp/ghost_hp3.txt", 1)
    ghost_boss_hp = handle_collision(light_attack_rect, light_attack2_rect, ghost_boss_rect, enemy_ghost_boss, player_light, ghost_boss_hp, "players_hp/ghost_boss_hp.txt", 1)
#-----------------------------------------------------------------------------------------------#
# OBRAZCE
#-----------------------------------------------------------------------------------------------#
    pygame.draw.line(screen, black, (1,1),(1200,1), 3)
    pygame.draw.line(screen, black, (1,70),(1200,70), 3)

    pygame.draw.line(screen, black, (1,1),(1,70), 3)
    pygame.draw.line(screen, black, (1198,1),(1198,70), 3)

    if run_game == 0:
        pygame.draw.line(screen, black, (127,70),(127,0), 3)

    if enemy_spider > 0:
        pygame.draw.line(screen, black, (width//2 - 140,70),(width//2 - 140,0), 3)
        pygame.draw.line(screen, black, (width//2 - 70,70),(width//2 - 70,0), 3)
        pygame.draw.line(screen, black, (width//2,70),(width//2,0), 3)
        pygame.draw.line(screen, black, (width//2 + 70,70),(width//2 + 70,0), 3)
        pygame.draw.line(screen, black, (width//2 + 140,70),(width//2 + 140,0), 3)
        pygame.draw.rect(screen,grey,(129,3,width//2 - 270,66))
        pygame.draw.rect(screen,grey,(width//2 + 143,3,454,66))
    if player_human > 0 or player_archer > 0 or player_fmag > 0 or player_light > 0:
        pygame.draw.line(screen, black, (127,70),(127,0), 3)
    if player_human < 0 or player_archer < 0 or player_fmag < 0 or player_light < 0:
        pygame.draw.line(screen, black, (127,70),(127,0), 3)

    if ghost_boss_hp <= 0 and run_game == 1:
         screen.blit(custom_end_text, custom_end_text_rect)
#-----------------------------------------------------------------------------------------------#
    pygame.display.update()
    clock.tick_busy_loop(fps)

# Ukončení hry
pygame.quit()