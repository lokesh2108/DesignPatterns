from tree_node import *

class BinarySearchTree:
    def __init__(self):
        self.root = None


    # define insert method to append node to a tree, according to strategy
    def insert(self, student, strategy=None):
        self.root = self._insert(self.root, student, strategy)
    
    def _insert(self, node, student, strategy):
        if node is None:
            return TreeNode(student)
        
        current = strategy.apply_strategy(student) if strategy is not None else student.red_id

        if current < (strategy.apply_strategy(node.student) if strategy is not None else node.student.red_id):
            node.left = self._insert(node.left, student, strategy)
        else:
            node.right = self._insert(node.right, student, strategy)
        return node