import pygame

class Board:
    def __init__(self, display, pos_x=30, pos_y=30, x_count=10, y_count=10, block_size=30, color=(0, 0, 0)):
        self.display = display
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.y_count = y_count
        self.x_count = x_count
        self.block_size = block_size
        self.color = color

    def draw(self):
        display_x_count = self.display.get_width() // self.block_size
        display_y_count = self.display.get_height() // self.block_size

        for i in range(display_y_count + 1):
            pygame.draw.line(self.display,
                             (150, 150, 150),
                             (0, i * self.block_size),
                             (display_x_count * self.block_size, i * self.block_size))
        for i in range(display_x_count + 1):
            pygame.draw.line(self.display,
                             (150, 150, 150),
                             (i * self.block_size, 0),
                             (i * self.block_size, display_y_count * self.block_size))

        for i in range(self.y_count + 1):
            pygame.draw.line(self.display,
                             self.color,
                             (self.pos_x, i * self.block_size + self.pos_x),
                             (self.pos_x + self.x_count * self.block_size, i * self.block_size + self.pos_x),
                             2)
        for i in range(self.x_count + 1):
            pygame.draw.line(self.display,
                             self.color,
                             (i * self.block_size + self.pos_y, self.pos_y),
                             (i * self.block_size + self.pos_y, self.pos_y + self.y_count * self.block_size),
                             2)