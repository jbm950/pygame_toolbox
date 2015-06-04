#-------------------------------------------------------------------------------
# Name:        pygame_toolbox.graphics.widgets.py
# Purpose:     This module holds basic graphics classes
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

# Module Contents
#   wButton
#   Checkbox

from .. import graphics as ptg
import pygame

# Variant on the button class that allows inputs to its call
class wButton(ptg.Button):
    def __init__(self, name, *args, **kargs):
        """This variation on the button class will pass arguments from
        its call into its function.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            name - This is the name of the widget that the menu will pass
                when exiting

            The rest of the inputs are passed directly to the graphics
                Button class and so that's where the definition of the
                remaining inputs can be found.

        (doc string updated ver 0.1)
        """

        self.name = name
        self.status = 0
        ptg.Button.__init__(self,*args,**kargs)
    def __call__(self,*args,**kargs):
        return self.func(*args,**kargs)


class Checkbox:
    def __init__(self, name, position, size, midpoint=False, surface=None,
                 checktype='r'):
        # Set the name, status and checktype of the checkbox widget
        self.name = name
        self.status = 0
        self.checktype = checktype

        # Create the surface that will hold the checkbox image
        self.image = pygame.Surface((size))
        self.image.fill((255,255,255))

        # Keep location information
        self.position = position
        self.midpoint = midpoint
        self.surface = surface
        ptg.Button.set_position(self, position, midpoint, surface)

    def draw_rect_check(self):
        # Create a black check that is 75% of the size of the whole box
        imagesize = self.image.get_size()
        imagemidp = (int(imagesize[0] * 0.5),int(imagesize[1] * 0.5))
        check = pygame.Surface((round(0.75*imagesize[0]),
                                round(0.75*imagesize[1])))
        check.fill((0,0,0))

        # Put the check in the middle of the checkbox
        checkmidp = (int(imagesize[0] * 0.375),int(imagesize[1] * 0.375))
        self.image.blit(check,(imagemidp[0]-checkmidp[0],
                               imagemidp[1]-checkmidp[1]))

    def draw_circle_check(self):
        # Create a black check circle that is 75% of the size of
        # the whole box
        imagesize = self.image.get_size()
        imagemidp = (int(imagesize[0] * 0.5),int(imagesize[1] * 0.5))
        check = pygame.draw.circle(self.image,(0,0,0),imagemidp,int(imagesize[0]*0.375))

    def __call__(self,*arg):
        if self.status:
            # If the checkbox was previously checked, set the status
            # to 0 and turn the whole box back to white.
            self.status = 0
            self.image.fill((255,255,255))

            # Draw the checkbox on the external surface
            ptg.Button.set_position(self, self.position, self.midpoint,
                                    self.surface)
        else:
            # If the checkbox was previously unchecked, set the status
            # to 1 and draw a check in the center of the checkbox
            self.status = 1
            if self.checktype == 'r':
                self.draw_rect_check()
            elif self.checktype == 'c':
                self.draw_circle_check()

            # Draw the new image on the external surface
            ptg.Button.set_position(self, self.position, self.midpoint,
                                    self.surface)






