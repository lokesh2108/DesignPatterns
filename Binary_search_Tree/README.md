

Task: Implement a binary search tree with addition. You don’t have to implement delete on the tree. The tree
contains Student objects. A student object contains first name, last name, red id and GPA.
You will implement the following patterns on your tree.

1. Internal iterator. The iterator accepts a lambda and evaluates the lambda on all of the elements in the
   tree.
2. Strategy pattern to order the tree. You will implement three strategies. One to sort by Red Id. Another is
   to sort by the last name and then by the first name if the two last names are equal. For the third strategy,
   first round the GPA to the nearest integer. Then sort by rounded GPA and when equal use Red Id.
3. Null Object pattern to add a null node to your tree to eliminate the need to check for null
   references or pointers in your tree.
4. Visitor pattern. Implement two visitors, One to count the number of null nodes. Another is to
   compute the longest path in the tree and the average path length in the tree.

To run the program, change directory to this folder and run:
`python main.py`

To conduct unit testing, change directory to this folder and run:
`python bst_test.py`

Design patterns used:

1. Strategy
2. Internal Iterator
3. Null Object pattern
4. Visitor pattern

Three strategies used:

1. Sorting based on RedId
2. Sorting based on Last name and First name.
3. Sorting based on rounded GPA and RedId.

Iterator pattern is used to iterate through each node in the tree and print in a designed format specified in a lambda.

Null Object pattern is used inorder to do some opertion like insert in the tree, it don't want to check the everytime wheather the node is null,so to avoid checking everytime we used Null object pattern.

Visior Pattern is used in:

1. To calculate the count of null node in the Tree.
2. To calculate the longest path in tree and average path in Tree.


