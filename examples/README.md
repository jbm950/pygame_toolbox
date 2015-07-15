#Welcome to the examples for Pygame Toolbox
Pygame Toolbox is a collection of tools to aid game making in Python. To better
understand how to use the library please reference the tutorials below.

Example usage of the menus. For more detail refer to the basic menus tutorial
below

```python
    # Import the graphics tools and pygame and sys
    import pygame_toolbox.graphics as ptg
    import pygame, sys

    def close():
        # close out pygame and the game window properly
        pygame.quit()
        sys.exit()

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

    if __name__ == '__main__':
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        screen = pygame.display.set_mode((800,600))
        Main().update(screen)
```
##Tutorials

* [Basic Menus Tutorial](./menu_example/menu_tutorial.md) - This tutorial goes
  over the main classes in the graphics module.
* [Basic Widgets Tutorial](./widget_examples/widgets_basic_tutorial.md) - This
  tutorial will introduce the basic structure of the widget objects used in
  this library.
* [Tilegame Tools Tutorial](./tiletools_example/tilegame_tools_tutorial.md) -
  This tutorial goes over the main tools provided in the tilegame module.
