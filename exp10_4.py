# WAP to draw Pie Chart and Contour Plot

import matplotlib.pyplot as plt

# Pie Chart
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
e*****e = (0, 0.1, 0, 0)

plt.pie(sizes,
        e*****e=e*****e,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        shadow=True,
        startangle=140)

plt.title("Pie Chart")
plt.axis('equal')
plt.show()


# Contour Plot
import numpy as np

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)

X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

plt.contour(X, Y, Z, levels=10, cmap='viridis')
plt.title("Contour Plot")
plt.colorbar()
plt.show()