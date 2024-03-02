# Visitor interface
class Visitor:
    def visit(self, node):
        pass


# Actual Tree Node
class TreeNode:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None

    def accept(self, visitor):
        visitor.visit(self)
        if self.left:
            self.left.accept(visitor)
        if self.right:
            self.right.accept(visitor)

# Null Node class for storing null nodes in the tree.


class NullNode(TreeNode):
    def __init__(self):
        self.student = None
        self.left = None
        self.right = None

    def accept(self, visitor):
        visitor.visit(self)

# Real Node class for storing the student's value.


class RealNode(TreeNode):
    def __init__(self, student, left=None, right=None):
        self.student = student
        self.left = left
        self.right = right

    def accept(self, visitor):
        visitor.visit(self)
        if self.left:
            self.left.accept(visitor)
        if self.right:
            self.right.accept(visitor)

