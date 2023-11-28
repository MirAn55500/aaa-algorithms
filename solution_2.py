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

    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def next_larger(self):
        if self.right is not None:
            return self.right.find_min()
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent

    def delete(self):
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        else:
            s = self.next_larger()
            self.key, s.key = s.key, self.key
            return s.delete()

    def find(self, key):
        if key == self.key:
            return self
        elif key < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(key)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(key)


def make_preorder(root, preorder=[]):
    if root.parent is None:
        preorder.append(root.key)
    if root.left is not None:
        preorder.append(root.left.key)
        make_preorder(root.left, preorder)
    if root.right is not None:
        preorder.append(root.right.key)
        make_preorder(root.right, preorder)
    return preorder


def find_and_left_rotate(preorder_keys: list, key: int):
    if not preorder_keys:
        return []

    root = TreeNode(parent=None, key=preorder_keys[0])

    for i in preorder_keys[1:]:
        node = TreeNode(parent=None, key=i)
        root.insert(node)

    found = root.find(key)

    if found is None or found.right is None:
        return preorder_keys

    right_child = found.right

    if found.parent is not None:
        if found.parent.key > found.key:
            found.parent.left = right_child
        else:
            found.parent.right = right_child

    right_child.parent = found.parent
    found.parent = right_child
    found.right = right_child.left

    if right_child.left is not None:
        right_child.left.parent = found

    right_child.left = found

    while root.parent is not None:
        root = root.parent

    return make_preorder(root)


def solution():
    preorder_keys = list(map(int, input().split()))
    key = int(input())
    preorder_keys_after_rotate = find_and_left_rotate(preorder_keys, key)
    print(' '.join(map(str, preorder_keys_after_rotate)))


solution()
