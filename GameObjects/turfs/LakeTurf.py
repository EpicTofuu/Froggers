from GameObjects.turfs.Turf import Turf
from GameObjects.Entities.Log import *
from Framework.TileSurface import *
import math
import random

class Water (Sprite):
    def __init__(self, rect):
        self.a = pygame.Surface ((1,1))
        super().__init__(img = self.a)
        self.rect = rect

class LakeTurf (Turf):
    def __init__(self, difficulty, direc):
        self.height = random.randrange (3, 6)
        self.width = random.randrange (3,5)
        Turf.__init__ (self, self.height, "res/textures/img_water.jpg")
        self.directions = [-1, 1]
        
        for y in range (self.height - 2):
            self.lanesp = random.randint (3, 7)
            self.lanedir = self.directions[random.randint (0,1)]
            self.laneoffset = random.randrange (0, 64)
            for x in range (math.floor (self.width)):
                self.Add (Log(self.lanedir, (self.laneoffset + x * 64 * 6, (1 + y) * 64), self.lanesp, self.width))
        
        self.waterbox = Water (pygame.Rect (0,64,pygame.display.get_surface().get_size()[0], (self.height - 2) * 64))
        self.Add (self.waterbox)

        # safe strips
        # start
        self.safestriptex = TileSurface ((pygame.display.get_surface().get_size()[0], 64), "res/textures/img_grass.png")
        self.safestripstart = Sprite (img = self.safestriptex)
        self.Add (self.safestripstart)
        
        # end
        self.safestripend = Sprite (img = self.safestriptex)
        self.safestripend.rect.y = (self.height - 1) * 64 
        self.Add (self.safestripend)
    
    def Update(self):
        pass

    def Active (self):
        Turf.Active(self)

    def NonActive (self):
        Turf.NonActive(self)
