from __future__ import print_function, division

# %matplotlib inline
# %precision 3

import warnings
warnings.filterwarnings('ignore')

import numpy as np
import matplotlib.pyplot as plt
from Cell2D import Cell2DViewer, Cell2D
import thinkplot

from matplotlib import rc
from scipy.signal import correlate2d

rc('animation', html='html5')

def island(a, val, noise=None):
        noise = val if noise is None else noise
        n, m = a.shape
        r = min(n, m) // 20
        a[n//2-r:n//2+r, m//2-r:m//2+r] = val
        a += noise * np.random.random((n, m))

class PredPrey(Cell2D):
    """Reaction-Diffusion Cellular Automaton."""

    kernel = np.array([[.05, .2, .05],
                       [ .2, -1, .2],
                       [.05, .2, .05]])

    options = dict(mode='same', boundary='wrap')

    def __init__(self, n, m=None, params=(0.5, 0.25, 0.035, 0.057)):
        """Initializes the attributes.

        n: number of rows
        m: number of columns
        params: tuple of (Da, Db, f, k)
        """
        
        self.params = params
        m = n if m is None else m
        self.array = np.ones((n, m), dtype=float)

        self.array2 = np.zeros((n, m), dtype=float)
        island(self.array2, val=0.1, noise=0.1)
        
    def step(self):
        """Executes one time step."""
        # A = self.array
        # B = self.array2
        # ra, rb, f, k = self.params
        H = self.array
        L = self.array2
        birth_rate, death_rate, a, c = self.params
        
        # cA = correlate2d(A, self.kernel, **self.options)
        # cB = correlate2d(B, self.kernel, **self.options)
        cH = correlate2d(H, self.kernel,**self.options)
        cL = correlate2d(L, self.kernel, **self.options)

        # reaction = A * B**2

        # self.array += ra * cA - reaction + f * (1-A) 
        # self.array2 += rb * cB + reaction - (f+k) * B
        self.array += birth_rate*cH - a*L*H
        self.array2 += c*cL*cH - death_rate*L    

class PredPreyViewer(Cell2DViewer):
    """Generates images and animations."""
    
    cmapu = plt.get_cmap('Reds')
    cmapv = plt.get_cmap('Blues')

    options = dict(alpha=0.7,
                  interpolation='bicubic')
        
    def __init__(self, viewee):
        """Initializes the attributes.
        
        viewee: the object to be represented
        """
        self.viewee = viewee
        self.imu = None
        self.imv = None
        self.hlines = None
        self.vlines = None

    def draw(self, grid=False):
        """Draws the cells."""
        au = self.viewee.array.copy()
        av = self.viewee.array2.copy()
        
        n, m = av.shape
        plt.axis([0, m, 0, n])
        plt.xticks([])
        plt.yticks([])

        self.options['extent'] = [0, m, 0, n]
        self.imu = plt.imshow(au, cmap=self.cmapu, **self.options)
        self.imv = plt.imshow(av, cmap=self.cmapv, **self.options)

    def animate_func(self, i):
        """Draws one frame of the animation."""
        if i > 0:
            self.step(iters=100)

        self.imu.set_array(self.viewee.array)
        self.imv.set_array(self.viewee.array2)
        return (self.imu, self.imv)