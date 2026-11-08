# opinions on this code for finding the "quality" of clusters? 

def distance(cluster, x, i, j):
    #x is cluster index, i is point 1 index, j is point 2 index
    return ((cluster[x][i][0]-cluster[x][j][0])**2+(cluster[x][i][1]-cluster[x][j][1])**2)**0.5

def silhouette(cluster):
    # sil will be the silhouette values; a measure of how appropriately data is clustered. list of values wrt order of clusters in cluster list
    sil = []
    # cluster ought to be the list of lists of lists defining clusters (i.e. [cluster, cluster, ...] where cluster = [[x,y], [a,b], ...])
    # start from 1st cluster at index 0 and cycle through all clusters
    for x in range(len(cluster)):
        aAvg = 0
        bAvg = 0
        # add all a and b values for every value in cluster[x] to aAvg and bAvg respectively 
        for i in range(len(cluster[x])):
            a = 0
            b = 0
            # calculate a
            for j in range(len(cluster[x])):
                if j!=i:
                    a+= distance(x,i,j)
            # finds avg distance
            a = a/(len(cluster[x]))
            
            # calculate b for all clusters; find lowest b value and set it to b
            bvalues = []
            for j in range(len(cluster)):
                btemp = 0
                if j!=x:
                    for k in range(len(cluster[j])):
                        btemp+= distance(j,i,k)
                    btemp = btemp/(len(cluster[j]))
                    # should append mean of distances from i to all values k in other cluster
                    bvalues.append(btemp)
            b = bvalues[0]
            closeCluster = 0
            # compares bvalues to find the lowest one (i.e. the b value for the closest cluster to point i that isn't x)
            for j in range(len(bvalues)):
                if bvalues[j]>b:
                    b = bvalues[j]
                    closeCluster = j
            # finds avg dist
            b = b/len(cluster[closeCluster])
            
            aAvg +=a
            bAvg +=b
        
        # take the avg of each 
        aAvg = aAvg/len(cluster[x])
        bAvg = bAvg/len(cluster[x])

        # sil calculation: b-a/max(a,b)
        s = 0
        if len(cluster[x])==1:
            s = 0
        else:
            if bAvg<=aAvg:
                m = aAvg
            else:
                m = bAvg
            s = (bAvg-aAvg)/m

        sil.append(s)
        
    return sil 

# yeah this should work in theory but in practice idfk

if __name__ == "__main__":
    print(silhouette([[1,2],[2,3],[10,7]]))