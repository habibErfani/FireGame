import pygame
pygame.init()
from game import Game

pygame.display.set_caption("Kevin Game")
screen = pygame.display.set_mode((1080,720))

game = Game()
background = pygame.image.load('assets/bg.jpg')

running = True
while running:
  
    
#appliquer l'arrere plan de notre jeu


    screen.blit(background, (0,0))

    "appliquer l'image de mon joeouer"
    screen.blit(game.player.image, game.player.rect)

    #recuperrer les projectiles

    for projectile in game.player.all_projectiles:
        projectile.move()

    game.player.all_projectiles.draw(screen)
    #mettre a jour la fenetre
    pygame.display.flip()


    

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width <1080:
        game.player.move_right()
        
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x>0:
        game.player.move_left()


    #si le joeuur ferme la fenetre
    for event in pygame.event.get():

        if event.type ==pygame.QUIT:
            running=False
            pygame.quit()

        #detecter si un joueur touche le clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #si la touche espace est enclanche pour tirer
            if event.key == pygame.K_SPACE:
                game.player.lunch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

    

