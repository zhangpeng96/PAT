def main():
    input_list = ['3', 'Joe Math990112 89', 'Mike CS991301 100', 'Mary EE990830 95']

    input_list = []
    for line in sys.stdin:
        tempStr = line.split()
        input_list.extend(tempStr)

    count = int(input_list[0])
    grade_dict = {}
    while (count):
        data = input_list[count].split(' ')
        grade_dict[int(data[2])]  = data[0]+' '+data[1]
        count = count - 1

    # dict = sorted(grade_dict.items(), key=lambda d:d[0]) 
    key = grade_dict.keys()
    print(grade_dict[max(key)])
    print(grade_dict[min(key)])

if __name__ == '__main__':
    main()