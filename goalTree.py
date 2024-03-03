class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def postorder_traversal(self):
        traversal = []
        for child in self.children:
            traversal.extend(child.postorder_traversal())
        traversal.append(self.value)
        return traversal
