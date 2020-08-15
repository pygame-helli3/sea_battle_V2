import pygame
import csv

class Ship:
    pos_x = 0
    pos_y = 0

    def __init__(self, ID, display, image_path, length, width, ix, iy):
        self.ID = ID
        self.image_path = image_path
        self.display = display
        self.length = length
        self.width = width
        self.image = pygame.transform.scale(pygame.image.load(image_path), (width, length))

        Ship.pos_x = ix
        Ship.pos_y = iy
        self.image = pygame.transform.rotate(self.image, 90)

    def build(self):
        self.display.blit(self.image, (Ship.pos_x, Ship.pos_y))

    def move(self, x, y):

        # set curser on the center of the ship
        Ship.pos_x = int(x - self.length / 2)
        Ship.pos_y = int(y - self.width / 2)

        #reading ships locations from database
        ships = {}

        ships_file = csv.reader(open('ships_location.csv', 'r+'))  # get ships location from database
        for ship in ships_file:
            if ship:
                ship = list(map(int, ship))
                ship_id = ship[0]
                ship_x = ship[1]
                ship_y = ship[2]
                ships[ship_id] = [ship_x, ship_y]

        #setting new coordinates for the moving ship
        ships[self.ID] = [Ship.pos_x, Ship.pos_y]

        #apply on database
        ships_file_writer = csv.writer(open('ships_location.csv', 'w'))
        for ship_id in ships.keys():
            ships_file_writer.writerow((ship_id, ships[ship_id][0], ships[ship_id][1], self.length, self.width))


        self.display.blit(self.image, (Ship.pos_x, Ship.pos_y))
