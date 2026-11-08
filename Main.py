import matplotlib.pyplot as plt
from MSTclustering import *
import stockData, gamingAddiction
import time
from primsAlgorithm import *
from dataCleaner import *
import trialDB1Importer
import trialDB2Importer
import copy

colours = ["black","red","purple","blue","tan","pink","orange","green","lightskyblue","teal","sienna","salmon","goldenrod","coral","darkkhaki","rebeccapurple","indigo","silver"]

loadingScreen = """\n\n\n\n\nLoading\n\n\n\n\n
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠟
⠀⠀⣀⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⠟⠋⠀⠀
⠘⠻⣿⣿⣿⣿⣿⣦⣄⣤⣠⣄⣤⣠⣄⣤⣴⣾⣿⣟⠁⠀⠀⠀⠀
⠀⠀⠸⣿⣿⣿⣿⣿⡿⠿⠻⣿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠀⠀⠀⠀
⠀⠀⠀⢿⣿⣿⣿⣇⣀⣤⣴⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢿⣿⣟⠛⠛⠛⢻⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠙⠛⠶⢶⡾⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣠⣿⣠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

dataSets = [
    {"id": 1, "name": "S&P 500", "file": "stockData.txt",
     "importer": stockData.importCSVChange, "xlabel": "Price", "ylabel": "% change"},
    {"id": 2, "name": "Gaming Addiction Study", "file": "gamingData.txt",
     "importer": gamingAddiction.importData, "xlabel": "Age", "ylabel": "Hours played daily"},
    {"id": 3, "name": "Trial Database 1", "file": "trialDB1.txt",
     "importer": trialDB1Importer.importCSVChange, "xlabel": "x", "ylabel": "y"},
    {"id": 4, "name": "Trial Database 2", "file": "trialDB2.txt",
     "importer": trialDB2Importer.importFile, "xlabel": "x", "ylabel": "y"},
]

def loadDataset(ds):
    """Load, clean, and build MST for a dataset. Returns (data, mst) or (None, None)."""
    print(loadingScreen)
    print("\n\n\n")
    try:
        data = ds["importer"](ds["file"])
    except Exception as e:
        print(f"Failed to import {ds['name']}: {e}")
        return None, None
    
    if not data:
        print(f"No data loaded from {ds['file']}")
        return None, None
    
    data = cleanData(copy.deepcopy(data))
    if not data:
        print("All data removed during cleaning")
        return None, None
    
    minimumDistanceTable = createMinimumDistances(copy.deepcopy(data))
    mst = prims(copy.deepcopy(minimumDistanceTable))
    return data, mst

def clusterLoop(data, mst, xlabel, ylabel):
    runSession = True
    while runSession:
        try:
            n_points = len(data)
            unique_distances = n_points * (n_points - 1) // 2
            clusterAmount = int(input(
                f"\n\nDataset successfully loaded!\n"
                f"Data points: {n_points}, Unique distances: {unique_distances}\n\n"
                f"Maximum clusters: {len(colours)}\n"
                f"Enter \"0\" to return to main menu\n"
                f"Enter number of clusters: "
            ))
        except ValueError:
            print("\n\nInvalid input. Please enter a number.\n\n")
            time.sleep(2)
            continue
        
        if clusterAmount == 0:
            print("\n\nReturning to Main Menu...\n\n")
            time.sleep(1)
            runSession = False
        elif clusterAmount < 0 or clusterAmount >= len(colours):
            print("\n\nInvalid cluster count. Must be 1-" + str(len(colours)-1) + "\n\n")
            time.sleep(2)
        else:
            toPlot = limitClustering(copy.deepcopy(mst), clusterAmount, copy.deepcopy(data))
            
            for i in range(len(toPlot)):
                x = [p[0] for p in toPlot[i]]
                y = [p[1] for p in toPlot[i]]
                plt.scatter(x, y, c=colours[i])
            
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.show()
            
            input("Press enter to close figure and return to dataset menu")
            plt.close()

def main():
    runMain = True
    while runMain:
        print("\nHello there!")
        print(f"This program currently has {len(dataSets)} datasets ready to run")
        print("Enter \"0\" to terminate the program")
        for ds in dataSets:
            print(f"Enter \"{ds['id']}\" to load the {ds['name']} dataset")
        
        try:
            datasetNumber = int(input("> "))
        except ValueError:
            print("\n\nInvalid input. Please enter a number.\n\n")
            time.sleep(2)
            continue
        
        if datasetNumber == 0:
            print("\n\nGoodbye :3c\n\n")
            runMain = False
        else:
            ds = next((d for d in dataSets if d["id"] == datasetNumber), None)
            if ds is None:
                print("\n\nIncorrect input...\n\n")
                time.sleep(2)
            else:
                data, mst = loadDataset(ds)
                if data is not None:
                    clusterLoop(data, mst, ds["xlabel"], ds["ylabel"])

if __name__ == "__main__":
    main()