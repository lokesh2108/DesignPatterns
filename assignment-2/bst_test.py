import unittest
from bst import *
from student import *
from strategy import *
from tree_node import *
from bst_iterator import *


class TestRedIdStrategy(unittest.TestCase):
    def test_red_id_strategy(self):
        tree = BinarySearchTree()
        students = [
            Student("John", "Smith", 82345, 3.0),
            Student("Alice", "Johnson", 45678, 3.5),
            Student("Bob", "Wilson", 12345, 2.8),
        ]

        expected_sorted_students = [students[2], students[1], students[0]]

        for student in students:
            tree.insert(student, RedIdStrategy())

        iterator = BSTIterator(tree.root)
        results = list(iterator)

        self.assertEqual(results, expected_sorted_students)

class TestLastNameFirstNameStrategy(unittest.TestCase):
    def test_last_name_first_name_strategy(self):
        tree = BinarySearchTree()
        students = [
            Student("John", "Smith", 82345, 3.0),
            Student("Alice", "Johnson", 45678, 3.5),
            Student("Bob", "Wilson", 12345, 2.8),
        ]

        expected_sorted_students = [students[1], students[0], students[2]]

        for student in students:
            tree.insert(student, LastNameFirstNameStrategy())

        iterator = BSTIterator(tree.root)
        results = list(iterator)

        self.assertEqual(results, expected_sorted_students)

class TestRoundedGpaRedIdStrategy(unittest.TestCase):
    def test_rounded_gpa_red_id_strategy(self):
        tree = BinarySearchTree()
        students = [
            Student("John", "Smith", 82345, 3.0),
            Student("Alice", "Johnson", 45678, 3.5),
            Student("Bob", "Wilson", 12345, 2.8),
        ]

        expected_sorted_students = [students[2], students[0], students[1]]

        for student in students:
            tree.insert(student, RoundedGpaRedIdStrategy())

        iterator = BSTIterator(tree.root)
        results = list(iterator)

        self.assertEqual(results, expected_sorted_students)

if __name__ == "__main__":
    unittest.main()
