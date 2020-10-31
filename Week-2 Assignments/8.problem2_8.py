Hello = [0.5,1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10.0]

def problem2_8(TLList):
    sum = 0
    for i in range(0,len(TLList)):
        sum = sum + TLList[i]
        #print(TLList[i])
    AVG = sum/len(TLList)
    print("Average:",AVG)
    print("High:",max(TLList))
    print("Low:",min(TLList))
