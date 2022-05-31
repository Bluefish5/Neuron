import matplotlib.pyplot as plt
import numpy as np


class Preceptron:
    w0 = 0
    w1 = 0
    w2 = 0
    error=0
    def learn(self,x, y, out):
        sum=self.w1*x+self.w2*y+self.w0*1
        if sum<=0:
            sum=-1
        else:
            sum=1
        if out!=sum:
            self.w0=self.w0+out
            self.w1=self.w1+out*x
            self.w2=self.w2+out*y
        return out==sum
    def calc_a(self):
        return -self.w1/self.w2
    def calc_b(self):
        return -self.w0/self.w2


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
    