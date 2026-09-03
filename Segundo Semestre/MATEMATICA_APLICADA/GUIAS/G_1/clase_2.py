import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 6, 0.01)
y = 120 * x + 2000
plt.plot(x, y)
plt.xlabel("Energia utilizada ({kWh})")
plt.ylabel("Costo para usuario ($)")
plt.title("Costo para el usuario según uso de energia")
plt.grid(True)
plt.show()

def C(e):
    return 129*e+2000