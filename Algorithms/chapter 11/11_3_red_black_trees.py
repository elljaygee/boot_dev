from typing import Any


class RBNode:
    def __init__(self, val: Any) -> None:
        self.red = False
        self.parent: "RBNode | None" = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self) -> None:
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val: Any) -> None:
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current is not self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            elif new_node.val == current.val:
                return
                
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        elif new_node.val > parent.val:
            parent.right = new_node 

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

'''
import random
from main import *
from user import *
from ref import *  # ref module is hidden because it has the solution!

run_cases = [
    (4),
    (8),
]

submit_cases = run_cases + [
    (10),
]


def print_tree(node):
    lines = []
    format_tree_string(node.root, lines)
    print("\n".join(lines))


def format_tree_string(node, lines, level=0):
    if node.val is not None:
        format_tree_string(node.right, lines, level + 1)
        lines.append(
            " " * 4 * level
            + "> "
            + str(node.val)
            + " "
            + ("[red]" if node.red else "[black]")
        )
        format_tree_string(node.left, lines, level + 1)


def test(num_users):
    users = get_users(num_users)
    ref_tree = RBTree()
    for user in users:
        ref_implementation(ref_tree, user)
    print("============ NEW TEST ===============")
    actual_tree = RBTree()
    for user in users:
        print(f"Inserting {user} into tree...")
        actual_tree.insert(user)
    print("-------------------------------------")
    print("Expecting Tree:")
    print("-------------------------------------")
    print_tree(ref_tree)
    print("-------------------------------------")
    print("Actual Tree:")
    print("-------------------------------------")
    print_tree(actual_tree)
    print("-------------------------------------")
    if ref_inorder(actual_tree.root, []) == ref_inorder(ref_tree.root, []):
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(test_case)
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


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
'''