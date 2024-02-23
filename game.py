import pygame
from player import player

#creation d'une classe charger de gerer les composant du jeu

class Game:
    
    def __init__(self):
          self.player = player() #creation de notre personnage joueur
          self.pressed =  {}

