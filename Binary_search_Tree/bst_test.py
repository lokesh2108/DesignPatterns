import unittest
from bst import *
from student import *
from strategy import *
from tree_node import *
from bst_iterator import *
from tree_visitors import *

#  Test for RedId strategy
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

        

        null_node_counter1 = NullNodeCounterVisitor()
        null_node_counter1.visit(tree.root)

        path_info_visitor1 = PathInfoVisitor()
        path_info_visitor1.visit(tree.root)

        iterator = BSTIterator(tree.root)
        results = list(iterator)

        # Unit Test for checking the expected tree and null node count, longest path and average path.
        self.assertEqual(results, expected_sorted_students)
        self.assertEqual(null_node_counter1.null_node_count, 4)
        self.assertEqual(path_info_visitor1.longest_path, 2)
        self.assertEqual(path_info_visitor1.average_path, 1.0)

# Test for LastName and FirstName strategy
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

        null_node_counter2 = NullNodeCounterVisitor()
        null_node_counter2.visit(tree.root)

        path_info_visitor2 = PathInfoVisitor()
        path_info_visitor2.visit(tree.root)

        iterator = BSTIterator(tree.root)
        results = list(iterator)

        # Unit Test for checking the expected tree and null node count, longest path and average path.
        self.assertEqual(results, expected_sorted_students)
        self.assertEqual(null_node_counter2.null_node_count, 4)
        self.assertEqual(path_info_visitor2.longest_path, 1)
        self.assertEqual(path_info_visitor2.average_path, 2.0)

# Test for RoundedGpa and RedId strategy
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

        

        null_node_counter3 = NullNodeCounterVisitor()
        null_node_counter3.visit(tree.root)

        path_info_visitor3 = PathInfoVisitor()
        path_info_visitor3.visit(tree.root)

        iterator = BSTIterator(tree.root)
        results = list(iterator)

        # Unit Test for checking the expected tree and null node count, longest path and average path.
        self.assertEqual(results, expected_sorted_students)
        self.assertEqual(null_node_counter3.null_node_count, 4)
        self.assertEqual(path_info_visitor3.longest_path, 1)
        self.assertEqual(path_info_visitor3.average_path, 2.0)

if __name__ == "__main__":
    unittest.main()
