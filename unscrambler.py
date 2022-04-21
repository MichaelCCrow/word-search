from typing import List


class Unscrambler(object):

    def __init__(self, words: List[str]):
        self.words = [word.strip() for word in words]

    def unscramble(self, letters: str) -> List[str]:
        words = self.unscramble_min_length_4(letters)
        return [word for word in words if not any(word.count(letter) > letters.count(letter) for letter in word)]

    def unscramble_min_length_4(self, letters: str) -> List[str]:
        words = [word for word in self.words if len(word) <= len(letters) and len(word) > 3]
        return [word for word in words if all(letter in letters for letter in word)]
        # return [word for word in self.words if len(word) <= len(letters) and len(word)>3 and all(letter in letters for letter in word) ]

    def unscramble_max_length(self, letters: str) -> List[str]:
        words = [word for word in self.words if len(word) == len(letters)]
        return [word for word in words if all(letter in letters for letter in word)]
