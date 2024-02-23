import pygame

class enemy(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1   
        self.image = pygame.image.load("C:\\Users\\0n3Th1nG\\Desktop\\Xe\\python-g\\PygameAssets-main\\mummy.Png")
        self.rect = self.image.get_rect()
        self.rect.x = 620
        self.rect.y = 470     
    def forward(self):
        # le deplacement se fait si il n'y a pas de collision avec un groupe de joueurs
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocity 
    
