def importCSVChange(fileName):
    """
    outputs data in the form:
    [[x,y]]
    

    """

    with open(fileName, "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    cleanData,xyCoordinates = [],[]

    for i in lines:
        j = i.replace("    "," ")
        text = j.split(" ")
        cleanData.append(text)

    """
    mrrrrp meow 

    """
    for i in cleanData:
        if i[0]!= '' and i[1] != '':
            xyCoordinates.append([float(i[0]), float(i[1])])
    return xyCoordinates