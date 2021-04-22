import numpy as np

def problemSolver(lockerNumber, kidsNumber):
    lockerOpen = '|'
    lockerClosed = 'x'
    lockers = []
    counter = 0

    for i in range(lockerNumber):
        lockers.append(lockerOpen)

    for j in range(kidsNumber):
        for v in lockers:
            # print(lockers.index(v))
            # print(j)
            if lockers.index(v)+1 % j+1 == 0:
                print('replace')

                
    print(lockers)
    print(counter)

problemSolver(10, 10)
