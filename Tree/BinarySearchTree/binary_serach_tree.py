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



    def in_order_traversal(self):
        elements=[]
        # Left-->Base-->Right
        #Visit left sub tree
        if self.left:
            elements += self.left.in_order_traversal()
        #Visit base node
        elements.append(self.data)

        #Visi right node
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search_element(self,val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search_element(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search_element(val)
            else:
                return False


def build_tree(element):
    root = BinarySearchTree(element[0])

    for i in range(1,len(element)):
        root.add_child(element[i])

    return root

numbers = [45,8,12,5,7,60,23,15]
traversal = build_tree(numbers)
print(traversal.in_order_traversal())
print(traversal.search_element(60))
