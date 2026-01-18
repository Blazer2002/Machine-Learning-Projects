#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
# Grades in Letters.
# --------------------------------------------------------------
def letterGrade(score):
    '''
    Assume that score is a floating point number from 0.0 to 100.0, inclusive.
    Convert a numerical grade to a letter grade, 'A', 'B', 'C', 'D' or 'F',
    where the cutoffs for 'A', 'B', 'C', 'D' are 90, 80, 70, and 60
    respectively. So 'F' will be below 60.
    Returns the letter grade corresponding to the score.

    For example, 90 to 100 inclusive is 'A',
    'B' is less than 90, but at least 80,
    and so on.
    '''
    try:
        letters = 'ABCDF'
        for i in range(len(letters)):
            if score >= (9.0 - i) * 10.0:
                return letters[i]
    except ValueError:
        print('must pass type float/int into parameter')
# --------------------------------------------------------------
# Jump to 1
# --------------------------------------------------------------
def jumpTo1(level):
    """
    Assumes that level is a positive integer.
    Returns the number of steps required to change level to 1, where
    a step is either
    (i) if level is even, change level to half of level
    (ii) if level is odd, change level to 3 * level + 1
    You can assume that these steps always lead to level 1.

    For example:
    jumpTo1(3) returns 7 since
       (1) 3*3+1 = 10,
       (2) 10//2 = 5,
       (3) 3 * 5 + 1 = 16,
       (4) 16/2 = 8,
       (5) 8/2 = 4,
       (6) 4/2 = 2,
       (7) 2/2 = 1
    """
    try:
     steps = 0
     l = level
     while l != 1:
      if l % 2 == 0:
       l /= 2
      else:
       l = 3 * l + 1
      steps += 1
     return steps
    except ValueError:
     print('must pass type int into parameter')
# --------------------------------------------------------------
# Keyword Cipher
# --------------------------------------------------------------
def encode(text, shuffled_alphabet):
    '''
    Assumes text and shuffled_alphabet are strings, and shuffled_alphabet
    is a shuffled version of the 26-letter English alphabet.
    Returns a string with the same length of text, by replacing
    each letter in text by the i'th letter of shuffled_alphabet, where
    i is the position of that letter in the English alphabet.
    Letters in text which are not in the English alphabet are not changed
    when coping to the encoded word.
    Assume that the English alphabet and the shuffled_alphabet are lower
    case, but the same two alphabets are used to encode uppercase letters
    in the obvious way.

    For example, if shuffled_alphabet is 'htraebcdfgijklmnopqsuvwxyz',
    and text is 'dog', then imagine lining up the two alphabets:

    'htraebcdfgijklmnopqsuvwxyz'
    'abcdefghijklmnopqrstuvwxyz'

    and choosing the letters directly above 'd', 'o' and 'g' in the
    English alphabet to find the corresponding letters in the shuffled
    alphabet, to produce the encode word to return, which is 'amc'.
    Similarly, 'Dog', is encoded to 'Amc'.  Thus,

    encode('Dog', 'htraebcdfgijklmnopqsuvwxyz') returns 'Amc'
    encode('deed', 'htraebcdfgijklmnopqsuvwxyz') returns 'aeea'
    encode('Blue7', 'htraebcdfgijklmnopqsuvwxyz') returns 'Tjue7'

    Hint: the find() function of str will be helpful.
    '''
    if len(shuffled_alphabet) != 26:
        raise ValueError
    try:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        shuffled = shuffled_alphabet.lower()
        encoded = ''
        for i in text:
            if i.isalpha():
                upper = i.isupper()
                index = alpha.find(i.lower())
                if upper:
                    encoded += shuffled[index].upper()
                else:
                    encoded += shuffled[index].lower()
            else:
                encoded += i
        return encoded
    except ValueError:
        print('must pass string, string into parameters')
# --------------------------------------------------------------
# Find the item with the greatest weight
# --------------------------------------------------------------
def greatestWeight(L):
    '''
    Assumes L is a nonempty list of pairs (item, weight).
    An item may occur in more than one tuple, in which case
    its total weight is the sum of the weights in its tuples.
    Return the item with the greatest cumulative weight.
    (In the case of a tie, return any item of greatest cumulative weight).

    CONSTRAINT: YOU MUST USE A DICTIONARY.

    For example,
    greatestWeight([('item1', 3)]) returns 'item1'
    greatestWeight([('item1', 3),('item2', 2)]) returns 'item1'
    greatestWeight([('item2', 2),('item1', 3),('item2', 2)]) returns 'item2'
    '''
    if len(L) < 1:
        raise ValueError
    weights = {}
    for pair in L:
        try:
            if pair[0] not in weights:
                weights[pair[0]] = pair[1]
            else:
                weights[pair[0]] += pair[1]
        except IndexError:
            print('All items in the list must be tuples of 2 elements')

    item = None
    greatest = 0
    for i in weights.keys():
        try:
            if weights[i] > greatest:
                greatest = weights[i]
                item = i
        except ValueError:
            print('All tuples in the list must be of (item, weight) pairs')

    return item
# --------------------------------------------------------------
# Find the sum of all of the numbers
# --------------------------------------------------------------
def recursiveSum(l) :
    '''
    Assumes l is a number or a list of numbers and lists (of numbers and lists of ...).
    Returns the sum of all the numbers

    You must use RECURSION to solve the problem.

    For example,
    recursiveSum(5) is 5
    recursiveSum([1,[[[[2]]]]]) is 3

	Note that type([1])==list
    '''
    # base case
    if type(l) == int:
        return l

    # general case
    sum = 0
    for i in l:
        sum += recursiveSum(i)

    return sum
# --------------------------------------------------------------
# 2D array
# --------------------------------------------------------------
def bigColumnAverage(matrix) :
    '''
    Assume that matrix is a two-dimensional rectangular matrix of integers.
    Return the index of the column which has the largest average.
    Recall that the average of n numbers is their sum divided by n.
    If there is a tie, report the lower index.
    For example, in the following matrix, the averages of the columns
    are 4.5, 5.5, and 8.5, respectively, so
    column 2 has the largest average and the function would return 2.
    sum:
    [[6, 1, 2],\
     [1, 1, 20],\
     [3, 10, 3],\
     [8, 10, 9]]
    '''
    greatest = -100000
    column = 0
    ave = 0
    for j in range(len(matrix[0])):
     for i in range(len(matrix)):
      ave += matrix[i][j]
     ave /= len(matrix)
     if ave > greatest:
      greatest = ave
      column = j
     ave = 0
    return column
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test16(self):
        self.assertEqual(bigColumnAverage([[6, 1, 2], [1, 1, 20], [3, 10, 3], [8, 10, 9]]), 2)
    def test26(self):
        self.assertEqual(bigColumnAverage([[-5, -1, -2], [-1, -1, -20], [-3, -10, -3], [-8, -10, -9]]), 0)
    def test36(self):
        self.assertEqual(bigColumnAverage([[-5, -1, -2]]), 1)
    def test46(self):
        self.assertEqual(bigColumnAverage([[3, 9, 1, 1, 2], [2, 1, 1, 9, 3]]), 1)
    def test56(self):
        self.assertEqual(bigColumnAverage([[-5], [-1], [-3], [-8]]), 0)

    def test15(self):
        self.assertEqual(recursiveSum([1,2,3]),6)
    def test25(self):
        self.assertEqual(recursiveSum([[1,[2],[[]]],3,[4]]),10)
    def test35(self):
        self.assertEqual(recursiveSum(5),5)
    def test45(self):
        self.assertEqual(recursiveSum([[[[]]]]),0)
    def test55(self):
        self.assertEqual(recursiveSum([1,[[[[2]]]]]),3)

    def test14(self):
        self.assertEqual(greatestWeight([('item1', 3)]), 'item1')
    def test24(self):
        self.assertEqual(greatestWeight([('item1', 3), ('item2', 2)]), 'item1')
    def test34(self):
        self.assertEqual(greatestWeight([('item2', 2), ('item1', 3), ('item2', 2)]),'item2')
    def test44(self):
        self.assertEqual(greatestWeight([('item2', 2), ('item1', 3), ('item2', 1), ('item2', 1)]),'item2')

    def test13(self):
        self.assertEqual(encode('deed', 'htraebcdfgijklmnopqsuvwxyz'), 'aeea')
    def test23(self):
        self.assertEqual(encode('dog', 'htraebcdfgijklmnopqsuvwxyz'), 'amc')
    def test33(self):
        self.assertEqual(encode('Dog', 'htraebcdfgijklmnopqsuvwxyz'), 'Amc')
    def test43(self):
        self.assertEqual(encode('7dogs oh', 'htraebcdfgijklmnopqsuvwxyz'), '7amcq md')
    def test53(self):
        self.assertEqual(encode('goodolddays', 'gnimolbacdefhjkpqrstuvwxyz'), 'bkkmkfmmgys')
    def test63(self):
        self.assertEqual(encode('hello world', 'neicsabdfghjklmopqrtuvwxyz'), 'dsjjm wmqjc')
    def test73(self):
        self.assertEqual(encode('blue', 'abcdefghijklmnopqrstuvwxyz'), 'blue')

    def test12(self):
      self.assertEqual(jumpTo1(3), 7)
    def test22(self):
        self.assertEqual(jumpTo1(5), 5)
    def test32(self):
        self.assertEqual(jumpTo1(10), 6)
    def test42(self):
        self.assertEqual(jumpTo1(99), 25)
    def test52(self):
        self.assertEqual(jumpTo1(44), 16)
    def test62(self):
        self.assertEqual(jumpTo1(1001), 142)

    def test11(self):
        self.assertEqual(letterGrade(77), 'C')
    def test21(self):
        self.assertEqual(letterGrade(90), 'A')
    def test31(self):
        self.assertEqual(letterGrade(100), 'A')
    def test41(self):
        self.assertEqual(letterGrade(59), 'F')
    def test51(self):
        self.assertEqual(letterGrade(60), 'D')
    def test61(self):
        self.assertEqual(letterGrade(70), 'C')


if __name__ == '__main__':
    unittest.main(exit=True)

# --------------------------------------------------------------
# The End
# --------------------------------------------------------------

