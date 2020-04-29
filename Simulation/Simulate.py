from __future__ import print_function, division

import warnings
warnings.filterwarnings('ignore')

import numpy as np
import matplotlib.pyplot as plt
import thinkplot
from matplotlib import rc
from matplotlib.animation import FuncAnimation
rc('animation', html='html5')
from PredPrey import PredPrey, PredPreyViewer

rd = PredPrey(50,params=(0.6,0.7,0.014,0.014))
print(rd.array)
print(rd.array2)
viewer  = PredPreyViewer(rd)
viewer.draw()

# anim = viewer.animate(frames=100)
# anim
# plt.show()
# anim.save('predpreyanimation.mp4',fps=30)
 
# viewer.draw()

thinkplot.preplot(cols=3)
viewer.step(1000)
viewer.draw()

thinkplot.subplot(2)
viewer.step(2000)
viewer.draw()
thinkplot.subplot(3)
viewer.step(4000)
viewer.draw()
plt.show()

# thinkplot.preplot(cols=5)
# viewer.step(500)
# viewer.draw()
# thinkplot.subplot(2)
# viewer.step(500)
# viewer.draw()

# thinkplot.subplot(3)
# viewer.step(500)
# viewer.draw()

# thinkplot.subplot(4)
# viewer.step(500)
# viewer.draw()

# thinkplot.subplot(5)
# viewer.step(3000)
# viewer.draw()

# plt.show()
# plt.savefig('PredPreyTest.pdf')