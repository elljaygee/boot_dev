from typing import Any


class BSTNode:
    def postorder(self, visited: list[Any]) -> list[Any]:
        # traverse left subtree, passing the same list down
        if self.left is not None:
            self.left.postorder(visited)
        # traverse right subtree, passing the same list down
        if self.right is not None:
            self.right.postorder(visited)
        if self.val is not None:
            visited.append(self.val)
        return visited

    # don't touch below this line

    def __init__(self, val: Any = None) -> None:
        self.left: "BSTNode | None" = None
        self.right: "BSTNode | None" = None
        self.val = val

    def insert(self, val: Any) -> None:
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

import random


class User:
    def __init__(self, id: int) -> None:
        self.id = id
        user_names = [
            "Blake",
            "Ricky",
            "Shelley",
            "Dave",
            "George",
            "John",
            "James",
            "Mitch",
            "Williamson",
            "Burry",
            "Vennett",
            "Shipley",
            "Geller",
            "Rickert",
            "Carrell",
            "Baum",
            "Brownfield",
            "Lippmann",
            "Moses",
        ]
        self.user_name = f"{user_names[id % len(user_names)]}#{id}"

    def __eq__(self, other: "User") -> bool:
        return isinstance(other, User) and self.id == other.id

    def __lt__(self, other: "User") -> bool:
        return isinstance(other, User) and self.id < other.id

    def __gt__(self, other: "User") -> bool:
        return isinstance(other, User) and self.id > other.id

    def __repr__(self) -> str:
        return "".join(self.user_name)


def get_users(num: int) -> list[User]:
    random.seed(1)
    users = []
    ids = []
    for i in range(num * 3):
        ids.append(i)
    random.shuffle(ids)
    ids = ids[:num]
    for id in ids:
        user = User(id)
        users.append(user)
    return users

'''from main import *
from user import *
import random

run_cases = [
    (
        4,
        [User(0), User(8), User(11), User(7)],
    ),
    (
        6,
        [User(0), User(9), User(5), User(17), User(16), User(10)],
    ),
]

submit_cases = run_cases + [
    (
        12,
        [
            User(11),
            User(10),
            User(18),
            User(17),
            User(19),
            User(2),
            User(23),
            User(27),
            User(33),
            User(30),
            User(22),
            User(34),
        ],
    ),
]


def test(num_characters, expected):
    characters = get_users(
        num_characters
    )  # Ensure this reflects your project structure
    bst = BSTNode()
    for character in characters:
        bst.insert(character)
    print("=====================================")
    print("Tree:")
    print("-------------------------------------")
    print(print_tree(bst))
    print("-------------------------------------\n")
    print(f"Expected: {expected}")
    try:
        actual = bst.postorder([])
        print(f"Actual:   {actual}")
        if expected == actual:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
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


def print_tree(bst_node):
    lines = []
    format_tree_string(bst_node, lines)
    return "\n".join(lines)


def format_tree_string(bst_node, lines, level=0):
    if bst_node is not None:
        format_tree_string(bst_node.right, lines, level + 1)
        lines.append(" " * 4 * level + "> " + str(bst_node.val))
        format_tree_string(bst_node.left, lines, level + 1)


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
'''