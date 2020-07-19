# The highest building in our city has only one elevator. A request list is 
# made up with N positive numbers. The numbers denote at which floors the 
# elevator will stop, in specified order. It costs 6 seconds to move the 
# elevator up one floor, and 4 seconds to move down one floor. The elevator
# will stay for 5 seconds at each stop. 
# For a given request list, you are to compute the total time spent to fulfill 
# the requests on the list. The elevator is on the 0th floor at the beginning 
# and does not have to return to the ground floor when the requests are fulfilled.


def main():
    input_data = '3 2 3 1'
    # input_data = input()

    timer = 0
    desti = input_data.split(' ')

    destiLen = int(desti[0])
    desti[0] = '0'
    
    for i in range(1, destiLen+1):
        print('r', desti[i], desti[i-1])
        subtract = int(desti[i]) - int(desti[i-1])
        if (subtract > 0):
            timer = timer + subtract*6
            print(subtract, timer)
        elif (subtract < 0):
            timer = timer + abs(subtract)*4
            print(subtract, timer)
        
        timer = timer + 5

    print(timer)

if __name__ == '__main__':
    main()
