from NumberMatch import NumberMatch
from collections import Counter
import itertools

# create from list
# guess = NumberMatch(numbers=[1, 2, 3, 2])
numbers = [0, 1, 3, 2, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 4, 5, 6, 9]

hint1 = NumberMatch([6, 8, 2], 1, 1)
hint2 = NumberMatch([6, 1, 4], 1, 0)
hint3 = NumberMatch([2, 0, 6], 2, 0)
hint4 = NumberMatch([7, 8, 0], 1, 0)
hint5 = NumberMatch([7, 3, 8], 0, 0)
# hint6 = NumberMatch([7, 8, 0], 1, 0)

hints = [hint1, hint2, hint3, hint4, hint5]

hintA = list(filter(lambda n: n.numCorrect == 0, hints))
# hintA = list((lambda n: n.numCorrect == 0, hints))
# print(hintA)
# print(hintA[0])

numbers = [x for x in numbers if x not in hintA[0].numbers]
# print(numbers)  # [1, 3, 5]

results = []
for guess in itertools.permutations(numbers, 3):
    found = True
    for hint in hints:
        pos_correct = sum(1 for g, s in zip(guess, hint.numbers) if g == s)
        hint_counts = Counter(hint.numbers)
        guess_counts = Counter(guess)
        numCorrect = sum(min(hint_counts[val], guess_counts[val]) for val in guess_counts)
        found = found and pos_correct == hint.numPositionCorrect and numCorrect == hint.numCorrect
            # print(number)
    if found == True:
        results.append(guess)
        # print(guess)
    # print(guess if found == True else "")
print(results)
