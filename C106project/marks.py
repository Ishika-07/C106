import csv
import plotly.express as px
import numpy as py

def getDataSource(dataPath):
    percent=[] 
    present=[]
    with open(dataPath) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x="Days Present", y="Marks In Percentage")   
        fig.show()    
        for row in df:
            percent.append(float(row["Marks In Percentage"]))
            present.append(float(row["Days Present"]))
    return{"x":percent, "y":present}
        
def findCorrelation(dataSource):
    correlation = py.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between percentage of the student and the number of days the student attended school ",correlation[0,1])

def setup():
    dataPath = "marks.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

setup()

