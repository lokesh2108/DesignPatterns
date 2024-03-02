from tree_node import *

# Null node class to visit each node and count the null nodes in the tree.
class NullNodeCounterVisitor:
    def __init__(self):
        self.null_node_count = 0

    #Function defines checks Null node and counts it.
    def visit(self, node):
        if isinstance(node, NullNode):
            self.null_node_count += 1
        if node.left:
            self.visit(node.left)
        if node.right:
            self.visit(node.right)

#Path Info class to visit each node and keep tracks of the path through which it is visited.
class PathInfoVisitor:
    def __init__(self):
        self.total_path_length = 0
        self.longest_path = 0
        self.node_count = 0
        self.average_path = 0
        self.real_node_count =0

    #Function counts the longest path and finds average path.
    def visit(self, node, current_path_length=0):
        if not isinstance(node, NullNode):
            self.node_count += 1
            self.total_path_length += current_path_length
            self.longest_path = max(self.longest_path, current_path_length)
            self.real_node_count +=1

            if node.left:
                self.visit(node.left, current_path_length + 1)
            if node.right:
                self.visit(node.right, current_path_length + 1)

            self.average_path = round((self.real_node_count - 1)/ self.longest_path, 2)

