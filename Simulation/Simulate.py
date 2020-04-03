from __future__ import print_function, division

import warnings
warnings.filterwarnings('ignore')

import numpy as np
import matplotlib.pyplot as plt
import thinkplot
from matplotlib import rc
rc('animation', html='html5')
from PredPrey import PredPrey, PredPreyViewer

rd = PredPrey(100,params=(0.6,0.7,0.014,0.014))
viewer  = PredPreyViewer(rd)
thinkplot.preplot(cols=3)
viewer.step(1000)
viewer.draw()

thinkplot.subplot(2)
viewer.step(2000)
viewer.draw()

thinkplot.subplot(3)
viewer.step(4000)
viewer.draw()

plt.savefig('PredPreyTest.pdf')