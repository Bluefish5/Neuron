class Preceptron:
    def __init__(self):
        self.w0=0
        self.w1=0
        self.w2=0
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
