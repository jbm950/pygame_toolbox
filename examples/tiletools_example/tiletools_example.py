#-------------------------------------------------------------------------------
# Name:        tiletools_example.py
# Purpose:     This module will go over how to use the basic classes in the
#              graphics module
#
# Contributors: James Milam
#
# Created:     01/06/2015
# Copyright:   (c) James 2015
# Licence:     MIT Licence
# Version:     0.1
# Written for: Python 3.3
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# Import the tile game toolbox, pygame and sys
import pygame_toolbox.tilegame_tools as pttt
import pygame, sys

# Create a custom Tile class
class Tile(pttt.Tile):
    def __init__(self,file,size):
        # Pass the file and size arguments to the init of the class
        # in the toolbox
        pttt.Tile.__init__(self,file,size)
        # Add a shade to the tiles shade dictionary
        pttt.Tile.initialize_shade(self,"orange red",(255,69,0),150)

# Create the tilemap object that will handle displaying all of the
# tiles
class Tilemap(pttt.Tilemap):
    def __init__(self,tilelist):
        pttt.Tilemap.__init__(self,(800,600),tilelist,1)

class Main:
    def __init__(self):
        # Create a 4x4 matrix of tiles and use the tilelist class to
        # obtain additional functionality for the matrix.
        self.tilelist = pttt.Tilelist([[Tile('forrest.png',(200,150)) for i in range(0,4)],
                                       [Tile('forrest.png',(200,150)) for i in range(0,4)],
                                       [Tile('forrest.png',(200,150)) for i in range(0,4)],
                                       [Tile('forrest.png',(200,150)) for i in range(0,4)]])
        self.clock = pygame.time.Clock()
        self.progress = 1
    def update(self,screen):
        while True:
            if self.progress == 1:
                # When a tile is clicked shade the 4 tiles around it
                # using the orange red shade we created
                tileclicked = Tilemap(self.tilelist).update(screen,self.clock)
                adjtiles = self.tilelist.adjacent_tiles(tileclicked,'p')
                for i in adjtiles:
                    i.toggle_shade("orange red")

# Initialize pygame and run the script.
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    Main().update(screen)