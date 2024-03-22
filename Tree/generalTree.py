class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children=[]
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent

        return level


    def print_tree(self):
        spaces = '  '*self.get_level()*3
        prefix = spaces +'|__'if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
            # print(child.data)
                child.print_tree()
def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Dell"))
    laptop.add_child(TreeNode("Acer"))

    mobile = TreeNode("Mobile")
    mobile.add_child(TreeNode("Iphone"))
    mobile.add_child(TreeNode("samsung"))
    mobile.add_child(TreeNode("Xaomi"))

    tv = TreeNode("Tv")
    tv.add_child(TreeNode("Andriod"))
    tv.add_child(TreeNode("LCD"))
    tv.add_child(TreeNode("LED"))


    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(tv)


    return root
if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()