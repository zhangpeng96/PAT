def main():
    number = input()
    count = 0
    while number != 1:
        if number % 2:
            number = (3 * number + 1) / 2
        else:
            number = number / 2            
        count = count + 1
        pass
    print(count)

if __name__ == '__main__':
    main()
