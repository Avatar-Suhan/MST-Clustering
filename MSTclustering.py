from leastDistances import *
from primsAlgorithm import *
import matplotlib.pyplot as plt
import copy
from silhouette import *

def sumiarithm():
    """
    Created at 11:47 pm lol
    Basically, start at first row
        A   B   C   D
    A   0   0   20  0
    B   0   0   0   5
    C   20  0   0   0
    D   0   5   0   0
    
    now, when you find the first-non-zero entry, delete it.
    Delete the related intry in row 3 and now go to row 3.
    Note down the point, in this case C. Repeat till A is zero.
    Now do the same with C and any other points
    DO until you terminate. Now for the next cluster, go to the next non-empty list

    repeat till table is all empty
    """

def isEmpty(toCheck):
    for i in toCheck:
        if i != 0:
            return False
    return True

def isTrulyEmpty(toCheck):
    if toCheck == []:
        return True
    return False

def alreadyInside(toCheckList,item):
    for i in toCheckList:
        if item == i:
            return True
    return False

def MinDistancesToClusters(mstTable, points):
    """
    Input : 
    
    mstTable is distances table representing minimum spanning tree
    points refers to data values as cooridnates

    output is a list of clusters in the form [[[x,y],...],[[x,y],...],...]
    """
    copyMST = mstTable
    backUp = copy.deepcopy(mstTable)
    """print("xxxxxxxxxxxxxxxxxxxxxxxxxxx")
    for i in mstTable:
        print(i)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxx")"""

    flag = True
    startingLine = 0
    allClusters,cluster = [],[points[0]]
    stack = [0]
  
    for i in range(0,len(copyMST)):
        if isEmpty(copyMST[i]):
            allClusters.append([points[i]])
    
    while flag:

        if isTrulyEmpty(stack):
            startingLine += 1
            if not isTrulyEmpty(cluster) and len(cluster) != 1:
                allClusters.append(cluster)
            cluster = []
            if startingLine >= len(mstTable):
                flag = False
                print(":3c")
            stack.append(startingLine)
  


        while not isTrulyEmpty(stack):
            try:
                if not alreadyInside(cluster, points[startingLine]):
                    cluster.append(points[startingLine])
            except:
                pass
            try:
                for i in range(0,len(copyMST[stack[0]])):
                    if copyMST[stack[0]][i] != 0:
                        if not alreadyInside(cluster,points[i]):
                                cluster.append(points[i])
                        copyMST[stack[0]][i],copyMST[i][stack[0]] = 0,0
                        stack.append(i)
                        """if not alreadyInside(cluster, points[i]):
                            cluster.append(points[i])"""
                stack.pop(0)
            except:
                stack = []
        
    """print("<<<<<<<<<<<<m>>>>>>>>>>>>>>>")
    for i in backUp:
        print(i)
    print(mstTable)
    print("<<<<<<<<<<<<m>>>>>>>>>>>>>>>")"""
    return allClusters

def clusterData(mst , clusters, points):
    """
    Input MST is a 2D list of the form:
    [[row 1],[row 2], ... ,[row n]]

    output is of the form [[cluster 1], ...] where [cluster1] = [[x,y],...]

    where the rows belong to the matrix containing
    the distances between the points on the tree,
    with 0 representing no link

    clusters represents how many clusters the user would like from the data
    points represents the list containing all the points that need to be clustered

    output is of the form [[cluster 1], ...] where [cluster1] = [[x,y],...]

    """
    
    if clusters == 1:
        return [points]
    
    clusters -= 1

    for counter in range(0,clusters):
        max,maxValue = [],0
        for i in range(0,len(mst)):
            for k in range(0,len(mst[i])):
                if mst[i][k] > maxValue:
                    max = [i,k]
                    maxValue = mst[i][k]
        mst[max[0]][max[1]] = 0
        mst[max[1]][max[0]] = 0

    return MinDistancesToClusters(mst,points)

def limitClustering(mst, clustersAmount, points):
    """
    Inputs :
    mst is the minimum spanning tree connecting all the data points
    clustersAmount is the amount of clusters needed
    points is a list of all the data points
    Output :
    List of clusters : [[[x,y],...],[[x,y],...]]
    """
    temp, minimumPoints = copy.deepcopy(mst), round(len(points)/(5*clustersAmount))
    if clustersAmount == 1:
        return [points]
    

    clusters = []

    counter = 0

    while counter < clustersAmount-1:
        counter += 1

        clusters = []
        max,maxValue = [],0
        for i in range(0,len(mst)):
            for k in range(0,len(mst[i])):
                if mst[i][k] > maxValue:
                    max = [i,k]
                    maxValue = mst[i][k]
        #print(F"Max Coordinates : {max}")
        mst[max[0]][max[1]] = 0
        mst[max[1]][max[0]] = 0
        #print(f"MST deleted : {max}")

        """print("--------------------------------")
        for i in mst:
            print(i)
        print("--------------------------------")
        """
        copyMst = copy.deepcopy(mst)
        clusters = MinDistancesToClusters(copyMst, points)

        """print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
        for i in mst:
            print(i)
        print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")"""

        resetTree = False

        # for loop checks if any cluster is too small
        for i in clusters:
            #print(f"i has length {len(i)}")
            if len(i) < minimumPoints:
                resetTree = True
                #print(F"Not deleting : {i}")
                """print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                for i in mst:
                    print(i)
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")"""
        
        if resetTree:
            mst[max[0]][max[1]] = 0.001
            mst[max[1]][max[0]] = 0.001
            print(f"Reset : {max}\nCounter: {counter}")
            counter -= 1

        else:
            # the two lines below delete the relevant side
            temp[max[0]][max[1]] = 0
            temp[max[1]][max[0]] = 0
            print(f"Deleted a point, counter : {counter}")
            #print(f"Chose to delete : {max}\nresetTree = {resetTree}")
            #counter += 1
        
    #print(f"Counter : {counter}")
    """for i in temp:
        print(i)"""
    return MinDistancesToClusters(temp,points)

def silhouetteClustering(mst, clustersAmount, points):
    """
    Inputs :
    mst is the minimum spanning tree connecting all the data points
    clustersAmount is the amount of clusters needed
    points is a list of all the data points
    Output :
    List of clusters : [[[x,y],...],[[x,y],...]]
    """
    temp = copy.deepcopy(mst)
    minimumPoints = round(len(points)/(100*clustersAmount))

    if clustersAmount == 1:
        return [points]
    
    clusters = []

    counter = 0

    while counter < clustersAmount:
        counter += 1

        clusters = []
        max,maxValue = [],0
        for i in range(0,len(mst)):
            for k in range(0,len(mst[i])):
                if mst[i][k] > maxValue:
                    max = [i,k]
                    maxValue = mst[i][k]
                    
        mst[max[0]][max[1]] = 0
        mst[max[1]][max[0]] = 0

        copyMst = copy.deepcopy(mst)
        clusters = MinDistancesToClusters(copyMst, points)

        resetTree = False

        # for loop checks if any cluster is too small
        for i in clusters:
            print(f"i has lenght {len(i)}")
            if len(i) < minimumPoints:
                resetTree = True
                print(F"Not deleting : {i}")

        
        if resetTree:
            mst[max[0]][max[1]] = 0.001
            mst[max[1]][max[0]] = 0.001
            print(f"Reset : {max}\nresetTree: {resetTree}")
            counter -= 1

        else:
            # the two lines below delete the relevant side
            temp[max[0]][max[1]] = 0
            temp[max[1]][max[0]] = 0
            print(f"Chose to delete : {max}\nresetTree = {resetTree}")
            counter += 1
        
    print(f"Counter : {counter}")

    return MinDistancesToClusters(temp,points)    
    
if __name__ == "__main__":
    colours = ["red","purple","blue","black","tan","pink","orange","green","lightskyblue","teal","sienna","salmon","goldenrod","coral","darkkhaki","rebeccapurple","indigo","silver"]
    examplePoints = [[1,34],[56,25],[42,43],[24,54],[24,45]]

    mst = prims(createMinimumDistances(examplePoints))
    toPlot = limitClustering(mst, 2, examplePoints)
    
    print(toPlot)
    for i in range(0,len(toPlot)):
        x,y = [],[]
        for k in toPlot[i]:
            x.append(k[0])
            y.append(k[1])
            plt.scatter(x, y, c = colours[i])
            
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()  