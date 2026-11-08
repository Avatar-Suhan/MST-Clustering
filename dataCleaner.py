import copy
iqr = lambda data : data[round(3*len(data)/4)-1] - data[round(len(data)/4)-1]
mean = lambda data : data[round(len(data)/2)-1]

def bubbleSort(list):
    temp = 0
    for i in range(0,len(list)):
        for k in range(1,len(list)):
            if list[k] <list[k-1]:
                temp = list[k]
                list[k] = list[k-1]
                list[k-1] = temp
    return list

def stripOutliers(list):
    """
    Input : any numerical list
    Output : list stripped of any items more than 1.5 times the IQR away from the mean
    """
    list = bubbleSort(list)
    mean = list[round(len(list)/2)-1]
    IQR = list[round(3*len(list)/4)-1] - list[round(len(list)/4)-1]

    for i in list:
        if i < mean - 1.5*IQR or i > mean + 1.5*IQR:
            list.remove(i)
    return list

def cleanData(dataOG):
    """
    Input: List of form [[x,y],...]
    Output: List with x,y having outliers stripped and IQR matched
    """
    data = copy.deepcopy(dataOG)
    x,y,points = [],[],[]
    for i in range(0,len(data)):
        x.append(data[i][0])
        y.append(data[i][1])

        points.append(i)
    


    x_iqr = iqr(bubbleSort(x))
    y_iqr = iqr(bubbleSort(y))

    """

    #Following removes outliers

    x_mean = mean(bubbleSort(x))
    y_mean = mean(bubbleSort(y))
    n = 1
    for i in data:
        print(f"{n}Considering : {i}")
        n += 1
        if i[0] == 6121.3:
            print("MUAHAHAHAHAHAHAH\n\n\n\n\n\n\n\n\n\n\n\n")
            print(i)
        if (i[0] < (x_mean - 1.5*x_iqr)) or (i[0] > (x_mean + 1.5*x_iqr)):
            data.remove(i)
            #print(f"Removed {i}, because of x")
        elif (i[1] < y_mean - 1.5*y_iqr) or (i[1] > y_mean + 1.5*y_iqr):
            data.remove(i)
            #print(f"Removed {i}, because of y")

    """

    for i in range(0,len(data)):
        data[i][0] = data[i][0]*(100/x_iqr)
        data[i][1] = data[i][1]*(100/y_iqr)

        

    return data

if __name__ == "__main__":

    examplePoints = [[1,1],[1,2],[1,3],[1,4],[1,5]]
    exampleMST = [[0,0,0,10,0],[0,0,0,20,0],[0,0,0,5,2],[10,20,5,0,0],[0,0,2,0,0]]
    
    annoyingExamplePoints = [[3,1],[1,2],[9,3],[2,4],[0.4,5],[5,6],[1,7],[10,8]]

    print(cleanData(annoyingExamplePoints))
    print("here")