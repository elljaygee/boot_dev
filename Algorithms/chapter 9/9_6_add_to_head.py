from linked_lists import Node

class LinkedList:
    def add_to_head(self, node: Node) -> None:
        node.set_next(self.head)
        self.head = node

    # don't touch below this line

    def add_to_tail(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            return
        last_node = self.head
        for current_node in self:
            last_node = current_node
        last_node.set_next(node)

    def __init__(self) -> None:
        self.head: Node | None = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)

'''
from main import *

run_cases = [
    (["Major Marquis Warren", "John Ruth"], ["John Ruth", "Major Marquis Warren"]),
    (
        ["Major Marquis Warren", "John Ruth", "Daisy Domergue"],
        ["Daisy Domergue", "John Ruth", "Major Marquis Warren"],
    ),
]

submit_cases = run_cases + [
    (
        ["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix"],
        ["Chris Mannix", "Daisy Domergue", "John Ruth", "Major Marquis Warren"],
    ),
    (
        ["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix", "Bob"],
        ["Bob", "Chris Mannix", "Daisy Domergue", "John Ruth", "Major Marquis Warren"],
    ),
    (
        [
            "Major Marquis Warren",
            "John Ruth",
            "Daisy Domergue",
            "Chris Mannix",
            "Bob",
            "Oswaldo Mobray",
        ],
        [
            "Oswaldo Mobray",
            "Bob",
            "Chris Mannix",
            "Daisy Domergue",
            "John Ruth",
            "Major Marquis Warren",
        ],
    ),
]


def test(inputs, expected_state):
    print("---------------------------------")
    linked_list = LinkedList()
    for val in inputs:
        linked_list.add_to_head(Node(val))
    result = linked_list_to_list(linked_list)

    print(f"Input:  {inputs}")
    print(f"Expect: {expected_state}")
    print(f"Actual: {result}")

    if result == expected_state:
        print("Pass")
        return True
    else:
        print("Fail")
        return False


def linked_list_to_list(linked_list):
    return [node.val for node in linked_list]


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        if test(*test_case):
            passed += 1
        else:
            failed += 1

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
'''