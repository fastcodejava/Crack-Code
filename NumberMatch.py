from dataclasses import dataclass, field
from typing import List, Iterable


@dataclass
class NumberMatch:
    """
    Represents a set of guessed numbers and two result counters:
      - numbers: the list of guessed numbers (ints)
      - numCorrect: how many guessed values appear anywhere in the secret
      - numPositionCorrect: how many guessed values are correct and in the correct position
    """
    numbers: List[int] = field(default_factory=list)
    numCorrect: int = 0
    numPositionCorrect: int = 0

    def __post_init__(self):
        # ensure numbers is a list of ints
        if isinstance(self.numbers, Iterable) and not isinstance(self.numbers, (str, bytes)):
            self.numbers = [int(x) for x in self.numbers]
        else:
            raise TypeError("numbers must be an iterable of integers")

        # coerce counters to ints and basic validation
        self.numCorrect = int(self.numCorrect)
        self.numPositionCorrect = int(self.numPositionCorrect)

        if self.numCorrect < 0 or self.numPositionCorrect < 0:
            raise ValueError("Counters must be non-negative")

    @classmethod
    def from_string(cls, s: str, sep: str = ","):
        """
        Create NumberMatch from a string like "1,2,3".
        """
        parts = [p.strip() for p in s.split(sep) if p.strip() != ""]
        nums = [int(p) for p in parts]
        return cls(numbers=nums)

    def update_counters(self, secret: Iterable[int]):
        """
        Given a secret sequence of integers, compute:
          - numPositionCorrect: count of elements equal in same index
          - numCorrect: count of values from guess that appear in secret (multiset aware)
        Both counters are updated on the instance and also returned as a tuple.
        """
        secret_list = list(secret)
        guess = self.numbers

        # numPositionCorrect: same index and same value
        pos_correct = sum(1 for g, s in zip(guess, secret_list) if g == s)

        # numCorrect: count matches considering multiplicity (multiset intersection)
        # build counts for secret
        from collections import Counter
        secret_counts = Counter(secret_list)
        guess_counts = Counter(guess)
        multiset_intersection_count = sum(min(secret_counts[val], guess_counts[val]) for val in guess_counts)

        self.numPositionCorrect = pos_correct
        self.numCorrect = multiset_intersection_count

        return self.numCorrect, self.numPositionCorrect

    def to_dict(self):
        return {
            "numbers": list(self.numbers),
            "numCorrect": self.numCorrect,
            "numPositionCorrect": self.numPositionCorrect,
        }

    def __repr__(self):
        return f"NumberMatch(numbers={self.numbers}, numCorrect={self.numCorrect}, numPositionCorrect={self.numPositionCorrect})"
