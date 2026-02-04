import numpy as np
import matplotlib.pyplot as plt
import os

#matrix of size 5*5 with random integer number
data = np.random.randint(1,101,size=(5,5))
#file in csv formate
file = "Data.csv"

class DataStatistics:
    #an __init__ method save the data in file
    def __init__(self):
        try:
            if os.path.exists(file):
                np.savetxt(file,data ,delimiter=",",fmt="%d")
                print(f"\nCSV file {file} created Successfully\n\n")
        except FileNotFoundError as err:
            print(err)
        except Exception as error:
            print(error)
        
    #display method to display the data
    def display(self):
        try:
            if os.path.exists(file):
                data = np.genfromtxt(file,delimiter=",",dtype="int32")
                print(f"Random 5 ,5 matrix :-\n\n{data}")
        except FileNotFoundError as err:
            print(err)
        except Exception as error:
            print(error)

    #calculate method to calculate mean standard deviation min and max
    def calculate(self):
        mean = data.mean(axis=1)
        mean = np.round(mean,2)

        std = data.std(axis=1)
        std = np.round(std,2)

        min = data.min(axis=1)
        max = data.min(axis=1)

        print(f"Minimum number of each row : {min}")
        print(f"Maximum number of each row : {max}")
        print(f"mean  of each row : {mean}")
        print(f"Standard deviation of each row : {std}\n\n")



class Normalization:
    #normalization method to normalize data min max formula
    def min_max_formula(self):
        print(f"Data normalize using min-max Normalization along column:-")
        normalize = (data - data.min(axis=0))/(data.max(axis=0) - data.min(axis=0))
        print(np.round(normalize,2))

        print(f"\n\nData normalize using min-max Normalization along row:-")
        normalize = (data - data.min(axis=1,keepdims=True))/(data.max(axis=1,keepdims=True) - data.min(axis=1,keepdims=True))
        print(np.round(normalize,2))

    #normalization method to normalize data using z-score formula
    def z_score_formula(self):
        print(f"\n\nData normalize using Z-Score Normalization:-")
        normalize = (data - data.mean(axis=0))/(data.std(axis=0))
        print(np.round(normalize,2),end="\n\n")


class Graph:
    def line_plot(self,x,y):
        plt.xlabel("x label")
        plt.ylabel("y label")
        plt.title("Simple Graph")
        plt.plot(x,y)
        plt.show()

    def muliple_line(self , x,y,z):
        plt.plot(x,y,label='line1')
        plt.plot(x,z,label='line2')
        plt.legend()
        plt.show()

    def scatter(self,x,y):
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Scatter Graph')
        plt.scatter(x,y)
        plt.show()

    def histogram(self,x):
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Histogram')
        plt.hist(x)
        plt.show()
    
    def bar_chart(self,catagory,value):
        plt.xlabel('catagory')
        plt.ylabel('value')
        plt.title('Bar chart')
        plt.bar(catagory,value)
        plt.show()

def main():
    datastatistics = DataStatistics()
    datastatistics.display()
    datastatistics.calculate()

    normalize = Normalization()
    normalize.min_max_formula()
    normalize.z_score_formula()

    x = [1,2,3,4,5,6]
    y = [45,48,52,50,55,60]

    z = [40,45,58,43,50,55]
    h = [1,1,2,3,4,5,3,5,6,5,3,6]
    catagory = ['a','b','c','d','e']
    value =[150,200,180,220,170] 
    graph = Graph()

    graph.line_plot(x = x,y= y)
    graph.muliple_line(x=x,y= y,z=z)

    graph.histogram(x=h)

    graph.scatter(x=x,y=y)
    graph.bar_chart(catagory = catagory,value=value)


if __name__ == "__main__":
    main()

