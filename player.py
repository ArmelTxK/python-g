import pygame
from projectile import projectile

#creation de notre personnage
class player(pygame.sprite.Sprite):

        def __init__(self) :
              super().__init__()
              self.health = 100
              self.max_health = 100
              self.attack = 15
              self.velocity = 1
              self.all_bullet = pygame.sprite.Group()
              self.image = pygame.image.load("C:\\Users\\0n3Th1nG\\Desktop\\Xe\\python-g\\PygameAssets-main\\player.png")
              self.rect = self.image.get_rect()
              self.rect.y = 430
        def shoot(self):
            #creation d'une instance de projectile et ajout dans notre groupe de projectille
            self.all_bullet.add(projectile(self))
            print("tire!")
        def move_left(self):
            self.rect.x -= self.velocity
          
        def move_right(self):
            self.rect.x += self.velocity
        
   
            
            
        