# Changing Bases

# Write a program that takes a number of any base from
# 1 to 16, that the user inputs, and output the number
# in a new base specified by the user

# converts numbers of a different base to decimal
# num is a string to consider if base > 10
def toDecimal(num: str, base: int):
    sum = 0  # the return value
    for i in range(len(num)):
        # variable to store the digit value
        element = num[i]
        # converts letters to numbers in decimal
        element = number(element)
        # the current digit is the length minus the current
        # loop number
        digit = len(num) - i
        # the math
        sum += base ** (digit - 1) * int(element)
    return sum

# converts letters to numbers (up to base 16)
def number(letter: str):
    # change the letter to uppercase
    letter = letter.upper()
    # starting from A being 10 to F being 15
    if letter == 'A':
        return 10
    elif letter == 'B':
        return 11
    elif letter == 'C':
        return 12
    elif letter == 'D':
        return 13
    elif letter == 'E':
        return 14
    elif letter == 'F':
        return 15
    else:
        return letter  # else do nothing

# converts decimal numbers to a different base
def toBase(base: int, dec: int):
    # base case
    # if the decimal number can no longer be divided by
    # the base number, then return the remainder
    if dec < base:
        return letter(dec % base)

    # general case
    return str(toBase(base, dec / base)) + letter(dec % base)

# converts numbers past 9 to letters (max 15)
def letter(num: int):
    # starting from 10 being A to 15 being F
    if num == 10:
        return 'A'
    elif num == 11:
        return 'B'
    elif num == 12:
        return 'C'
    elif num == 13:
        return 'D'
    elif num == 14:
        return 'E'
    elif num == 15:
        return 'F'
    else:
        # else do nothing (return num as a string)
        return str(int(num))

def changeBase(num: str, prevBase: int, newBase: int):
    # first convert the number into a decimal
    dec = toDecimal(num, prevBase)
    # then convert the decimal into the new base number
    newNum = toBase(newBase, dec)
    return newNum  # return the new number

# Ask the user for 3 inputs - number, base, new base
num = input('Give me a number from any base (maximum base 16): ')
prevBase = int(input('Give me the base of the number: '))
newBase = int(input('Give me the new base for the number: '))
# convert the number to the new base and print
newNum = changeBase(num, prevBase, newBase)
print(num + ', from base', str(prevBase) + ', to base', str(newBase) + ', is', newNum)