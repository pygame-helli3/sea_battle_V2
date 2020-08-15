import pygame
import sys
import math
from board import Board
from ship import Ship
import motion_manager
import csv
import drag_manager

def in_range(first, last, radius):
    if math.sqrt((first[0] - last[0]) ** 2 + (first[1] - last[1]) ** 2) < radius:
        return True
    return False


pygame.init()

width = 810
height = 480

white = (255, 255, 255)
black = (0, 0, 0)


screen = pygame.display.set_mode((width, height))

screen.fill(white)

board = Board(screen) #initate board

ships = {}

button = 'Up'
motion = False
drag = False
last_down = []
last_pos = []

while True:
    ships_file = csv.reader(open('ships_location.csv', 'r+')) #get ships location from database
    for ship in ships_file:
        if ship:
            ship = list(map(int, ship))
            ship_id = ship[0]
            ship_x = ship[1]
            ship_y = ship[2]
            ships[ship_id] = [ship_x, ship_y]

    hover = True
    screen.fill(white)
    board.draw()
    ship41 = Ship(41, screen, 'assets/images/ship.jpg', 120, 30, ships[41][0], ships[41][1])
    ship41.build()
    ship31 = Ship(31, screen, 'assets/images/ship.jpg', 90, 30, ships[31][0], ships[31][1])
    ship31.build()

    for event in pygame.event.get():

        if event.type == 12:  # exit
            sys.exit()

        if event.type == 5:  # Button down
            last_down = event.pos
            button = 'Down'

        if event.type == 4:  # motion
            last_pos = event.pos
            if button == 'Down':  # Drag
                position = event.pos
                if not in_range(position, last_down, 5):
                    drag = True

        if event.type == 6:  # Button up
            position = event.pos

            if drag:  # Drop
                print('Drop')
                drag = False
                button = 'Up'
            if button == 'Down' and in_range(position, last_down, 5):  # click in range
                button = 'Up'
                print('click')
            elif motion and button == 'Down':  # drag and drop
                button = 'Up'
                motion = False
                print('drag and drop')

    #motion_manager.hover(screen, last_pos[0], last_pos[1], 'assets/images/cross.jpg')
    if drag:
        ship_id = drag_manager.get_ship_id(screen, event.pos[0], event.pos[1])
        if ship_id:
            if ship_id == 31:
                ship31.move(event.pos[0], event.pos[1])
            if ship_id == 41:
                ship41.move(event.pos[0], event.pos[1])


    pygame.display.update()