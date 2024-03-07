from strategy import *
from student import *
from bst_iterator import *
from bst import *

# Create a BinarySearchTree and prepopulate with data
# Insert according to the strategy
tree1 = BinarySearchTree()
tree1.insert(Student("John", "Smith", 8432, 3.8), RedIdStrategy())
tree1.insert(Student("Zayn", "Smith", 4113, 3.1), RedIdStrategy())
tree1.insert(Student("Bob", "Smith", 2678, 2.7), RedIdStrategy())
tree1.insert(Student("Eva", "Brown", 1098, 3.9), RedIdStrategy())
tree1.insert(Student("Tom", "Corey", 9567, 1.3), RedIdStrategy())
tree1.insert(Student("Anderson", "James", 6768, 4.0), RedIdStrategy())

tree2 = BinarySearchTree()
tree2.insert(Student("John", "Smith", 8432, 3.8), LastNameFirstNameStrategy())
tree2.insert(Student("Zayn", "Smith", 4113, 3.1), LastNameFirstNameStrategy())
tree2.insert(Student("Bob", "Smith", 2678, 2.7), LastNameFirstNameStrategy())
tree2.insert(Student("Eva", "Brown", 1098, 3.9), LastNameFirstNameStrategy())
tree2.insert(Student("Tom", "Corey", 9567, 1.3), LastNameFirstNameStrategy())
tree2.insert(Student("Anderson", "James", 6768, 4.0), LastNameFirstNameStrategy())

tree3 = BinarySearchTree()
tree3.insert(Student("John", "Smith", 8432, 3.8), RoundedGpaRedIdStrategy())
tree3.insert(Student("Zayn", "Smith", 4113, 3.1), RoundedGpaRedIdStrategy())
tree3.insert(Student("Bob", "Smith", 2678, 2.7), RoundedGpaRedIdStrategy())
tree3.insert(Student("Eva", "Brown", 1098, 3.9), RoundedGpaRedIdStrategy())
tree3.insert(Student("Tom", "Corey", 9567, 1.3), RoundedGpaRedIdStrategy())
tree3.insert(Student("Anderson", "James", 6768, 4.0), RoundedGpaRedIdStrategy())


# Define a lambda function to print each element
print_lambda = lambda x: print(f"Name: {x.first_name} {x.last_name}, RedId: {x.red_id}, GPA: {x.gpa}")

# Use the iterator to traverse the elements in the BinarySearchTree with the lambda function
print("Traversing BinarySearchTree:")
bst_iterator1 = BSTIterator(tree1.root, print_node=print_lambda)
bst_iterator2 = BSTIterator(tree2.root, print_node=print_lambda)
bst_iterator3 = BSTIterator(tree3.root, print_node=print_lambda)

# Print students in all the trees using iterator
print("\nTree 1 based on red_id ")
for iteration in bst_iterator1:
    pass


print("\nTree 2 based on LastName and FirstName")
for iteration in bst_iterator2:
    pass

print("\nTree 3 based on rounded gpa and red_id")
for iteration in bst_iterator3:
    pass