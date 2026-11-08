def importFile(fileName):
    """
    outputs data in the form:
    [[x,y]]
    

    """

    with open(fileName, "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    cleanData,xyCoordinates = [],[]
    text = []
    for i in range(len(lines)):
        if (i%3) == 0:
            text.append(lines[i])
        if (i%3) == 1:
            text.append(lines[i])
        if len(text)==2:
            cleanData.append(text)
            text = []



    for i in cleanData:
        if i[0]!= '' and i[1] != '':
            xyCoordinates.append([float(i[0]), float(i[1])])
        

    return xyCoordinates