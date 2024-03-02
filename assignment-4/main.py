import math

# Point class for representing points


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Turtle class for keeping track of turtle state


class Turtle:
    def __init__(self):
        self.location = Point(0, 0)
        self.direction = 0
        self.variables = {}

    def move(self, distance):
        radians = self.direction * math.pi / 180
        deltaX = math.cos(radians) * distance
        deltaY = math.sin(radians) * distance
        self.location.x += deltaX
        self.location.y += deltaY
        self.location.x = round(self.location.x)
        self.location.y = round(self.location.y)

    def turn(self, degrees):
        self.direction += degrees
        self.direction %= 360

    def distance_to(self, target):
        return math.sqrt((self.location.x - target.x)**2 + (self.location.y - target.y)**2)

    def bearing_to(self, target):
        radians = math.atan2(target.y - self.location.y,
                             target.x - self.location.x)
        degrees = math.degrees(radians)
        return degrees if degrees >= 0 else 360 + degrees


# Abstract Command class

class Command:
    def interpret(self, turtle):
        pass


# Concrete Command classes

class MoveCommand(Command):
    def __init__(self, distance):
        self.distance = distance

    def interpret(self, turtle):
        if isinstance(self.distance, str):
            variable_value = turtle.variables.get(self.distance, 0)
            turtle.move(variable_value)
        else:
            turtle.move(self.distance)


class TurnCommand(Command):
    def __init__(self, degrees):
        self.degrees = degrees

    def interpret(self, turtle):
        if isinstance(self.degrees, str):
            numeric_degrees = turtle.variables.get(self.degrees, 0)
        else:
            numeric_degrees = float(self.degrees)

        turtle.turn(numeric_degrees)


class DistanceToCommand(Command):
    def __init__(self, variable, label):
        self.variable = variable
        self.label = label

    def interpret(self, turtle):
        target = points[self.label]
        distance = turtle.distance_to(target)
        turtle.variables[self.variable] = distance
        return distance


class BearingToCommand(Command):
    def __init__(self, variable, label):
        self.variable = variable
        self.label = label

    def interpret(self, turtle):
        target = points[self.label]
        bearing = turtle.bearing_to(target)
        turtle.variables[self.variable] = bearing
        return bearing


class DefinePointCommand(Command):
    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y

    def interpret(self, turtle):
        points[self.label] = Point(self.x, self.y)


class DefineVariableCommand(Command):
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

    def interpret(self, turtle):
        turtle.variables[self.variable] = self.value


class RepeatCommand(Command):
    def __init__(self, repetitions, statements):
        self.repetitions = repetitions
        self.statements = statements

    def interpret(self, turtle):
        for _ in range(self.repetitions):
            for statement in self.statements:
                statement.interpret(turtle)


# Example program with added commands
points = {}
program1 = [
    MoveCommand(10),
    TurnCommand(90),
    MoveCommand(20),
    TurnCommand(-60),
    MoveCommand(15)
]
program2 = [

    DefinePointCommand('s', 10, 10),
    DefinePointCommand('t', 10, 20),
    DistanceToCommand('#d', 's'),
    BearingToCommand('#a', 's'),
    TurnCommand('#a'),
    MoveCommand('#d'),
    BearingToCommand('#u', 't'),
    TurnCommand('#a'),
    MoveCommand(5),
    TurnCommand(90),
    MoveCommand(5),
    RepeatCommand(4, [
        TurnCommand(90),
        MoveCommand(10),
    ]),

]

# Execute the programs
turtle1 = Turtle()
for command in program1:
    command.interpret(turtle1)
print("Final Turtle Location with program 1:",
      turtle1.location.x, turtle1.location.y)

turtle2 = Turtle()
for command in program2:
    command.interpret(turtle2)
print("Final Turtle Location with program 2:",
      turtle2.location.x, turtle2.location.y)
