#Welcome to the Widgets Basic Tutorial

(Note: This tutorial is written for pygame_toolbox version 0.1)

In this tutorial we will cover the basic structure of the widgets that this
library uses. To begin let's define what this library refers to as a widget.
Normally the definition of a widget is an interactable object in GUI
programming. In this module, however, it has a much more specific definition. A
widget in Pygame Toolbox is an object that will be called by the graphic
module's menu object without exiting the menu. Normally the menu object will
return the result of an interactable such as a button and exit the menu's
update method. The widgets therefore give the capability to create objects that
will interact within the menu or to allow the menu to collect state information
given by the user.

##Widget Fundamentals

The widgets in Pygame Toolbox will all come with some specific attributes to be
made use of by your event handlers. Each widget will have a name attribute and
a status attribute. The name attribute can be used to identify the specific
widget and the status attribute will allow the widget to pass along state
information to your program. For example you could use the checkbox widget to
determine what class the player of your game wishes to be and the name
attributes would be 'warrior' and 'mage'. Then based on the status attribute of
the widget you're code will be able to assign the proper class for their
character. In addition each widget will need to be callable and accept at least
one argument in addition to self, even if the call does nothing important. In
sum each widget will need to somewhat match the following format.

```python
    class Widget:
        def __init__(self, name):
            self.name = name
            self.status = 0

        def __call__(self, menu):
            pass
```

