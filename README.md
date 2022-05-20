# Uncovering the mechanisms of Pt catalyst restructuring under a pressure of gas

# Structural Data
All the structural data (trajectory files including the positions, energy and force information) used for training & validation of HDNNP and the data  generated from Basin Hopping simulations has been included in the NOMAD dataset.  
https://nomad-lab.eu/prod/v1/gui/user/datasets/dataset/id/62t1IqjnRS68DFVaZ34evQ

Data strucuture:
```
.
├── HDNNP
│   ├── train
│   │   └── TRAIN.traj
│   └── valid
│       └── VALIDATION.traj
└── basin_hopping_data
    ├── 111
    │   ├── 0pt
    │   │   └── 0pt_dft.traj
    │   ├── 10pt
    │   │   ├── 10ad_ref.traj
    │   │   └── 10pt_dft.traj
    │   ├── 12pt
    │   │   ├── 12ad_ref.traj
    │   │   └── 12pt_dft.traj
    │   ├── 19pt
    │   │   ├── 19ad_ref.traj
    │   │   └── 19pt_dft.traj
    │   ├── 1pt
    │   │   ├── 1ad_ref.traj
    │   │   └── 1pt_dft.traj
    │   ├── 3pt
    │   │   ├── 1ad_ref.traj
    │   │   └── 3pt_dft.traj
    │   ├── 7pt
    │   │   ├── 7ad_ref.traj
    │   │   └── 7pt_dft.traj
    │   └── clean_surf
    │       └── clean_111_island_surf.traj
    ├── 553
    │   ├── clean_surf
    │   │   └── clean_553.traj
    │   ├── island_extraction
    │   │   ├── 1ad
    │   │   │   └── 1ad_kink_dft.traj
    │   │   ├── 2ad
    │   │   │   └── 2ad_kink_dft.traj
    │   │   └── 3ad
    │   │       └── 3ad_kink_dft.traj
    │   ├── island_from_bulk
    │   │   ├── 1ad
    │   │   │   └── 1ad_NR_dft.traj
    │   │   ├── 2ad
    │   │   │   └── 2ad_NR_dft.traj
    │   │   └── 3ad
    │   │       └── 3ad_NR_dft.traj
    │   └── step_wandering
    │       ├── 0ad
    │       │   └── 0ad_attached_dft.traj
    │       ├── 1ad
    │       │   └── 1ad_attached_dft.traj
    │       ├── 2ad
    │       │   └── 2ad_attached_dft.traj
    │       └── 3ad
    │           └── 3ad_attached_dft.traj
    └── 557
        ├── clean_surf
        │   └── clean_557.traj
        ├── island_extraction
        │   ├── 1ad
        │   │   └── 1ad_kink_dft.traj
        │   ├── 2ad
        │   │   └── 2ad_kink_dft.traj
        │   └── 3ad
        │       └── 3ad_kink_dft.traj
        ├── island_from_bulk
        │   ├── 1ad
        │   │   └── 1ad_NR_dft.traj
        │   ├── 2ad
        │   │   └── 2ad_NR_dft.traj
        │   └── 3ad
        │       └── 3ad_NR_dft.traj
        └── step_wandering
            ├── 0ad
            │   └── 0ad_attached_dft.traj
            ├── 1ad
            │   └── 1ad_attached_dft.traj
            ├── 2ad
            │   └── 2ad_attached_dft.traj
            └── 3ad
                └── 3ad_attached_dft.traj
 ```
 
