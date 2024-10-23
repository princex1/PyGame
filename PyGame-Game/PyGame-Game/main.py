import pygame
import sys
pygame.init()
window = pygame.display.set_mode((600, 360))
pygame.display.set_caption('fist game')
clock = pygame.time.Clock()

surface = pygame.image.load('images/bg.png')
character = pygame.image.load('images/main_char11.png')
diamond = pygame.image.load('images/diamond2.png')
character_x_pos = 450
character_y_pos = 105
D_1_pos_x = 200
D_2_pos_x = 100
D_3_pos_x = 0

while True:
    input_ = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if input_[pygame.K_a]:
        print(character_x_pos)
        character_x_pos -= 6
    elif input_[pygame.K_d]:
        print(character_x_pos)
        character_x_pos += 6
    # elif input_[pygame.K_w]:
    #     character_y_pos -= 10
    # elif input_[pygame.K_s]:
    #     character_y_pos += 10
    if character_x_pos < -50:
        character_x_pos = 570
    elif character_x_pos > 650:
        character_x_pos = -50
    elif character_x_pos < 200:
        D_1_pos_x = -200
    if character_x_pos < 50:
        D_2_pos_x = 700
    if character_x_pos < 0:
        D_3_pos_x = -200

    window.blit(surface, (0, 0))
    window.blit(character, (character_x_pos, character_y_pos))
    window.blit(diamond, (D_1_pos_x, 206))
    window.blit(diamond, (D_2_pos_x, 206))
    window.blit(diamond, (D_3_pos_x, 206))
    pygame.display.update()
    clock.tick(60)
