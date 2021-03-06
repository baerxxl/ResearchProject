import numpy as np
class connection:

    xlayer = None
    ylayer = None
    xnum = None
    ynum = None
    Widx = None # reshape to lnum by unum
    Wcoef = None
    def __init__(self, xlayer, ylayer, xnum, ynum, Widx, Wcoef=1.0):
        self.xlayer = xlayer
        self.ylayer = ylayer
        self.xnum = xnum
        self.ynum = ynum
        self.Widx = Widx
        self.Wcoef = Wcoef
        xlayer.connectUp.append(self)
        ylayer.connectDown.append(self)

    def getW(self, W):
        #print self.xlayer.name, self.ylayer.name
        #print self.Widx
        #print W.shape
        #print W[self.Widx]
        return W[self.Widx].reshape((self.ynum, self.xnum))
    def forwardprop(self, W, numData):
        ylayer = self.ylayer
        xlayer = self.xlayer
        xnum = self.xnum
        ynum = self.ynum
        if ylayer.z is None:
            ylayer.z = np.zeros( (ylayer.numUnit, numData) )
        tmpW = self.getW(W)
        tmpforward =  np.dot( tmpW,  xlayer.y ) * self.Wcoef
        ylayer.z += tmpforward
    def backprop(self, Weights, gradWeights, numData):
        xlayer = self.xlayer
        ylayer = self.ylayer
        dEdz = ylayer.dE_by_dz
        #W = Weights[con.Widx].reshape(ynum,-1)
        W = self.getW(Weights)
        # with size y
        dEdx = np.dot( W.T, dEdz ) * self.Wcoef#* (xlayer.yL) / (curLayer.xL)
        # plug into the proper dE/dy of the lower layer
        if xlayer.dE_by_dy is None:
            xlayer.dE_by_dy = np.zeros((xlayer.numUnit,numData))
        xlayer.dE_by_dy += dEdx

        # update current weights
        dEdW = np.dot(  dEdz, (xlayer.y).T ) * self.Wcoef # do not normalize by numData
        # plug into the gradient

        Widx = self.Widx
        gradWeights[Widx] += dEdW.reshape(-1,1) #* (xlayer.yL) / (curLayer.xL)
    def display(self, Weights, direction):
        print '    ',direction, self.xlayer.name, '->', self.ylayer.name, 'with W', self.Widx[0:5],\
                    ' Wcoefficents', self.Wcoef\
                    , ' =', Weights[self.Widx[0:5]]

class PoolConnection():
    xlayer = None
    ylayer = None
    xnum = None
    ynum = None
    def __init__(self, xlayer, ylayer):
        self.xlayer = xlayer
        self.ylayer = ylayer
        xlayer.connectUp.append(self)
        ylayer.connectDown.append(self)

    def forwardprop(self, W, numData):
        if self.ylayer.z is None:
            self.ylayer.z = []
        self.ylayer.z.append(self.xlayer.y)
    def backprop(self, Weights, gradWeights, numData):
        if self.ylayer.poolType == 'max':
            if self.xlayer.dE_by_dy is None:
                self.xlayer.dE_by_dy = self.ylayer.dE_by_dy * (self.ylayer.y == self.xlayer.y)
            else:
                self.xlayer.dE_by_dy+= self.ylayer.dE_by_dy * (self.ylayer.y == self.xlayer.y)
        elif self.ylayer.poolType == 'sum':
            if self.xlayer.dE_by_dy is None:
                self.xlayer.dE_by_dy = self.ylayer.dE_by_dy
            else:
                self.xlayer.dE_by_dy += self.ylayer.dE_by_dy
    def display(self, Weights, direction):
        print '    ', direction, self.xlayer.name, '->', self.ylayer.name,\
            'type = ', self.ylayer.poolType
