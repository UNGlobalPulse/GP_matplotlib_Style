import matplotlib.pyplot as plt
import gp_colours as gpc

gpc.setStyle()

plt.plot([i*i for i in range(10)],gpc.gpLightBlue,label='Line 1')
plt.plot([i for i in range(10)],gpc.gpBlue,label='Line 2')
plt.plot([0.5*i for i in range(10)],gpc.gpLightGray,label='Line 3')
plt.annotate('Global Pulse Graph',xy=(0.5,0.5),xycoords='axes fraction')
plt.ylabel('Spherical Giga-Inches')
plt.xlabel('Kilo-Micro Nautical Volts')

plt.legend()

plt.show()
