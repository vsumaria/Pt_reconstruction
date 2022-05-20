import sys
import os
from ase.io import *
import numpy as np
from ase.neighborlist import neighbor_list
from ase.io.trajectory import Trajectory, TrajectoryWriter
import subprocess
import matplotlib.pyplot as plt
from ase.neighborlist import neighbor_list, natural_cutoffs, NeighborList
import ast
import glob

def e_corr(atoms):
    e = atoms.get_potential_energy()
    atoms.set_pbc([1,1,0])
    nC = len([atom.index for atom in atoms if atom.symbol == 'C'])
    nPt = len([atom.index for atom in atoms if atom.symbol == 'Pt'])
    nat_cut = natural_cutoffs(atoms, mult=0.85)
    nl = NeighborList(nat_cut, self_interaction=False, bothways=True)
    nl.update(atoms)
    nld = neighbor_list('D', atoms, {('C', 'O'): 2.0})
    nld = np.array(nld)
    dvec = nld[range(nC),:]
    d_co = np.zeros([len(dvec),1])
    for i,dm in enumerate(dvec):
        d_co[i]=np.sqrt(np.sum(dm**2))
    deltaf = lambda df: 4.77*df-5.37
    delta = deltaf(d_co)
    corr = sum(delta)
    e = e+corr
    return e[0], nC, nPt

os.mkdir('plots')

mu_CO_collect = [-15.33, -15.5, -15.68]
mu_Pt = -6.059
name = glob.glob('*_dft.traj')[0]
name_ref = glob.glob('*_ref.traj')[0]

min_traj = TrajectoryWriter('minima.traj')
ref_atoms = read(name_ref,':')

for cnt_mu,mu_CO in enumerate(mu_CO_collect):

    traj = read(name,':')
    traj2 = read(name,':')
    ref_struc = ref_atoms[cnt_mu]
    e_ref, nC_ref, nPt_ref = e_corr(ref_struc)    
    nC_collect = []
    gd_collect = []
    gn_collect = []
    collect = []
    for cnt,atoms in enumerate(traj):
        ed, nC, nPt = e_corr(atoms)
        gd = (ed-nPt*mu_Pt-nC*mu_CO) - (e_ref - nPt_ref*mu_Pt - nC_ref*mu_CO)
        nC_collect.append(nC)
        gd_collect.append(gd)
        collect.append(atoms)

    ndx = np.where(gd_collect==np.min(gd_collect))[0][0]

    gmin = np.min(gd_collect)
    
    plt.plot(nC_collect,gd_collect,'_')
    plt.ylim([gmin-0.1, gmin+2])
    plt.savefig('plots/plot_'+str(abs(mu_CO))+'.png', bbox_inches='tight',pad_inches = 0)
    plt.close()
    atoms = traj2[ndx]
    min_traj.write(atoms)
    # atoms.write('minima/mu_'+str(abs(mu_CO))+'.xyz')
    # print(nC_collect[ndx])
    # print(np.min(gd_collect))

    
# nC_collect = np.array(nC_collect)
# gd_collect = np.array(gd_collect)
# gn_collect = np.array(gn_collect)
# ylim = [min(gd_collect)-0.05, min(gd_collect)+0.55]

# plt.plot(nC_collect,gd_collect,'_')
# plt.plot(nC_collect,gn_collect,'_')
# plt.legend(['DFT','NN'])
# plt.ylim(ylim)
# plt.savefig('plot_'+str(abs(mu_CO))+'.png', bbox_inches='tight',pad_inches = 0)
# plt.show()
