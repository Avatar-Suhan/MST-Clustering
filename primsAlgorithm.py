from stockData import *

def symm(list):
    for x in range(len(list)):
        for y in range(len(list)):
            if list[x][y]!=0 or list[x][y]!=0.0:
                list[y][x] = list[x][y]
    return list

def prims(list):
    emp = []
    for x in range(len(list)):
        temporary = []
        for y in range(len(list)):
            temporary.append(0)
        emp.append(temporary)

    for x in range(len(list)):
        list[x][0] = 0
    #l is ummmm the list of rows we can check x
    l = []
    l.append(0)
    for x in range(len(list)-1):
        row = 0
        cur = {}
        # ts loop below creates dictionary of lowest values per each row available
        for y in l:
            col = 0 
            curr = list[y][0]
            for z in range(len(list)):
                if curr == 0 or curr==0.0:
                    curr = list[y][z]
                    col = z
                if list[y][z] < curr and (list[y][z]!=0.0 or list[y][z]!=0): 
                    curr = list[y][z] 
                    col = z
            cur[y] = col
            #y is epic row and i guess col is column (obv)
        curr = 0
        col = 0
        # ok yay now we can find lowest value from dictionary XD
        for z in cur.keys(): 
            if curr == 0:
                curr = list[z][cur[z]]
                col = cur[z]
                row = z
            elif list[z][cur[z]]< curr:
                curr = list[z][cur[z]]
                col = cur[z]
                row = z
        
        emp[row][col] = list[row][col]
    
        #makes chosen column 0 XDXDXD
        for x in range(len(list)):
            list[x][col] = 0        
        l.append(col)
    return symm(emp)

if __name__ == "__main__":
    for i in prims([[0,3,1,7],[3,0,5,3],[1,5,0,4],[7,3,4,0]]):
        print(i)