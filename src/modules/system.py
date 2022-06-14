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
        self.tab = []
        self.maxIteration = 100000
        self.goalError = 0.0
        self.p = Preceptron()
        self.fileText = ""
        self.resultText = ""
        self.resultErrorText = ""
        self.defaultFileName = "data.txt"
        self.currIteration = 0
        self.currError = 0.0
        self.readFromFile()
        self.fileTextToCoordinates()

    def readFromFile(self):
        file = open(self.defaultFileName, "r")
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
        most_left_x = min(min(self.A_x),min(self.B_x))
        most_right_x = max(max(self.A_x),max(self.B_x))
        self.F_x = np.linspace(most_left_x, most_right_x, 10)
        self.F_y = self.F_x

    def lin_function(self,a,b,x):
        return a*x+b

    def oneStepLearning(self):
        count = 0
        self.currIteration=self.currIteration+1
        for i in range(0,len(self.A_x)):
            self.p.learn(self.A_x[i],self.A_y[i],1)
        for i in range(0,len(self.B_x)):
            self.p.learn(self.B_x[i],self.B_y[i],0)

        for i in range(0,len(self.A_x)):
            count=count+self.p.calculate(self.A_x[i],self.A_y[i],1)
        for i in range(0,len(self.B_x)):
            count=count+self.p.calculate(self.B_x[i],self.B_y[i],0)
        self.currError=1-count/(len(self.A_x)+len(self.B_x))
        
        self.resultErrorText = self.resultErrorText + str(self.currError) + "\n"
        try:
            b = self.p.calc_b()
            a = self.p.calc_a()
        except:
            raise Exception("Vert")
        self.F_y=[]
        for i in self.F_x:
            self.F_y.append(self.lin_function(a,b,i))
        
    def stopCondition(self):
        return (self.currIteration>self.maxIteration or self.currError<=self.goalError)
    
    def generateResaults(self):
        w0,w1,w2=self.p.getAtributes()
        self.resultText = "Iter: " + str(self.currIteration) + "\nw0: "+ str(w0) + "\nw1: " + str(w1) +"\nw2: "+ str(w2) + "\nf(x)=" + str(round(self.p.calc_a(),2)) + "x"
        if self.p.calc_b()>=0:
            self.resultText=self.resultText+"+"
        self.resultText=self.resultText+str(round(self.p.calc_b(),2))+"\nError: "+str(round(self.currError,5))
