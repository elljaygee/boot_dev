from typing import Any


class Trie:
    def search_level(
        self, current_level: dict[str, Any], current_prefix: str, words: list[str]
    ) -> list[str]:
        if self.end_symbol in current_level:
            words.append(current_prefix)
        for letter in sorted(dict.keys(current_level)):
            if letter != self.end_symbol:
                extended_prefix = current_prefix + letter
                self.search_level(current_level[letter], extended_prefix, words)
        return words

    def words_with_prefix(self, prefix: str) -> list[str]:
        words_list = []
        current_level = self.root
        for letter in prefix:
            if letter not in current_level:
                return []
            current_level = current_level[letter]
        return self.search_level(current_level, prefix, words_list)

    # don't touch below this line

    def __init__(self) -> None:
        self.root = {}
        self.end_symbol = "*"

    def add(self, word: str) -> None:
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                current_level[letter] = {}
            current_level = current_level[letter]
        current_level[self.end_symbol] = True

"""
import json
from main import *

run_cases = [
    (["dev", "devops", "designer", "director"], "de", ["dev", "devops", "designer"]),
    (["manager", "intern"], "z", []),
    (["cto", "cfo", "coo", "ceo"], "c", ["cto", "cfo", "coo", "ceo"]),
]

submit_cases = run_cases + [
    (
        ["developer", "designer", "devops", "director"],
        "de",
        ["developer", "designer", "devops"],
    ),
]


def test(words, prefix, expected_matches):
    print("---------------------------------")
    print("Trie:")
    trie = Trie()
    for word in words:
        trie.add(word)
    print(json.dumps(trie.root, sort_keys=True, indent=2))
    print(f'Words with prefix: "{prefix}":')
    print(f"Expected: {sorted(expected_matches)}")
    try:
        actual = trie.words_with_prefix(prefix)
        print(f"Actual:   {actual}")
        if (actual) == sorted(expected_matches):
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


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
"""