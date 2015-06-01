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

# Variant on the button class that allows inputs to its call
class wButton(ptg.Button):
    def __init__(self,name,*args,**kargs):
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
    def __init__(self):