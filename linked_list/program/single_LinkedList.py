class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # this is reversely data is appending
    def insert_at_begning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return 
        
        itr = self.head
        linked_list_str = ''
        while itr:
            linked_list_str += str(itr.data) + "-->"
            itr = itr.next
        print(linked_list_str)

    #this technique working like appending data to the end
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return 
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index!")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count  = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index!")
        
        if index == 0:
            self.insert_at_begning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):
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



if __name__ == "__main__":
    linked_list = LinkedList()

    # inserting element at the start
    linked_list.insert_at_begning(99)
    linked_list.insert_at_begning(999)

    # inserting element at the end
    linked_list.insert_at_end(9)

    # inserting the data list
    linked_list.insert_values(["banana","mango","grapes","orange"])
    linked_list.print()

    # insert element after this values
    #linked_list.insert_after_value("mango","apple")
    #linked_list.print()

    # insert element after this values
    linked_list.remove_by_value("orange")
    linked_list.print()

    # insert element at specific index
    #linked_list.insert_at(1,"zzz")
    #linked_list.print()

    # remove element at specific index
    #linked_list.remove_at(1)
    #linked_list.print()

    # get the length of the linked list
    #print("length :", linked_list.get_length())
