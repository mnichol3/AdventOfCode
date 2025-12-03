"""
tree_sort.py

Basic tree sort algo.
"""
from typing import Any


class BinarySearchTree:
    """Construct a Binary Search Tree."""

    class Node:
        """A node in the binary search tree."""

        def __init__(self, value) -> None:
            """Initialize a Node instance."""
            self.value = value
            self.left: Node = None
            self.right: Node = None

    def __init__(self) -> None:
        """Initialize an empty BST."""
        self.root = None
        self.flattened_values = []

    def insert(self, item: Any) -> None:
        """Insert a new node non-recursively"""
        new_node = BinarySearchTree.Node(item)

        if self.root:
            parent = self.root
            while True:
                if item < parent.value:
                    if parent.left:
                        parent = parent.left
                    else:
                        parent.left = new_node
                        break
                else:
                    if parent.right:
                        parent = parent.right
                    else:
                        parent.right = new_node
                        break
        else:
            self.root = new_node

    def load(self, item_list: list[Any]) -> None:
        """Populate the BST from a list of items."""
        for x in item_list:
            self.insert(x)

    def _traverse(self, parent: Node) -> Node:
        if parent is None:
            return

        self._traverse(parent.left)
        self.flattened_values.append(parent.value)
        self._traverse(parent.right)

    def sort(self) -> list[Node]:
        """Sort, or flatten, the BST. List will be sorted least -> greatest."""
        if self.root:
            self._traverse(self.root)

        return self.flattened_values

    @property
    def is_empty(self) -> bool:
        return self.root == None