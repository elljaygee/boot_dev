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

        self.fix_insert(new_node)

    def fix_insert(self, new_node: RBNode) -> None:
        current_node = new_node
        while current_node is not self.root and current_node.parent is not None and current_node.parent.parent is not None and current_node.parent.red == True:
            parent = current_node.parent
            grandparent = parent.parent
            
            if parent is grandparent.right:
                uncle = grandparent.left
                if uncle.red == True:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    current_node = grandparent

                elif uncle.red == False:
                    if current_node is parent.left:
                        current_node = parent
                        self.rotate_right(current_node)
                        parent = current_node.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_left(grandparent)

            elif parent is grandparent.left:
                uncle = grandparent.right
                if uncle.red == True:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    current_node = grandparent

                elif uncle.red == False:
                    if current_node is parent.right:
                        current_node = parent
                        self.rotate_left(current_node)
                        parent = current_node.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_right(grandparent)

        self.root.red = False
                    

    def exists(self, val: Any) -> RBNode:
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def rotate_left(self, pivot_parent: RBNode) -> None:
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent: RBNode) -> None:
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        else:
            pivot_parent.parent.left = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot

'''
from main import *
from user import *
from ref import *  # ref module is hidden because it has the solution!

run_cases = [
    (4),
]

submit_cases = run_cases + [
    (10),
]


def test(num_users):
    users = get_users(num_users)
    tree = RBTree()
    reference_tree = RBTree()
    for user in users:
        tree.insert(user)
        ref_impl_ins(reference_tree, user)
    print("=====================================")
    print("Expected:")
    print("-------------------------------------")
    print(print_tree(reference_tree))
    print("-------------------------------------\n")
    print("Actual:")
    print("-------------------------------------")
    print(print_tree(tree))
    print("-------------------------------------\n")

    if print_tree(tree) == print_tree(reference_tree):
        print("Pass \n")
        return True
    print("Fail \n")
    return False


def print_tree(node):
    lines = []
    format_tree_string(node.root, lines)
    return "\n".join(lines)


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