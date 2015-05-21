#-------------------------------------------------------------------------------
# Name:        menu_examples.py
# Purpose:     This module will go over how to use the basic classes in the
#              graphics module
#
# Contributors: James Milam
#
# Created:     21/05/2015
# Copyright:   (c) James 2015
# Licence:     MIT Licence
# Version:     0.1
# Written for: Python 3.3
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame_toolbox.graphics as ptg
import pygame,sys

def close():
    # close out pygame and the game window properly
    pygame.quit()
    sys.exit()

class Simple_menu(ptg.Menu):
    def __init__(self):
        header = ["This is an example of an easy menu to put together."]
        buttons = [["Detailed menu",lambda:2],["Simple text screens",lambda:3],
                   ["Detailed text screens",lambda:4],["Close",close]]
        ptg.Menu.__init__(self,(800,600),(200,200,200),header,buttons)

class Detailed_menu(ptg.Menu):
    def __init__(self):
        # set the arguments for the menu class and initialize it
        size = (800,600)
        header = ['This is and example of a more detailed menu']
        background = 'fortress.png'
        ptg.Menu.__init__(self,size,background,header,[])

        # Create the customized buttons and add them to the button list
        self.buttonlist += [ptg.Button(0,'Simple menu',(300,450),True,self.image,
                       resize = (170,37),func = lambda:1,sound = 'button_click.wav',
                       background = 'button_box.png')]
        self.buttonlist += [ptg.Button(0,'Close',(500,450),True,self.image,
                       resize = (80,37),func = close,sound = 'button_click.wav',
                       background = 'button_box.png')]

class Simple_text_screens(ptg.Textscreens):
    def __init__(self):
        text = [["These screens will display","multiple lines of text until","The last list of text is reached"],
                ["Last screen of text"]]
        lastbutton = ["Return",lambda:1]
        ptg.Textscreens.__init__(self,(800,600),(200,200,200),text,lastbutton)

class Detailed_text_screens(ptg.Textscreens):
    def __init__(self):
        text = [["Like the menu, text screens can give more control over customization",
                 "As can be seen the back ground and the buttons can be customized if",
                 "more is wanted than the default options"],["Last page"]]
        lastbutton = ['Continue',lambda:1]
        background = 'background_03.png'
        self.nextbutton = ptg.Button(0,'Next',(0,0),resize = (80,37),sound = 'button_click.wav',background = 'button_box.png')
        self.backbutton = ptg.Button(0,'Back',(0,0),resize = (80,37),sound = 'button_click.wav',background = 'button_box.png')
        self.lastbutton = ptg.Button(0,'Return',(0,0),resize = (150,37),sound = 'button_click.wav',background = 'button_box.png')
        ptg.Textscreens.__init__(self,(800,600),background,text,lastbutton,1)

class Main(object):
    def __init__(self):
        self.progress = 1
        self.clock = pygame.time.Clock()

    def update(self,screen):
        while True:
            if self.progress == 1:
                self.progress = Simple_menu().update(screen,self.clock)
            elif self.progress == 2:
                self.progress = Detailed_menu().update(screen,self.clock)
            elif self.progress == 3:
                self.progress = Simple_text_screens().update(screen,self.clock)
            elif self.progress == 4:
                self.progress = Detailed_text_screens().update(screen,self.clock)

if __name__ == '__main__':
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    Main().update(screen)

