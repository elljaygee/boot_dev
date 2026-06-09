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


from typing import Any


class BSTNode:
    def get_min(self) -> Any:
        current = self # start at the root
        while current.left is not None: # check if there is a value to the left of the current position
            current = current.left # if there is then you're not at the leftmost position so "walk" one step left
        return current.val # once there are no more values on the left, then return the value of the current position

    def get_max(self) -> Any:
        current = self
        while current.right is not None:
            current = current.right
        return current.val

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


'''
import random
from main import *
from user import *

run_cases = [
    (5, "Blake#0", "Carrell#14"),
    (10, "Ricky#1", "Vennett#29"),
]

submit_cases = run_cases + [
    (15, "Shelley#2", "George#42"),
]


def test(num_users, min_user, max_user):
    users = get_users(num_users)
    bst = BSTNode()
    for user in users:
        bst.insert(user)
    print("=====================================")
    print("Tree:")
    print("-------------------------------------")
    print_tree(bst)
    print("-------------------------------------\n")
    print(f"Expected min: {min_user}, max: {max_user}")
    try:
        actual_min = bst.get_min()
        actual_max = bst.get_max()
        print(f"Actual min: {actual_min.user_name}, max: {actual_max.user_name}")
        if actual_max.user_name == max_user and actual_min.user_name == min_user:
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
    print("\n".join(lines))


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