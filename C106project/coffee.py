import csv
import plotly.express as px
import numpy as py

def getDataSource(dataPath):
    coffee=[]
    sleep=[]
    with open(dataPath) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x="Coffee in ml", y="sleep in hours")   
        fig.show() 
        for row in df:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return{"x":coffee, "y":sleep}

def findCorrelation(dataSource):
    correlation = py.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between coffee consumed and amount of time the person slept ",correlation[0,1])

def setup():
    dataPath = "coffee.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

setup()

