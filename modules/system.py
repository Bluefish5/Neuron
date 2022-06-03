from traceback import print_tb
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
        self.maxIteration = 10000
        self.F_x = np.linspace(0, 100, 10)
        self.F_y = [1,2,3,4,5,6,7,8,9,10]
        self.fileText = ""
        self.result = ""
        self.p = Preceptron()
        self.fileName = "data.txt"
        self.readFromFile()
        self.fileTextToCoordinates()
        

    def readFromFile(self):
        file = open(self.fileName, "r")
        text = file.readlines()
        x=0
        self.fileText = ""
        for i in text:
            self.fileText = self.fileText+str(i)
    
    
    def fileTextToCoordinates(self):
        self.A_x = []
        self.A_y = []
        self.B_x = []
        self.B_y = []
        x=0
        for i in self.fileText.split("\n"):
            if i!="":
                if i[0]!="#":
                    if x == 0:
                        self.A_x.append(float(i.split("\t")[0]))
                        self.A_y.append(float(i.split("\t")[1]))
                    elif x == 1:
                        self.B_x.append(float(i.split("\t")[0]))
                        self.B_y.append(float(i.split("\t")[1]))
            else:
                x=x+1

    def lin_function(self,a,b,x):
        return a*x+b

    def oneStepLearning(self):
        count = 0
        for i in range(0,15):
            count=count+self.p.learn(self.A_x[i],self.A_y[i],1)
        for i in range(0,15):
            count=count+self.p.learn(self.B_x[i],self.B_y[i],-1)
        self.error=1-count/32
        print("%f" % (self.error))
        self.F_y=[]
        try:
            b = self.p.calc_b()
            a = self.p.calc_a()
        except:
            raise Exception("Vert")
        for i in self.F_x:
            self.F_y.append(self.lin_function(a,b,i))

            
            