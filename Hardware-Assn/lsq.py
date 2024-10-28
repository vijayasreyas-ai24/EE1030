import numpy as np
import matplotlib.pyplot as plt

A = np.loadtxt('training_data.txt')
X = np.hstack((np.ones((A.shape[0],1)),A[:,[0]],A[:,[0]]**2))
T = A[:,[0]]
Y = A[:,[1]]

# Least squares method
v, av, bv = np.linalg.lstsq(X, Y, rcond=None)[0]
theta = np.zeros((3,1))
theta[0][0] = v.item()
theta[1][0] = av.item()
theta[2][0] = bv.item()
print(theta)

# Plot both the results
plt.plot(T, X@theta)
plt.plot(T, Y, 'k.')
plt.grid()
plt.ylabel('Output Voltage (V)')
plt.xlabel(r'Temperature ($^{\circ}$C)')
plt.tight_layout()
plt.savefig('/home/vijaya-sreyas/EE1030/EE1030/Hardware-Assn/train.png')

# Close current figure(s)
plt.close('all')

# Plot for validation
B = np.loadtxt('validation_data.txt')
Xv = np.hstack((np.ones((B.shape[0],1)),B[:,[0]],B[:,[0]]**2))
Yv = B[:,[1]]
Tv = B[:,[0]]
plt.plot(Tv, Xv@theta)
plt.plot(Tv, Yv, 'k.')
plt.ylabel('Output Voltage (V)')
plt.xlabel(r'Temperature ($^{\circ}$C)')
plt.grid()
plt.tight_layout()
plt.savefig('/home/vijaya-sreyas/EE1030/EE1030/Hardware-Assn/valid.png')

