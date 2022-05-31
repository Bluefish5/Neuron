import matplotlib.pyplot as plt
import numpy as np


class Preceptron:
    w0 = 0
    w1 = 0
    w2 = 1

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
            return 0
        return 1
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

def lin_function(a,b,x):
    return a*x+b



if __name__ == "__main__":
    p = Preceptron()
    error=1
    
    x = np.linspace(0, 100, 10)
    A_x,A_y,B_x,B_y = readFromFile()
    while error>0.07:
        count=0
        for i in range(0,15):
            count=count+p.learn(A_x[i],A_y[i],1)
            count=count+p.learn(B_x[i],B_y[i],-1)
        error=1-count/32
        print("%f" % (error))
        y=[]
        for i in x:
            y.append(lin_function(p.calc_a(),p.calc_b(),i))
        plt.plot(x,y)
        plt.scatter(A_x,A_y)
        plt.scatter(B_x,B_y)
        plt.draw()
        plt.pause(0.0001)
        plt.clf()

   
    
    