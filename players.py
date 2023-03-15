import pygame

class Player:

    def __init__(self, name, level, img, in_map = False):
        self.img = img
        self.name = name
        if in_map == True:
            self.level = level
    
    def attack(self):
        return "Útok"

class WizardPlayer(Player):

    def __init__(self, element, name, level, img):
        super().__init__(name, level, img, in_map = False)
        self.element = element
        
    def attack(self):
        return "Útok *"
    

class ArcherPlayer(Player):

    def __init__(self, animal, name, level):
        super().__init__(name, level, in_map = False)
        self.animal = animal
        
    def attack(self):
        return "Útok ->"
    
#lidi
#player0 = Player("Sam", 1)

#kouzelníci
player1 = WizardPlayer("Dave","fire", 1,("img/firemag.png"))

"""player2 = WizardPlayer("Anna", "water", 1)
player3 = WizardPlayer("Ronald", "earth", 1)
player4 = WizardPlayer("Jinora","wind", 1)
player5 = WizardPlayer("Amon" ,"black magic", 1)

#lukostřelci
player6 = ArcherPlayer("Robin", "bird", 1)
player7 = ArcherPlayer("Parek", "wolf", 1)
player8 = ArcherPlayer("Amy", "bear", 1)"""




