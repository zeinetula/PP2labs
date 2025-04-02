#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing
pygame.init()

#Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load(r"lab8\textures\AnimatedStreet.png")

#Create a white screen
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\ayanz\OneDrive\Desktop\PP2labs\lab8\textures\coin.png")
        self.image = pygame.transform.scale(self.image, (int(20), int(20)))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 520)
    def move(self):
        #random width
        sc= int(random.randint(5, 40))
        self.image = pygame.transform.scale(self.image, (int(sc),int(20)))
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 520)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"lab8\textures\Enemy.png")
        self.image = pygame.transform.scale(self.image, (int(50), int(100)))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"lab8\textures\Player.png")
        self.image = pygame.transform.scale(self.image, (int(50), int(100)))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        #if pressed_keys[K_UP]:
        #self.rect.move_ip(0, -5)
        #if pressed_keys[K_DOWN]:
        #self.rect.move_ip(0,5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

#Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
n=10

#Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
ac=False
#Game Loop
while True:

    #accelerator
    if (ac==False and COINS==n):
        SPEED += 10
        ac=True
    #Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coinsscore = font_small.render(str(COINS), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coinsscore, (SCREEN_WIDTH-20,10))



    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)

        if ((entity in coins)==False):
            entity.move()

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(r'lab8\sounds\crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    #coins-player collision
    if pygame.sprite.spritecollideany(P1, coins):
        COINS+=1
        ColCoins=pygame.sprite.spritecollide(P1,coins,False)
        for i in ColCoins:
            i.move()
    pygame.display.update()
    FramePerSec.tick(FPS)