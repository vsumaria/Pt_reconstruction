import numpy as np
import matplotlib.pyplot as plt
from ase.io import *
from ase.neighborlist import neighbor_list, natural_cutoffs, NeighborList
import sys
from ase.constraints import FixAtoms
from ase.io.trajectory import TrajectoryWriter
import os

clean = -307.413*2

for mu_co in [-15.33]:
    
    traj = read('3ad_attached_dft.traj',':')
    traj3 = read('3ad_attached_dft.traj',':')
    correction=[]
    nc = []
    edft=[]
    traj2=[]
    
    for cnt,atoms in enumerate(traj):
        
        e = atoms.get_potential_energy()
    
        pos = atoms.get_positions()
        posz = pos[:,2]
        ndx = np.where(posz<18.5)[0]
        c = FixAtoms(ndx)
        atoms.set_constraint(c)
        
        f = atoms.get_forces()
        fmax = np.max(f)
        if fmax>1:
            print('high f '+str(cnt))
            continue
    
        atoms.set_pbc([1,1,0])
        C_ndx = [atom.index for atom in atoms if atom.symbol == 'C']
        O_ndx =[atom.index for atom in atoms if atom.symbol == 'O']
        Pt_ndx = [atom.index for atom in atoms if atom.symbol == 'Pt']
        
        nC = len(C_ndx)
        cutoff = natural_cutoffs(atoms, 1.1)
        nl = NeighborList(cutoff , self_interaction=False,  bothways=True)
        nl.update(atoms)
        O_ndx_sort=[]
        for i in C_ndx:
            indices, offsets = nl.get_neighbors(i)
            O_ndx_sort.append(np.intersect1d(indices,O_ndx))
    
        pos = atoms.get_positions()
        d_co = []
        for i,j in zip(C_ndx, O_ndx_sort):
            d = atoms.get_distance(i,j, mic=True, vector=False)
            d_co.append(d)
                
        d_co = np.array(d_co)
        deltaf = lambda df: 4.77*df-5.37
        delta = deltaf(d_co)
        c = sum(delta)

        #check for reconstruction
        indices, offsets = nl.get_neighbors(45)
        x = np.intersect1d(indices,Pt_ndx)
        if len(x)==7:
            print(cnt)
            continue
            
        correction.append(c)
        nc.append(nC)
        edft.append(e)
        traj2.append(traj3[cnt])
    
    correction = np.array(correction)
    nc = np.array(nc)
    edft = np.array(edft)
    g_dft = edft - nc*mu_co - clean + correction# - (-15.94)
    
    ylim = [np.min(g_dft)-0.05, np.min(g_dft)+1]
    
    nc_unq = np.unique(nc)
    
    os.mkdir('mu_'+str(abs(mu_co)))
    os.chdir('mu_'+str(abs(mu_co)))
    trajw = TrajectoryWriter('min_nc_'+str(abs(mu_co))+'.traj','a')
    
    for c in nc_unq:
        ndx = np.where(nc==c)[0]
        nc_ = np.take(nc,ndx)
        traj_ = np.take(traj2,ndx)
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
