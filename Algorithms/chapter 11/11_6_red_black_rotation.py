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

    def rotate_left(self, pivot_parent: RBNode) -> None:
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left is not self.nil:
            pivot.left.parent = pivot_parent
        pivot.parent = pivot_parent.parent
        if pivot_parent == self.root:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot
            
    def rotate_right(self, pivot_parent: RBNode) -> None:
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot.right is not self.nil:
            pivot.right.parent = pivot_parent
        pivot.parent = pivot_parent.parent
        if pivot_parent == self.root:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot

        # don't touch below this line

    def insert(self, val: Any) -> None:
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # duplicate, just ignore
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node


'''
import random
from main import *
from user import *
from ref import *  # ref module is hidden because it has the solution!

run_cases = [
    (4),
]

submit_cases = run_cases + [
    (10),
]


def test_rotate(tree, node, reference_tree, reference_node, direction):
    print(f"Rotating {direction} at {node.val}...")
    print("-------------------------------------")
    if direction == "left":
        tree.rotate_left(node)
        ref_impl_left(reference_tree, reference_node)
    else:
        tree.rotate_right(node)
        ref_impl_right(reference_tree, reference_node)
    print("Expected Tree:")
    print("-------------------------------------")
    print_tree(reference_tree)
    print("-------------------------------------")
    print("Actual Tree:")
    print("-------------------------------------")
    print_tree(tree)
    print("-------------------------------------")
    return ref_compare(tree.root, reference_tree.root)


def test_rotations(tree, reference_tree):
    return (
        test_rotate(tree, tree.root, reference_tree, reference_tree.root, "left")
        and test_rotate(tree, tree.root, reference_tree, reference_tree.root, "right")
        and test_rotate(
            tree, tree.root.right, reference_tree, reference_tree.root.right, "left"
        )
        and test_rotate(
            tree, tree.root.left, reference_tree, reference_tree.root.left, "right"
        )
    )


def test(num_users):
    users = get_users(num_users)
    tree = RBTree()
    reference_tree = RBTree()
    for user in users:
        tree.insert(user)
        reference_tree.insert(user)
    print("=====================================")
    print("Starting Tree:")
    print("-------------------------------------")
    print_tree(tree)
    print("-------------------------------------")

    if test_rotations(tree, reference_tree):
        print("Pass \n")
        return True
    print("Fail 1 \n")
    return False


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


def print_tree(node):
    lines = []
    format_tree_string(node.root, lines)
    print("\n".join(lines))


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