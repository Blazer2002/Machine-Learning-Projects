#4
L = ''
for i in 'supercalifragilisticexpialidocious':
  L += chr(ord(i) + 4)
print(L)
print('-----------------')
#5
sum = 0
for i in range(99, 1001):
  if i % 47 == 0 and i % 15 != 0:
    sum += i
print(sum)
print('-----------------')
#6
x = 113
g = 113
count = 1
epsilon = 1
while abs(g ** 2 - x) > epsilon:
  ave = (g + (x / g)) / 2
  g = ave
  count += 1
print(count)
print('-----------------')
#7
def sumOrds(string):
  sum = 0
  for i in string:
    sum += ord(i)
  print(sum)

sumOrds('abcdefghijklmnopqrstuvwxyz')
print('-----------------')
#8
x = 800
low = 0
high = x
y = (low + high) / 2
epsilon = 0.01
count = 1
while abs(y ** 2 - x) > epsilon:
  if y ** 2 > x:
    high = y
  elif y ** 2 < x:
    low = y
  y = (low + high) / 2
  count += 1
print(count)
print('-----------------')
#9
def single(string):
  last = ''
  s = ''
  for i in string:
    if i != last:
      s += i
    last = i
  print(s)
  return(s)

single('eeeeezippppppppzzddddaaaannnnnywwwwiiskauuuuuaaaavvnqqyyyyppppphhhhhyyyyjnnnnnufffdddxxxxxnnnnnvvjjjssssqqqqsppxxxxnnlllllwwwccccvvvvvddqqqqllllxpjjjjjsssssmmfffffhyyrrrrrhhhhqqqsssooovvvvvtmmmmmzzqqqqqggggbbbblllllrrqqqqpppnnnaaaaarrrrrzzzzzkkkktzzuurrrrrfzzzzzzzzbcoyyyhhhdddddfffjffiiiiifffuuuoooppppdjjjjkkkk')
print('-----------------')
#10
def happy(num):
  # base case
  if(num == 1):
    return True
  if(num == 4):
    return False
  # general case
  sum = 0
  for i in str(num):
    sum += int(i) ** 2
  return happy(sum)

count = 0
for i in range(10000, 12000):
  if happy(i):
    count += 1
print(count)
print('-----------------')
#11
def first(string):
  for i in range(len(string)):
    i += 1
    first = string[0:i]
    second = string[i:i+len(first)]
    third = string[i+len(first):i+2*len(first)]
    if int(second) - int(first) == 1:
      if int(third) - int(second) == 1:
        print(first)
        return

first('142354142355142356142357142358142359142360142361142362142363142364142365')