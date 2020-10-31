#ran_list=[82.4, 89.5, 18.8, 30.4, 47.8, 16.3, 9.2, 74.4, 33.3, 74.0, 93.0, 44.3, 75.0, 5.1, 82.5, 13.9, 83.1, 49.0, 94.8, 68.0, 48.1, 12.8, 5.6, 80.1, 56.8]
import random
import statistics

def problem4_2(ran_list):
    numList = []
    random.seed(150)
    for i in range(0,25):
        numList.append(round(100*random.random(),1))
    #print(numList)
    x=statistics.mean(ran_list)
    y=statistics.stdev(ran_list)
    print(x)
    print(y)

            
