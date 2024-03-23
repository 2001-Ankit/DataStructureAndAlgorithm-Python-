# 1. find_min(): finds minimum element in entire binary tree
# 2. find_max(): finds maximum element in entire binary tree
# 3. calculate_sum(): calcualtes sum of all elements
# 4. post_order_traversal(): performs post order traversal of a binary tree
# 5. pre_order_traversal(): perofrms pre order traversal of a binary tree
class BinarySearchTree:
    def __init__(self,data):
        self.data= data
        self.left=None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return
        if data<self.data:
          # add it to the ledt subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTree(data)

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


    def find_max(self):
        if self.right is None:
           return self.data
        return self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        total = self.data+left_sum+right_sum
        return total

    def pre_traversal(self):
        elements =[self.data]
        # Visit left node
        if self.left:
            elements += self.left.pre_traversal()
        #Visi right node
        if self.right:
            elements += self.right.pre_traversal()

        return elements


    def post_traversal(self):
        elements =[]
        if self.left:
            elements += self.left.post_traversal()
        if self.right:
            elements += self.right.post_traversal()
        elements.append(self.data)

        return elements
    #Deleting value using right subtree min mum value as it copy
    # def delete(self, val):
    #     if val < self.data:
    #         if self.left:
    #             self.left.delete(val)
    #     elif val > self.data:
    #         if self.right:
    #             self.right.delete(val)
    #     else:
    #         if self.left is None and self.right is None:
    #             return None
    #         elif self.left is None:
    #             return self.right
    #         elif self.right is None:
    #             return self.right
    #         min_val = self.right.find_min()
    #         self.data = min_val
    #         self.right = self.right.delete(min_val)
    #
    #     return self

    # Deletig using left subtree using its maximum vale
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right= self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right
            min_val = self.left.find_max()
            self.data = min_val
            self.left = self.left.delete(min_val)

        return self


def build_tree(element):
    root = BinarySearchTree(element[0])
    for i in range(1,len(element)):
        root.add_child(element[i])

    return root

numbers = [15,12,7,14,27,20,23,88 ]
traversal = build_tree(numbers)
print(traversal.find_min())
print(traversal.calculate_sum())
print(traversal.post_traversal())
traversal.delete(27)
print(traversal.post_traversal())