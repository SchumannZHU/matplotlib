from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import genfromtxt

#(when use jupyter notebook)
#%matplotlib notebook

f=genfromtxt(r"C:\Users\jasmi\Desktop\12.csv", delimiter=",")

fig = pyplot.figure()
ax = Axes3D(fig)

ax.set_xlabel("Present tense")
ax.set_ylabel("Subject")
ax.set_zlabel("Onomatopoeia")

ax.set_xlim(-20, 20)
ax.set_ylim(-90, 50)
ax.set_zlim(-30, 20)

d1 = f[0:3,:]
d2=f[3:6,:]
d3=f[6:9,:]
d4=f[9:12,:]

ax.plot(d1[:,0], d1[:,1], d1[:,2], "o", color="#000000", ms=10, mew=0.5)
ax.plot(d2[:,0], d2[:,1], d2[:,2], "o", color="#696969", ms=10, mew=0.5)
ax.plot(d3[:,0], d3[:,1], d3[:,2], "o", color="#c0c0c0", ms=10, mew=0.5)
ax.plot(d4[:,0], d4[:,1], d4[:,2], "o", color="#ffffff", ms=10, mew=0.5)

plt.legend(('C->J', 'J->C', 'E->J','E->C'), loc='upper left') 
pyplot.show()
