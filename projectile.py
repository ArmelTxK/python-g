import pygame
 
class projectile(pygame.sprite.Sprite):
    
    def __init__(self, player):
        
        super().__init__()
        self.velocity = 1
        self.player = player
        self.porter_max = 500
        self.image = pygame.image.load("C:\\Users\\0n3Th1nG\\Desktop\\2d games test\\PygameAssets-main\\projectile.Png")
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 125
        self.rect.y = player.rect.y + 88
        self.origine_image = self.image
        self.angle = 0
        
    def rotation(self):
        self.angle += 1
        self.image  = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)
    def remove(self, player):
                self.player.all_bullet.remove(self)
                
    def move(self):
            self.rect.x += self.velocity
            self.rotation()
            if self.rect.x>self.porter_max:
                self.remove(self.player)
                print("projectille detruit!")
