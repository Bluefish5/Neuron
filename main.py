import matplotlib.pyplot as plt
import numpy as np
def readFromFile():
    file = open("data.txt", "r")
    text = file.readlines()
    x=0
    A_x=[]
    A_y=[]
    B_x=[]
    B_y=[]
    for i in text:
        if i[0] == "#":
            pass
        elif i[0] == "\n":
            x=x+1
        else:
            if x == 0:
                A_x.append(float(i.split("\t")[0]))
                A_y.append(float(i.split("\t")[1]))
            elif x == 1:
                pass
                B_x.append(float(i.split("\t")[0]))
                B_y.append(float(i.split("\t")[1]))
    return A_x,A_y,B_x,B_y

def function(a,b,x):
    return a*x+b



if __name__ == "__main__":
    x = np.linspace(0, 100, 10)
    y=[]
    for i in x:
        y.append(function(1,0,i))
        
    A_x=[]
    A_y=[]
    B_x=[]
    B_y=[]
    A_x,A_y,B_x,B_y = readFromFile()

    plt.plot(x,y)
    plt.scatter(A_x,A_y)
    plt.scatter(B_x,B_y)
    plt.show()
    