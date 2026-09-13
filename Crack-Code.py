from NumberMatch import NumberMatch
from collections import Counter
import itertools
import random
from PIL import Image,ImageDraw,ImageFont
import os

# create from list
# guess = NumberMatch(numbers=[1, 2, 3, 2])
numbers = [x for x in range(10)]
numDigits = 5
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

# hint1 = NumberMatch("682", 1, 1)
# hint2 = NumberMatch("614", 1, 0)
# hint3 = NumberMatch("206", 2, 0)
# hint4 = NumberMatch("780", 1, 0)
# hint5 = NumberMatch("738", 0, 0)
# hint6 = NumberMatch("780", 1, 0)

# hint4 = NumberMatch("305", 2, 0)
# hint2 = NumberMatch("712", 1, 0)
# hint3 = NumberMatch("153", 2, 0)
# hint1 = NumberMatch("247", 0, 0)
# hint5 = NumberMatch("361", 2, 1)

# hint4 = NumberMatch("435", 2, 0)
# hint2 = NumberMatch("732", 1, 0)
# hint3 = NumberMatch("853", 2, 0)
# hint1 = NumberMatch("125", 0, 0)
# hint5 = NumberMatch("318", 2, 1)

# hint4 = NumberMatch("971", 2, 0)
# hint2 = NumberMatch("375", 1, 0)
# hint3 = NumberMatch("957", 2, 0)
# hint1 = NumberMatch("860", 0, 0)
# hint5 = NumberMatch("790", 2, 1)
# hint6 = NumberMatch("219", 2, 1)

# hint4 = NumberMatch("107", 2, 0)
# hint3 = NumberMatch("195", 2, 0)
# hint2 = NumberMatch("741", 1, 0)
# hint1 = NumberMatch("248", 0, 0)
# hint5 = NumberMatch("914", 2, 1)
# hint6 = NumberMatch("051", 2, 1)

# 0145
# hints = (
#         NumberMatch("89461", 3, 1),
#         NumberMatch("12873", 2, 1),
#         NumberMatch("07452", 3, 2),
#         NumberMatch("20346", 2, 1),
#         NumberMatch("34527", 2, 0)
#         )
# 01946
# hints = (
#         NumberMatch("01563", 3, 2),
#         NumberMatch("83296", 2, 1),
#         NumberMatch("12486", 3, 1),
#         NumberMatch("06783", 2, 1),
#         NumberMatch("74581", 2, 0)
#         )
# 75093
# hints = (
#         NumberMatch("", 3, 2),
#         NumberMatch("", 2, 1),
#         NumberMatch("", 3, 1),
#         NumberMatch("", 2, 1),
#         NumberMatch("", 2, 0)
#         )

# 87931
hints = (
        NumberMatch("12936", 3, 2),
        NumberMatch("47523", 2, 1),
        NumberMatch("09135", 3, 1),
        NumberMatch("85207", 2, 1),
        NumberMatch("45716", 2, 0)
        )
# 01589
# hints = (
#         NumberMatch("01973", 3, 2),
#         NumberMatch("71245", 2, 1),
#         NumberMatch("81254", 3, 1),
#         NumberMatch("25369", 2, 1),
#         NumberMatch("12406", 2, 0)
#         )
# 09173
# 59418
# 05126
# 12467
# [(6, 4, 1, 2, 7), (6, 4, 2, 1, 7)]
# 0491
# hints = (
#         NumberMatch("9546", 2, 0),
#         NumberMatch("0587", 1, 1),
#         NumberMatch("2501", 2, 1),
#         NumberMatch("8056", 1, 0),
#         NumberMatch("4859", 2, 0)
        # NumberMatch("45679", 3, 0)
# )
# 0217
# hints = (
#         NumberMatch("4016", 2, 1),
#         NumberMatch("0389", 1, 1),
#         NumberMatch("3512", 2, 1),
#         NumberMatch("8046", 1, 0),
#         NumberMatch("7059", 2, 0)
#         )
# 5149
# hints = (
#         NumberMatch("5301", 2, 1),
#         NumberMatch("7389", 1, 1),
#         NumberMatch("3169", 2, 1),
#         NumberMatch("7528", 1, 0),
#         NumberMatch("7895", 2, 0)
#         )
# 8704
# hints = (
#         NumberMatch("5401", 2, 1),
#         NumberMatch("9736", 1, 1),
#         NumberMatch("6834", 2, 1),
#         NumberMatch("0351", 1, 0),
#         NumberMatch("5481", 2, 0)
#         )
# 05173
# hints = (
#         NumberMatch("06129", 2, 2),
#         NumberMatch("14872", 2, 1),
#         NumberMatch("25983", 2, 2),
#         NumberMatch("52648", 1, 0),
#         NumberMatch("97048", 2, 0)
#         # NumberMatch("45679", 3, 0)
#         )
# hints = (
#         NumberMatch("92634", 2, 0),
#         NumberMatch("57184", 2, 1),
#         NumberMatch("07329", 2, 2),
#         NumberMatch("45398", 1, 1),
#         NumberMatch("19786", 2, 1)
        # NumberMatch("45679", 3, 0)
        # )
# 0127
# hints = (
#         NumberMatch("9182", 2, 1),
#         NumberMatch("3570", 2, 0),
#         NumberMatch("8253", 1, 0),
#         NumberMatch("3467", 1, 1),
#         NumberMatch("4329", 1, 1)
#         )
# 97385
# hints = (
#         NumberMatch("57609", 3, 1),
#         NumberMatch("24865", 2, 1),
#         NumberMatch("49381", 3, 2),
#         NumberMatch("17826", 2, 1),
#         NumberMatch("30428", 2, 0)
#         )
# hints = (
#         NumberMatch("50718", 0, 0),
#         NumberMatch("10426", 3, 2),
#         NumberMatch("94730", 3, 2),
#         NumberMatch("02419", 3, 0)
#         )

# hint4 = NumberMatch("5410", 2, 0)
# hint3 = NumberMatch("3675", 1, 0)
# hint2 = NumberMatch("4587", 2, 1)
# hint1 = NumberMatch("0592", 1, 0)
# hint5 = NumberMatch("9034", 1, 1)

# hint4 = NumberMatch("4293", 3, 0)
# hint3 = NumberMatch("6734", 3, 2)
# hint2 = NumberMatch("7916", 1, 0)
# hint1 = NumberMatch("2817", 1, 1)

# hint4 = NumberMatch("2170", 3, 1)
# hint3 = NumberMatch("94861", 0, 0)
# hint2 = NumberMatch("85096", 2, 1)
# hint1 = NumberMatch("23956", 3, 3)

# hint4 = NumberMatch("1807", 2, 0)
# hint3 = NumberMatch("7469", 2, 0)
# hint2 = NumberMatch("8247", 1, 1)
# hint1 = NumberMatch("0973", 2, 2)

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
# hints = [hint1, hint2, hint3]
# hints = [hint1, hint2, hint3, hint4]
# hints = [hint1, hint2, hint3, hint4, hint5, hint6]
# hints = [hint1, hint2, hint3, hint4, hint5]

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
    pos_correct = sum(1 for g, s in zip(guess, hint.numbers) if g == s)
    hint_counts = Counter(hint.numbers)
    guess_counts = Counter(guess)
    numCorrect = sum(min(hint_counts[val], guess_counts[val]) for val in guess_counts)
    # print(guess, pos_correct, numCorrect)
    return pos_correct == hint.numPositionCorrect and numCorrect == hint.numCorrect

    # fnd = (k, v) in counts True if v > 1 else False

def findHints(numbr, numbrs, hints):
    hnts = []
    guesses = itertools.permutations(numbrs, numDigits)
    guesses1 = itertools.permutations(numbrs, numDigits)
    guesses2 = itertools.permutations(numbrs, numDigits)
    guesses3 = itertools.permutations(numbrs, numDigits)
    guesses4 = itertools.permutations(numbrs, numDigits)
    guesses5 = itertools.permutations(numbrs, numDigits)

    guesses = itertools.permutations(numbrs, numDigits)
    # res = [guess for guess in guesses if all(validGuess(guess, hint) for hint in hints)]

    for guess in guesses:
        for guess1 in guesses1:
            hint1 = hints[0]
            hint1.numbers = guess1
            # print(hint1
            # print(guess1)
            # print(validGuess(guess1, hint1))
            if validGuess(guess, hint1):
                # print(hint1)
                for guess2 in guesses2:
                    hint2 = hints[1]
                    hint2.numbers = guess2
                    if validGuess(guess, hint2):
                        for guess3 in guesses3:
                            hint3 = hints[2]
                            hint3.numbers = guess3
                            if validGuess(guess, hint3):
                                for guess4 in guesses4:
                                    hint4 = hints[3]
                                    hint4.numbers = guess4
                                    if validGuess(guess, hint4):
                                        for guess5 in guesses5:
                                            hint5 = hints[4]
                                            hint5.numbers = guess5
                                            results = findResults(numbrs, hints)
                                            # print(results)
                                            print(hints)
                                            if (len(results) == 1 and results[0] == numbr):
                                                # print(results)
                                                print(hints)

    # for guess1 in guesses1:
    #     hint1 = hints[0]
    #     hint1.numbers = guess1
    #     # print(hint1)
    #     # print(guess1)
    #     # print(validGuess(guess1, hint1))
    #     for guess2 in guesses2:
    #         hint2 = hints[1]
    #         hint2.numbers = guess2
    #         for guess3 in guesses3:
    #             hint3 = hints[2]
    #             hint3.numbers = guess3
    #             for guess4 in guesses4:
    #                 hint4 = hints[3]
    #                 hint4.numbers = guess4
    #                 for guess5 in guesses5:
    #                     hint5 = hints[4]
    #                     hint5.numbers = guess5
    #                     # results = findResults(numbrs, hints)
    #                     # print(results)
    #                     guesses = itertools.permutations(numbrs, numDigits)
    #                     print(guess1, guess2, guess3, guess4, guess5)
    #                     res = [guess for guess in guesses if all(validGuess(guess, hint) for hint in hints)]
    #                     if len(res) > 1:
    #                         print(res)
    #                     if len(res) == 1 and res[0] == numbr:
    #                         print(hints)
    return hints

def findResults(numbrs, hints):
    count = 0
    # print(numbers)
    guesses = itertools.permutations(numbrs, numDigits)
    # print(guesses)
    res = [guess for guess in guesses if all(validGuess(guess, hint) for hint in hints)]

    # print(count, results)
    return res

def getInts(str):
    return [int(ch) for ch in str]

def buildHints(original, pick_positions, target_positions):

    n = len(original)

    result = [''] * n

    used_digits = set(original)

    available = [str(d) for d in range(10)
                 if str(d) not in used_digits]

    random.shuffle(available)

    for src, dst in zip(pick_positions, target_positions):
        result[dst] = original[src]

    idx = 0

    for i in range(n):
        if result[i] == '':
            result[i] = available[idx]
            idx += 1

    return ''.join(result)

# hn = buildHints(numb, [int(ch) for ch in "124"], [int(ch) for ch in "120"])
# hn = buildHints(numb, getInts("124"), getInts("120"))12589
# print(hn)

def check_answer(answer, clues):

    all_good = True

    for guess, expected_total, expected_well in clues:

        # Count well placed digits
        well_placed = sum(
            a == g
            for a, g in zip(answer, guess)
        )

        # Count correct digits
        total_correct = len(
            set(answer) & set(guess)
        )

        misplaced = total_correct - well_placed
        expected_misplaced = expected_total - expected_well

        print(f"\nChecking clue: {guess}")

        errors = []

        # Check total correct digits
        if total_correct != expected_total:
            errors.append(
                f"Wrong number of matching digits "
                f"(expected {expected_total}, got {total_correct})"
            )

        # Check well placed
        if well_placed != expected_well:
            errors.append(
                f"Wrong number of well-placed digits "
                f"(expected {expected_well}, got {well_placed})"
            )

        # Check misplaced
        if misplaced != expected_misplaced:
            errors.append(
                f"Wrong number of misplaced digits "
                f"(expected {expected_misplaced}, got {misplaced})"
            )

        if errors:
            all_good = False
            print("❌ FAILED")
            for err in errors:
                print("   -", err)
        else:
            print("✅ clue satisfied")

    # Final result
    if all_good:
        print("\n🎉 GOOD ANSWER — matches all clues")
    else:
        print("\n❌ Answer does not satisfy all clues")

def getClue(numberMatch: NumberMatch):
    if numberMatch.numCorrect == 3 and numberMatch.numPositionCorrect == 2:
        return "3 digits are correct, 2 well placed"
    if numberMatch.numCorrect == 3 and numberMatch.numPositionCorrect == 1:
        return "3 digits are correct, 1 well placed"
    if numberMatch.numCorrect == 3:
        return "3 digits are correct, wrongly placed"
    if numberMatch.numCorrect == 1 and numberMatch.numPositionCorrect == 1:
        return "1 digit is correct, it is well placed"
    if numberMatch.numCorrect == 1 and numberMatch.numPositionCorrect == 1:
        return "1 digit is correct, it is well placed"
    if numberMatch.numCorrect == 1:
        return "1 digit is correct it is wrongly placed"
    if numberMatch.numCorrect == 2 and numberMatch.numPositionCorrect == 2:
        return "2 digits are correct, both are well placed"
    if numberMatch.numCorrect == 2 and numberMatch.numPositionCorrect == 1:
        return "2 digits are correct, 1 well placed"
    if numberMatch.numCorrect == 2:
        return "2 digits are correct, both wrongly placed"


# clues1 = [
#     ("79083", 2, 1),  # 3 correct digits, 2 well placed
#     ("31802", 3, 1),
#     ("05941", 2, 1),
#     ("91786", 3, 2),
#     ("54296", 2, 0),  # both wrongly placed
# ]


# hints = [
#         NumberMatch(buildHints(numb, getInts("03"), getInts("04")), 2, 1),
#         NumberMatch(buildHints(numb, getInts("012"), getInts("132")), 3, 1),
#         NumberMatch(buildHints(numb, getInts("134"), getInts("124")), 3, 2),
#         NumberMatch(buildHints(numb, getInts("24"), getInts("23")), 2, 1),
#         NumberMatch(buildHints(numb, getInts("24"), getInts("03")), 2, 0)
# ]

# hints = [
#         NumberMatch(buildHints(numb, getInts("01"), getInts("03")), 2, 1),
#         NumberMatch(buildHints(numb, getInts("014"), getInts("134")), 3, 1),
#         NumberMatch(buildHints(numb, getInts("134"), getInts("124")), 3, 2),
#         NumberMatch(buildHints(numb, getInts("14"), getInts("13")), 2, 1),
#         NumberMatch(buildHints(numb, getInts("24"), getInts("03")), 2, 0)
# ]

# print(hints)
# print(check_answer("81046", clues1))

# leng = 2
results = []
colors = ["blue", "green", "orange", "purple", "pink"]
numb = "45721"
ind = random.choice([0, 1, 2, 3, 4])

def createOutput(rows):
    W, H = 2160, 3840
    im = Image.new('RGB', (W, H), (8, 9, 24))
    d = ImageDraw.Draw(im)
    F = lambda n: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', n)
    for y in range(H):
        d.line((0, y, W, y), fill=(10 + int(14 * y / H), 10 + int(8 * y / H), 28 + int(20 * y / H)))
    d.rounded_rectangle((30, 30, W - 30, H - 30), 70, outline=(75, 220, 255), width=9)
    d.text((1080, 130), 'GUESS THE CODE', font=F(140), fill=(255, 225, 75), anchor='mm')
    d.rounded_rectangle((150, 250, 2010, 620), 52, fill='black', outline=(75, 220, 255), width=8)
    d.text((1080, 355), 'The code is a 5-digit number.', font=F(60), fill='white', anchor='mm')
    d.text((1080, 452), 'All digits are different.', font=F(60), fill='white', anchor='mm')
    for i in range(5):
        x = 341 + i * 358
        d.rounded_rectangle((x, 730, x + 280, 1010), 30, fill='black', outline=(75, 220, 255), width=8)
        d.text((x + 140, 870), '?', font=F(154), fill='white', anchor='mm')
    d.text((1080, 1190), 'CLUES', font=F(104), fill=(255, 220, 40), anchor='mm')
    # rows = [
    #     ('93850', '2 digits are correct, 1 well placed', (80, 190, 255)),
    #     ('03795', '3 digits are correct, 2 well placed', (80, 255, 130)),
    #     ('62135', '3 digits are correct, 1 well placed', (255, 185, 70)),
    #     ('26097', '2 digits are correct, 1 well placed', (190, 120, 255)),
    #     ('48159', '2 digits are correct, both wrongly placed', (255, 90, 170)),
    # ]
    for i, (code, txt, c) in enumerate(rows):
        y = 1305 + i * 380
        d.rounded_rectangle((90, y - 10, 2070, y + 300), 50, fill=(4, 4, 15), outline=c, width=7)
        d.ellipse((120, y + 48, 220, y + 148), fill=c, outline='white', width=4)
        d.text((170, y + 98), str(i + 1), font=F(72), fill='white', anchor='mm')
        for j, z in enumerate(code):
            d.text((275 + j * 92, y + 120), z, font=F(114), fill=c, anchor='lm')
        d.line((965, y + 70, 965, y + 245), fill=c, width=6)
        d.rounded_rectangle((1005, y + 32, 1990, y + 280), 36, fill='black', outline=c, width=7)
        words = txt.split()
        a = 0
        s = 0
        for k, z in enumerate(words):
            if a + len(z) + (1 if a else 0) > len(txt) // 2:
                s = k
                break
            a += len(z) + (1 if a else 0)
        d.text((1035, y + 88), ' '.join(words[:s]), font=F(54), fill=c)
        d.text((1035, y + 162), ' '.join(words[s:]), font=F(54), fill=c)
    d.rounded_rectangle((165, 3365, 1995, 3605), 44, fill='black', outline=(75, 220, 255), width=7)
    d.text((1080, 3435), 'CAN YOU CRACK THE CODE?', font=F(64), fill=(255, 220, 40), anchor='mm')
    d.text((1080, 3520), 'Find the exact 5-digit code!', font=F(58), fill='white', anchor='mm')
    os.makedirs('output', exist_ok=True)
    path = 'output/neon_code128.png'
    im.save(path, quality=95)
    print(path)

while True:
    hints1 = [
            NumberMatch(buildHints(numb, getInts("03"), getInts("04")), 2, 1),
            NumberMatch(buildHints(numb, getInts("012"), getInts("132")), 3, 1),
            NumberMatch(buildHints(numb, getInts("134"), getInts("124")), 3, 2),
            NumberMatch(buildHints(numb, getInts("24"), getInts("23")), 2, 1),
            NumberMatch(buildHints(numb, getInts("24"), getInts("03")), 2, 0)
    ]

    hints2 = [
            NumberMatch(buildHints(numb, getInts("4"), getInts("4")), 1, 1),
            NumberMatch(buildHints(numb, getInts("023"), getInts("134")), 3, 0),
            NumberMatch(buildHints(numb, getInts("02"), getInts("02")), 2, 2),
            NumberMatch(buildHints(numb, getInts("03"), getInts("13")), 2, 1),
            NumberMatch(buildHints(numb, getInts("14"), getInts("02")), 2, 0)
    ]

    hints3 = [
            NumberMatch(buildHints(numb, getInts("2"), getInts("2")), 1, 1),
            NumberMatch(buildHints(numb, getInts("023"), getInts("134")), 3, 0),
            NumberMatch(buildHints(numb, getInts("01"), getInts("01")), 2, 2),
            NumberMatch(buildHints(numb, getInts("03"), getInts("13")), 2, 1),
            NumberMatch(buildHints(numb, getInts("14"), getInts("02")), 2, 0)
    ]

    hints4 = [
            NumberMatch(buildHints(numb, getInts("3"), getInts("3")), 1, 1),
            NumberMatch(buildHints(numb, getInts("013"), getInts("124")), 3, 0),
            NumberMatch(buildHints(numb, getInts("01"), getInts("01")), 2, 2),
            NumberMatch(buildHints(numb, getInts("02"), getInts("12")), 2, 1),
            NumberMatch(buildHints(numb, getInts("14"), getInts("02")), 2, 0)
    ]

    hints5 = [
            NumberMatch(buildHints(numb, getInts("03"), getInts("04")), 2, 1),
            NumberMatch(buildHints(numb, getInts("014"), getInts("134")), 3, 1),
            NumberMatch(buildHints(numb, getInts("134"), getInts("124")), 3, 2),
            NumberMatch(buildHints(numb, getInts("14"), getInts("13")), 2, 1),
            NumberMatch(buildHints(numb, getInts("24"), getInts("03")), 2, 0)
    ]

    hintsList = [hints1, hints2, hints3, hints4, hints5]

    # hints = random.choice(hintsList)
    hints = hintsList[ind]

    # hints = hints4

    # hints = [
    #     NumberMatch(buildHints(numb, getInts("13"), getInts("14")), 2, 1),
    #     NumberMatch(buildHints(numb, getInts("012"), getInts("132")), 3, 1),
    #     NumberMatch(buildHints(numb, getInts("012"), getInts("312")), 3, 2),
    #     NumberMatch(buildHints(numb, getInts("03"), getInts("13")), 2, 1),
    #     NumberMatch(buildHints(numb, getInts("14"), getInts("02")), 2, 0)
    # ]
    colors = [(80, 190, 255),(80, 255, 130),(255, 185, 70),(190, 120, 255),(255, 90, 170)]
    rows = []
    random.shuffle(hints)
    random.shuffle(colors)
    clue_texts = [getClue(h) for h in hints]
    results = findResults(numbers, hints)
    # leng =
    # print(results)
    if len(results) == 1:
        with open("output/output.txt", "a") as file:
                    # print("Create a " + str(numDigits) + " digit puzzle image like above with the following clues, keep the text within the boxes and same color as the numbers for each row:")
            for i, h in enumerate(hints):
                print(h.number + " \"" + getClue(h) + "\"")
                file.write(h.number + " " + getClue(h) + "\n")
                rows.append((h.number, getClue(h), colors[i]))
            file.write(str(results[0]) + "\n")
            file.write("\n\n\n\n")
            createOutput(rows)
        break
print(str(results[0]))

# findHints("75093", numbers, hints)
