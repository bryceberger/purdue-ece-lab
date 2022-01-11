import numpy as np
import matplotlib.pyplot as plt

# thevenin voltage and impedance
v = 4/5 + 2/5*1j
z = 1 - 1j

# range to test input load angle at
t = np.linspace(-np.pi,np.pi,1000)
# input load
l = np.absolute(z) * (np.cos(t) + 1j * np.sin(t))

# power to load
p = .5 * np.absolute(v / (z + l)) ** 2 * np.real(l)

print("degrees at max:", np.degrees(np.angle(l[np.argmax(p)])))
print("max value:", np.max(p))

plt.plot(t*180/np.pi, p)
plt.show()

with open("power", 'w') as data:
  for p in zip(t*180/np.pi, p):
    data.write(f"{p[0]} {p[1]}\n")
