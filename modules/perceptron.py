from os import execl
import random


class Preceptron:
    def __init__(self):
        
        self.w0=random.randint(-1000000,1000000)
        self.w1=random.randint(-1000000,1000000)
        self.w2=random.randint(-1000000,1000000)
        self.l=100
    def learn(self,x, y, out):
        sum=self.w1*x+self.w2*y+self.w0
        if sum<0:
            sum=0
        else:
            sum=1
        diff=out-sum
        self.w0=self.w0+self.l*diff
        self.w1=self.w1+self.l*(diff*x)
        self.w2=self.w2+self.l*(diff*y)

        return (diff==0)
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
