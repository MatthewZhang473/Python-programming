import numpy as np
import matplotlib.pyplot as plt


Voltages = [3.1,3.25,3.5,4,4.06,4.16]
Currents = [1.4,2,3.6,12,17,23]

plt.plot(Voltages,Currents)
plt.xlabel('$Voltages(V)$')
plt.ylabel('$Currents(mA)$')
plt.show()
