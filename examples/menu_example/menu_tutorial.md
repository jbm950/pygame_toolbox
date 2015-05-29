#Menu Tutorial
(Note: This tutorial is written for pygame_toolbox version 0.1)

In this tutorial I'm going to go over the code in the script menu_examples.py where we build 3 different menu 
objects (simple menu, detailed menu and mini menu) and two different text_screens objects (simple text screens 
and detailed text screens). This script can be found [here](./menu_examples.py)

First let us begin by importing the modules that we will need. Since pygame_toolbox.graphics is a bit verbose I'm 
going to import it as ptg.
    
```python
    # Import the graphics tools and pygame and sys
    import pygame_toolbox.graphics as ptg
    import pygame,sys
```

Next I'm going to define a function to properly close out of the program when needed. Without this you'll get errors 
when trying to close the pygame screen.

```python
    def close():
        # close out pygame and the game window properly
        pygame.quit()
        sys.exit()
```

##Simple menu

Now we're ready to begin coding the simple menu. To start create a simple menu class that inherits from Pygame Toolbox 
graphic's menu class.

```python
        class Simple_menu(ptg.Menu):
```

Next we define the size of the menu in number of pixels (for this tutorial the screen size is going to be 800x600 pixels) and 
the text displayed at the top of the menu as a header variable.

```python
        def __init__(self):
            # Define the size of the screen (x,y) in number of pixels
            size = (800,600)
            # Create a header which will be the text at the top of the menu screen
            header = ["This is an example of an easy menu to put together."]
```

Next we're going to define what buttons we want to include in the menu. To do this we use embedded lists where the first item 
in the inner list is the text to be displayed on the button and the second item is the function returned when the button is clicked 
upon. For now we're going to just include a single button and a button that will close out of the screen using our close function 
from earlier.

```python
            # Give the text and functions for the buttons that the menu class will create
            buttons = [["Simple Button",lambda:2],["Close",close]]
```

*Side Note on Functionality*: The clicked on function is also returned by the menu and the menu 
object exits out when a button is clicked. To get a better idea of what is happening, I'm going to 
show the update function of the menu.(**NOTE: This is not actual code for the example, 
but rather some of the code from the graphics file.**)
        
```python
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for i in self.buttonlist:
                if event.type == pygame.MOUSEBUTTONUP and i.rect.collidepoint(pygame.mouse.get_pos()):
                    if self.music is not None:
                        pygame.mixer.music.stop()
                    return i()
```

It should also be noted that this is only a part of the update function, not the full function. If 
you'd rather something not exit the menu when its function is run look to the widgets, however, 
at the time of this writing widgets have not been developed yet.

Back to the simple menu you should now have the size of the menu, the header text and the 
buttons defined for the menu. All that is left is to call the inherited menu's \__init__ function and 
pass in our variables (the values could be passed in manually without the use of intermediate 
variables if desired). The tuple input is for the background variable of the menu. For this menu 
we're using a tuple that gives a color as a rgb value and the menu will make this color the 
background color.

```python
            # Run the menu class's init function
            ptg.Menu.__init__(self,size,(200,200,200),header,buttons)
```
                
Your whole class should now look like this.

```python
    class Simple_menu(ptg.Menu):
        def __init__(self):
            # Define the size of the screen (x,y) in number of pixels
            size = (800,600)
            # Create a header which will be the text at the top of the menu screen
            header = ["This is an example of an easy menu to put together."]
            # Give the text and functions for the buttons that the menu class will create
            buttons = [["Simple Button",lambda:2],["Close",close]]
    
            # Run the menu class's init function
            ptg.Menu.__init__(self,size,(200,200,200),header,buttons)
```

We aren't ready to display anything yet unfortunately. Lets start our next step by building an 
event handler in a class called Main. in the initialization method we're going to set a progress 
attribute to 1 and this will handle switching between screens. Also we're going to create a pygame 
Clock object and attach it to main in a clock attribute. The code for these steps can be seen below.

```python
    class Main:
        def __init__(self):
            self.progress = 1
            self.clock = pygame.time.Clock()
```

We now need to code the event handling portion of the class and to do this we're going to use an 
infinite while loop in an update method. The while loop will check the progress attribute and call the 
corresponding screen. The return from the screen will then be the next value of the progress attribute 
to direct to other screens (The return of the button function will determine what the menu returns as 
discussed above). The update function is given below.

```python
        def update(self,screen):
            # Handle the events using a progress indicator and the update method of
            # the menu and text screen classes
            while True:
                if self.progress == 1:
                    self.progress = Simple_menu().update(screen,self.clock)
                elif self.progress == 2:
                    close()
```
                        
For now I'm leaving progress = 2 (our simple button was pressed) as returning the close function so 
that we do not create an error when checking to see if the button works. The menu is then called 
along with its update method to let it have control of the screen. The full main class is given as

```python
    class Main:
        def __init__(self):
            self.progress = 1
            self.clock = pygame.time.Clock()

        def update(self,screen):
            # Handle the events using a progress indicator and the update method of
            # the menu and text screen classes
            while True:
                if self.progress == 1:
                    self.progress = Simple_menu().update(screen,self.clock)
                elif self.progress == 2:
                    close()
```

Last thing we need before we can run the script is something to run the necessary inits and the Main 
class event handler. I'm going to put this code under a script/module test so that the screen will only 
appear if the file is being run itself instead of being imported else where. where we are going to want 
to run the pre_init of pygame's mixer, run pygame's init and create a screen. Now we can create and 
call the Main class and its update method. This code can be seen below.

```python
    if __name__ == '__main__':
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        screen = pygame.display.set_mode((800,600))
        Main().update(screen)
```

Now we're ready to run the script. If you've done everything so far your pygame window should look 
like this

![alt text](./simple_screen_screenshot.png "Simple Menu Screenshot")

Now we're ready to start working on some of the other menus that can be built with Pygame Toolbox.

##Detailed Menu

This part of the tutorial is going to go over many of the options that the menu class (and button class) 
have to offer. To begin we're going define the size and header inside an init of the detailed menu.

```python
    class Detailed_menu(ptg.Menu):
        def __init__(self):
            # set the arguments for the menu class and initialize it
            size = (800,600)
            header = ['This is an example of a more detailed menu']
```

This time we're going to use a picture for the background instead of an rgb value. This allows us to 
create screen that look much nicer for projects we share and the rgb value method gives us a way 
to make a rapid prototype. We're also going to pass a music variable that is the string of a sound file 
name. This music will be played when the detailed menu is open.

```python
            background = 'fortress.png'
            music = "sports_card.wav"
```

Now we're ready to call the ptg.Menu's init function. You'll notice that this time we are passing an empty 
list to the buttons argument. This is because we are going to define the buttons we want manually to 
take full advantage of the Button class's functionality.

```python
            ptg.Menu.__init__(self,size,background,header,[],music)
```

If you look at the update function for the graphic's menu class that was presented earlier you'll notice 
that when checking for button interactions it checks the items in the attribute buttonlist. We can take 
advantage of this by putting buttons in this list ourselves. (**Note: Manually adding buttons to 
buttonlist needs to be done AFTER the ptg.Menu.\__init__() because the \__init__() will create the list 
thereby overwriting your manually made buttons**) To add the buttons we're going to use the following 
syntax.

```python
            self.buttonlist += [ptg.Button()]
```

####Mini Button Tutorial

Before we can go ahead and add the buttons though I need to go over the different input arguments 
of the button class. To do this I'm going to show the first button we'll add to the Detailed menu and go 
over each of the inputs one by one.

```python
            self.buttonlist += [ptg.Button(0,'Simple menu',(300,450),True,self.image,
                                           resize = (170,37),func = lambda:1,sound = 'button_click.wav',
                                           background = 'button_box.png')]
```

The Button class can be used for either picture buttons or text buttons and so the first argument 
passed is to differentiate between these two. A zero is passed to let it know this will be a text button 
(1 for picture button). The next item is the text of the button itself and in this case we're going to let 
the user of the menu know that the button will return them to the simple menu (on a picture button this 
will be a string of a file name to the picture to be used). The next item is a tuple of the x,y position of the 
button in pixels. Using this method of adding buttons to the screen will therefore allow us to place the 
buttons anywhere. The next item (True) is a flag to let the class know if we want the position we passed 
to be a center of button value. The default otherwise is pygame's default and the position will be taken 
as the top left pixel of the button. The self.image attribute is the pygame surface that has the complete 
visual information of how the menu is supposed to look. By passing it to the button object the button will 
automatically add itself (blit) to the image so you don't have to manually. The last four inputs are a bit 
easier to understand as their keywords are indicative of their identitys. Resize will change the size of 
the box behind the button text. Func is the variable containing the function that the button will return if 
clicked upon. The sound input is a string of a sound file to be played when the button is clicked on. Last 
the background is a string of a picture to act as the background for the button's text. Now we're ready 
to continue on with the menu tutorial. (The button information is reflected in depth in its docstring if 
additional reading is desired)

####Continuing Detailed Menu Tutorial

For this menu we're going to have two buttons, one to return to the simple menu and one to close the 
window. If you remember from earlier the event handler calls the simple menu when its self.progress 
variable equals 1. In order to return to this menu then we'll want the "Simple menu" button to return 1 
when clicked on and so you'll see this in the func argument being passed in. Both buttons for this menu 
are given below.

```python
            # Create the customized buttons and add them to the button list
            self.buttonlist += [ptg.Button(0,'Simple menu',(300,450),True,self.image,
                                           resize = (170,37),func = lambda:1,sound = 'button_click.wav',
                                           background = 'button_box.png')]
            self.buttonlist += [ptg.Button(0,'Close',(500,450),True,self.image,
                                           resize = (80,37),func = close,sound = 'button_click.wav',
                                           background = 'button_box.png')]
```

We're now done creating the Detailed menu class and it's code viewed in full is

```python
    class Detailed_menu(ptg.Menu):
        def __init__(self):
            # set the arguments for the menu class and initialize it
            size = (800,600)
            header = ['This is an example of a more detailed menu']
            background = 'fortress.png'
            music = "sports_card.wav"
            ptg.Menu.__init__(self,size,background,header,[],music)
    
            # Create the customized buttons and add them to the button list
            self.buttonlist += [ptg.Button(0,'Simple menu',(300,450),True,self.image,
                                           resize = (170,37),func = lambda:1,sound = 'button_click.wav',
                                           background = 'button_box.png')]
            self.buttonlist += [ptg.Button(0,'Close',(500,450),True,self.image,
                                           resize = (80,37),func = close,sound = 'button_click.wav',
                                           background = 'button_box.png')]
```

If we run the script, however we still won't see this menu. First lets change the name of the button in 
the simple menu that returns 2 so that it is more apparent that it will lead to the detailed menu.

```python
    ["Simple Button",lambda:2] >>>> ["Detailed menu",lambda:2]
```

Now lets add the detailed menu to the event handler when its progress attribute equals 2.

```python
    elif self.progress == 2:  >>>>  elif self.progress == 2:
        close()               >>>>      self.progress = Detailed_menu().update(screen,self.clock)
```

The script should now be able to go back and forth between the detailed and simple screens and the
detailed screen should look like this

![alt text](./detailed_screen_screenshot.png "Detailed Menu Screenshot")

##Mini Menu

The last menu we are going to go over is a mini menu. This is a menu with a size smaller than the size 
of the full screen. With such a menu the desire to place it anywhere on the screen is natural. To achieve
this we are going to take advantage of the menu's set_offset() method. First though we need to define 
our mini menu class. Since creation of a simple menu was already discussed I'm simply going to show the
code

```python
    class Mini_menu(ptg.Menu):
        def __init__(self):
            # Define the size of the screen (x,y) in number of pixels
            # (Note that this size is smaller than the full screen
            #  size in this code)
            size = (400,300)
            # Create the text to be displayed at the top of the menu
            header = ["This is a menu of reduced size"]
            # Create the list of buttons to pass to the Menu.__init__
            buttons = [["Back",lambda:1]]
            # Run the initialization of the menu function
            ptg.Menu.__init__(self,size,(100,200,100),header,buttons)
```

As you can see the size of the menu is half the size of the full screen. Also the only button we're adding 
is one to return to the simple menu. Without a set_offset() method call this menu would be placed in the 
upper left hand corner of the screen. For this tutorial we're going to place the menu in the center of the 
screen (though can can really place it anywhere we want. Since the screen dimensions are 800x600 the 
mid point of the screen will be located at (400,300). We'll now call the ptg.Menu's offset method in our 
mini menu's \__init__.

```python
        # Move the menu to the center of the screen
        ptg.Menu.set_offset(self,(400,300),mid = 'c')
```

Notice we also pass a mid argument to the method. This is because the default (like the button) is to use
our position argument as the top left pixel of our menu. The other possible mid arguments are 'x' if you
want to just use the x position as a mid point and the y value will still refer to the top of the menu and 'y'
if you want only the y value to be taken as the middle of the menu and the x value will still refer to the left
edge. The whole mini menu class should now look like

```python
    class Mini_menu(ptg.Menu):
        def __init__(self):
            # Define the size of the screen (x,y) in number of pixels
            # (Note that this size is smaller than the full screen
            #  size in this code)
            size = (400,300)
            # Create the text to be displayed at the top of the menu
            header = ["This is a menu of reduced size"]
            # Create the list of buttons to pass to the Menu.__init__
            buttons = [["Back",lambda:1]]
            # Run the initialization of the menu function
            ptg.Menu.__init__(self,size,(100,200,100),header,buttons)
            # Move the menu to the center of the screen
            ptg.Menu.set_offset(self,(400,300),mid = 'c')
```

Now we'll need to update the simple menu class and the event handler to accommodate the new menu.
This time we'll use the progress value of 3 to represent our mini menu and so a button will need to be
added to the simple menu class like this.

```python
    buttons = [["Detailed menu",lambda:2],["Mini menu",lambda:3],["Close",close]]
```

Also we need to add the extra menu in the event handler. After the check for the progress attribute
equaling 2 we'll add another elif statement to check for the progress attribute equaling 3. When this
case is detected we'll call the update method of the mini menu exactly the same as the previous two 
menus.

```python
    elif self.progress == 2:
        self.progress = Detailed_menu().update(screen,self.clock)
    elif self.progress == 3:
        self.progress = Mini_menu().update(screen,self.clock)
```

Now the script should be ready to handle the new menu and when open the screen should look like this.

![alt text](./mini_screen_screenshot.png "Mini Menu Screenshot")

##Simple Text Screens
The mini menu concluded our exploration of the graphics module's menu class. We're going to cover one 
more class of the graphics module before we wrap up this tutorial, however, and that is the text screens
class. This class is designed to make the presentation of lots of text easy. It will provide multiple screens that can be flipped back and forth through using next and back buttons. On the last page of presented 
text a last button is provided that can be used in conjunction with an event handler like the one we've 
got in this tutorial.