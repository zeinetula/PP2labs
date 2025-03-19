import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        pygame.mixer.music.load('foo.mp3')
                        pygame.mixer.music.play(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                        pygame.mixer.music.stop

                
        pygame.display.flip()