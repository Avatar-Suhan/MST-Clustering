from stockData import *

def createMinimumDistances(eList):
    tList = []
    for v in range(len(eList)):
        tempList = []
        for x in range(len(eList)):
            tempList.append(((eList[v][0]-eList[x][0])**2+(eList[v][1]-eList[x][1])**2)**0.5)
        tList.append(tempList)


    return tList

if __name__ == "__main__":

    eList = importCSVChange("testingFile.txt")



    for i in createMinimumDistances(eList):
        print(f"{i}\n")

    print("\n\n:3c")

    #eList is the list you probably created 


    #clustering standard dataset