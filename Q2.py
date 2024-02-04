class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def clear(self):
        self.root = None

    def search(self, x):
        return self._search(self.root, x)

    def _search(self, node, x):
        if node is None or node.value == x:
            return node
        elif x < node.value:
            return self._search(node.left, x)
        else:
            return self._search(node.right, x)

    def insert(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, node, x):
        if node is None:
            return Node(x)
        if x < node.value:
            node.left = self._insert(node.left, x)
        elif x > node.value:
            node.right = self._insert(node.right, x)
        return node

    def breadth(self):
        if not self.root:
            return []

        result = []
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result

    def preorder(self, p):
        if p:
            print(p.value, end=" ")
            self.preorder(p.left)
            self.preorder(p.right)

    def inorder(self, p):
        if p:
            self.inorder(p.left)
            print(p.value, end=" ")
            self.inorder(p.right)

    def postorder(self, p):
        if p:
            self.postorder(p.left)
            self.postorder(p.right)
            print(p.value, end=" ")

    def count(self):
        return self._count(self.root)

    def _count(self, node):
        if node is None:
            return 0
        return 1 + self._count(node.left) + self._count(node.right)

    def dele(self, x):
        self.root = self._delete(self.root, x)

    def _delete(self, root, x):
        if root is None:
            return root

        if x < root.value:
            root.left = self._delete(root.left, x)
        elif x > root.value:
            root.right = self._delete(root.right, x)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.value = self._minValueNode(root.right).value
            root.right = self._delete(root.right, root.value)

        return root

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def min(self):
        return self._min(self.root)

    def _min(self, node):
        while node.left:
            node = node.left
        return node

    def max(self):
        return self._max(self.root)

    def _max(self, node):
        while node.right:
            node = node.right
        return node

    def _sum(self, node):
        if node is None:
            return 0
        return node.value + self._sum(node.left) + self._sum(node.right)

    def sum(self):
        return self._sum(self.root)

    def _height(self, node):
        if node is None:
            return -1
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return 1 + max(left_height, right_height)

    def height(self):
        return self._height(self.root)

    def _expensive_path_cost(self, node):
        if node is None:
            return 0
        left_cost = self._expensive_path_cost(node.left)
        right_cost = self._expensive_path_cost(node.right)
        return node.value + max(left_cost, right_cost)

    def expensive_path_cost(self):
        return self._expensive_path_cost(self.root)

    def is_avl(self):
        return self._is_avl(self.root)

    def _is_avl(self, node):
        if node is None:
            return True

        left_height = self._height(node.left)
        right_height = self._height(node.right)

        if abs(left_height - right_height) <= 1 and \
           self._is_avl(node.left) and \
           self._is_avl(node.right):
            return True

        return False

    def is_heap(self):
        return self._is_heap(self.root)

    def _is_heap(self, node):
        if node is None:
            return True

        if node.left and node.left.value > node.value:
            return False

        if node.right and node.right.value > node.value:
            return False

        return self._is_heap(node.left) and self._is_heap(node.right)