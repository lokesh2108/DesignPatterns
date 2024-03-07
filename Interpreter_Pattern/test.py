import unittest
from main import *


# Unit testing to check the Move command
class TestMoveCommand(unittest.TestCase):
    def test_interpret_with_constant_distance(self):
        turtle = Turtle()
        move_command = MoveCommand(10)
        move_command.interpret(turtle)
        self.assertEqual(turtle.location.x, 10)
        self.assertEqual(turtle.location.y, 0)

    def test_interpret_with_variable_distance(self):
        turtle = Turtle()
        turtle.variables['#distance'] = 15
        move_command = MoveCommand('#distance')
        move_command.interpret(turtle)
        self.assertEqual(turtle.location.x, 15)
        self.assertEqual(turtle.location.y, 0)

# Unit testing for Turning the direction of turtle


class TestTurnCommand(unittest.TestCase):
    def test_interpret_with_constant_degrees(self):
        turtle = Turtle()
        turn_command = TurnCommand(90)
        turn_command.interpret(turtle)
        self.assertEqual(turtle.direction, 90)

    def test_interpret_with_variable_degrees(self):
        turtle = Turtle()
        turtle.variables['#degrees'] = 45
        turn_command = TurnCommand('#degrees')
        turn_command.interpret(turtle)
        self.assertEqual(turtle.direction, 45)

# Unit testing for calculating the distance between two points


class TestDistanceToCommand(unittest.TestCase):
    def test_interpret(self):
        turtle = Turtle()
        points['s'] = Point(3, 4)
        distance_command = DistanceToCommand('#d', 's')
        result = distance_command.interpret(turtle)
        self.assertEqual(turtle.variables['#d'], 5.0)
        self.assertEqual(result, 5.0)

# Unit testing for checking the Bearing angle at which it should move.


class TestBearingToCommand(unittest.TestCase):
    def test_interpret(self):
        turtle = Turtle()
        points['s'] = Point(1, 1)
        bearing_command = BearingToCommand('#a', 's')
        result = bearing_command.interpret(turtle)
        self.assertEqual(turtle.variables['#a'], 45.0)
        self.assertEqual(result, 45.0)

# Unit testing for checking the repeat commond to repeat the statemnets within them.


class TestRepeatCommand(unittest.TestCase):
    def test_interpret(self):
        turtle = Turtle()
        move_command = MoveCommand(5)
        turn_command = TurnCommand(90)
        repeat_command = RepeatCommand(2, [move_command, turn_command])
        repeat_command.interpret(turtle)
        self.assertEqual(turtle.location.x, 5)
        self.assertEqual(turtle.location.y, 5)
        self.assertEqual(turtle.direction, 180)

# Testing the  final location of turtle after executing both Program.


class TestPrograms(unittest.TestCase):
    def test_program1(self):
        turtle = Turtle()
        for command in program1:
            command.interpret(turtle)
        self.assertEqual(turtle.location.x, 23)
        self.assertEqual(turtle.location.y, 28)

    def test_program2(self):
        turtle = Turtle()
        for command in program2:
            command.interpret(turtle)
        self.assertEqual(turtle.location.x, 5)
        self.assertEqual(turtle.location.y, 15)


if __name__ == '__main__':
    unittest.main()
