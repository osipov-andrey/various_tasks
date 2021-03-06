from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

    @property
    def is_leaf(self):
        return not self.left and not self.right

    @property
    def left_value(self) -> Optional[int]:
        try:
            return self.left.value
        except AttributeError:
            return

    @property
    def right_value(self) -> Optional[int]:
        try:
            return self.right.value
        except AttributeError:
            return

    def __repr__(self):
        return f"{self.left_value} <= ({self.value}) => {self.right_value}"


class Tree:
    def __init__(self, root: TreeNode):
        self.root = root

    def max_depth(self) -> int:
        return self._get_min_or_max_depth(self.root, max)

    def min_depth(self) -> int:
        return self._get_min_or_max_depth(self.root, min)

    def is_balanced(self) -> bool:
        return self.max_depth() - self.min_depth() <= 1

    @staticmethod
    def _get_min_or_max_depth(root: TreeNode, func: [min, max]):
        # TODO: by stack
        if root is None:
            return 0
        return 1 + func(
            Tree._get_min_or_max_depth(root.left, func),
            Tree._get_min_or_max_depth(root.right, func)
        )

    @staticmethod
    def linearize(root: TreeNode) -> list:
        values_ = [root.value]
        stack = [root, ]
        while stack:
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            values_.append(node.left_value)
            values_.append(node.right_value)
        return values_

    @staticmethod
    def delinearize(values_: list) -> Optional[TreeNode]:
        # TODO: by stack
        if not values_:
            return

        def _get_next_node_val(i):
            try:
                val = values_[i]
            except IndexError:
                val = None
            return val

        def _gen_node(root_index, left_index, right_index):

            root_value = _get_next_node_val(root_index)

            left_node = None
            left_val = _get_next_node_val(left_index)

            right_node = None
            right_val = _get_next_node_val(right_index)

            if left_val:
                left_node = _gen_node(left_index, left_index * 2 + 1, left_index * 2 + 2)
            if right_val:
                right_node = _gen_node(right_index, right_index * 2 + 1, right_index * 2 + 2)

            return TreeNode(val=root_value, left=left_node, right=right_node)

        tree_root = _gen_node(0, 1, 2)
        return tree_root


if __name__ == "__main__":
    # TODO: tests
    values = [3, 2, None]
    root_node = Tree.delinearize(values)
    tree = Tree(root_node)
    print(tree.max_depth())
    print(tree.min_depth())
    print(tree.is_balanced())

    linearized_tree = Tree.linearize(root_node)
    print(linearized_tree)

