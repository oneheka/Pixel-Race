import pygame

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((512, 512))
screen.fill((255,255,255))

font = pygame.font.SysFont('Comic Sans MS', 30)

pygame.display.set_caption('Прикол')

while True:
    text_surface = font.render('Начать', False, (0, 0, 0))
    screen.blit(text_surface, (0,0))
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            pygame.quit()
    pygame.display.flip()
