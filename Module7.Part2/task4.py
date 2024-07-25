# Create a linked list and its iterator and generator.
from dataclasses import dataclass
from typing import Any, Optional


class LinkedList:
    def __init__(self) -> None:
        self.__first_item = None
        self.__last_item = None
        self.__count = 0

    def add_item(self, item: Any) -> None:
        new_node = self.Node(None, item)

        if self.__first_item is None:
            self.__first_item = self.__last_item = new_node
        else:
            self.__last_item.next = new_node
            self.__last_item = new_node

        self.__count += 1

    def __len__(self):
        return self.__count

    def __iter__(self):
        return self.LinkedListIterator(self)

    @dataclass
    class Node:
        next: Optional["Node"]
        value: Any

    class LinkedListIterator:
        def __init__(self, linked_list: "LinkedList"):
            self.linked_list = linked_list
            self.current_item = linked_list._LinkedList__first_item

        def __iter__(self):
            return self

        def __next__(self):
            if self.current_item:
                current_item = self.current_item
                self.current_item = self.current_item.next
                return current_item.value
            raise StopIteration

    def get_linked_list_generator(self):
        current_linked_list_item = self.__first_item

        while current_linked_list_item:
            yield current_linked_list_item.value
            current_linked_list_item = current_linked_list_item.next


def get_linked_list_generator(linked_list):
    current_linked_list_item = linked_list._LinkedList__first_item

    while current_linked_list_item:
        yield current_linked_list_item.value
        current_linked_list_item = current_linked_list_item.next


test_linked_list = LinkedList()
test_linked_list.add_item(34)
test_linked_list.add_item(68)
test_linked_list.add_item(78)
test_linked_list.add_item(100)
test_linked_list.add_item(200)

for item in test_linked_list:
    print(item)

for item in get_linked_list_generator(test_linked_list):
    print(item)

for item in test_linked_list.get_linked_list_generator():
    print(item)
