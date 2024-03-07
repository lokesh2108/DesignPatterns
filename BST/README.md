

Task: Implement a binary search tree with addition. You don’t have to implement delete on the tree. The tree
contains Student objects. A student object contains first name, last name, red id, and GPA.
You will implement the following patterns on your tree.

1. Internal iterator. The iterator accepts a lambda and evaluates the lambda on all of the elements in the
   tree.
2. Strategy pattern to order the tree. You will implement three strategies. One to sort by Red Id. Another is
   to sort by the last name and then by the first name if the two last names are equal. For the third strategy,
   first round the GPA to the nearest integer. Then sort by rounded GPA and when equal use Red Id.

To run the program, change directory to this folder and run:
`python main.py`

To conduct unit testing, change directory to this folder and run:
`python bst_test.py`

Design patterns used:

1. Strategy
2. Internal Iterator

Three strategies used:

1. Sorting based on RedId
2. Sorting based on Last name and First name.
3. Sorting based on rounded GPA and RedId.

Iterator pattern is used to iterate through each node in the tree and print in a designed format specified in a lambda.
