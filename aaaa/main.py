from string import ascii_lowercase
from itertools import product


class aaaa(object):
    """docstring"""

    def __init__(self, length=2):
        self._index = -1
        sequence = []

        for letter in product(ascii_lowercase, repeat=length):
            sequence.append(''.join([*letter]))

        self._sequence = sequence

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence) - 1:
            self._index += 1
            return self._sequence[self._index]
        else:
            raise StopIteration
