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


def close():
    pygame.quit()
    sys.exit()


def randombackgroundcolor(menu):
    back = (random.randint(0, 255), random.randint(0, 255),
            random.randint(0, 255))
    ptg.Menu.__init__(menu, (800, 600), back, menu.header, menu.buttons)
    menu.widgetlist += [ptgw.wButton("randomize button", 0, "Randomize Color",
                                     (200, 200), True, menu.image,
                                     func=randombackgroundcolor)]
    menu.widgetlist += [ptgw.wButton("reset button", 0, "Reset Color",
                                     (200, 300), True, menu.image,
                                     func=resetbackgroundcolor)]


def resetbackgroundcolor(menu):
    ptg.Menu.__init__(menu, (800, 600), (150, 69, 69), menu.header,
                      menu.buttons)
    menu.widgetlist += [ptgw.wButton("randomize button", 0, "Randomize Color",
                                     (200, 200), True, menu.image,
                                     func=randombackgroundcolor)]
    menu.widgetlist += [ptgw.wButton("reset button", 0, "Reset Color",
                                     (200, 300), True, menu.image,
                                     func=resetbackgroundcolor)]


class Screen_1(ptg.Menu):
    def __init__(self):
        self.header = ['Screen 1']
        self.buttons = [['Screen 2', lambda:2], ['Quit', close]]
        ptg.Menu.__init__(self, (800, 600), (150, 69, 69), self.header,
                          self.buttons)

        self.widgetlist += [ptgw.wButton("randomize button", 0,
                                         "Randomize Color", (200, 200), True,
                                         self.image,
                                         func=randombackgroundcolor)]
        self.widgetlist += [ptgw.wButton("reset button", 0, "Reset Color",
                                         (200, 300), True, self.image,
                                         func=resetbackgroundcolor)]
        for i in self.widgetlist:
            i.status = 0


class Screen_2(ptg.Menu):
    def __init__(self):
        header = ['Screen 2']
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
                print(self.progress)
                self.progress = self.progress[0]
            elif self.progress == 2:
                self.progress = Screen_2().update(screen, self.clock)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    Main().update(screen)
