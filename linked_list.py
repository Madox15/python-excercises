# Linked list workshop from freeCodeCamp python cert


class LinkedList:
    class Node:  # Just a containder to store a value and address of the next container
        def __init__(self, element):
            self.element = element
            self.next = None

    def __init__(
        self,
    ):  # Initialization of an empty linked list, stores it's total length of 0 and initial value of the head - None
        self.length = 0
        self.head = None

    def is_empty(
        self,
    ):  # Method to check if the list is empty, depends heavily on dev not forgetting to update the length after adding/removing element
        return self.length == 0

    def add(self, element):  # Method that adds a new element to the linked list
        node = self.Node(element)  # node variable, creates a new Node class object
        if (
            self.is_empty()
        ):  # sets the newly added element to be the head if said element is the first one in the list
            self.head = node
        else:  # if there are already elements in the list
            current_node = (
                self.head
            )  # points at the head of the entire list before iterating over elements, tl;dr says "start here"
            while (
                current_node.next is not None
            ):  # goes into the stored Node class object, takes the next attribute and checks whether it's not None, tl;dr checks if there are more elements further down the list tl;dr iterates over the entire list till it finds the end
                current_node = current_node.next  # jumps to the next element
            current_node.next = node  # sets the Node class object as the next attribute if it's currently None
        self.length += 1

    def remove(self, element):
        previous_node = None
        current_node = self.head
        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        elif previous_node is not None:
            previous_node.next = current_node.next
        else:
            self.head = current_node.next
        self.length -= 1


if __name__ == "__main__":
    my_list = LinkedList()
    print(my_list.is_empty())

    my_list.add(1)
    my_list.add(2)
    print(my_list.is_empty())
    print(my_list.length)

    my_list.remove(1)
    print(my_list.is_empty())
    print(my_list.length)
