import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
WIDTH, HEIGHT = 800, 600
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        pygame.mixer.music.load(r'C:\Users\ayanz\OneDrive\Desktop\PP2labs\lab7\audios\Kanye West feat. Pusha T - Runaway.mp3')
                        pygame.mixer.music.play(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                        pygame.mixer.music.pause()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                        pygame.mixer.music.unpause()



                
        pygame.display.flip()