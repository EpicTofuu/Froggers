import pygame
import random
import math
from Framework.GeometricGroup import *
from Framework.TileSurface import *
from GameObjects.turfs.RailTurf import *
from GameObjects.turfs.RoadTurf import *
from GameObjects.turfs.GrassTurf import *
from GameObjects.turfs.LakeTurf import *
from Framework.KeyboardListener import *
from Stats import GameStats
import logging

# the physical composition of the level itself.
class Level (GeometricGroup): 
    def __init__(self, game, stats = GameStats(), difficulty=1, properties = None):
        super().__init__()
        
        self.properties = properties
        self.game = game
        self.stats = stats

        # arbitrary value defining relatively difficulty of current level
        # influences variables like level length, entity speeds, general complexity etc
        self.difficulty = difficulty if properties is None else properties["difficulty"]

        # list of all available turfs
        self.turfs = [RailTurf, RoadTurf, LakeTurf]

        self.length = 0

    # randomly generates the level
    def generate (self, seed = None):
        self.empty()
        logging.info ("Starting level {0}".format(self.difficulty))

        # if no seed is available, generate a random one
        if seed is None:
            seed = random.randint (0,2147483647)    # maximum int size for maximum number of seeds :)
            
        random.seed (seed)      # set the seed   
        logging.info (seed)

        self.stats.Seeds.append (str(seed)) # add seed to the seeds list

        # number of turfs to be generated
        _upperbound = math.log (self.difficulty + 2)
        _lowerbound = 2 * math.log (self.difficulty + 2)
        self.turflen = random.randint (math.ceil (_upperbound), math.ceil (_lowerbound)) 

        #print (self.turflen)

        # list of all turfs in the level
        self.levelturfs = list()

        # first strip
        self.levelturfs.append (GrassTurf(self.game))
        self.length += 3 * 64

        # generate turfs
        for _ in range(self.turflen):
            # add turf to level turfs
            self.turfid = random.randint (0, len (self.turfs)-1)
            self.directions = [-1, 1]
            self.workingturf = self.turfs[self.turfid](self.difficulty, self.directions[random.randint (0,1)], self.game)

            # place the turf (should be directly adjacent to all other turfs)
            self.workingturf.change_pos_y (self.length)
            self.length += self.workingturf.background.rect.height

            self.levelturfs.append (self.workingturf)

        # last strip
        self._l = GrassEndTurf(self.game)
        # place the turf (should be directly adjacent to all other turfs)
        for t in self.levelturfs:
            self._l.change_pos_y (t.background.rect.height)
        self.levelturfs.append (self._l)

        for t in self.levelturfs:
            self.Add (t)
        
    # this update method is NOT included in the group call
    # and is instead called MANUALLY
    def Update (self):
        self.performculling()
    
    # prevents turfs that aren't currently on screen from drawing
    # marginally increases performance
    def performculling (self):
        for t in self.levelturfs:
            # check if the turf is on screen
            if (t.background.rect.bottom >= 0 and t.background.rect.y < pygame.display.get_surface().get_size()[1]):
                t.Active()
                t.Update()
            else:
                t.NonActive()