import pygame
from player import player
from enemy import enemy

#creation d'une classe charger de gerer les composant du jeu

class Game:
    
    def __init__(self):
          self.all_player = pygame.sprite.Group()
          self.player = player(self) #creation de notre personnage joueur
          self.all_player.add(self.player)
          self.all_monster = pygame.sprite.Group()
          self.pressed =  {}
          self.spawn_monster()
          
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = enemy(self)
        self.all_monster.add(monster)
            
        
