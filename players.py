class Background:
    def __init__(self, img):
        self.img = img


class Player:
    def __init__(self, name, level, img, img2, img_attack, img_attack2, in_map = False):
        self.name = name
        self.level = level
        self.img = img
        self.img2 = img2
        self.img_attack = img_attack
        self.img_attack2 = img_attack2
        if in_map == True:
            pass
              
    def attack(self):
        return "Útok"


class WizardPlayer(Player):
    def __init__(self, name, element, level, img, img2, img_attack, img_attack2):
        super().__init__(name, level, img, img2, img_attack, img_attack2, in_map = False)
        self.element = element
        
    def attack(self):
        return "Útok *"
    

class ArcherPlayer(Player):
    def __init__(self, name, animal, level):
        super().__init__(name, level, in_map = False)
        self.animal = animal
        
    def attack(self):
        return "Útok ->"
    

#Background
background = Background(("img/background.png"))
    
#lidi
player0 = Player("Sam", 1,("img/human.png"),("img/human_attack.png"))

#kouzelníci
player1 = WizardPlayer("Dave","fire", 1,("img/firemag.png"),("img/firemag2.png"),("img/fireball.png"),("img/fireball2.png"))
player2 = WizardPlayer("Anna", "water", 1,("img/watermag.png"),("img/watermag2.png"),("img/watermag_attack.png"),("img/watermag_attack2.png"))

"""player3 = WizardPlayer("Ronald", "earth", 1)
player4 = WizardPlayer("Jinora","wind", 1)
player5 = WizardPlayer("Amon" ,"black magic", 1)

#lukostřelci
player6 = ArcherPlayer("Robin", "bird", 1)
player7 = ArcherPlayer("Parek", "wolf", 1)
player8 = ArcherPlayer("Amy", "bear", 1)"""




