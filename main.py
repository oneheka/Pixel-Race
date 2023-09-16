import pygame

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((512, 512))
screen.fill((255,255,255))

font = pygame.font.SysFont('Comic Sans MS', 30)

running = True

while running:
    text_surface = font.render('Some Text', False, (0, 0, 0))
    screen.blit(text_surface, (0,0))
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False
    pygame.display.flip()

pygame.quit()
