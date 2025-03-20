import pygame
import datetime
import math


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

image = pygame.image.load(r'C:\Users\ayanz\OneDrive\Desktop\PP2labs\lab7\textures\clock.png')
image = pygame.transform.scale(image, (WIDTH, HEIGHT))
min_hand = pygame.image.load(r'C:\Users\ayanz\OneDrive\Desktop\PP2labs\lab7\textures\min_hand.png')
sec_hand = pygame.image.load(r'C:\Users\ayanz\OneDrive\Desktop\PP2labs\lab7\textures\sec_hand.png')

min_rect = min_hand.get_rect()
sec_rect = sec_hand.get_rect()

center_x, center_y = WIDTH // 2, HEIGHT // 2
min_rect.center = (center_x, center_y)
sec_rect.center = (center_x, center_y)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.blit(image, (0, 0))


    date = datetime.datetime.now()

    second = math.ceil(date.second + date.microsecond / 1_000_000)
    minute = date.minute + second / 60

    angle_sec = 360 - (second * 6)  
    angle_min = 310 - (minute * 6)  
    print(str(angle_min)+"--"+str(minute))  

    
    rotated_min = pygame.transform.rotate(min_hand, angle_min)
    min_rect = rotated_min.get_rect(center=(center_x, center_y))
    screen.blit(rotated_min, min_rect.topleft)
    
    rotated_sec = pygame.transform.rotate(sec_hand, angle_sec)
    sec_rect = rotated_sec.get_rect(center=(center_x, center_y))
    screen.blit(rotated_sec, sec_rect.topleft)

    pygame.display.flip()