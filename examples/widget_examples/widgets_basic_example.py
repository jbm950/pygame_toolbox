# -----------------------------------------------------------------------------
# Name:        widgets_basic_example.py1
# Purpose:     This will go over some of the basics on how to code the widgets
#              using pygame_toolboxe
#
# Contributors: James Milam
# Created:     01/06/2015
# Copyright:   (c) James 2015
# Licence:     MIT Licence
# Version:     0.1
# Written for: Python 3.3
# ------------------------------------------------------------------------------
# !/usr/bin/env python

import pygame_toolbox.graphics as ptg
import pygame_toolbox.graphics.widgets as ptgw
import pygame
import random
import sys


# Function to close out of the window and interpreter
def close():
    pygame.quit()
    sys.exit()


# Redraw Screen 1 with a random background color
def randombackgroundcolor(menu):
    # Create a random rgb value.
    back = (random.randint(0, 255), random.randint(0, 255),
            random.randint(0, 255))

    # Re-run the menu's __init__ function with the new background
    # color.
    ptg.Menu.__init__(menu, (800, 600), back, menu.header, menu.buttons)

    # Re-add the widgets to the menu.
    menu.widgetlist += [ptgw.wButton("randomize button", 0, "Randomize Color",
                                     (200, 200), True, menu.image,
                                     func=randombackgroundcolor)]
    menu.widgetlist += [ptgw.wButton("reset button", 0, "Reset Color",
                                     (200, 300), True, menu.image,
                                     func=resetbackgroundcolor)]
    menu.widgetlist += [ptgw.Checkbox("Box 1", (500, 200), (20, 20), True,
                                      menu.image)]


# Redraw Screen 1 with the original background color
def resetbackgroundcolor(menu):
    # Re-run the menu's __init__function with the original background
    ptg.Menu.__init__(menu, (800, 600), (150, 69, 69), menu.header,
                      menu.buttons)

    # Re-add the widgets to the menu.
    menu.widgetlist += [ptgw.wButton("randomize button", 0, "Randomize Color",
                                     (200, 200), True, menu.image,
                                     func=randombackgroundcolor)]
    menu.widgetlist += [ptgw.wButton("reset button", 0, "Reset Color",
                                     (200, 300), True, menu.image,
                                     func=resetbackgroundcolor)]
    menu.widgetlist += [ptgw.Checkbox("Box 1", (500, 200), (20, 20), True,
                                      menu.image)]


class Screen_1(ptg.Menu):
    def __init__(self):
        self.header = ['Screen 1']
        self.buttons = [['Screen 2', lambda:2], ['Quit', close]]
        ptg.Menu.__init__(self, (800, 600), (150, 69, 69), self.header,
                          self.buttons)

        # Set up the widgets for the screen
        self.widgetlist += [ptgw.wButton("randomize button", 0,
                                         "Randomize Color", (200, 200), True,
                                         self.image,
                                         func=randombackgroundcolor)]
        self.widgetlist += [ptgw.wButton("reset button", 0, "Reset Color",
                                         (200, 300), True, self.image,
                                         func=resetbackgroundcolor)]
        self.widgetlist += [ptgw.Checkbox("Box 1", (500, 200), (20, 20), True,
                                          self.image)]


class Screen_2(ptg.Menu):
    def __init__(self, checkbox):
        header = ['Screen 2', '%s was %s' % (checkbox[0], checkbox[1])]
        buttons = [['Screen 1', lambda:1], ['Quit', close]]
        ptg.Menu.__init__(self, (800, 600), (150, 69, 150), header, buttons)


class Main(object):
    def __init__(self):
        self.progress = 1
        self.clock = pygame.time.Clock()

    def update(self, screen):
        while True:
            if self.progress == 1:
                self.progress = Screen_1().update(screen, self.clock)
                # Pull out the checkbox info and pass the progress
                # argument along
                self.checkbox = self.progress[-1][-1]
                self.progress = self.progress[0]
            elif self.progress == 2:
                self.progress = Screen_2(self.checkbox).update(screen,
                                                               self.clock)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    Main().update(screen)
