class TreeNode:
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
        if x < node.value:
            return self._search(node.left, x)
        else:
            return self._search(node.right, x)

    def insert(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, node, x):
        if node is None:
            return TreeNode(x)
        if x < node.value:
            node.left = self._insert(node.left, x)
        elif x > node.value:
            node.right = self._insert(node.right, x)
        return node

    def breadth(self):
        if self.root is None:
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
        if p is not None:
            print(p.value, end=" ")
            self.preorder(p.left)
            self.preorder(p.right)

    def inorder(self, p):
        if p is not None:
            self.inorder(p.left)
            print(p.value, end=" ")
            self.inorder(p.right)

    def postorder(self, p):
        if p is not None:
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

    def _delete(self, node, x):
        if node is None:
            return None
        if x < node.value:
            node.left = self._delete(node.left, x)
        elif x > node.value:
            node.right = self._delete(node.right, x)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.value = self._min_value(node.right)
            node.right = self._delete(node.right, node.value)
        return node

    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.value

    def min(self):
        return self._min(self.root)

    def _min(self, node):
        while node.left is not None:
            node = node.left
        return node.value if node else None

    def max(self):
        return self._max(self.root)

    def _max(self, node):
        while node.right is not None:
            node = node.right
        return node.value if node else None

    def sum(self):
        return self._sum(self.root)

    def _sum(self, node):
        if node is None:
            return 0
        return node.value + self._sum(node.left) + self._sum(node.right)

    def avg(self):
        count = self.count()
        if count == 0:
            return 0
        return self.sum() / count

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return 1 + max(left_height, right_height)

    def cost_of_most_expensive_path(self):
        return self._cost_of_most_expensive_path(self.root)

    def _cost_of_most_expensive_path(self, node):
        if node is None:
            return 0
        left_cost = self._cost_of_most_expensive_path(node.left)
        right_cost = self._cost_of_most_expensive_path(node.right)
        return node.value + max(left_cost, right_cost)

    def is_avl(self):
        return self._is_avl(self.root)

    def _is_avl(self, node):
        if node is None:
            return True
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        if abs(left_height - right_height) > 1:
            return False
        return self._is_avl(node.left) and self._is_avl(node.right)

    def is_heap(self):
        return self._is_heap(self.root)

    def _is_heap(self, node):
        if node is None:
            return True
        if node.left is not None and node.left.value > node.value:
            return False
        if node.right is not None and node.right.value > node.value:
            return False
        return self._is_heap(node.left) and self._is_heap(node.right)
