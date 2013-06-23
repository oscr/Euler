#!/usr/bin/env python


toEnglishZeroToNinteen = {
    0:    '',
    1:    'one',
    2:    'two',
    3:    'three',
    4:    'four',
    5:    'five',
    6:    'six',
    7:    'seven',
    8:    'eight',
    9:    'nine',
    10:   'ten',
    11:   'eleven',
    12:   'twelve',
    13:   'thirteen',
    14:   'fourteen',
    15:   'fifteen',
    16:   'sixteen',
    17:   'seventeen',
    18:   'eighteen',
    19:   'nineteen'
}

toEnglishTwentyToNinety = {
    2:   'twenty',
    3:   'thirty',
    4:   'forty',
    5:   'fifty',
    6:   'sixty',
    7:   'seventy',
    8:   'eighty',
    9:   'ninety'

}


def toEnglish(n):
    word = ""
    if n >= 1000:
        word += toEnglishZeroToNinteen[n // 1000] + 'thousand'
        n %= 1000

    if n >= 100:
        word += toEnglishZeroToNinteen[n // 100] + 'hundred'
        n %= 100

    # Do we need to add and?
    if word is not "" and n != 0:
        word += "and"

    # Since 11-19 are special cases
    if n < 20:
        return word + toEnglishZeroToNinteen[n]
    else:
        word += toEnglishTwentyToNinety[n // 10]
        n %= 10
        return word + toEnglishZeroToNinteen[n]

print(sum([len(toEnglish(i)) for i in range(1, 1001)]))
