# -*- coding: utf-8 -*-

import random

import numpy as np
import matplotlib.pyplot as mpl

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

## class implementing 2d and 3d drunkardwalk
class DrunkardsWalk(object):

        ## the heart of DW2d 
        def __nextXY(self, CurrentLocation=(0, 0, 0)):
                return [(CurrentLocation[0]+random.randint(-1, 1),
                         CurrentLocation[1]+random.randint(-1, 1), 0)]

        ## the heart of DW3d
        def __nextXYZ(self, CurrentLocation=(0, 0, 0)):
                return [(CurrentLocation[0]+random.randint(-1, 1),
                         CurrentLocation[1]+random.randint(-1, 1),
                         CurrentLocation[2]+random.randint(-1, 1))]

        def _DrunkardsWalk(self, steps, start, fun):
            for i in range(1, steps):
                start = start+fun(start[-1])
            return start

        def dw(self, steps, seed, fun):
               return self._DrunkardsWalk(steps, seed, fun)

        def runDW3d(self,):
                fig = mpl.figure()
                ## run drunkardwalk in 3d for 10000 iterations
                points = self.dw(steps=1000, seed=[(0, 0, 0)], fun=self.__nextXYZ)
                x = map(lambda x: x[0], points)
                y = map(lambda y: y[1], points)
                z = map(lambda z: z[2], points)
                ax = fig.add_subplot(111, projection='3d')

                lines = ax.plot(x, y, z, label='my drunkard walk in 3d', c=(25, 0, 65))
                mpl.setp(lines, color='blue', linewidth=1.0)

                ax.set_xlabel('X Axis')
                ax.set_ylabel('Y Axis')
                ax.set_zlabel('Z Axis')
                ax.legend()
                mpl.show()
        
        def runDW2d(self,):
                fig = mpl.figure()
                ## run drunkardwalk in 2d for 10000 iterations
                points = self.dw(steps=1000, seed=[(0, 0)], fun=self.__nextXY)
                x = map(lambda x: x[0], points)
                y = map(lambda y: y[1], points)
                ax = fig.add_subplot(111)

                lines = ax.plot(x, y, label='my drunkard walk in 2d', c=(25, 0, 65))
                mpl.setp(lines, color='purple', linewidth=1.0)

                ax.set_xlabel('X Axis')
                ax.set_ylabel('Y Axis')
                ax.legend()
                mpl.show()

## running the code ..
dw = DrunkardsWalk()
dw.runDW2d()
dw.runDW3d()

