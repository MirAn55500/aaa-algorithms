class TreeNode:

    def __init__(self, parent, key: int):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent
    def insert(self, node):
        if node is None:
            return
        if node.key < self.key:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)

def get_level_order_keys_and_levels(preorder_keys: list):
    root = TreeNode(parent=None, key=preorder_keys[0])
    keys = [root.key]
    levels = [0]

    for i in preorder_keys[1:]:
        node = TreeNode(parent=None, key=i)
        root.insert(node)

    current_level = [root]

    while current_level:
        next_level = []
        next_level_levels = []

        for node in current_level:
            if node.left is not None:
                keys.append(node.left.key)
                next_level.append(node.left)
                next_level_levels.append(levels[-1] + 1)

            if node.right is not None:
                keys.append(node.right.key)
                next_level.append(node.right)
                next_level_levels.append(levels[-1] + 1)

        current_level = next_level
        levels += next_level_levels

    return keys, levels

def solution():
    preorder_keys = list(map(int, input().split()))
    level_order_keys, levels = get_level_order_keys_and_levels(preorder_keys)
    print(' '.join(map(str, level_order_keys)))
    print(' '.join(map(str, levels)))

solution()