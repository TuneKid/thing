import numpy as np

def problemSolver(lockerNumber, kidsNumber):
    lockerOpen = '|'
    lockerClosed = 'x'
    lockers = []
    openCounter = 0
    

    for i in range(lockerNumber):
        lockers.append(lockerClosed)

    for j in range(kidsNumber):
        indexCounter = 0
        for v in lockers:
            # print(lockers.index(v))
            mod = (indexCounter+1) % (j+1)
            
            if mod == 0:
                if v == lockerOpen:
                    lockers[indexCounter] = lockerClosed
                    openCounter -= 1
                if v == lockerClosed:
                    lockers[indexCounter] = lockerOpen
                    openCounter += 1
            print(v, indexCounter)
            

            indexCounter += 1

                
    print(lockers)
    print(openCounter)

problemSolver(100, 100)   
