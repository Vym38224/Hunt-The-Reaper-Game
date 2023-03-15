import pygame, random
from pygame.locals import *
from SaveLoadManager import SaveLoadSystem

#obrázky --> https://icons.iconarchive.com/

##
##
##
############ ZÁKLADNÍ NASTAVENÍ ############
##
##ahoj
##
   
# INICIALIZACE HRY 
pygame.init()

# OBRAZOVKA
width = 1600
height = 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Monkey Adventure")
clock = pygame.time.Clock()

# POZADÍ
background_img = pygame.image.load("pictures/backgroundzk.png")
background2_img = pygame.image.load("pictures/background2.png")

# ULOŽENÍ HRY
saveLoadmanager = SaveLoadSystem(".save", "save_data")

# BARVIČKY
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
pink = (255,150,255)
green = (0,255,0)
blue = (0,0,255)
lblue = (50,155,255)
orange = (255,155,0)
yellow = (250,250,0)
lorange = (255,200,0)
screen_color = (0,95,0)

# ZÁKLADNÍ NASTAVENÍ
distance = 12
clock = pygame.time.Clock()
score = saveLoadmanager.load_game_data(["score"], [0.0])
food3 = saveLoadmanager.load_game_data(["food3"], [0])
food2 = saveLoadmanager.load_game_data(["food2"], [0])
food = saveLoadmanager.load_game_data(["food"], [0])
luck = saveLoadmanager.load_game_data(["luck"], [0])
penize = saveLoadmanager.load_game_data(["penize"], [0.0])
level = saveLoadmanager.load_game_data(["level"], [0])
penizeint = ()
scoreint = ()
luckint = ()
click_x = 0
click_y = 0
duck_x = random.choice ([-1,1])
duck_y = random.choice([-1,1])
pig_x = random.choice ([-1,1])
pig_y = random.choice([-1,1])
ostrich2_x = random.choice ([-1,1])
ostrich2_y = random.choice ([-1,1])
duck_speed = 2
duck_speed2 = 4
duck_speed3 = 6
duck_speed4 = 7
ostrich2_speed = 3
ostrich2_speed2 = 5
ostrich2_speed3 = 7
ostrich2_speed4 = 8
ostrich2_speed5 = 10

# OBRÁZKY
cat_image = pygame.image.load("pictures/Monkey.png")
cat_rect = cat_image.get_rect()
cat_rect.center = (100,800)
up_image = pygame.image.load("pictures/up.png")
up_rect = up_image.get_rect()
up_rect.center = (1500,500)
money_image = pygame.image.load("pictures/Money.png")
money_rect = money_image.get_rect()
money_rect.center = (265,335)

money1_image = pygame.image.load("pictures/Money.png")
money1_rect = money1_image.get_rect()
money1_rect.center = (265,335)
money2_image = pygame.image.load("pictures/Money.png")
money2_rect = money2_image.get_rect()
money2_rect.center = (265,335)
money3_image = pygame.image.load("pictures/Money.png")
money3_rect = money3_image.get_rect()
money3_rect.center = (265,335)

duck_image = pygame.image.load("pictures/Duck.png")
duck_rect = duck_image.get_rect()
duck_rect.center = (1500,150)
egg_image = pygame.image.load("pictures/egg.png")
egg_rect = egg_image.get_rect()
egg_rect.center = (1500,170)
ostrich2_image = pygame.image.load("pictures/ostrich2.png")
ostrich2_rect = ostrich2_image.get_rect()
ostrich2_rect.center = (1500,150)
egg2_image = pygame.image.load("pictures/egg2.png")
egg2_rect = egg2_image.get_rect()
egg2_rect.center = (1500,170)
home_image = pygame.image.load("pictures/home.png")
home_rect = home_image.get_rect()
home_rect.center = (100,800)
rain_image = pygame.image.load("pictures/rainbow.png")
rain_rect = rain_image.get_rect()
rain_rect.center = (250,300)
bank_image = pygame.image.load("pictures/bank.png")
bank_rect = bank_image.get_rect()
bank_rect.center = (1500,300)
rypak_image = pygame.image.load("pictures/rypak.png")
rypak_rect = rypak_image.get_rect()
rypak_rect.center = (1500,330)
atm_image = pygame.image.load("pictures/shop.png")
atm_rect = atm_image.get_rect()
atm_rect.center = (1500,650)
food_image = pygame.image.load("pictures/Food.png")
food_rect = food_image.get_rect()
food_rect.center = (325,30)
coin_image = pygame.image.load("pictures/coin.png")
coin_rect = coin_image.get_rect()
coin_rect.center = (75,30)
clover_image = pygame.image.load("pictures/clover.png")
clover_rect = clover_image.get_rect()
clover_rect.center = (1500,800)       

# ZVUKY, HLASITOST
if cat_rect.colliderect(home_rect):
        pygame.mixer.music.load("media/backroung.wav")
        pygame.mixer.music.set_volume(0.01)
        pygame.mixer.music.play()

##
##      
##
############ HLAVNÍ CYKLUS ############ 
##
##
##       
                       
lets_continue = True
while lets_continue:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            saveLoadmanager.save_game_data([score], ["score"])
            saveLoadmanager.save_game_data([penize], ["penize"])
            saveLoadmanager.save_game_data([food], ["food"])
            saveLoadmanager.save_game_data([food2], ["food2"])
            saveLoadmanager.save_game_data([food3], ["food3"])
            saveLoadmanager.save_game_data([luck], ["luck"])
            saveLoadmanager.save_game_data([level], ["level"])
            lets_continue = False           
    
# POHYB OPICE WASD
        keys = pygame.key.get_pressed()
        if keys [pygame.K_w] and cat_rect.top > 80:
            cat_rect.y = cat_rect.y - distance
        elif keys [pygame.K_s] and cat_rect.bottom < height:
            cat_rect.y = cat_rect.y + distance
        elif keys [pygame.K_a] and cat_rect.left > 0:
            cat_rect.x = cat_rect.x - distance
        elif keys [pygame.K_d] and cat_rect.right < width:
            cat_rect.x = cat_rect.x + distance
                
# POHYB OPICE MYŠÍ
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1 and cat_rect.top > 80:
            cat_rect.y = cat_rect.y - distance
            cat_rect.centerx = event.pos[0]
            cat_rect.centery = event.pos[1]
        elif event.type == pygame.MOUSEMOTION and event.buttons[0] == 1 and cat_rect.bottom < height:
            cat_rect.y = cat_rect.y + distance          
        elif event.type == pygame.MOUSEMOTION and event.buttons[0] == 1 and cat_rect.left > 0:
            cat_rect.x = cat_rect.x - distance           
        elif event.type == pygame.MOUSEMOTION and event.buttons[0] == 1 and cat_rect.right < width:
            cat_rect.x = cat_rect.x + distance
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_x = event.pos[0]
            click_y = event.pos[1]


# VRÁTIT ZVÍŘATA NA VÝCHOZÍ POZICI
        elif event.type == pygame.MOUSEBUTTONUP and duck_rect.collidepoint(click_x, click_y):
            pygame.mixer.music.load("media/boom.wav")
            pygame.mixer.music.set_volume(0.01)
            pygame.mixer.music.play()
            duck_image = pygame.image.load("pictures/Duck.png")
            duck_rect = duck_image.get_rect()
            duck_rect.center = (1500,150)

        elif event.type == pygame.MOUSEBUTTONUP and ostrich2_rect.collidepoint(click_x, click_y):
            pygame.mixer.music.load("media/boom.wav")
            pygame.mixer.music.set_volume(0.01)
            pygame.mixer.music.play()
            ostrich2_image = pygame.image.load("pictures/ostrich2.png")
            ostrich2_rect = ostrich2_image.get_rect()
            ostrich2_rect.center = (1500,150)

        elif event.type == pygame.MOUSEBUTTONUP and bank_rect.collidepoint(click_x, click_y):
            pygame.mixer.music.load("media/boom.wav")
            pygame.mixer.music.set_volume(0.01)
            pygame.mixer.music.play()
            bank_image = pygame.image.load("pictures/bank.png")
            bank_rect = bank_image.get_rect()
            bank_rect.center = (1500,300)

# NÁKUPY
        elif event.type == pygame.MOUSEBUTTONUP and cat_rect.colliderect(rain_rect):
            luck = luck + 0.25
            luckstr = str(luck)
            try:
                f7 = open("luck.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f7.write(luckstr)
            f7.close()
            pygame.mixer.music.load("media/clover.wav")
            pygame.mixer.music.set_volume(0.008)
            pygame.mixer.music.play()

        elif event.type == pygame.MOUSEBUTTONUP and score > 0 and cat_rect.colliderect(atm_rect):
            score = score - 1
            scorestr = str(score)
            penize = penize + 1     
            penizestr = str(penize)
            try:
                f4 = open("banka.txt","w",)
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f4.write(penizestr)
            f4.close()
            pygame.mixer.music.load("media/buy.wav")
            pygame.mixer.music.set_volume(0.01)
            pygame.mixer.music.play()

        elif event.type == pygame.MOUSEWHEEL and score > 0 and cat_rect.colliderect(atm_rect):
            score = score - 1
            scorestr = str(score)
            penize = penize + 1     
            penizestr = str(penize)
            try:
                f4 = open("banka.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f4.write(penizestr)
            f4.close()
            pygame.mixer.music.load("media/buy.wav")
            pygame.mixer.music.set_volume(0.01)
            pygame.mixer.music.play()

        elif event.type == pygame.MOUSEBUTTONUP and score > 0 and cat_rect.colliderect(clover_rect):
            score = score - 1
            scorestr = str(score)
            luck = luck + 1
            luckstr = str(luck)
            try:
                f6 = open("luck.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f6.write(luckstr)
            f6.close()
            pygame.mixer.music.load("media/clover.wav")
            pygame.mixer.music.set_volume(0.008)
            pygame.mixer.music.play()

        elif event.type == pygame.MOUSEWHEEL and score > 0 and cat_rect.colliderect(clover_rect):
            score = score - 1
            scorestr = str(score)
            luck = luck + 1
            luckstr = str(luck)
            try:
                f6 = open("luck.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f6.write(luckstr)
            f6.close()
            pygame.mixer.music.load("media/clover.wav")
            pygame.mixer.music.set_volume(0.008)
            pygame.mixer.music.play()
    
        elif event.type == pygame.MOUSEWHEEL and cat_rect.colliderect(egg_rect) and level == 0 and penize >= 0.5:
            penize = penize - 1
            penizestr = str(penize)
            food2 = food2 + 1      
            food2str = str(food2)
            try:
                f5 = open("food2.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f5.write(food2str)
            f5.close()
            pygame.mixer.music.load("media/duck.wav")
            pygame.mixer.music.set_volume(0.01)
            pygame.mixer.music.play()
        
        elif event.type == pygame.MOUSEWHEEL and cat_rect.colliderect(egg2_rect) and level == 1 and penize >= 50:
            penize = penize - 50
            penizestr = str(penize)
            food3 = food3 + 1     
            food3str = str(food3)
            try:
                f9 = open("food3.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f9.write(food3str)
            f9.close()
            pygame.mixer.music.load("media/ostrich.wav")
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play()

        elif event.type == pygame.MOUSEWHEEL and cat_rect.colliderect(rypak_rect) and penize >= 0.5:
            penize = penize - 1
            penizestr = str(penize)
            food = food + 1      
            foodstr = str(food)
            try:
                f5 = open("food2.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f5.write(foodstr)
            f5.close()
            pygame.mixer.music.load("media/pig.wav")
            pygame.mixer.music.set_volume(0.01)
            pygame.mixer.music.play()

        elif event.type == pygame.MOUSEWHEEL and cat_rect.colliderect(ostrich2_rect) and level == 1 and penize >= 10:
            penize = penize - 10
            penizestr = str(penize)
            food3 = food3 + 1     
            food3str = str(food3)
            try:
                f10 = open("food3.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f10.write(food3str)
            f10.close()
            pygame.mixer.music.load("media/ostrich.wav")
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play()

        elif event.type == pygame.MOUSEWHEEL and cat_rect.colliderect(duck_rect) and level == 0 and penize >= 0.5:
            penize = penize - 0.5
            penizestr = str(penize)
            food2 = food2 + 0.5      
            food2str = str(food2)
            try:
                f5 = open("food2.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f5.write(food2str)
            f5.close()
            pygame.mixer.music.load("media/duck.wav")
            pygame.mixer.music.set_volume(0.01)
            pygame.mixer.music.play()

        
        elif event.type == pygame.MOUSEWHEEL and cat_rect.colliderect(bank_rect) and penize > 0.5:
            penize = penize - 1
            penizestr = str(penize)
            food = food + 0.5      
            foodstr = str(food)
            try:
                f1 = open("food.txt","w")
            except FileNotFoundError:
                print("Soubor nebyl nalezen")
            text = f1.write(foodstr)
            f1.close()
            pygame.mixer.music.load("media/pig.wav")
            pygame.mixer.music.set_volume(0.03)
            pygame.mixer.music.play()

        elif cat_rect.colliderect(up_rect) and keys [pygame.K_b] and score >= 10000:
            level = level + 1
            levelstr = str(level)
            score = score - 10000
            scorestr = str(score)
            try:
                f8 = open("levelup.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f8.write(levelstr)
            f8.close()
            #pygame.mixer.music.load("media/clover.wav")
            #pygame.mixer.music.set_volume(0.008)
            #pygame.mixer.music.play()

# NÁKUPY ZA 100
        elif keys [pygame.K_l] and cat_rect.colliderect(clover_rect) and score >= 100:
            luck = luck + 50
            luckstr = str(luck)
            score = score - 50
            scorestr = str(score)
            try:
                f7 = open("luck.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f7.write(luckstr)
            f7.close()
            pygame.mixer.music.load("media/clover.wav")
            pygame.mixer.music.set_volume(0.008)
            pygame.mixer.music.play()


        elif keys [pygame.K_f] and cat_rect.colliderect(egg_rect) and level == 0 and penize >= 100:
            penize = penize - 50
            penizestr = str(penize)
            food2 = food2 + 50   
            food2str = str(food2)
            try:
                f5 = open("food2.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f5.write(food2str)
            pygame.mixer.music.load("media/duck.wav")
            pygame.mixer.music.set_volume(0.01)
            pygame.mixer.music.play()

        elif keys [pygame.K_f] and cat_rect.colliderect(egg2_rect) and level == 1 and penize >= 100:
            penize = penize - 100
            penizestr = str(penize)
            food3 = food3 + 20   
            food3str = str(food3)
            try:
                f10 = open("food3.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f10.write(food3str)
            pygame.mixer.music.load("media/ostrich.wav")
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play()
    
        elif keys [pygame.K_f] and cat_rect.colliderect(rypak_rect) and penize >= 100:
            penize = penize - 50
            penizestr = str(penize)
            food = food + 50  
            foodstr = str(food)
            try:
                f5 = open("food2.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f5.write(foodstr)
            f5.close()
            pygame.mixer.music.load("media/pig.wav")
            pygame.mixer.music.set_volume(0.01)
            pygame.mixer.music.play()

        elif cat_rect.colliderect(atm_rect) and keys [pygame.K_b] and score >= 100:
            score = score - 50
            scorestr = str(score)
            penize = penize + 50   
            penizestr = str(penize)
            try:
                f4 = open("banka.txt","w",)
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f4.write(penizestr)
            f4.close()
            pygame.mixer.music.load("media/buy.wav")
            pygame.mixer.music.set_volume(0.01)
            pygame.mixer.music.play()

# KONTROLA KOLIZE
        if cat_rect.colliderect(money_rect):
            money_rect.centerx = random.randint(0 + 100, width - 700)
            money_rect.centery = random.randint(0 + 100, height - 600)
            score +=10000
            scorestr=str(score)
            try:
                f2 = open("score.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f2.write(scorestr)
            pygame.mixer.music.load("media/earn.wav")
            pygame.mixer.music.set_volume(0.008)
            pygame.mixer.music.play()
        if luck > 1000:
            if cat_rect.colliderect(money1_rect):
                money1_rect.centerx = random.randint(0 + 100, width - 700)
                money1_rect.centery = random.randint(0 + 100, height - 600)
                score +=1
                scorestr=str(score)
                try:
                    f2 = open("score.txt","w")
                except FileNotFoundError:
                        print("Soubor nebyl nalezen")
                text = f2.write(scorestr)
                pygame.mixer.music.load("media/earn.wav")
                pygame.mixer.music.set_volume(0.008)
                pygame.mixer.music.play()
        if luck > 5000:
            if cat_rect.colliderect(money2_rect):
                money2_rect.centerx = random.randint(0 + 100, width - 700)
                money2_rect.centery = random.randint(0 + 100, height - 600)
                score +=1
                scorestr=str(score)
                try:
                    f2 = open("score.txt","w")
                except FileNotFoundError:
                        print("Soubor nebyl nalezen")
                text = f2.write(scorestr)
                pygame.mixer.music.load("media/earn.wav")
                pygame.mixer.music.set_volume(0.008)
                pygame.mixer.music.play() 
        if luck > 15000:
            if cat_rect.colliderect(money3_rect):
                money3_rect.centerx = random.randint(0 + 100, width - 700)
                money3_rect.centery = random.randint(0 + 100, height - 600)
                score +=1
                scorestr=str(score)
                try:
                    f2 = open("score.txt","w")
                except FileNotFoundError:
                        print("Soubor nebyl nalezen")
                text = f2.write(scorestr)
                pygame.mixer.music.load("media/earn.wav")
                pygame.mixer.music.set_volume(0.008)
                pygame.mixer.music.play()              
                                    
        if duck_rect.colliderect(money_rect):
            money_rect.centerx = random.randint(0 + 100, width - 700)
            money_rect.centery = random.randint(0 + 100, height - 600)
            scorestr=str(score)
            try:
                f2 = open("score.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f2.write(scorestr)
            f2.close()
            pygame.mixer.music.load("media/earn.wav")
            pygame.mixer.music.set_volume(0.008)
            pygame.mixer.music.play()
            if food2 > 50:
                score += 1
            if food2 > 150:
                score += 1
            if food2 > 500:
                score += 2
            if food2 > 1000:
                score += 2
            if food2 > 2000:
                score += 3
            if food2 > 4000:
                score += 5

        if luck > 1000:
            if duck_rect.colliderect(money1_rect):
                money1_rect.centerx = random.randint(0 + 100, width - 700)
                money1_rect.centery = random.randint(0 + 100, height - 600)
                scorestr=str(score)
                try:
                    f2 = open("score.txt","w")
                except FileNotFoundError:
                        print("Soubor nebyl nalezen")
                text = f2.write(scorestr)
                f2.close()
                pygame.mixer.music.load("media/earn.wav")
                pygame.mixer.music.set_volume(0.008)
                pygame.mixer.music.play()
                if food2 > 50:
                    score += 1
                if food2 > 150:
                    score += 1
                if food2 > 500:
                    score += 2
                if food2 > 1000:
                    score += 2
                if food2 > 2000:
                    score += 3
                if food2 > 4000:
                    score += 5
        if luck > 5000:
            if duck_rect.colliderect(money2_rect):
                money2_rect.centerx = random.randint(0 + 100, width - 700)
                money2_rect.centery = random.randint(0 + 100, height - 600)
                scorestr=str(score)
                try:
                    f2 = open("score.txt","w")
                except FileNotFoundError:
                        print("Soubor nebyl nalezen")
                text = f2.write(scorestr)
                f2.close()
                pygame.mixer.music.load("media/earn.wav")
                pygame.mixer.music.set_volume(0.008)
                pygame.mixer.music.play()
                if food2 > 50:
                    score += 1
                if food2 > 150:
                    score += 1
                if food2 > 500:
                    score += 2
                if food2 > 1000:
                    score += 2
                if food2 > 2000:
                    score += 3
                if food2 > 4000:
                    score += 5
        if luck > 15000:
            if duck_rect.colliderect(money3_rect):
                money3_rect.centerx = random.randint(0 + 100, width - 700)
                money3_rect.centery = random.randint(0 + 100, height - 600)
                scorestr=str(score)
                try:
                    f2 = open("score.txt","w")
                except FileNotFoundError:
                        print("Soubor nebyl nalezen")
                text = f2.write(scorestr)
                f2.close()
                pygame.mixer.music.load("media/earn.wav")
                pygame.mixer.music.set_volume(0.008)
                pygame.mixer.music.play()
                if food2 > 50:
                    score += 1
                if food2 > 150:
                    score += 1
                if food2 > 500:
                    score += 2
                if food2 > 1000:
                    score += 2
                if food2 > 2000:
                    score += 3
                if food2 > 4000:
                    score += 5

        if ostrich2_rect.colliderect(money_rect):
            money_rect.centerx = random.randint(0 + 100, width - 700)
            money_rect.centery = random.randint(0 + 100, height - 600)
            scorestr=str(score)
            try:
                f2 = open("score.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f2.write(scorestr)
            f2.close()
            pygame.mixer.music.load("media/earn.wav")
            pygame.mixer.music.set_volume(0.008)
            pygame.mixer.music.play()
            if food3 > 50:
                score += 2
            if food3 > 150:
                score += 3
            if food3 > 500:
                score += 3
            if food3 > 1000:
                score += 4
            if food3 > 2000:
                score += 5
            if food3 > 4000:
                score += 8
                
        if luck > 1000:
            if duck_rect.colliderect(money1_rect):
                money1_rect.centerx = random.randint(0 + 100, width - 700)
                money1_rect.centery = random.randint(0 + 100, height - 600)
                scorestr=str(score)
                try:
                    f2 = open("score.txt","w")
                except FileNotFoundError:
                        print("Soubor nebyl nalezen")
                text = f2.write(scorestr)
                f2.close()
                pygame.mixer.music.load("media/earn.wav")
                pygame.mixer.music.set_volume(0.008)
                pygame.mixer.music.play()
                if food2 > 50:
                    score += 1
                if food2 > 150:
                    score += 1
                if food2 > 500:
                    score += 2
                if food2 > 1000:
                    score += 2
                if food2 > 2000:
                    score += 3
                if food2 > 4000:
                    score += 5
        if luck > 5000:
            if duck_rect.colliderect(money2_rect):
                money2_rect.centerx = random.randint(0 + 100, width - 700)
                money2_rect.centery = random.randint(0 + 100, height - 600)
                scorestr=str(score)
                try:
                    f2 = open("score.txt","w")
                except FileNotFoundError:
                        print("Soubor nebyl nalezen")
                text = f2.write(scorestr)
                f2.close()
                pygame.mixer.music.load("media/earn.wav")
                pygame.mixer.music.set_volume(0.008)
                pygame.mixer.music.play()
                if food2 > 50:
                    score += 1
                if food2 > 150:
                    score += 1
                if food2 > 500:
                    score += 2
                if food2 > 1000:
                    score += 2
                if food2 > 2000:
                    score += 3
                if food2 > 4000:
                    score += 5
        if luck > 15000:
            if duck_rect.colliderect(money3_rect):
                money3_rect.centerx = random.randint(0 + 100, width - 700)
                money3_rect.centery = random.randint(0 + 100, height - 600)
                scorestr=str(score)
                try:
                    f2 = open("score.txt","w")
                except FileNotFoundError:
                        print("Soubor nebyl nalezen")
                text = f2.write(scorestr)
                f2.close()
                pygame.mixer.music.load("media/earn.wav")
                pygame.mixer.music.set_volume(0.008)
                pygame.mixer.music.play()
                if food2 > 50:
                    score += 1
                if food2 > 150:
                    score += 1
                if food2 > 500:
                    score += 2
                if food2 > 1000:
                    score += 2
                if food2 > 2000:
                    score += 3
                if food2 > 4000:
                    score += 5

        if bank_rect.colliderect(money_rect):
            money_rect.centerx = random.randint(0 + 100, width - 700)
            money_rect.centery = random.randint(0 + 100, height - 600)
            scorestr=str(score)
            try:
                f2 = open("score.txt","w")
            except FileNotFoundError:
                    print("Soubor nebyl nalezen")
            text = f2.write(scorestr)
            pygame.mixer.music.load("media/earn.wav")
            pygame.mixer.music.set_volume(0.008)
            pygame.mixer.music.play()
            if food > 50:
                score += 1
            if food > 150:
                score += 2
            if food > 500:
                score += 2
            if food > 1000:
                score += 3
            if food > 2000:
                score += 3
            if food > 4000:
                score += 4
        if luck > 1000:
            if bank_rect.colliderect(money1_rect):
                money1_rect.centerx = random.randint(0 + 100, width - 700)
                money1_rect.centery = random.randint(0 + 100, height - 600)
                scorestr=str(score)
                try:
                    f2 = open("score.txt","w")
                except FileNotFoundError:
                        print("Soubor nebyl nalezen")
                text = f2.write(scorestr)
                pygame.mixer.music.load("media/earn.wav")
                pygame.mixer.music.set_volume(0.008)
                pygame.mixer.music.play()
                if food > 50:
                    score += 1
                if food > 150:
                    score += 2
                if food > 500:
                    score += 2
                if food > 1000:
                    score += 3
                if food > 2000:
                    score += 3
                if food > 4000:
                    score += 4
        if luck > 5000:
            if bank_rect.colliderect(money2_rect):
                money2_rect.centerx = random.randint(0 + 100, width - 700)
                money2_rect.centery = random.randint(0 + 100, height - 600)
                scorestr=str(score)
                try:
                    f2 = open("score.txt","w")
                except FileNotFoundError:
                        print("Soubor nebyl nalezen")
                text = f2.write(scorestr)
                pygame.mixer.music.load("media/earn.wav")
                pygame.mixer.music.set_volume(0.008)
                pygame.mixer.music.play()
                if food > 50:
                    score += 1
                if food > 150:
                    score += 2
                if food > 500:
                    score += 2
                if food > 1000:
                    score += 3
                if food > 2000:
                    score += 3
                if food > 4000:
                    score += 4
        if luck > 15000:
            if bank_rect.colliderect(money3_rect):
                money3_rect.centerx = random.randint(0 + 100, width - 700)
                money3_rect.centery = random.randint(0 + 100, height - 600)
                scorestr=str(score)
                try:
                    f2 = open("score.txt","w")
                except FileNotFoundError:
                        print("Soubor nebyl nalezen")
                text = f2.write(scorestr)
                pygame.mixer.music.load("media/earn.wav")
                pygame.mixer.music.set_volume(0.008)
                pygame.mixer.music.play()
                if food > 50:
                    score += 1
                if food > 150:
                    score += 2
                if food > 500:
                    score += 2
                if food > 1000:
                    score += 3
                if food > 2000:
                    score += 3
                if food > 4000:
                    score += 4
                                                
        if cat_rect.colliderect(clover_rect) and score > 0:
            if luck >= 1000:
                money1_image = pygame.image.load("pictures/Money.png")
                money1_rect.center = (265,335)
            if luck >= 5000:
                money2_image = pygame.image.load("pictures/Money.png")
                money2_rect.center = (265,335)
            if luck >= 15000:
                money3_image = pygame.image.load("pictures/Money.png")
                money3_rect.center = (265,335)
            
# CHOZENÍ KÁČI
    if food2 >= 50 and food2 < 100:
        duck_rect.x += duck_x * duck_speed
        duck_rect.y += duck_y * duck_speed
        if duck_rect.left < 0 or duck_rect.left >= width:
            duck_x = -1 * duck_x
        elif duck_rect.top < 70 or duck_rect.bottom >= 400:
            duck_y = -1 * duck_y
    if food2 >= 100 and food2 < 300:
        duck_rect.x += duck_x * duck_speed2
        duck_rect.y += duck_y * duck_speed2
        if duck_rect.left < 0 or duck_rect.left >= width:
            duck_x = -1 * duck_x
        elif duck_rect.top < 70 or duck_rect.bottom >= 400:
            duck_y = -1 * duck_y
    if food2 >= 300 and food2 < 500:
        duck_rect.x += duck_x * duck_speed3
        duck_rect.y += duck_y * duck_speed3
        if duck_rect.left < 0 or duck_rect.left >= width:
            duck_x = -1 * duck_x
        elif duck_rect.top < 70 or duck_rect.bottom >= 400:
            duck_y = -1 * duck_y
    if food2 >= 500 and food < 1000:
        duck_rect.x += duck_x * duck_speed4
        duck_rect.y += duck_y * duck_speed4
        if duck_rect.left < 0 or duck_rect.left >= width:
            duck_x = -1 * duck_x
        elif duck_rect.top < 70 or duck_rect.bottom >= 400:
            duck_y = -1 * duck_y
    if food2 >= 1000:
        duck_rect.x += duck_x * duck_speed4
        duck_rect.y += duck_y * duck_speed4
        if duck_rect.left < 0 or duck_rect.left >= width:
            duck_x = -1 * duck_x
        elif duck_rect.top < 100 or duck_rect.bottom >= 400:
            duck_y = -1 * duck_y   

# CHOZENÍ PŠTROSE
    if food3 >= 50 and food3 < 150:
        ostrich2_rect.x += ostrich2_x * ostrich2_speed
        ostrich2_rect.y += ostrich2_y * ostrich2_speed
        if ostrich2_rect.left < 0 or ostrich2_rect.left >= width:
            ostrich2_x = -1 * ostrich2_x
        elif ostrich2_rect.top < 67 or ostrich2_rect.bottom >= 300:
            ostrich2_y = -1 * ostrich2_y
    if food3 >= 150 and food3 < 500:
        ostrich2_rect.x += ostrich2_x * ostrich2_speed2
        ostrich2_rect.y += ostrich2_y * ostrich2_speed2
        if ostrich2_rect.left < 0 or ostrich2_rect.left >= width:
            ostrich2_x = -1 * ostrich2_x
        elif ostrich2_rect.top < 67 or ostrich2_rect.bottom >= 300:
            ostrich2_y = -1 * ostrich2_y
    if food3 >= 500 and food3 < 1000:
        ostrich2_rect.x += ostrich2_x * ostrich2_speed2
        ostrich2_rect.y += ostrich2_y * ostrich2_speed2
        if ostrich2_rect.left < 0 or ostrich2_rect.left >= width:
            ostrich2_x = -1 * ostrich2_x
        elif ostrich2_rect.top < 67 or ostrich2_rect.bottom >= 300:
            ostrich2_y = -1 * ostrich2_y
    if food3 >= 1000 and food3 < 2000 :
        ostrich2_rect.x += ostrich2_x * ostrich2_speed4
        ostrich2_rect.y += ostrich2_y * ostrich2_speed4
        if ostrich2_rect.left < 0 or ostrich2_rect.left >= width:
            ostrich2_x = -1 * ostrich2_x
        elif ostrich2_rect.top < 67 or ostrich2_rect.bottom >= 400:
            ostrich2_y = -1 * ostrich2_y
    if food3 >= 2000:
        ostrich2_rect.x += ostrich2_x * ostrich2_speed5
        ostrich2_rect.y += ostrich2_y * ostrich2_speed5
        if ostrich2_rect.left < 0 or ostrich2_rect.left >= width:
            ostrich2_x = -1 * ostrich2_x
        elif ostrich2_rect.top < 67 or ostrich2_rect.bottom >= 400:
            ostrich2_y = -1 * ostrich2_y   

# CHOZENÍ PIGI
    if food >= 50 and food < 100:
        bank_rect.x += pig_x * duck_speed
        bank_rect.y += pig_y * duck_speed
        if bank_rect.left < 0 or bank_rect.left >= width:
            pig_x = -1 * pig_x
        elif bank_rect.top < 225 or bank_rect.bottom >= 400:
            pig_y = -1 * pig_y 
    if food >= 100 and food < 250:
        bank_rect.x += pig_x * duck_speed2
        bank_rect.y += pig_y * duck_speed2
        if bank_rect.left < 0 or bank_rect.left >= width:
            pig_x = -1 * pig_x
        elif bank_rect.top < 225 or bank_rect.bottom >= 400:
            pig_y = -1 * pig_y 
    if food >= 250 and food < 1000:
        bank_rect.x += pig_x * duck_speed3
        bank_rect.y += pig_y * duck_speed3
        if bank_rect.left < 0 or bank_rect.left >= width:
            pig_x = -1 * pig_x
        elif bank_rect.top < 225 or bank_rect.bottom >= 400:
            pig_y = -1 * pig_y
    if food >= 1000:
        bank_rect.x += pig_x * duck_speed4
        bank_rect.y += pig_y * duck_speed4
        if bank_rect.left < 0 or bank_rect.left >= width:
            pig_x = -1 * pig_x
        elif bank_rect.top < 150 or bank_rect.bottom >= 400:
            pig_y = -1 * pig_y

# TIKÁNÍ HODIN
    clock.tick(60)

# OTOČENÍ OBRÁZKU
    if bank_rect.left < 0: 
        bank_image = pygame.image.load("pictures/bank2.png")
    if bank_rect.left >= width: 
        bank_image = pygame.image.load("pictures/bank.png")

    if duck_rect.left < 0: 
        duck_image = pygame.image.load("pictures/Duck2.png")
    if duck_rect.left >= width: 
        duck_image = pygame.image.load("pictures/Duck.png")
    
    if ostrich2_rect.left < 0: 
        ostrich2_image = pygame.image.load("pictures/ostrich.png")
    if ostrich2_rect.left >= width: 
        ostrich2_image = pygame.image.load("pictures/ostrich2.png")

# TEXTY
    system_font = pygame.font.SysFont("Moncerat", 64)
    system_text = system_font.render(f"{score}", True, lorange)
    system_text_rect = system_text.get_rect()
    system_text_rect.center = (175,35)

    system_font2 = pygame.font.SysFont("Moncerat", 64)
    system_text2 = system_font2.render(f"{penize}", True, lblue)
    system_text2_rect = system_text2.get_rect()
    system_text2_rect.center = (450,35)

    system_font5 = pygame.font.SysFont("Moncerat", 64)
    system_text5 = system_font5.render(f"{level}", True, white)
    system_text5_rect = system_text2.get_rect()
    system_text5_rect.center = (1575,35)

    if level == 0:
        system_font6 = pygame.font.SysFont("Moncerat", 21)
        system_text6 = system_font6.render("10K coins to upgrade", True, lblue)
        system_text6_rect = system_text6.get_rect()
        system_text6_rect.center = (1500,550)
    if level == 1:
        system_font6 = pygame.font.SysFont("Moncerat", 21)
        system_text6 = system_font6.render("50K coins to upgrade", True, lblue)
        system_text6_rect = system_text6.get_rect()
        system_text6_rect.center = (1500,550)
  
    if luck < 1000:
        system_font1 = pygame.font.SysFont("Moncerat", 24)
        system_text1 = system_font1.render(f"{luck}/1000", True, green)
        system_text1_rect = system_text1.get_rect()
        system_text1_rect.center = (1510,855)
    if luck > 1000 and luck < 5000:
        system_font1 = pygame.font.SysFont("Moncerat", 24)
        system_text1 = system_font1.render(f"{luck}/5000", True, green)
        system_text1_rect = system_text1.get_rect()
        system_text1_rect.center = (1510,855)
    if luck > 5000 and luck < 15000:
        system_font1 = pygame.font.SysFont("Moncerat", 24)
        system_text1 = system_font1.render(f"{luck}/15000", True, green)
        system_text1_rect = system_text1.get_rect()
        system_text1_rect.center = (1510,855)
    if luck > 15000:
        system_font1 = pygame.font.SysFont("Moncerat", 24)
        system_text1 = system_font1.render(f"{luck}", True, green)
        system_text1_rect = system_text1.get_rect()
        system_text1_rect.center = (1510,855)

    if food < 50:
        system_font3 = pygame.font.SysFont("Moncerat", 24)
        system_text3 = system_font3.render(f"{food}/50", True, pink)
        system_text3_rect = system_text3.get_rect()
        system_text3_rect.center = (1510,360)
    if food > 50 and food < 150:
        system_font3 = pygame.font.SysFont("Moncerat", 24)
        system_text3 = system_font3.render(f"{food}/150", True, pink)
        system_text3_rect = system_text3.get_rect()
        system_text3_rect.center = (1510,360)
    if food > 150 and food < 500:
        system_font3 = pygame.font.SysFont("Moncerat", 24)
        system_text3 = system_font3.render(f"{food}/500", True, pink)
        system_text3_rect = system_text3.get_rect()
        system_text3_rect.center = (1510,360)              
    if food > 500 and food < 2000:
        system_font3 = pygame.font.SysFont("Moncerat", 24)
        system_text3 = system_font3.render(f"{food}/1000", True, pink)
        system_text3_rect = system_text3.get_rect()
        system_text3_rect.center = (1510,360)           
    if food > 1000 and food < 5000:
        system_font3 = pygame.font.SysFont("Moncerat", 24)
        system_text3 = system_font3.render(f"{food}/2000", True, pink)
        system_text3_rect = system_text3.get_rect()
        system_text3_rect.center = (1510,360)
    if food > 2000:
        system_font3 = pygame.font.SysFont("Moncerat", 24)
        system_text3 = system_font3.render(f"{food}", True, pink)
        system_text3_rect = system_text3.get_rect()
        system_text3_rect.center = (1510,360)

    if food2 < 50:
        system_font4 = pygame.font.SysFont("Moncerat", 24)
        system_text4 = system_font4.render(f"{food2}/50", True, yellow)
        system_text4_rect = system_text4.get_rect()
        system_text4_rect.center = (1510,200)
    if food2 >= 50 and food2 < 150:
        system_font4 = pygame.font.SysFont("Moncerat", 24)
        system_text4 = system_font4.render(f"{food2}/150", True, yellow)
        system_text4_rect = system_text4.get_rect()
        system_text4_rect.center = (1510,200)               
    if food2 >150 and food2 < 500:
        system_font4 = pygame.font.SysFont("Moncerat", 24)
        system_text4 = system_font4.render(f"{food2}/500", True, yellow)
        system_text4_rect = system_text4.get_rect()
        system_text4_rect.center = (1510,200)                  
    if food2 >= 500 and food2 < 2000:
        system_font4 = pygame.font.SysFont("Moncerat", 24)
        system_text4 = system_font4.render(f"{food2}/1000", True, yellow)
        system_text4_rect = system_text4.get_rect()
        system_text4_rect.center = (1510,200)
    if food2 >= 1000 and food2 < 5000:
        system_font4 = pygame.font.SysFont("Moncerat", 24)
        system_text4 = system_font4.render(f"{food2}/2000", True, yellow)
        system_text4_rect = system_text4.get_rect()
        system_text4_rect.center = (1510,200)
    if food2 >= 2000:
        system_font4 = pygame.font.SysFont("Moncerat", 24)
        system_text4 = system_font4.render(f"{food2}", True, yellow)
        system_text4_rect = system_text4.get_rect()
        system_text4_rect.center = (1510,200)

    if food3 < 50:
        system_font7 = pygame.font.SysFont("Moncerat", 24)
        system_text7 = system_font7.render(f"{food3}/50", True, beige)
        system_text7_rect = system_text7.get_rect()
        system_text7_rect.center = (1500,220)
    if food3 >= 50 and food3 < 150:
        system_font7 = pygame.font.SysFont("Moncerat", 24)
        system_text7 = system_font7.render(f"{food3}/150", True, beige)
        system_text7_rect = system_text7.get_rect()
        system_text7_rect.center = (1500,200)
    if food3 >= 150 and food3 < 500:
        system_font7 = pygame.font.SysFont("Moncerat", 24)
        system_text7 = system_font7.render(f"{food3}/500", True, beige)
        system_text7_rect = system_text7.get_rect()
        system_text7_rect.center = (1500,220)              
    if food3 >= 500 and food3 < 1000:
        system_font7 = pygame.font.SysFont("Moncerat", 24)
        system_text7 = system_font7.render(f"{food3}/1000", True, beige)
        system_text7_rect = system_text7.get_rect()
        system_text7_rect.center = (1500,220)           
    if food3 >= 1000 and food3 < 2000:
        system_font7 = pygame.font.SysFont("Moncerat", 24)
        system_text7 = system_font7.render(f"{food3}/2000", True, beige)
        system_text7_rect = system_text7.get_rect()
        system_text7_rect.center = (1500,220)
    if food3 >= 2000 and food3 < 4000:
        system_font7 = pygame.font.SysFont("Moncerat", 24)
        system_text7 = system_font7.render(f"{food3}/4000", True, beige)
        system_text7_rect = system_text7.get_rect()
        system_text7_rect.center = (1500,220)
    if food3 >= 4000:
        system_font7 = pygame.font.SysFont("Moncerat", 24)
        system_text7 = system_font7.render(f"{food3}", True, beige)
        system_text7_rect = system_text7.get_rect()
        system_text7_rect.center = (1500,220)


    custom_font1 = pygame.font.SysFont("Moncerat", 20)
    custom_text1 = custom_font1.render("money can't buy happiness", True, orange)
    custom_text1_rect = custom_text1.get_rect()
    custom_text1_rect.center = (1500,747)

    custom_font2 = pygame.font.SysFont("Moncerat", 28)
    custom_text2 = custom_font2.render("SHOP", True, orange)
    custom_text2_rect = custom_text2.get_rect()
    custom_text2_rect.center = (1500,596)

    custom_font3 = pygame.font.SysFont("Moncerat", 20)
    custom_text3 = custom_font3.render("(press b to buy 100)", True, orange)
    custom_text3_rect = custom_text3.get_rect()
    custom_text3_rect.center = (1500,700)

    custom_font4 = pygame.font.SysFont("Moncerat", 64)
    custom_text4 = custom_font4.render("Monkey Business", True, orange)
    custom_text4_rect = custom_text4.get_rect()
    custom_text4_rect.center = (800,30)

    custom_font5 = pygame.font.SysFont("Moncerat", 20)
    custom_text5 = custom_font5.render("(press f to feed 100)", True, orange)
    custom_text5_rect = custom_text5.get_rect()
    custom_text5_rect.center = (1500,80)

    custom_font6 = pygame.font.SysFont("Moncerat", 44)
    custom_text6 = custom_font6.render("L:", True, white)
    custom_text6_rect = custom_text6.get_rect()
    custom_text6_rect.center = (1480,35)

# PŘIDÁNÍ POZADÍ
    if level == 0:
        screen.blit(background_img,(0,0))
    if level == 1:
        screen.blit(background2_img,(0,0))

# PŘIDÁNÍ OBRÁZKŮ (BLIT)
    screen.blit(rain_image, rain_rect)
    screen.blit(money_image, money_rect)
    if luck >= 1000:
        screen.blit(money1_image, money1_rect)
    if luck >= 5000:
        screen.blit(money2_image, money2_rect)
    if luck >= 15000:
        screen.blit(money3_image, money3_rect)
    #lv1
    if level == 1:  
        if food3 > 50:
            screen.blit(egg2_image, egg2_rect)
        screen.blit(ostrich2_image, ostrich2_rect)
    #lv0:
    if level == 0: 
        if food2 > 50 and level == 0:
            screen.blit(egg_image, egg_rect)
        screen.blit(duck_image, duck_rect)
        if food > 50 and level == 0:
            screen.blit(rypak_image, rypak_rect)
        screen.blit(bank_image, bank_rect)
    
    screen.blit(home_image, home_rect)
    screen.blit(atm_image, atm_rect)
    screen.blit(clover_image, clover_rect)
    screen.blit(food_image, food_rect)
    screen.blit(coin_image, coin_rect)
    screen.blit(up_image, up_rect)
    

# PŘIDÁNÍ TVARŮ
    pygame.draw.line(screen, black, (0,70),(1600,70), 3)
    pygame.draw.line(screen, white, (0,400),(1600,400), 3)

# PŘIDÁNÍ TEXTŮ (BLIT)
    screen.blit(system_text, system_text_rect)
    screen.blit(system_text1, system_text1_rect)
    screen.blit(system_text2, system_text2_rect)
    #lv1
    if level == 0:
        screen.blit(system_text3, system_text3_rect)
    if level == 0:
        screen.blit(system_text4, system_text4_rect)
    #lv2
    if level == 1:
        screen.blit(system_text7, system_text7_rect)

    screen.blit(system_text5, system_text5_rect)
    screen.blit(system_text6, system_text6_rect)

    screen.blit(custom_text1, custom_text1_rect)
    screen.blit(custom_text2, custom_text2_rect)
    screen.blit(custom_text3, custom_text3_rect)
    screen.blit(custom_text4, custom_text4_rect)
    screen.blit(custom_text5, custom_text5_rect)
    screen.blit(custom_text6, custom_text6_rect)

# HLAVNÍ POSTAVA OPICE (BLIT)
    screen.blit(cat_image, cat_rect)

# UPGRADE OBRAZOVKY
    pygame.display.update()

pygame.quit()