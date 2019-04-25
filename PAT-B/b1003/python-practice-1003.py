

def judge(input_str):
    lst = list(input_str)

    for i, char in enumerate(lst):
        if (char != 'P' and char != 'A' and char != 'T'):
            return False
        else:
            if (char == 'P' and lst[i+1] == 'A' and lst[i+2] == 'T'):
                if ( (len(lst)-i-3) != i):
                    return False
                else:
                    count = i
                    while count:
                        if (lst[count] != lst[i+3 + count] or lst[count]!= 'A'):
                            return False
                        count = count - 1
                        pass
                    return True
                    # temp_lst = lst[:i] + lst[(i+3):]


def main():
    result = judge('AAAAPATAAAA')
    print(result)

if __name__ == '__main__':
    main()