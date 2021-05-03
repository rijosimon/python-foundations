#!/usr/bin/env python3

class SingleLinkedNode:

    def __init__(self, value = '', next = None):
        self.value = value
        self.next = next

    def printList(self):
        """This function prints the list start at this node."""
        print(self.value)
        while(self.next != None):
            self = self.next
            print(self.value)

    def insert_sorted(self, num):
        """This function inserts a number into the list in sorted order."""
        num_node = SingleLinkedNode(num)
        if self.value >= num:
            print("Do i get here.")
            num_node.next = self
            return num_node
        else:
            return_head = self
            while(self.next!=None):
                prev_self = self
                self = self.next
                if self.value >= num:
                    prev_self.next = num_node
                    num_node.next = self
                    return return_head
            self.next = num_node
            return return_head

    def insert_list_sorted(self, num):
        """This function inserts a list into the linked list in sorted order."""
        pass
                

def test_single_linked_list():
    print("Creating a single linked list with 5 nodes!!")
    head = SingleLinkedNode(5)
    head_perm = head
    for i in range(0, 4):
        head.next = SingleLinkedNode((5 + (i+1)*5))
        head = head.next
    print("Printing the generate 5 node single linked list.")
    head_perm.printList()
    num = input("Give me a number and I will insert it in a sorted order to the above list: ")
    head_perm = head_perm.insert_sorted(int(num))
    print("The new linked list.")
    head_perm.printList()

if __name__ == "__main__":
    test_single_linked_list()        
