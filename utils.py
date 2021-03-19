def orderBigSmall(myList, myKey = False):
    if not myKey:
        # 1
        for i in range(len(myList)):

            inDes = i
            # 2
            for j in range(i+1, len(myList)):
                if myList[inDes] < myList[j]:
                    inDes = j
            
            myList[i], myList[inDes] = myList[inDes], myList[i]
        # 3
        return myList
    else:
        # 1
        for i in range(len(myList)):

            inDes = i
            # 2
            for j in range(i+1, len(myList)):
                if myList[inDes][myKey] < myList[j][myKey]:
                    inDes = j
            
            myList[i], myList[inDes] = myList[inDes], myList[i]
        # 3
        return myList


def orderSmallBig(myList, myKey = False):

    if not myKey:
        # 1
        for i in range(len(myList)):

            inDes = i
            # 2
            for j in range(i+1, len(myList)):
                if myList[inDes] > myList[j]:
                    inDes = j
            
            myList[i], myList[inDes] = myList[inDes], myList[i]
        # 3
        return myList
    else:
        # 1
        for i in range(len(myList)):

            inDes = i
            # 2
            for j in range(i+1, len(myList)):
                if myList[inDes][myKey] > myList[j][myKey]:
                    inDes = j
            
            myList[i], myList[inDes] = myList[inDes], myList[i]
        # 3
        return myList


def desTipica(myList):
    media = 0
    N = len(myList)
    for element in myList:
        media += element
    media = media / N

    sumatorio = 0
    for element in myList:
        sumatorio += (element - media) ** 2

    desviacion = (sumatorio / N) ** (1/2)

    return desviacion