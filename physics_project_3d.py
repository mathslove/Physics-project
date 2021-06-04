
import matplotlib.pyplot as plt
import numpy as np
import scipy.special as scp

theta, phi = np.linspace(0, 2 * np.pi, 40), np.linspace(0, np.pi, 40)
THETA, PHI = np.meshgrid(theta, phi)
#
# # U = math.sqrt(3/(4*math.pi))*np.sin(THETA)*np.cos(PHI)
# # U = [i ** 2 for i in R]
# U = math.sqrt(1/(4*math.pi))
#
# X = U * np.sin(THETA) * np.cos(PHI)
# Y = U * np.sin(PHI) * np.sin(THETA)
# Z = U * np.cos(THETA)
#
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1, projection='3d')
# plot = ax.plot_surface(
#     X, Y, Z, rstride=1, cstride=1, cmap=None,
#     linewidth=0, antialiased=False, alpha=0.5)
# plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
U = scp.sph_harm(0, 1, THETA, PHI)
X = U * np.sin(THETA) * np.cos(PHI)
Y = U * np.sin(PHI) * np.sin(THETA)
Z = U * np.cos(THETA)
plot = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                       linewidth=0, antialiased=False, alpha=0.5)
plt.show()