import pygame
from game import Game


pygame.init()



#creation de la fenetre de notre jeu

pygame.display.set_caption("Alien invasion")
screen = pygame.display.set_mode((800,600))

game = Game()
#gestion du fonctionnement de la fenêtre de jeu

running = True #fonction charger de la verification du fonctionnement de notre jeu

#creation de l'arriere plan de notre fenetre

background = pygame.image.load("C:\\Users\\0n3Th1nG\\Desktop\\Xe\\python-g\\PygameAssets-main\\bg.jpg")  #variable chargé contenir l'arriere plan de notre jeu 
 

while running:
   
    screen.blit(background, (0,-250 )) #affichage de l'arriere plan sur la fenetre
    
    screen.blit(game.player.image, game.player.rect)
    
    #faire avancé les projectile déja présent sur le terrain
    for projectille in game.player.all_bullet:
        projectille.move()
    #faire avancé des monstres vers notre joueurs
    for enemy in game.all_monster :
        enemy.forward()
    
    
    
    #faire  apparaitre les projectilles lorsque le joueur appuis sur la touche 
    game.player.all_bullet.draw(screen)
    
    #faire apparaitres des monstres
    game.all_monster.draw(screen)
    
    print(game.pressed)
    print(game.player.rect.x)
    #verifier si le joueur souhaites ce déplacer
    if game.pressed.get(pygame.K_q) and game.player.rect.x   >-59:
        game.player.move_left()
    elif game.pressed.get(pygame.K_d) and game.player.rect.x  < 649:
        game.player.move_right()
    
    pygame.display.flip() #fontion chargé de l'actualisation de la fenetre
    
     #ici on verifiera si l'utilisateur ferme la fenetre de jeu et si c'est le cas on la ferme
    for event in pygame.event.get(): 
        
        if event.type == pygame.QUIT: #on verifie si l'évenement effectuer est la fermeture de la fenetre
            
            running = False 
            pygame.quit()
            print("bye bye")
        #gestion du déplacement du joueur
        
        elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
                
                #definition de la touche de tire et attribution de la fonction charger de celui ci
                if event.key == pygame.K_t:
                    game.player.shoot()
                    print("tire!")
        elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
  
           