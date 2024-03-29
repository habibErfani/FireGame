import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):

        super().__init__()
        self.velocity = 1
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origine_image = self.image
        self.angle = 0

    def rotate(self):
        #tourner les projctiles
        self.angle += 4
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
    def remove(self):
        self.player.all_projectiles.remove(self)
    
    def move(self):
        self.rect.x += self.velocity
        self.rotate()


        #verifie si le projectile n'est plus present sur l'ecran

        if self.rect.x > 1080:
            self.remove()
            #print ("propjectile deleted")

