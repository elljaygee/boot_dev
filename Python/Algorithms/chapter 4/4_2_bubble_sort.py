def bubble_sort(nums):
    end = len(nums)
    swapping = False
    for i in range(end):
        for j in range(0, end - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapping = True
        if not swapping:
            break  
    return nums

'''
Explanation:
- for i in range(n): Runs multiple passes; each pass positions the next largest element at the end.
- swapped = False: Flag to detect if any swap occurs in the current pass.
- for j in range(0, n - i - 1): Iterates through unsorted elements; range shrinks as the end becomes sorted.
- if arr[j] > arr[j + 1]: Checks for inversion between adjacent elements.
- arr[j], arr[j + 1] = arr[j + 1], arr[j]: Swaps elements in place using tuple unpacking.
- if not swapped: break, Stops early if no swaps occur, indicating the array is already sorted.
'''

'''
from main import *

run_cases = [
    ([5, 7, 3, 6, 8], [3, 5, 6, 7, 8]),
    ([2, 1], [1, 2]),
]

submit_cases = run_cases + [
    ([], []),
    ([1], [1]),
    ([1, 5, -3, 2, 4], [-3, 1, 2, 4, 5]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 3, 2, 5, 4], [1, 2, 3, 4, 5]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input:\n * {input1}")
    print(f"Expected: {expected_output}")
    result = bubble_sort(input1)
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