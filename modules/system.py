from .perceptron import Preceptron
import matplotlib.pyplot as plt
import numpy as np

class System:
    def __init__(self):
        self.A_x = []
        self.A_y = []
        self.B_x = []
        self.B_y = []
        self.error = 1
        self.fileText = ""
        self.result = ""
        self.readFromFile()
        self.most_left_x = min(min(self.A_x),min(self.B_x))
        self.most_right_x = max(max(self.A_x),max(self.B_x))
        self.p = Preceptron()
        self.F_x = np.linspace(self.most_left_x, self.most_right_x, 10)
        self.F_y = self.F_x

    def readFromFile(self):
        file = open("data.txt", "r")
        text = file.readlines()
        x=0
        for i in text:
            self.fileText=  self.fileText+str(i)
            if i[0] == "#":
                pass
            elif i[0] == "\n":
                x=x+1
            else:
                if x == 0:
                    self.A_x.append(float(i.split("\t")[0]))
                    self.A_y.append(float(i.split("\t")[1]))
                elif x == 1:
                    pass
                    self.B_x.append(float(i.split("\t")[0]))
                    self.B_y.append(float(i.split("\t")[1]))
        

    def lin_function(self,a,b,x):
        return a*x+b

    def oneStepLearning(self):
        count = 0
        for i in range(0,len(self.A_x)):
            count=count+self.p.learn(self.A_x[i],self.A_y[i],1)
        for i in range(0,len(self.B_x)):
            count=count+self.p.learn(self.B_x[i],self.B_y[i],0)
        self.error=1-count/(len(self.A_x)+len(self.B_x))
        print("%f" % (self.error))
        try:
            b = self.p.calc_b()
            a = self.p.calc_a()
        except:
            raise Exception("Vert")
        self.F_y=[]
        for i in self.F_x:
            self.F_y.append(self.lin_function(a,b,i))

            
            