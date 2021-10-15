import random

input = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F',
              'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L',
              'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R',
              's', 'S', 't', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x',
              'X', 'y', 'Y', 'z', 'Z', '1', '2', '3' , '4', '5', '6', '7',
              '8', '9']

count = 27
account = ''

while True:
    account = account + random.choice(input)
    count = count - 1
    if count == 0:
        break

print(account)
