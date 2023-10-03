import pygame
import hui

pygame.init()
pygame.font.init()

with open("level/level1.csv") as file:
    map = [list(map(int, line.strip().split(","))) for line in file]

screen = pygame.display.set_mode((512, 512))
screen.fill((255,255,255))

font = pygame.font.SysFont('Comic Sans MS', 30)

pygame.display.set_caption('Прикол')

player_pos = (1, 1)

tiles = {
    0:
        pygame.image.load("assets/images/bricks.png"),
    1:
        pygame.image.load("assets/images/player.jpg")
}

tile_size = 32

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                map[player_pos[1]][player_pos[0]] = 0
            if event.key == pygame.K_UP:
                if map[player_pos[0]][player_pos[1] - 1] != 1:
                    player_pos = (player_pos[0], player_pos[1] - 1)
            elif event.key == pygame.K_DOWN:
                if map[player_pos[0]][player_pos[1] + 1] != 1:
                    player_pos = (player_pos[0], player_pos[1] + 1)
            elif event.key == pygame.K_LEFT:
                if map[player_pos[0] - 1][player_pos[1]] != 1:
                    player_pos = (player_pos[0] - 1, player_pos[1])
            elif event.key == pygame.K_RIGHT:
                if map[player_pos[0] + 1][player_pos[1]] != 1:
                    player_pos = (player_pos[0] + 1, player_pos[1])


        map[player_pos[1]][player_pos[0]] = 2

        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 0:
                    pygame.draw.rect(screen, (255,255,255), pygame.Rect(j*32, i*32, 32,32))
                if map[i][j] == 1:
                    screen.blit(tiles[0], (j * tile_size, i * tile_size))
                if map[i][j] == 2:
                    screen.blit(tiles[1], (j * tile_size, i * tile_size))
    pygame.display.flip()
