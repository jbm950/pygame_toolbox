#Welcome to the Widgets Basic Tutorial

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

