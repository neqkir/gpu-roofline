##### AMD MI100 GPU roofline model

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


GPU_TFLOPS=47.9*1000
GPU_BW=3.2*1000
GPU_SLOPE=GPU_TFLOPS/GPU_BW

x=np.linspace(1,10e5,100)

inflexion=GPU_TFLOPS/GPU_SLOPE

y=np.piecewise(x, [x<inflexion, x>inflexion], [lambda x:GPU_SLOPE*x, GPU_TFLOPS])

plt.plot(x, y, '-r', color='#3B7A57')

plt.title('MI100 Roofline Analysis')
plt.xlabel('Arithmetic Intensity (Flops/Byte)', color='#1C2833')
plt.ylabel('GFLOPs', color='#3B7A57')
plt.semilogx()
plt.semilogy()
plt.legend(loc='upper left')
plt.grid()
plt.show()








