# Simple-Python-Card-Deck-Library
Simple functionality for a deck of cards in python for games such as Blackjack, Texas Hold 'em, etc.

Intended for teaching about classes and libraries in Python at an introductory level.

## Getting Started

### Importing Your New Library

So, you've decided to take a look at classes and libraries, using multiple files for your ambitious projects. Lets start by getting all those juicy functions into your new file.

Start by making a new Python script in your favourite text editor or IDE. You may have learned how to import libraries such as ```random``` already. This is almost no different! Go ahead and place the files included here in the same directory, and simply write:

```import Deck as d```

This will give you access to all that this library has to offer by using the prefix ```d```.

This is how we will specify between functions/classes you create, and those imported by the library. In languages such as C++, there are other considerations such as overloading that we will make, but we will keep this tutorial simple and leave it as such.

### The basis of classes

Before we go on to use our library and its classes, lets first learn about their nature.

Classes have extreme importance across the field of computer science. We use them to bundle data and functions together (however, in this context, they are called methods).

You can think of a class as a blueprint for a specific kind of object. For example, there may be a class "Car", which we can use to create many different cars with a unique set of attributes. Each object will have the same kinds of attributes, but may have a different value. While there is only one class car, we might create a red car with manual transmission, or a blue car that is automatic. Importantly however, both will have access to the same functionality, such as driving.

Immediately, it should become evident that we can use this to our advantage when managing large sets of data that is connected. 

## Classes in python

### Creating a class

To create a class, we will write the following code:

```
class myClass:

    def __init__(self, somevalue):
      self._someattribute = somevalue
      *** Initialize some more values

    def somefunction(self):
      *** Do some calcultion
```

The class is composesd of its methods (the function definitions within the class) and its attributes. The methods define what we may do to or within an object of this class, and the attributes are what describe the object.

### Objects of a class

When we create an object of a class, we will instantiate all of its attributes to some given or default value. Each class may also have functions that we can call that alter, receive, or calculate some sort of value related to our object. We can create a new object by calling the class as we would a function, with the initial required conditions. In Python, when a new object of a given class is created, an initial function within the class is called. 

For all classes, this initial function is denoted ```def __init__(self):```. Note, we will always have the parameter *self* in our ```__init__``` (or constructor), and in most functions of the class. This is because we use the parameter *self* to refer to the given object. However, we do not need to include *self* when calling this method, as it is automatically included when called under the object.

For instance, if we have a class rectangle which we instantiate with length and width, we would access these values within other methods of the class using ```self.length``` or ```self.width```. This tells Python to look for the length and width values associated with the object from which the method is called. 

This all is getting a little complicated, so lets take a look at some code.

```
class 2DPoint:
  
   def __init__(self, x, y):
      self._x = x
      self._y = y
      
   def printPoint(self):
      print('(' + str(self.x) + ', ' + str(self.y) + ')')
      
   def changeX(self, x):
      self._x = x
      
   def changeY(self y):
      self._y = y
 
def __main__():

   point1 = 2DPoint(1, 2)
   point2 = 2DPoint(2, 1)
   
   point1.printPoint()
   point2.printPoint()
   
   point1.changeY(2)
   point2.changeX(1)
   
   point1.printPoint()
   point2.printPoint()
   
```

Take a look and try to determine how this code will run, assuming ```__main__()``` is called at run-time.

To start, we create two points, ```point1``` and ```point2```. Think of these as simply points on a 2D plane, with an x value, and a y value. There are no other attributes to consider in this scenario.

Next, we print the points in the format ```(x, y)```. We call this method by using the notation ```object.method(parameters)```, where the method is defined as a form of function within the class definition.  Each object will use its own values when these methods are called, making them unique to the given object.  For instance, we will only ever git the values we've set in ```point1``` when calling ```point1.printPoint()```, but we will get different values when ```point2.printPoint()``` is called.

### Object Methods and Access

Generally, there are two main branches of methods for a class: getters, and setters. You may have been wondering when viewing this code why we can't simply call ```object.x``` to get the x value of our point. This is because we have declared that this attribute is protected. This means that only this class and its subclasses (don't worry, we'll talk about this later) may access this attribute. So, if we try to call ```object.x``` from our main function, we will get an error. We do this to protect our data from being accessed from places it should not be, as well as a myriad of other reasons. For now, know that it is a convention, and should be done.

Our methods, however, are members of this class, and can have access to them. We gain access to the data our object holds by using methods called 'getters'. Likewise, if we need to alter an attribute, we will use a setter, which does retain access to the data as well.

In Python, we have three different 'access levels' for any given function or attribute of a class:

__Public__
  - These do not have a prefix, and can be accessed from anywhere within our program

__Protected__
  - A prefix of _ declares that this is protected.
  - It may only be accessed by members of this class and subclasses

__Private__
  - A prefix of __ declares that this is private.
  - It may only be accessed by members of this class.

Generally, we will want to use either Public or Private declarations until we get to subclasses.

# Cont. Here
