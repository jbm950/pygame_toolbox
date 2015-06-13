# ------------------------------------------------------------------------------
# Name:        pygame_toolbox.tilegame_tools.py
# Purpose:     This module is the location of multiple classes that will assist
#              in the development of games that use tiles. (like board games not
#              tiled maps)
#
# Contributors: James Milam
#
# Created:     18/05/2015
# Copyright:   (c) James 2015
# Licence:     MIT Licence
# Version:     0.1
# Written for: Python 3.3
# ------------------------------------------------------------------------------
# !/usr/bin/env python

# Module Contents
#   Tile
#   Tilelist
#   Tilemap

from .. import graphics as ptg
import pygame
import sys


class Tile(ptg.Button):
    def __init__(self, file, size):
        """This will load an image and resize it as specified. The class comes
        with shading features and can be used as a parent class for board game
        like tiles that need additional attributes.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            file - This is a string of the picture file name including extension

            size - This is a tuple containing the length and height of the tile

        (doc string updated ver 0.1)
        """

        # Initialize button class and set the picture attribute of the instance
        ptg.Button.__init__(self, 1, file, (0, 0), resize=size)
        self.pic = pygame.Surface(self.image.get_size())
        self.pic.blit(self.image, (0, 0))

        # Set up the shades dictionary. The first item determines if the shade
        # is on and the second item is the surface containing the shade.
        self.shades = {}

        # Create blue and red shades for the tile
        self.initialize_shade('blue', (0, 0, 255), 150)
        self.initialize_shade('red', (255, 0, 0), 150)

    def initialize_shade(self, shade_name, shade_color, alpha):
        """This method will create semi-transparent surfaces with a specified
        color. The surface can be toggled on and off.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            Shade_name - String of the name that you want to associate with the
                surface

            Shade_color - An rgb tuple of the color of the shade

            Alpha - Level of transparency of the shade (0-255 with 150 being a
                good middle value)

        (doc string updated ver 0.1)
        """

        # Create the pygame surface
        self.shades[shade_name] = [0, pygame.Surface(self.image.get_size())]

        # Fill the surface with a solid color or an image
        if type(shade_color) == str:
            background = pygame.image.load(shade_color).convert()
            background = pygame.transform.scale(background,
                                                (self.image.get_width(),
                                                 self.image.get_height()))
            self.shades[shade_name][1].blit(background, (0, 0))
        # Otherwise the background should contain an rgb value
        else:
            self.shades[shade_name][1].fill(shade_color)

        # Set the alpha value for the shade
        self.shades[shade_name][1].set_alpha(alpha)

    def toggle_shade(self, shade):
        """This method will overlay a semi-transparent shade on top of the
        tile's image.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            shade - This will designate which shade you wish to turn on or off.
                Blue and red shades are available by default.

        (doc string updated ver 0.1)
        """

        # First toggle the user specified shade
        if self.shades[shade][0]:
            self.shades[shade][0] = 0
        else:
            self.shades[shade][0] = 1

        # Now draw the image with the active shades
        self.image.blit(self.pic, (0, 0))
        for key in self.shades:
            if self.shades[key][0]:
                self.image.blit(self.shades[key][1], (0, 0))


class Tilelist(list):
    """This class will act as the holding spot for a matrix of tiles with
    additional processing methods that are specific to game making.

    (doc string updated ver 0.1)
    """

    def adjacent_tiles(self, tile, pattern):
            """This will return a list of the tiles adjacent to a given tile.
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            Inputs:
                tile - This is the tile object for which the method will find
                    adjacent tiles.

                pattern - This will designate the pattern type that you want the
                    method to return

                    'p' = plus sign
                    'x' = diagonal
                    'b' = box

            (doc string updated ver 0.1)
            """

            # Initialize the list of tiles to return
            adj_tiles = []

            # Find the row and column of the input tile
            for i in self:
                for j in i:
                    if j == tile:
                        row = self.index(i)
                        column = self[row].index(j)

            # Define functions for the 2 distinct patterns
            def plus_sign(self, row, column):
                nonlocal adj_tiles
                if row - 1 >= 0:
                    adj_tiles += [self[row - 1][column]]
                if row + 1 != len(self):
                    adj_tiles += [self[row + 1][column]]
                if column - 1 >= 0:
                    adj_tiles += [self[row][column - 1]]
                if column + 1 != len(self[row]):
                    adj_tiles += [self[row][column + 1]]

            def diagonal(self, row, column):
                nonlocal adj_tiles
                if column - 1 >= 0:
                    if row - 1 >= 0:
                        adj_tiles += [self[row - 1][column - 1]]
                    if row + 1 != len(self):
                        adj_tiles += [self[row + 1][column - 1]]
                if column + 1 != len(self[row]):
                    if row - 1 >= 0:
                        adj_tiles += [self[row - 1][column + 1]]
                    if row + 1 != len(self):
                        adj_tiles += [self[row + 1][column + 1]]

            # Return the tiles that form a plus sign with the given input tile
            if pattern == 'p':
                plus_sign(self, row, column)

            # Return the tiles touching the four corners of the input tile
            elif pattern == 'x':
                diagonal(self, row, column)

            # Return all of the tiles surrounding the input tile
            elif pattern == 'b':
                plus_sign(self, row, column)
                diagonal(self, row, column)

            return adj_tiles


class Tilemap(ptg.BaseScreen):
    def __init__(self, size, tilelist, buttonflag):
        """This class will draw an array of tile objects to a screen and return
        a clicked tile or use a given button. It also currently contains basic
        tilelist processing methods.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            size - This is the (x,y) size of the screen. (you need to make the
                tiles the correct size for this screen when the tiles are
                initialized.

            tilelist - This is a list of tile objects to be drawn to the screen.

            buttonflag - If a 1 is passed the update function will return a tile
                that was clicked. If a 0 is passed the update function will
                check the buttons in the button list and call the function of
                a button that was clicked.

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Important Attributes:
            buttonlist - If you add button objects to this list the tilemap will
                automatically check if they're clicked in its update function if
                0 is passed for buttonflag.
                (you need to blit the added button to self.image manually)

        (doc string updated ver 0.1)
        """

        # Initialize the screen class
        ptg.BaseScreen.__init__(self, size)

        # Create the list of tile objects and draw them on the screen
        self.tilelist = tilelist
        xlen = self.tilelist[0][0].image.get_width()
        ylen = self.tilelist[0][0].image.get_height()
        for x in range(0, size[0], xlen):
            for y in range(0, size[1], ylen):
                try:
                    self.image.blit(self.tilelist[x // xlen][y // ylen].image,
                                    (x, y))
                    self.tilelist[x // xlen][y // ylen].set_position((x, y))
                except:
                    pass

        # Set up an empty button list and the buttonflag
        self.buttonlist = []
        self.buttonflag = buttonflag

    def set_offset(self, offset, mid=None):
        """This method will allow the menu to be placed anywhere in the open
           window instead of just the upper left corner.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            offset - This is the x,y tuple of the position that you want to
                move the screen to.

            mid - The offset will be treated as the value passed in instead of
                the top left pixel.

                'x' (the x point in offset will be treated as the middle of the
                      menu image)

                'y' (the y point in offset will be treated as the middle of the
                      menu image)

                'c' (the offset will be treated as the center of the menu image)

        (doc string updated ver 0.1)
        """

        ptg.BaseScreen.set_offset(self, offset, mid)
        for i in self.tilelist:
            for j in i:
                j.rect[0] += offset[0]
                j.rect[1] += offset[1]

    def update(self, screen, clock):

        def find_mouse():
            return pygame.mouse.get_pos()

        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # If the button flag is set to 1 return any tile clicked
                if self.buttonflag:
                    for i in self.tilelist:
                        for x in i:
                            if (event.type == pygame.MOUSEBUTTONUP and
                                    x.rect.collidepoint(find_mouse())):
                                return x
                # If the button flag is not set to one use a list of buttons
                # and call the function of any button that is called.
                else:
                    for i in self.buttonlist:
                        if (event.type == pygame.MOUSEBUTTONUP and
                                i.rect.collidepoint(find_mouse())):
                            return i()

            screen.blit(self.image, self.pos)
            pygame.display.flip()
