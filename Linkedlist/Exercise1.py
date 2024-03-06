class Node:
    """This represents a single node in the linked list.
     It has two attributes: data, which stores the data of the node,
    and next, which points to the next node in the list."""
    def __init__(self, data=None, next =None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node


    def print(self):
        if self.head is None:
            print("List is empty")
            return
        itr = self.head
        llistr = ''
        while itr:
            llistr += str(itr.data) + '-->'
            itr = itr.next
        print(llistr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self,data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next

        return count


    def remove_at(self,index):
        if index<0 or index>= self.get_length():
            raise Exception("invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index to insert")

        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1


    def insert_after_value(self, data_after, data_to_insert):

        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return


        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                break

            itr = itr.next


    def remove_by_value(self, data):
    # Remove first node that contains data
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break

            itr = itr.next


li = Linkedlist()

# li.insert_at_end(20)
# li.insert_at_begining(55)
# li.insert_at_begining(260)
li.insert_values(['apple', 'banana', 'car'])
li.print()
# # li.remove_at(1)
# # li.print()
# # li.insert_at_begining('banana')
# li.insert_at(0, 'papaya')
# li.print()
# li.insert_at(4, 'grapes')
# li.print()
li.insert_after_value('banana', 'tensor')
li.print()

# li.remove_by_value('apple')
# li.print()

# li.remove_by_value('tensor')
# li.print()
#
# li.remove_by_value('banana')
# li.remove_by_value('apple')
# li.print()
li.print_forward()
print("Length of my linked list is ", li.get_length())