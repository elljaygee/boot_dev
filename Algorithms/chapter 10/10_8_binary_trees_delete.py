''' EXPLANATION:
“What node should replace the root of this subtree after deletion?”
The flow:
1. If the value is smaller
if val < self.val:
    if self.left is not None:
        self.left = self.left.delete(val)
    return self

The value must be somewhere on the left. You ask the left child to delete it, then update self.left in case that subtree changed.
You return self because the current node is still the root.

2. If the value is larger
Same idea, but on the right:

self.right = self.right.delete(val)
return self

3. If this is the node to delete
If there's no right child:

return self.left

The left child replaces this node.

If there's no left child:

return self.right

The right child replaces this node.

4. If it has two children
You can't simply return left or right, because that would lose half the tree.
So you find the smallest value in the right subtree:

current = self.right
while current.left is not None:
    current = current.left

That value is the next-largest value after self.val, so it's safe to move into this node:

self.val = current.val

Then you delete the duplicate from the right subtree:

self.right = self.right.delete(current.val)

Finally:

return self

Because this node still exists; it just has a new value.

In short: recursive delete works by returning the new subtree root after each deletion.'''

from typing import Any


class BSTNode:
    def delete(self, val: Any) -> "BSTNode | None":
        if self.val is None:
            return None
        if val < self.val: # if the 
            if self.left is not None:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right is not None:
                self.right = self.right.delete(val)
            return self
        if val == self.val:
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            if self.right is not None:
                current = self.right
                while current.left is not None:
                    current = current.left
                self.val = current.val
                self.right = self.right.delete(current.val)
                return self
                

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

    def get_min(self) -> Any:
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self) -> Any:
        current = self
        while current.right is not None:
            current = current.right
        return current.val

'''
import random
from main import *
from user import *
from ref import *  # ref module is hidden because it has the solution!

run_cases = [
    (6, 2, [User(0), User(9), User(16), User(17)]),
    (
        12,
        4,
        [
            User(2),
            User(10),
            User(11),
            User(17),
            User(22),
            User(27),
            User(30),
            User(33),
        ],
    ),
]

submit_cases = run_cases + [
    (
        24,
        6,
        [
            User(2),
            User(3),
            User(9),
            User(10),
            User(12),
            User(16),
            User(18),
            User(19),
            User(22),
            User(23),
            User(35),
            User(39),
            User(45),
            User(51),
            User(54),
            User(68),
            User(69),
            User(70),
        ],
    ),
]


def test(num_users, num_to_delete, expected):
    users = get_users(num_users)
    users_copy = users.copy()
    random.shuffle(users_copy)
    users_to_delete = users_copy[:num_to_delete]
    bst = BSTNode()
    for user in users:
        bst.insert(user)
    print("=====================================")
    print("Tree:")
    print_tree(bst)
    print("-------------------------------------\n")
    try:
        actual_bst = BSTNode()
        for user in users:
            actual_bst.insert(user)
        print("Deleting users: " + str(users_to_delete))
        for user in users_to_delete:
            actual_bst = actual_bst.delete(user)
        print("Actual Tree:")
        print_tree(actual_bst)
        print("-------------------------------------")
        actual = ref_inorder(actual_bst, [])
        print(f"Expected: {expected}")
        print(f"Actual:   {actual}")
        if expected == actual:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def print_tree(bst_node):
    if bst_node is not None:
        lines = []
        format_tree_string(bst_node, lines)
        for line in lines:
            print(line)


def format_tree_string(bst_node, lines, level=0):
    if bst_node is not None:
        format_tree_string(bst_node.right, lines, level + 1)
        lines.append(" " * 4 * level + "> " + str(bst_node.val))
        format_tree_string(bst_node.left, lines, level + 1)


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


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
'''