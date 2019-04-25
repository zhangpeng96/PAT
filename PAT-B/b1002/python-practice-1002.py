def parseNumber(input):
    number_dict = {
        0: 'ling',
        1: 'yi',
        2: 'er',
        3: 'san',
        4: 'si',
        5: 'wu',
        6: 'liu',
        7: 'qi',
        8: 'ba',
        9: 'jiu'
    }
    return number_dict[input]


def main():
    # inputNumber = input()
    inputNumber = 1234567890987654321123456789
    inputList = list(str(inputNumber))
    calcNumber = 0
    for number in inputList:
        calcNumber = calcNumber + int(number)

    calcList = list(str(calcNumber))

    output = ''
    for i, number in enumerate(calcList):
        parse = parseNumber(int(number))
        output = output + parse
        if (i < (len(calcList) - 1)):
            output = output + ' '

    print(output)

if __name__ == '__main__':
    main()