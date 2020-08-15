import pygame
import csv

ships = {}

def get_ship_id(display, pos_x, pos_y):
    ships_file = csv.reader(open('ships_location.csv', 'r+'))
    for ship in ships_file:
        if ship:
            ship = list(map(int, ship))
            ship_id = ship[0]
            ship_x = ship[1]
            ship_y = ship[2]
            ship_length = ship[3]
            ship_width = ship[4]

            pygame.draw.rect(display, (0,0,0), (ship_x, ship_y, ship_length, ship_width))
            if ship_x - ship_length // 2 <= pos_x and ship_x + ship_length // 2 >= pos_x:
                if ship_y - ship_width // 2 <= pos_y and ship_y + ship_width // 2 >= pos_y:
                    return ship_id
            if ship_length // 2 + ship_x > pos_x > ship_length // 2 - ship_x:
                if ship_width // 2 + ship_y > pos_y > ship_width // 2 - ship_y:
                    return ship_id

