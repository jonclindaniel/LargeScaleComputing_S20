'''
This file solves PS1 for MACS 30123
'''
import numpy as np
import scipy.stats as sts
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import os

# Create directory if images directory does not already exist
cur_path = os.path.split(os.path.abspath(__file__))[0]
images_fldr = 'images'
images_dir = os.path.join(cur_path, images_fldr)
if not os.access(images_dir, os.F_OK):
    os.makedirs(images_dir)

# Set model parameters
num_rhovals = int(199)
rho_vals = np.linspace(-0.95, 0.95, num_rhovals)
# rho = 0.5
mu = 3.0
sigma = 0.8
z_0 = mu - 3 * sigma

# Set simulation parameters, draw all idiosyncratic random shocks,
# and create empty containers
S = 1000  # S = 1000  # Set the number of lives to simulate
T = int(1000)  # T = int(4160)  # Set the number of periods for each simulation
np.random.seed(25)
eps_mat = sts.norm.rvs(loc=0, scale=sigma, size=(T, S))

avg_zmat_lteq0_per_vec = np.zeros(num_rhovals)

for r_ind in range(num_rhovals):
    rho = rho_vals[r_ind]
    print('Value of rho =', rho)
    z_mat = np.zeros((T, S))
    z_mat_lteq0_per = T * np.ones(S, dtype=int)
    z_mat[0, :] = z_0

    for s_ind in range(S):
        z_tm1 = z_0
        z_t_pos = True
        for t_ind in range(T):
            e_t = eps_mat[t_ind, s_ind]
            z_t = rho * z_tm1 + (1 - rho) * mu + e_t
            z_mat[t_ind, s_ind] = z_t
            if z_t <= 0 and z_t_pos:
                z_mat_lteq0_per[s_ind] = t_ind + 1
                z_t_pos = False
            z_tm1 = z_t
        if s_ind == 0 and np.isclose(rho, 0.85, atol=0.003):
            # Plot one time series for 100 periods
            fig, ax = plt.subplots()
            plt.plot(np.arange(1, 101), z_mat[:100, s_ind])
            # for the minor ticks, use no labels; default NullFormatter
            minorLocator = MultipleLocator(1)
            ax.xaxis.set_minor_locator(minorLocator)
            plt.grid(b=True, which='major', color='0.65', linestyle='-')
            # plt.title(r'One time path of $z_t$ for first 100 periods', fontsize=20)
            plt.xlabel(r'Period $t$')
            plt.ylabel(r'Health index value $z_t$')
            # plt.show()
            output_path = os.path.join(images_dir, 'zt_path')
            plt.savefig(output_path)
            plt.close()

    avg_zmat_lteq0_per = z_mat_lteq0_per.mean()

    # print('Max minimum value across simulations =', z_mat.min(axis=0).max())
    # print('Average first period in which value is negative =', avg_zmat_lteq0_per)

    avg_zmat_lteq0_per_vec[r_ind] = avg_zmat_lteq0_per

# Plot the average first period to have value less than or equal to zero as a
# function of rho

rho_max = rho_vals[avg_zmat_lteq0_per_vec.argmax()]
pers_max = avg_zmat_lteq0_per_vec.max()
print(r'$\rho$ with maximum periods to negative=', rho_max)
print(r'$Max periods to negative=', pers_max)

fig, ax = plt.subplots()
plt.plot(rho_vals, avg_zmat_lteq0_per_vec)
# for the minor ticks, use no labels; default NullFormatter
minorLocator = MultipleLocator(1)
ax.xaxis.set_minor_locator(minorLocator)
plt.grid(b=True, which='major', color='0.65', linestyle='-')
plt.title(r'Values of $\rho$ and avg. first negative period', fontsize=20)
plt.xlabel(r'$\rho$ value')
plt.ylabel(r'Avg. first period for which $z_t\leq 0$')
# plt.show()
output_path = os.path.join(images_dir, 'RhoNegPer')
plt.savefig(output_path)
plt.close()
