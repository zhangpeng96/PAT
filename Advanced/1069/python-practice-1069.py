# A1069 The Black Hole of Numbers
# For any 4-digit integer except the ones with all the digits being the same, 
# if we sort the digits in non-increasing order first, and then in non-decreasing 
# order, a new number can be obtained by taking the second number from the first 
# one. Repeat in this manner we will soon end up at the number 6174 -- the black 
# hole of 4-digit numbers. This number is named Kaprekar Constant.
# 
# Given any 4-digit number, you are supposed to illustrate the way it gets into 
# the black hole.

def sortNumber(digits, direction):
    result = 0
    digiList = list(map(int, str(digits)))
    # Python 3.x, the map function return a map object NOT LIST
    if direction == 1:
        digiList.sort()
    elif direction == -1:
        digiList.sort()
        digiList.reverse()

    for dig in digiList:
        result = result * 10 + dig

    return result

def main():
    difference = 0
    inputDigit = input()

    while (difference != 6174):
        subtract1 = sortNumber(inputDigit, -1)
        subtract2 = sortNumber(inputDigit, 1)
        difference = subtract1 - subtract2
        inputDigit = difference
        print(str(subtract1)+' - '+str(subtract2)+' = '+str(difference))

if __name__ == '__main__':
    main()