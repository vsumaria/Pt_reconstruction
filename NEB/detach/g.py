from ase.io import *
import numpy as np
import matplotlib.pyplot as plt

mu_co = -15.33


atoms = read('neb.traj@0')
e0 = atoms.get_potential_energy()
nC = len([atom.index for atom in atoms if atom.symbol == 'C'])
g0 = e0-nC*mu_co

traj = read('detach.traj',':')
e = np.array([atoms.get_potential_energy() for atoms in traj])
nC = np.array([len([atom.index for atom in atoms if atom.symbol == 'C']) for atoms in traj])

g = e-nC*mu_co
g = g-g0

plt.figure(figsize=(4.5,6))
plt.plot(g,'o--')
plt.ylabel('Relative Formation Energy', fontsize=12)

ax = plt.gca()

plt.xticks(range(10), ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])

#ax.get_xaxis().set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
#ax.spines['bottom'].set_visible(False)

plt.grid(axis = 'y', linestyle = '--', linewidth = 0.2)

plt.savefig('g.png', bbox_inches='tight', pad_inches=0.01)
plt.show()
