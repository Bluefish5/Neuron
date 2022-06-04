from os import execl


class Preceptron:
    def __init__(self,system):
        self.system=system
        self.w0=100
        self.w1=10
        self.w2=10
        self.l=0.5
    def learn(self,x, y, out):
        sum=(self.w1*x)+(self.w2*y)+(self.w0*1)
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
            return -float(self.w1)/self.w2
        except:
            raise Exception("ZERO")
            
    def calc_b(self):
        try:
            return -float(self.w0)/self.w2
        except:
            raise Exception("ZERO")
        