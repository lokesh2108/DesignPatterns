from collections.abc import Iterator
from typing import Any, Callable
from tree_node import *

# define an iterator class and implement iterator strategy
class BSTIterator(Iterator):
    def __init__(self, root: TreeNode, print_node: Callable[[Any], None] = None):
        self.root = root
        self.stack = []
        self._print_node = print_node
        self._inorder_traversal(root)

    def _inorder_traversal(self, node: TreeNode):
        while node and not isinstance(node, NullNode):
            self.stack.append(node)
            node = node.left
            

    def __next__(self):
        if not self.stack:
            raise StopIteration()

        node = self.stack.pop()

        if isinstance(node, RealNode):
            if self._print_node:
                self._print_node(node.student)

            if node.right:
                self._inorder_traversal(node.right)

            return node.student

        return None