import numpy as np
import matplotlib.pyplot as plt
from ase.io import *
from ase.neighborlist import neighbor_list, natural_cutoffs, NeighborList
import sys
from ase.constraints import FixAtoms
from ase.io.trajectory import TrajectoryWriter
import os
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

name = glob.glob('*.traj')[0]

clean = -803.01

for mu_co in [-15.33, -15.5, -15.68]:
    
    traj = read(name,':')
    nc = []
    edft=[]
    
    for cnt,atoms in enumerate(traj):
        e, nC, nP = e_corr(atoms)             
        nc.append(nC)
        edft.append(e)
    
    nc = np.array(nc)
    edft = np.array(edft)
    g_dft = edft - nc*mu_co - clean
    
    ylim = [np.min(g_dft)-0.05, np.min(g_dft)+1]
    
    nc_unq = np.unique(nc)
    
    os.mkdir('mu_'+str(abs(mu_co)))
    os.chdir('mu_'+str(abs(mu_co)))

    trajw = TrajectoryWriter('min_nc_'+str(abs(mu_co))+'.traj','a')
    
    for c in nc_unq:
        ndx = np.where(nc==c)[0]
        nc_ = np.take(nc,ndx)
        traj_ = np.take(traj,ndx)
        g_ = np.take(g_dft,ndx)
        ndx_min = np.where(g_==np.min(g_))[0][0]
        atoms = traj_[ndx_min]
        trajw.write(atoms)
    
    
    plt.plot(nc, g_dft, '_', markersize=15)
    plt.legend(['DFT', 'NN'])
    
    plt.xlabel('$n_C$')
    plt.ylabel('$G_{ads}^{rel}$')
    
    plt.savefig('plot_'+str(abs(mu_co))+'.png', bbox_inches='tight',pad_inches = 0)
    # plt.show()
    plt.close()
    os.chdir('../')
