from os import execl
import random


class Preceptron:
    def __init__(self):
        self.w0=random.random()
        self.w1=random.random()
        self.w2=random.random()
        self.l=0.001
    def learn(self,x, y, out):
        suma=self.w1*x+self.w2*y+self.w0
        diff=out-suma
        self.w0=self.w0+self.l*diff
        self.w1=self.w1+self.l*diff*x
        self.w2=self.w2+self.l*diff*y
        if suma<=0:
            suma=0
        else:
            suma=1
        if suma==out:
            return 1
        else:
            return 0
    def calc_a(self):
        try:
            return -self.w1/self.w2
        except:
            raise Exception("ZERO")

    def calc_b(self):
        try:
            return -self.w0/self.w2
        except:
            raise Exception("ZERO")
    def getAtributes(self):
        return self.w0,self.w1,self.w2
