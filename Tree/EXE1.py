class TreeNode:
    def __init__(self,name,designation):
        self.name=name
        self.designation = designation
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

    def print_tree(self, type):
        if type == 'both':
            value = self.name + " (" + self.designation + ")"
        elif type == 'name':
            value = self.name
        else:
            value = self.designation

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(type)


def build_management_tree():
    ceo = TreeNode("Nilupul", "CEO")
    # CTO Hierarchy
    cto = TreeNode("Chinmay", "CTO")
    infra_head = TreeNode("Vishwa", "Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Gels", "HR Head")
    hr_head.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))


    #CEO hierarchy
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo

root_node = build_management_tree()
root_node.print_tree("name")
root_node.print_tree("designation")
root_node.print_tree("both")