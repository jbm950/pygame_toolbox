# ------------------------------------------------------------------------------
# Name:        pygame_toolbox.graphics.__init__.py
# Purpose:     This module holds basic graphics classes
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
#   Button
#   Linesoftext
#   BaseScreen
#   Menu
#   Textscreens

import pygame
import sys


class Button:
    def __init__(self, type_of_button, file_or_text, position, midpoint=None,
                 surface=None, **kargs):
        """This class will help make quick buttons for use with pygame.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            type_of_button - This input will differentiate between a picture
                button and a text button.
                0 = text button
                1 = picture button

            file_or_text - This input is a string containing either the text for
                a text button or a file name for the picture button (include
                extension for picture files such as .png)

            position - This is the x, y position of the top left corner of the
                button. (defining point can be changed to midpoint)

            midpoint - If true is passed to midpoint the button will be blitted
                to a surface, either automatically if a surface is passed or
                manually, such that the position input is the center of the
                button rather than the top left corner.

            surface - If a pygame surface or display is passed the button will
                automatically blit itself to that surface.

            resize - If a height and width are passed to this input the button
                will be adjusted to that size. For text buttons the background
                box will be adjusted to the given size while not altering the
                font size of the text.

            fontsize - This controls the size of the font of the text buttons.
                The default font size is 36.

            func - If a function is passed to the button the function will be
                called when the button is called and the button will return
                whatever the function would have returned.

            background - This can either be a rgb tuple of numbers or a string
                for a file to be loaded as the background image. (used for text
                buttons.)

            sound - This can be a string of a sound file. If given the sound
                will play whenever the button is clicked.

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Important Attributes:
            image - This will be the pygame surface that contains the image
                of the button to be blitted onto another surface.

            pos - This is a tuple of the x, y cordinates of the button for
                blitting purposes.

            rect - This is a pygame rectangle object associated with the
                size and position of the button. This is used for collision
                detection with the mouse.

            blitinfo - This is a tuple containing the image and the position
                of the button. This can be unpacked into the blit method for
                convenience.

        (doc string updated ver 0.1)
        """

        # Initialize pygame font and sprite class
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()

        # Unpack the **kargs dictionary into the possible inputs (resize,
        # fontsize and func). If there are still items in kargs return
        # an error.
        resize = kargs.pop('resize', None)
        fontsize = kargs.pop('fontsize', 36)
        func = kargs.pop('func', None)
        background = kargs.pop('background', (67, 110, 238))
        sound = kargs.pop('sound', None)
        if kargs:
            raise KeyError('An invalid input was passed')

        # Create a text button
        if type_of_button == 0:

            # Create the font object
            basicfont = pygame.font.Font(None, fontsize)

            # Create the text surface and find the size and midpoint
            # of that surface
            text = basicfont.render(file_or_text, 0, (1, 1, 1))
            textsize = text.get_size()
            textmidp = (int(textsize[0] * 0.5), int(textsize[1] * 0.5))

            # Create the background box
            if resize:
                self.image = pygame.Surface(resize)
            else:
                self.image = pygame.Surface((int(textsize[0] * 1.25),
                                             int(textsize[1] * 1.429)))
            imagesize = self.image.get_size()
            imagemidp = (int(imagesize[0] * 0.5), int(imagesize[1] * 0.5))

            # Create the background for the screen
            # If the backround is a filename load the file and blit it
            # to the image
            if type(background) == str:
                background = pygame.image.load(background).convert()
                background = pygame.transform.scale(background,
                                                    (self.image.get_width(),
                                                     self.image.get_height()))
                self.image.blit(background, (0, 0))
            # Otherwise the background should contain an rgb value
            else:
                self.image.fill(background)

            # Center the text at the center of the box
            self.image.blit(text, (imagemidp[0]-textmidp[0],
                                   imagemidp[1]-textmidp[1]))

        # Create a picture button
        elif type_of_button == 1:

            # Load the given file
            self.image = pygame.image.load(file_or_text).convert()

            # Change the size of the picture if necessary
            if resize:
                self.image = pygame.transform.scale(self.image, resize)
            imagemidp = (int(self.image.get_width() * 0.5),
                         int(self.image.get_height() * 0.5))

        # Set the position of the button
        self.set_position(position, midpoint, surface)

        # Set the function for the button to pass into the call for the class
        if func is not None:
            self.func = func

        # If a sound is given load the sound file
        if sound is not None:
            self.sound = pygame.mixer.Sound(sound)
        else:
            self.sound = None

    def set_position(self, position, midpoint=False, surface=None):
        """This method allows the button to be moved manually and keep the click
        on functionality.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            position - This is the x, y position of the top left corner of the
                            button. (defining point can be changed to midpoint)

            midpoint - If true is passed to midpoint the button will be blitted
                to a surface, either automatically if a surface is passed or
                manually, such that the position input is the center of the
                button rather than the top left corner.

        (doc string updated ver 0.1)"""

        # Find the image size and midpoint of the image
        imagesize = self.image.get_size()
        imagemidp = (int(imagesize[0] * 0.5), int(imagesize[1] * 0.5))

        # if a midpoint arguement is passed, set the pos to the top left pixel
        # such that the position passed in is in the middle of the button
        if midpoint:
            self.pos = (position[0] - imagemidp[0], position[1] - imagemidp[1])
        else:
            self.pos = position

        # set the rectangle to be used for collision detection
        self.rect = pygame.Rect(self.pos, self.image.get_size())

        # Set up the information that is needed to blit the image to the surface
        self.blitinfo = (self.image, self.pos)

        # automatically blit the button onto an input surface
        if surface:
            surface.blit(*self.blitinfo)

    def __call__(self):
        """Calling the button will call what ever function was passed to it when
           it was initialized. The button object returns whatever was returned
           by the function assigned to it. If a sound was given this sound will
           be played before the given function is called.
           (doc string updated ver 0.1)
           """

        # If a sound is given play the sound before returning the given function
        if self.sound is not None:
            self.sound.play()

        return self.func()


class Linesoftext:
    def __init__(self, text, position, xmid=None, surface=None, **kargs):
        """This object will create an image of text with multiple lines.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            text - This is a list of strings. Each item in the list will be
                drawn on a separate line.

            position - This is the x, y postion of the top left pixel of the
                text image.

            xmid - If passed True the position argument will be treated as the
                middle of the top of the text image.

            surface - If a pygame surface or screen is passed in the Linesoftext
                object will automatically blit itself to that surface/screen.

            fontsize - This is the size of the font of the rendered text. The
                default fontsize is 36.

            align - This will determine if the text is aligned to the left,
                right or center. The default is left aligned.
                'l' = left align
                'c' = center align
                'r' = right align

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Important Attributes:
            image - This will be the pygame surface that contains the image
                of the text to be blitted onto another surface.

            pos - This is a tuple of the x, y cordinates of the text for
                blitting purposes.

            blitinfo - This is a tuple containing the image and the position
                of the text. This can be unpacked into the blit method for
                convenience.

        (doc string updated ver 0.1)
        """

        # Initialize the pygame font class.
        pygame.font.init()

        # Unpack the **kargs dictionary
        fontsize = kargs.pop('fontsize', 36)
        align = kargs.pop('align', 'l')

        # Create the font object
        basicfont = pygame.font.Font(None, fontsize)

        # Figure out the size of the image that will be drawn on and create that
        # image
        linewidths = []
        for x in text:
            texttemp = basicfont.render(x, 0, (1, 1, 1))
            linewidths.append(texttemp.get_width())
        # The width of the image is the width of the text that corresponds to
        # the index of linewidths that contains the largest number in linewidths
        maxlinewidth = linewidths.index(max(linewidths))
        maxlinerender = basicfont.render(text[maxlinewidth], 0, (1, 1, 1))
        self.imagewidth = maxlinerender.get_width()
        self.imageheight = len(text) * fontsize + (len(text)-1) * 10
        self.image = pygame.Surface((self.imagewidth, self.imageheight))
        self.image.fill((200, 200, 200))

        # make the background transparent
        self.image.set_colorkey((200, 200, 200))

        # Draw the text to the image using the user chosen alignment
        n = 0
        if align == 'l':
            for x in text:
                texttemp = basicfont.render(x, 0, (1, 1, 1))
                self.image.blit(texttemp, (0, n * fontsize + n * 10))
                n += 1
        elif align == 'c':
            for x in text:
                texttemp = basicfont.render(x, 0, (1, 1, 1))
                self.image.blit(texttemp,
                                (self.imagewidth//2 - texttemp.get_width()//2,
                                 n * fontsize + n * 10))
                n += 1
        elif align == 'r':
            for x in text:
                texttemp = basicfont.render(x, 0, (1, 1, 1))
                self.image.blit(texttemp,
                                (self.imagewidth - texttemp.get_width(),
                                 n * fontsize + n * 10))
                n += 1

        # Set the position of the text. If xmid is passed in as true set the
        # pos to the top middle pixel of the text
        if xmid:
            self.pos = (position[0]-int(self.image.get_width()/2), position[1])
        else:
            self.pos = position

        # Set up the information that will be needed to blit the image to a
        # surface
        self.blitinfo = (self.image, self.pos)

        # automatically blit the text onto an input surface
        if surface:
            surface.blit(*self.blitinfo)

    def test(self, windowsize=False):
        """This can be used to quickly test the spacing of the words.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            windowsize - A (width,height) tuple can be passed to create a window
                with a specific size otherwise a window will be sized to the
                given text.

        (doc string updated ver 0.1)
        """

        # set up a specific window to test the text in
        if windowsize:
            self.screen = pygame.display.set_mode(windowsize)
            self.screen.fill((200, 200, 200))
            self.screen.blit(*self.blitinfo)

        # if no specific window is specified create a small one around the
        # outside of the text
        else:
            self.screen = pygame.display.set_mode((self.imagewidth + 20,
                                                   self.imageheight + 20))
            self.screen.fill((200, 200, 200))
            self.screen.blit(self.image, (10, 10))

        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


class BaseScreen:
    def __init__(self, size, background=None, music=None):
        """This is a base class for the other screens offered in the pygametools
        module.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            size - an (x,y) tuple defining the width and height of the screen to
                be made (in pixels).

            background - The background can either be a rgb tuple or a sting for
                 a file name.
        (doc string updated ver 0.1)
        """

        # Create the image that the screen will be drawn on
        self.image = pygame.Surface((size[0], size[1]))

        # Create the background for the screen
        # If the backround is a filename load the file and blit it to the image
        if type(background) == str:
            background = pygame.image.load(background).convert()
            background = pygame.transform.scale(background, size)
            self.image.blit(background, (0, 0))
        # Otherwise the background should contain an rgb value
        elif type(background) == tuple:
            self.image.fill(background)

        # Set the default position of the screen to (0,0)
        self.pos = (0, 0)

        # If background music is passed in load the sound file
        if music is not None:
            pygame.mixer.music.load(music)
            self.music = True
        else:
            self.music = None

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

        if mid:
            imagesize = self.image.get_size()
            imagemidp = (int(imagesize[0] * 0.5), int(imagesize[1] * 0.5))
            if mid == 'x':
                offset = (offset[0] - imagemidp[0], offset[1])
            if mid == 'y':
                offset = (offset[0], offset[1] - imagemidp[1])
            if mid == 'c':
                offset = (offset[0] - imagemidp[0], offset[1] - imagemidp[1])

        self.pos = offset

        for i in self.buttonlist:
                i.rect[0] += offset[0]
                i.rect[1] += offset[1]

        try:
            for i in self.widgetlist:
                i.rect[0] += offset[0]
                i.rect[1] += offset[1]
        except AttributeError:
            pass


class Menu(BaseScreen):
    def __init__(self, size, background, header, buttons, music=None):
        """This will create a screen with header text and buttons that call the
        user specified functions when clicked.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            size - This will specify the size of the menu in pixels. An x and a
                y value are to be given.

            background - This can either be a rgb tuple of numbers or a string
                for a file to be loaded as the background image.

            header - This is the text that will be displayed at the top of the
                menu screen. The text needs to be entered as a string in a list

            buttons - This is a list containing text function pairs for each
                desired button. Example [['Play',lambda:2],['quit',lambda:3]]

            music - This will be a string of the music file you wish to play
                while the menu is open
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Important Attributes:
            buttonlist - If you add button objects to this list the menu will
                automatically check if they're clicked in its update function
                (you need to blit the added button to self.image manually)

        (doc string updated ver 0.1)
        """

        # Initialize the screen class
        BaseScreen.__init__(self, size, background, music)

        # Determine the mid position of the given screen size and the
        # y button height
        xmid = size[0]//2
        ybuth = int(size[1]*0.583333)

        # Create the header text
        Linesoftext(header, (xmid, 40), xmid=True, surface=self.image)

        # Create the buttons
        self.buttonlist = []
        for i in buttons:
            self.buttonlist += [Button(0, i[0],
                                       (xmid, ybuth + buttons.index(i) * 50),
                                       True, surface=self.image, func=i[1])]

        # Create an empty list of widgets
        self.widgetlist = []

    def widget_status(self):
        """This method will return the status of all of the widgets in the
        widget list"""
        widget_status_list = []
        for i in self.widgetlist:
            widget_status_list += [[i.name, i.status]]
        return widget_status_list

    def update(self, screen, clock):
        """Event handling loop for the menu"""

        # If a music file was passed, start playing it on repeat
        if self.music is not None:
            pygame.mixer.music.play(-1)

        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Check if any of the buttons were clicked
                for i in self.buttonlist:
                    if (event.type == pygame.MOUSEBUTTONUP and
                            i.rect.collidepoint(pygame.mouse.get_pos())):
                        if self.music is not None:
                            pygame.mixer.music.stop()
                        if self.widgetlist:
                            return [i(), self.widget_status()]
                        else:
                            return i()
                # If there is a widget list, check to see if any were clicked
                if self.widgetlist:
                    for i in self.widgetlist:
                        if (event.type == pygame.MOUSEBUTTONDOWN and
                                i.rect.collidepoint(pygame.mouse.get_pos())):
                            # Call the widget and give it the menu information
                            i(self)
            screen.blit(self.image, self.pos)
            pygame.display.flip()


class Textscreens(BaseScreen):
    def __init__(self, size, background, text, lastbutton, manual_buttons=None,
                 music=None):
        """This is a class that will make multiple screens for displaying text,
        like a book using  pages that can be flipped back and forth between.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            size - This is the (x,y) size of the screen in pixels.

            background - This can either be a rgb tuple of numbers or a string
                for a file to be loaded as the background image.

            text - This is a list containing a separate list of text for each
                page. Each page's text will have the lines of the text separated
                by commas.

            lastbutton - This is a list containing a string of what the last
                button should display and a function that should be run if the
                last button is clicked. If manual buttons are used a function
                still has to be provided as the second item in a list here.

            manual_buttons - If a 1 is passed then the nextbutton, backbutton
                and lastbutton need to be initialized separately before this
                class's __init__ function is run.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Important Attributes:
            nextbutton - This is the button that progresses through the pages

            backbutton - This is the button that will return to previous pages

            lastbutton - This is the button that replaces the nextbutton on the
                last page of the text to allow the program to move on.

        (doc string updated ver 0.1)
        """

        # Make the inputs into attributes to pass to the individual screens
        self.size = size
        self.background = background
        self.text = text
        self.lastbutton_func = lastbutton[1]
        self.music = music
        self.widgetlist = []

        # Set the progress counter for the text and page indicator for the
        # individual screens
        self.progress = 0
        self.page = 1

        # Set up the buttons for the screens
        xthird = size[0]//3
        ybut = int(size[1] * 0.9)

        # If the buttons are created manually set the func and pos attributes
        # for the text screens
        if manual_buttons:
            self.nextbutton.func = lambda: 2
            self.nextbutton.set_position((size[0] - xthird, ybut), True)

            self.backbutton.func = lambda: 3
            self.backbutton.set_position((xthird, ybut), True)

            self.lastbutton.func = lambda: 4
            self.lastbutton.set_position((size[0] - xthird, ybut), True)

        # If the defaullt buttons are being used create them
        else:
            self.nextbutton = Button(0, 'Next', (size[0] - xthird, ybut), True,
                                     func=lambda: 2)
            self.backbutton = Button(0, 'Back', (xthird, ybut), True,
                                     func=lambda: 3)
            self.lastbutton = Button(0, lastbutton[0], (size[0] - xthird, ybut),
                                     True, func=lambda: 4)

    def Screens(self, text, prog, screen, clock):
        """Prog = 0 for first page, 1 for middle pages, 2 for last page"""
        # Initialize the screen class
        BaseScreen.__init__(self, self.size, self.background)

        # Determine the mid position of the given screen size and the
        # y button height
        xmid = self.size[0]//2

        # Create the header text
        Linesoftext(text, (xmid, 40), xmid=True, surface=self.image,
                    fontsize=30)

        # Create the buttons
        self.buttonlist = []
        if prog == 0:
            self.buttonlist += [self.nextbutton]

        elif prog == 1:
            self.buttonlist += [self.nextbutton]
            self.buttonlist += [self.backbutton]

        elif prog == 2:
            self.buttonlist += [self.lastbutton]
            self.buttonlist += [self.backbutton]

        # Draw the buttons to the screen
        for i in self.buttonlist:
            self.image.blit(*i.blitinfo)

        # Use the menu update method to run the screen and process button clicks
        return Menu.update(self, screen, clock)

    def update(self, screen, clock):
        # If a music file was passed, start playing it on repeat
        if self.music is not None:
            pygame.mixer.music.load(self.music)
            pygame.mixer.music.play(-1)
            self.music_textscreens = 1
        else:
            self.music_textscreens = 0

        while True:
            # Navigation through the screens
            # page = 1 - pages of text
            # page = 2 - Advance to next page of text
            # page = 3 - return a page of text
            # page = 4 - exit the set of pages
            if self.page == 1:
                # check for last page then first page then make the middle pages
                if self.progress == (len(self.text) - 1):
                    self.page = self.Screens(self.text[self.progress], 2,
                                             screen, clock)
                elif self.progress == 0:
                    self.page = self.Screens(self.text[self.progress], 0,
                                             screen, clock)
                else:
                    self.page = self.Screens(self.text[self.progress], 1,
                                             screen, clock)
            elif self.page == 2:
                self.progress += 1
                self.page = 1
            elif self.page == 3:
                self.progress -= 1
                self.page = 1
            elif self.page == 4:
                if self.music_textscreens:
                    pygame.mixer.music.stop()
                return self.lastbutton_func()
