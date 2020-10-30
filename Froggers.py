import sys
import pygame
import tkinter as tk

# add framework to sys path 
# (dont want a repeat of *last time*)
sys.path.insert (0, "Framework")

from Framework.Game import *
from Screens.MainMenuScreen import *
from Screens.GameOverScreen import *
from Framework.ResourceManagement.ResourceCache import *
from gachaTools.CardCollection import *

# Froggers game instance
class FroggersGame (Game):
    def __init__(self, w=1366,h=768):
        super().__init__(title = "Froggers", width=w, height=h)

        cardCollection = CardCollection (self) 

        # initialise tkinter
        root = tk.Tk()
        root.withdraw()

        self.ChangeScreen (MainMenuScreen(self))
        #self.ChangeScreen (GachaplayScreen(self, 8))    

    def Update (self):
        super().Update()

    def Draw (self):
        super().Draw()

    def Run(self):
        super().Run()

# entry point
game = FroggersGame(1366, 768)
game.Run()  
