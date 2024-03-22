class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children = []
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

    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = '  ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                # print(child.data)
                child.print_tree(level)


def build_location_tree():
    root = TreeNode("Global")

    #Country
    india = TreeNode("India")
    usa = TreeNode("USA")

    #State
    gujrat = TreeNode("Gujarat")
    karnata = TreeNode("Karnataka")
    new_jersy = TreeNode("New Jersey")
    california = TreeNode("California")

    # city
    ahm = TreeNode("Ahemedbad")
    bar = TreeNode("Baroda")
    bang = TreeNode("Bengaluru")
    ms = TreeNode("Masore")
    pri = TreeNode("Princeton")
    tre=TreeNode("Trenton")
    san = TreeNode("San Faransisco")
    mv = TreeNode("Mountain View")
    pa= TreeNode("Palo Alto")

    #state hierarchy
    gujrat.add_child(ahm)
    gujrat.add_child(bar)
    karnata.add_child(bang)
    karnata.add_child(ms)

    new_jersy.add_child(pri)
    new_jersy.add_child(tre)
    california.add_child(san)
    california.add_child(mv)
    california.add_child(pa)

    #Country Hierarchy

    india.add_child(gujrat)
    india.add_child(karnata)

    usa.add_child(new_jersy)
    usa.add_child(california)

    #global
    root.add_child(india)
    root.add_child(usa)

    return root



root_node = build_location_tree()
root_node.print_tree(1)
root_node.print_tree(2)
root_node.print_tree(3)


