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

from .. import graphics as ptg

# Variant on the button class that allows inputs to its call
class wButton(ptg.Button):
    def __call__(self,*args,**kargs):
        return self.func(*args,**kargs)