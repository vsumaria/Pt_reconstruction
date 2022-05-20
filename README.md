# Uncovering the mechanisms of Pt catalyst restructuring under a pressure of gas

## Basin Hopping Data
All the structural data (trajectory files including the positions, energy and force information) used for training & validation of HDNNP and the data  generated from Basin Hopping simulations has been included also as a `NOMAD dataset`.  
https://nomad-lab.eu/prod/v1/gui/user/datasets/dataset/id/62t1IqjnRS68DFVaZ34evQ

`free_energy_plot.py` script generates Adsorption Energy vs CO Coverage plots and minima energy structures at each coverage for 450 Torr (mu_15.33), 0.5 Torr (mu_15.5) and 0.0007 Torr (mu_15.68). The minima strucutres are used to understand restructuring. 

```
.
├── 111
│   ├── 0pt
│   ├── 10pt
│   ├── 12pt
│   ├── 19pt
│   ├── 1pt
│   ├── 3pt
│   └── 7pt
├── 553
│   ├── island_extraction
│   ├── island_from_bulk
│   └── step_wandering
└── 557
    ├── island_extraction
    ├── island_from_bulk
    └── step_wandering
```

## HDNNP
```
.
├── n2p2_weights
```
Contains the files to utilize the n2p2-Neural Network Potential. The files can be used with - 
- `LAMMP` - https://compphysvienna.github.io/n2p2/interfaces/if_lammps.html
- `ASE` - https://github.com/vsumaria/ASE_N2P2

## NEB
```
.
├── detach
└── diffusion
```
Contrains the NEB trajectories and python script used to generate Fig. 5 on manuscript.
