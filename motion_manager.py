import pygame

last_block = (-1, -1)

def pos_to_block(x, y):
    x_count = x // 30
    y_count = y // 30
    return x_count, y_count


def hover(display, x, y, image_path):
    x_count = x // 30
    y_count = y // 30
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (26, 26))
    display.blit(image, (x_count*30 + 3, y_count*30 + 3))
    #pygame.draw.rect(display, color, (x_count*30 + 1, y_count*30 + 1, 30, 30))
