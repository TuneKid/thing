import numpy as np

def problemSolver(lockerNumber, kidsNumber):
    lockerOpen = '|'
    lockerClosed = 'x'
    lockers = []
    counter = 0

    for i in range(lockerNumber):
        lockers.append(lockerOpen)

    for j in range(kidsNumber):
        lockersNew =  np.arange(1, 10, int(j+1))
        print(lockersNew)
       

                
    print(lockers)
    print(counter)

problemSolver(10, 10)
