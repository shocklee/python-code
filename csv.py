import csv
import os
myPath = "C:/Users/shockma/My Documents/Special/Other"
with open(os.path.join(myPath, "fnames.csv"), "rb") as myFile:
    myFileReader = csv.reader(myFile)
    for row in myFileReader:
        print row
