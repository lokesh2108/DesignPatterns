# DesignPatterns
In this Project, we practice Different design Patterns inorder to get familiar with the concepts.

Implement a binary search tree with addition. You don’t have to implement delete on the tree. The tree contains Student objects. A student object contains first name, last name, red id, and GPA. You will implement the following patterns on your tree.

1. Internal iterator. The iterator accepts a lambda and evaluates the lambda on all of the elements in the
   tree.
2. Strategy pattern to order the tree. You will implement three strategies. One to sort by Red Id. Another is
   to sort by the last name and then by the first name if the two last names are equal. For the third strategy,
   first round the GPA to the nearest integer. Then sort by rounded GPA and when equal use Red Id.
3. Null Object pattern to add a null node to your tree to eliminate the need to check for null
   references or pointers in your tree.
4. Visitor pattern. Implement two visitors, One to count the number of null nodes. Another is to
   compute the longest path in the tree and the average path length in the tree.


We are going to implement part of a program inspired by Etoys (http://www.squeakland.org), Scratch (https://scratch.mit.edu) and turtle graphics (http://en.wikipedia.org/wiki/Turtle_graphics). We will have a turtle object that moves on the 2D plane. At the start of a program we can add labels points on the plane. We will support the turtle moving and turning. The goal is to create a small language that kids can use to program the turtle. We will not implement the graphics part of the program, even though that is a key part of EToys, Scratch and Turtle graphics. We are just interested in the section of the program that interprets the language.

Implements a trie using a linked structure.
Be able to add words and find words.
Find all words in the trie that contain the letters "ar". The letters must be contiguous in the word. For example, "hardware" does contain the letters "ar" contiguously but the word "batter" does not.
Print out all words in the trie.



Design patterns that are used completely all over the project:

1. Strategy
2. Internal Iterator
3. Null Object pattern
4. Visitor pattern
5. Interpreter pattern


To run the program, change directory to this folder and run: `python3 main.py` or `python main.py`
