#Menu Tutorial
In this tutorial I'm going to go over the code in the script menu_examples.py.
This script can be found [here](./menu_examples.py)

First let us begin by importing the modules that we will need. Since pygame_toolbox.graphics is a bit verbose I'm going to import it as ptg.
    
        # Import the graphics tools and pygame and sys
        import pygame_toolbox.graphics as ptg
        import pygame,sys

Next I'm going to define a function to properly close out of the program when needed. Without this you'll get errors when trying to close the pygame screen.

    def close():
        # close out pygame and the game window properly
        pygame.quit()
        sys.exit()