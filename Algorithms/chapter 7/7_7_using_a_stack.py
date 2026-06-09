from typing import Any


class Stack:
    def __init__(self) -> None:
        self.items: list[Any] = []

    def push(self, item: Any) -> None:
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def peek(self) -> Any:
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def pop(self) -> Any:
        if len(self.items) == 0:
            return None
        item = self.items[-1]
        del self.items[-1]
        return item


def is_balanced(input_str: str) -> bool:
    new_stack = Stack()

    for char in input_str:
        # add char to stack
        if char == "(":
            new_stack.push(char)
        elif char == ")":
            # check if the new stack is empty, if it is, then the string is automatically unbalanced because the first char is ")"
            if new_stack.size() == 0:
                return False
            # otherwise remove the "(" and don't add the ")" to keep the new stack balanced
            new_stack.pop()
    # check if new stack is empty, if it is, that means it's balanced
    if new_stack.size() == 0:
        return True
    # otherwise there is something left in the stack meaning it is unbalanced
    return False

'''
from main import *

run_cases = [
    ("(", False),
    ("()", True),
    ("(())", True),
]

submit_cases = run_cases + [
    ("()()", True),
    ("(()))", False),
    ("((())())", True),
    ("(()(()", False),
    (")(", False),
    (")()(()", False),
    ("())(()", False),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expected: {expected_output}")
    result = is_balanced(input1)
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
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


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
'''