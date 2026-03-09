from NumberMatch import NumberMatch
from collections import Counter
import itertools

# create from list
# guess = NumberMatch(numbers=[1, 2, 3, 2])
numbers = [x for x in range(10)]
numDigits = 4
# print(numbers)

hints = (
        NumberMatch("5410", 2, 0),
        NumberMatch("3675", 1, 0),
        NumberMatch("4587", 2, 1),
        NumberMatch("0592", 1, 0),
        NumberMatch("9034", 1, 1)
        )

hintA = list(filter(lambda n: n.numCorrect == 0, hints))
# hintA = hintA if hintA is not None else []
print(hintA)

# numbers = [x for x in numbers if len(hintA) > 0 and x not in hintA[0].numbers] if hintA is not None else numbers
# print(numbers)
if len(hintA) > 0:
    # numbers = [x for x in numbers if len(hintA) > 0 and x not in hintA[0].numbers]
    numbers = [x for x in numbers if x not in hintA[0].numbers]
# print(numbers)

def validGuess(guess, hint):
    # print(guess)
    pos_correct = sum(1 for g, s in zip(guess, hint.numbers) if g == s)
    hint_counts = Counter(hint.numbers)
    guess_counts = Counter(guess)
    numCorrect = sum(min(hint_counts[val], guess_counts[val]) for val in guess_counts)
    # print(guess, pos_correct, numCorrect)
    return pos_correct == hint.numPositionCorrect and numCorrect == hint.numCorrect

count = 0
# print(numbers)
guesses = itertools.permutations(numbers, numDigits)
# print(guesses)
results = [guess for guess in guesses if all(validGuess(guess, hint) for hint in hints)]

# print(count, results)
print(results)
