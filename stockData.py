from dataCleaner import *

def importCSVRange(fileName):
    """
    outputs data in the form:
    [[closingPrice,Range of Price]]
    
    Input format:
    "Name";"Last";"High";"Low";"Chg.";"Chg. %";"Vol.";"Time"

    """

    with open(fileName, "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    cleanData,xyCoordinates = [],[]

    for i in lines:
        j = i.replace(",","")
        text = j.split("\"")
        cleanData.append(text)

    """
    cleanData contains all the s&p 500 data, but split into individual items as 
    dictated by the ";"
    format : [["Name","Last","High","Low","Chg.","Chg. %","Vol.","Time"]]
    index :      1      3      5      7     9       11      13     15

    """
    for i in cleanData:
        xyCoordinates.append([float(i[3]), round(float(i[5]) - float(i[7]),3)])

    return xyCoordinates

def importCSVChange(fileName):
    """
    outputs data in the form:
    [[closingPrice,Range of Price]]
    
    Input format:
    "Name";"Last";"High";"Low";"Chg.";"Chg. %";"Vol.";"Time"

    """

    with open(fileName, "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    cleanData,xyCoordinates,x,y = [],[],[],[]

    xInsert, yInsert = [],[]

    for i in lines:
        j = i.replace(",","")
        text = j.split("\"")
        cleanData.append(text)

    """
    cleanData contains all the s&p 500 data, but split into individual items as 
    dictated by the ";"
    format : [["Name","Last","High","Low","Chg.","Chg. %","Vol.","Time"]]
    index :      1      3      5      7     9       11      13     15

    """
    for i in cleanData:
        x.append(float(i[3]))
        y.append(float(i[11][:-1]))

    x_copy,y_copy = copy.deepcopy(x), copy.deepcopy(y)

    x_copy = sorted(x_copy)
    y_copy = sorted(y_copy)

    xMean, yMean, xIQR, yIQR = mean(x_copy), mean(y_copy), iqr(x_copy), iqr(y_copy)

    for i in range(0,len(x)):
        if not (x[i] < xMean - 1.5*xIQR or x[i] > xMean + 1.5*xIQR):
            if not (y[i] < yMean - 1.5*yIQR or y[i] > yMean + 1.5*yIQR):
                xyCoordinates.append([float(cleanData[i][3]), float(cleanData[i][11][:-1])])
        else:
            print(f"deleted : [{x[i]},{y[i]}]")

    return xyCoordinates

if __name__ == "__main__":
    #print(importCSV("stockData.txt"))
    pass