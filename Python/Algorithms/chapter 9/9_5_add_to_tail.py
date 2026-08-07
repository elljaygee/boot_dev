from linked_lists import Node


class LinkedList:
    def add_to_tail(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            return
        last_node = self.head
        for current_node in self:
            last_node = current_node
        last_node.set_next(node)

'''
If the list is empty, self.head = node makes the new node the first node.
If the list is not empty, last = self.head starts at the first node.
for item in self: uses your __iter__ method to visit each node from head to tail.
Each loop sets last = item, so when the loop finishes, last is the final node.
last.set_next(node) connects the old tail to the new node.'''        
            
    # don't touch below this line

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
    (["Major Marquis Warren", "John Ruth"],),
    (["Major Marquis Warren", "John Ruth", "Daisy Domergue"],),
]

submit_cases = run_cases + [
    (["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix"],),
    (["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix", "Bob"],),
    (
        [
            "Major Marquis Warren",
            "John Ruth",
            "Daisy Domergue",
            "Chris Mannix",
            "Bob",
            "Oswaldo Mobray",
        ],
    ),
]


def test(inputs):
    print("---------------------------------")
    linked_list = LinkedList()
    for val in inputs:
        linked_list.add_to_tail(Node(val))
    actual = linked_list_to_list(linked_list)

    print(f"Expected: {inputs}")
    print(f"Actual  : {actual}")

    if actual == inputs:
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
        if test(test_case[0]):
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