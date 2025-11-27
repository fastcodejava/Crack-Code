from NumberMatch import NumberMatch
from collections import Counter
import itertools

# create from list
# guess = NumberMatch(numbers=[1, 2, 3, 2])
numbers = [x for x in range(10)]

# print(numbers)

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

# hint1 = NumberMatch(689, 1, 1)
# hint2 = NumberMatch(104, 1, 0)
# hint3 = NumberMatch(205, 2, 0)
# hint4 = NumberMatch(738, 0, 0)
# hint5 = NumberMatch(587, 1, 0)

# hint1 = NumberMatch("548", 1, 1)
# hint2 = NumberMatch("530", 0, 0)
# hint3 = NumberMatch("157", 2, 0)
# hint4 = NumberMatch("806", 1, 0)
# hint5 = NumberMatch("647", 1, 0)

hint1 = NumberMatch("682", 1, 1)
hint2 = NumberMatch("614", 1, 0)
hint3 = NumberMatch("206", 2, 0)
hint4 = NumberMatch("780", 1, 0)
hint5 = NumberMatch("738", 0, 0)
hint6 = NumberMatch("780", 1, 0)

# hint1 = NumberMatch("548", 1, 1)
# hint2 = NumberMatch("350", 0, 0)
# hint3 = NumberMatch("157", 2, 0)
# hint4 = NumberMatch("806", 1, 0)
# hint5 = NumberMatch("647", 1, 0)
# 046
# hint1 = NumberMatch("549", 1, 1)
# hint2 = NumberMatch("350", 0, 0)
# hint3 = NumberMatch("157", 2, 0)
# hint4 = NumberMatch("806", 1, 0)
# hint5 = NumberMatch("573", 1, 0)
# hint6 = NumberMatch("268", 1, 0)

# hint1 = NumberMatch("368", 1, 1)
# hint2 = NumberMatch("527", 0, 0)
# hint3 = NumberMatch("176", 1, 0)
# hint4 = NumberMatch("471", 2, 0)

# hint1 = NumberMatch("3682", 1, 1)
# hint2 = NumberMatch("5271", 0, 0)
# hint3 = NumberMatch("1768", 1, 0)
# hint4 = NumberMatch("4710", 2, 0)


# hints = [hint1, hint2, hint3, hint4, hint5, hint6]
# hints = [NumberMatch(682, 1, 1), NumberMatch(614, 1, 0), NumberMatch(206, 2, 0), NumberMatch(780, 1, 0), NumberMatch(738, 0, 0), NumberMatch(780, 1, 0)]
# hints = [hint1, hint2, hint3, hint4]
hints = [hint1, hint2, hint3, hint4, hint5, hint6]

hintA = list(filter(lambda n: n.numCorrect == 0, hints))

numbers = [x for x in numbers if x not in hintA[0].numbers]

def validGuess(guess, hint):
    pos_correct = sum(1 for g, s in zip(guess, hint.numbers) if g == s)
    hint_counts = Counter(hint.numbers)
    guess_counts = Counter(guess)
    numCorrect = sum(min(hint_counts[val], guess_counts[val]) for val in guess_counts)
    return pos_correct == hint.numPositionCorrect and numCorrect == hint.numCorrect

results = []
count = 0
for guess in itertools.permutations(numbers, 3):
    count += 1
    if all(validGuess(guess, hint) for hint in hints):
        results.append(guess)

# print(count, results)
print(results)
