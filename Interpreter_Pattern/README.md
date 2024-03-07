

We are going to implement part of a program inspired by Etoys (http://www.squeakland.org),
Scratch (https://scratch.mit.edu) and turtle graphics
(http://en.wikipedia.org/wiki/Turtle_graphics).
We will have a turtle object that moves on the 2D plane. At the start of a program we can add
labels points on the plane.
We will support the turtle moving and turning. The goal is to create a small language that kids
can use to program the turtle. We will not implement the graphics part of the program, even
though that is a key part of EToys, Scratch and Turtle graphics. We are just interested in the
section of the program that interprets the language.

Task: 
1. Using the interpreter pattern we want to take the following two turtle programs and
represent the program as abstract syntax trees which we can execute. So if our file contained
the following program after Reading (reading part is not necessary) and executing the program
the turtle would end up at (23, 28).
```move 10
turn 90
move 20
turn -60
move 15
```

2. The other program is the following square example:
```#Ps = 10, 10
#Pt = 10, 20
#d = distanceTo #s
#a = bearingTo #s
turn #a
move #d
#u = bearingTo #t
move 5
turn 90
move 5
repeat 4
turn 90
move 10
end
```

### To run this program, use "python main.py" and to test, use "python test.py"
