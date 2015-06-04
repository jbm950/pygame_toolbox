#Tilegame Tutorial

This tutorial will go over the tile and tilelist classes in the tilegame_tools module and wrap up by using the tilemap class to put the previous sections together. The [tiletools example](./tiletools_example.py) script is what this tutorial will be following. (Note these tiles are similar to board game tiles. If you were looking for code to interact with the tiled editor I would suggest checking out [PyTMX](https://github.com/bitcraft/PyTMX).)

To begin the tutorial we'll import the tilegame tools from pygame toolbox along with pygame and sys.

```python
    # Import the tile game toolbox, pygame and sys
    import pygame_toolbox.tilegame_tools as pttt
    import pygame, sys
```

Now we can begin the disscussion on the different classes that are covered in this tutorial.

##The Tile Class

This is the main class for tilegames. It will hold information for each individual space on the game board. Lets begin by subclassing the tile class in our script.

```python
    # Create a custom Tile class
    class Tile(pttt.Tile):
        def __init__(self,file,size):
            # Pass the file and size arguments to the init of the class
            # in the toolbox
            pttt.Tile.__init__(self,file,size)
```

The file input is the string of the picture file that we want to be the image for the tile. The size argument is the x,y size of the tile in pixels. As is it seems like subclassing has not provided us with any benefit from the original class but now we can attach additional attributes to each instance. For example if we were doing a city building type of board game we could attach resources to the tile or an attribute to determine which player owns the tile. What we are going to do in the tutorial, though, is cover the other main aspect of the tile class, shades. Here we are going to initialize a shade to be put over the tile under certain conditions. I'm going to go ahead and show the code then explain each of the inputs.

```python
            # Add a shade to the tiles shade dictionary
            pttt.Tile.initialize_shade(self,"orange red",(255,69,0),150)
```

The "orange red" argument in the method is what we want our shade to be called. The three item tuple is the rgb value of the shade (a planned addition is to allow strings with a picture file's name to be used instead of rgb values). The last item in the method call is the alpha value of the shade. This number ranges from 0 to 255 and determines the transparency of the shade where 0 is completely transparent and 255 is completely solid. The initialize shade method will take these arguments and will add them to the instances shade dictionary where the key is the name we gave the shade and the value is a pygame surface with the color and transparency we passed.