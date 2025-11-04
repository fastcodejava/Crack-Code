from NumberMatch import NumberMatch
from collections import Counter
import itertools

# create from list
# guess = NumberMatch(numbers=[1, 2, 3, 2])
numbers = [0, 1, 3, 2, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 4, 5, 6, 9]

# hint1 = NumberMatch(281, 1, 1)
# hint2 = NumberMatch(619, 1, 0)
# hint3 = NumberMatch(348, 2, 0)
# hint4 = NumberMatch(924, 1, 0)
# hint5 = NumberMatch(731, 1, 0)
# hint6 = NumberMatch(462, 0, 0)

# hint1 = NumberMatch(612, 1, 1)
# hint2 = NumberMatch(308, 0, 0)
# hint3 = NumberMatch(792, 2, 2)
# hint4 = NumberMatch(014, 1, 0)
# hint5 = NumberMatch(874, 1, 0)
# hint1 = NumberMatch(682, 1, 1)
# hint2 = NumberMatch(614, 1, 0)
# hint3 = NumberMatch(206, 2, 0)
# hint4 = NumberMatch(780, 1, 0)
# hint5 = NumberMatch(738, 0, 0)
# hint6 = NumberMatch(780, 1, 0)

hint1 = NumberMatch(548, 1, 1)
hint2 = NumberMatch(350, 0, 0)
hint3 = NumberMatch(157, 2, 0)
hint4 = NumberMatch(806, 1, 0)
hint5 = NumberMatch(647, 1, 0)


# hints = [hint1, hint2, hint3, hint4, hint5, hint6]
hints = [hint1, hint2, hint3, hint4, hint5]

hintA = list(filter(lambda n: n.numCorrect == 0, hints))
# hintA = list((lambda n: n.numCorrect == 0, hints))
# print(hintA)
# print(hintA[0])

numbers = [x for x in numbers if x not in hintA[0].numbers]
# print(numbers)  # [1, 3, 5]

results = []
# for guess in itertools.product(numbers, 3):
count = 0
for guess in itertools.permutations(numbers, 3):
    found = True
    count += 1
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
print(count, results)
