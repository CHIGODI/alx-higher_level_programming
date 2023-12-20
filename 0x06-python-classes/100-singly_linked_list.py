#!/usr/bin/python3

""" Definition of a node that defines a node """


class Node:
    """ Represents a node in a singly linked list """

    def __init__(self, data, next_node=None):
        """ Initializes a Node with data and a reference to the next node """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Getter method to retrieve the data of the node """
        return self.__data

    @data.setter
    def data(self, value):
        """ Setter method to set the data of the node """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Getter method to retrieve the reference to the next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Setter method to set the reference to the next node """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object or None")
        self.__next_node = value


""" Defines a Singly Linked List class """


class SinglyLinkedList:
    """ Represents a singly linked list """

    def __init__(self):
        """ Initializes a SinglyLinkedList with a head node as None """
        self.__head = None

    def sorted_insert(self, value):
        """ Inserts a new node with value into the sorted linked list """

        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """ Returns a string representation of the linked list """

        nodes = []
        current = self.__head

        while current:
            nodes.append(str(current.data))
            current = current.next_node

        return "\n".join(nodes)
