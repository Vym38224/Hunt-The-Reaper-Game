class Background:
    def __init__(self, img):
        self.img = img


class Player:
    def __init__(self, name, hp, img, img2, img_attack, img_attack2):
        self.name = name
        self.hp = hp
        self.img = img
        self.img2 = img2
        self.img_attack = img_attack
        self.img_attack2 = img_attack2
      

class WizardPlayer(Player):
    def __init__(self, name, element, hp, img, img2, img_attack, img_attack2):
        super().__init__(name, hp, img, img2, img_attack, img_attack2)
        self.element = element
    

class ArcherPlayer(Player):
    def __init__(self, name, animal, hp, img, img2, img_attack, img_attack2):
        super().__init__(name, hp, img, img2, img_attack, img_attack2)
        self.animal = animal
        
class EnemyPlayer:
    def __init__(self, name, hp, img, img2):
        self.name = name
        self.hp = hp
        self.img = img
        self.img2 = img2



#Background
background_home = Background(("img/background_home.png"))
background_spider = Background(("img/background_spider.png"))
background_skelet = Background(("img/background_skelet.png"))
background_goblin = Background(("img/background_goblin.png"))
background_ghost = Background(("img/background_ghost.png"))
    
#lidi
player0 = Player("Sam", 1000,("img/human.png"),("img/human2.png"),("img/human_attack.png"),("img/human_attack2.png"))

#kouzelníci
player1 = WizardPlayer("Dave","fire", 300,("img/firemag.png"),("img/firemag2.png"),("img/fireball.png"),("img/fireball2.png"))
player2 = WizardPlayer("Anna", "water", 125,("img/watermag.png"),("img/watermag2.png"),("img/watermag_attack.png"),("img/watermag_attack2.png"))

#lukostřelci
player3 = ArcherPlayer("Robin", "bird", 400,("img/archer.png"),("img/archer2.png"),("img/arrow.png"),("img/arrow2.png"))

#enemáci
 
enemy0 = EnemyPlayer("Kostlivec", 25,("img/sceleton.png"),("img/sceleton2.png"))
enemy1 = EnemyPlayer("BOSS Kostlivec", 200,("img/scelet_boss.png"),("img/scelet_boss2.png"))

enemy2 = EnemyPlayer("Pavouk", 15, ("img/spider.png"),("img/spider2.png"))
enemy3 = EnemyPlayer("BOSS Pavouk", 125, ("img/spider_boss.png"),("img/spider_boss2.png"))

enemy4 = EnemyPlayer("Goblin", 50, ("img/goblin.png"),("img/goblin2.png"))
enemy5 = EnemyPlayer("BOSS Goblin", 1000, ("img/goblin_boss.png"),("img/goblin_boss2.png"))

enemy6 = EnemyPlayer("Ghost", 60, ("img/ghost.png"),("img/ghost2.png"))
enemy7 = EnemyPlayer("Ghost", 750, ("img/ghost_boss.png"),("img/ghost_boss2.png"))




