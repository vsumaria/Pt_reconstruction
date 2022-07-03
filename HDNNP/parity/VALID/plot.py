import numpy as np
import matplotlib.pyplot as plt

data_e = np.genfromtxt('energy.comp', skip_header=15)
natoms = data_e[:,1]
edft = data_e[:,2]
enn = data_e[:,3]
edft = edft/natoms
enn = enn/natoms
ee = abs(edft-enn)*1000
e_rmse = np.sqrt(np.mean(ee**2))
e_all = np.concatenate((edft,enn))
e_min = np.min(np.min(e_all))
e_max = np.max(np.max(e_all))
xx = [e_min,e_max]
x_text = np.mean(xx)-0.05*(e_max-e_min)
y_text = np.mean(xx)-0.3*(e_max-e_min)

plt.figure(figsize=(10,7.5))
plt.subplot(1, 2, 1)
plt.plot(edft,enn,'o', color='#1f77b4')
plt.plot(xx,xx,'--')
plt.text(x_text,y_text,'RMSE(V) = %.02f meV/atom'% (e_rmse))
plt.xlabel('$E_{DFT}$ eV/atom')
plt.ylabel('$E_{NN}$ eV/atom')

data_f = np.genfromtxt('forces.comp', skip_header=15)
fdft = data_f[:,2]
fnn = data_f[:,3]

fe = abs(fdft-fnn)
f_rmse = np.sqrt(np.mean(fe**2))

f_all = np.concatenate((fdft,fnn))
f_min = np.min(np.min(f_all))
f_max = np.max(np.max(f_all))
xx = [f_min,f_max]
x_text = np.mean(xx)-0.05*(f_max-f_min)
y_text = np.mean(xx)-0.3*(f_max-f_min)

plt.subplot(1, 2, 2)
plt.plot(fdft,fnn,'o', color='#1f77b4')
plt.plot(xx,xx,'--')
plt.text(x_text,y_text,'RMSE(V) = %.02f eV/$\AA$'% (f_rmse))
plt.xlabel('$F_{DFT}$ eV/$\AA$')
plt.ylabel('$F_{NN}$ eV/$\AA$')

plt.savefig('parity.png')
plt.show()
