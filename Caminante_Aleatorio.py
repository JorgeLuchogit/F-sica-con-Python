"""
Simulación de un caminante aleatorio en 1, 2 y 3 dimensiones.
"""

from numpy import random, array
from pandas import DataFrame
import matplotlib.pyplot as plt

#----------------------------------------------------------------
# PREELIMINARES
#----------------------------------------------------------------

# Colores para la gráfica
colores_graficas =['#DA2222','#DA9222','#D2DA22','#74DA22','#22DA90','#228BDA','#2822DA','#B422DA','#DA2283','#0E0108','#698658']

# Tamaño del paso:
lx = 1; ly = 1; lz = 1

pasos_totales = 500
caminantes = 5
promedio = 0

# Se establecen las gráficas de los casos 1D y 2D:
fig, axs = plt.subplots(2, 2)
fig.suptitle('Caminante aleatorio simple', fontsize='20')

# Se establecen las gráficas del caso 3D:
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

#----------------------------------------------------------------
# CAMINATAS ALEATORIAS
#----------------------------------------------------------------

for j in range (caminantes):

    # Preeliminares:
    paso_x = paso_y = paso_z = 0
    info_x = [0]; info_y = [0]; info_z = [0]
    info_x = [0]; info_y = [0]; info_z = [0]

    # Se generan 3 caminatas simultáneas:
    for i in range (pasos_totales):
        paso_x = paso_x + random.choice((-lx,lx))
        info_x.append(paso_x)    
    for i in range (pasos_totales):
        paso_y = paso_y + random.choice((-ly,ly))
        info_y.append(paso_y)
    for i in range (pasos_totales):
        paso_z = paso_z + random.choice((-lz,lz))
        info_z.append(paso_z)

    # Promedio de la distancia recorrida por los caminantes e 1D:
    auxiliar = array(info_x)+ array(info_y) + array(info_z)
    promedio = promedio + auxiliar

    # Gráfica 1D:
    axs[0,0].plot(info_x, alpha=0.7, color=colores_graficas[j])    
    axs[0,0].plot(info_y, alpha=0.7, color=colores_graficas[j])    
    axs[0,0].plot(info_z, alpha=0.7, color=colores_graficas[j]) 

    # Gráfica 2D:  
    axs[0,1].plot(info_x, info_y, alpha=0.7, color=colores_graficas[j+4])

    # Gráfica 3D:
    ax.plot(info_x, info_y, info_z,alpha=0.7, color=colores_graficas[j+4])

    # Se colocan las etiquetas del el inicio y el final de las caminatas:
    if j == caminantes-1:

        # 2D:
        axs[0,1].scatter(info_x[0],   info_y[0], color='r', label='Inicio' )
        axs[0,1].scatter(info_x[-1], info_y[-1], color='b', label='Final')  

        # 3D:
        ax.scatter(info_x[0], info_y[0], info_z[0], color='r', label='Inicio')
        ax.scatter(info_x[-1], info_y[-1], info_z[-1], color='b', label='Final')
    
    # Inicio y el final de las caminatas 1D:
    axs[0,1].scatter(info_x[0],   info_y[0], color='r' )
    axs[0,1].scatter(info_x[-1], info_y[-1], color='b' )

    # Inicio y el final de las caminatas 2D:
    ax.scatter(info_x[0], info_y[0], info_z[0], color='r')
    ax.scatter(info_x[-1], info_y[-1], info_z[-1], color='b')

# Estadística del promedio de la distancia (1D):
df=DataFrame(promedio/15).describe()
print('\n Estadistica de la distancia promedio (1D):\n\n', df)
prom_val=df[0]['mean']
std_val=df[0]['std']

#----------------------------------------------------------------
# GRÁFICAS
#----------------------------------------------------------------

# Estética de la gráfica 1D:
axs[0,0].axhline(prom_val+std_val, color='b', ls='--', lw=0.9, alpha=0.9, label='$\overline{x}+\sigma$')  
axs[0,0].axhline(prom_val, color='black', ls='-', lw=0.9, alpha=0.9, label= '$\overline{x}$')  
axs[0,0].axhline(prom_val-std_val, color='b', ls='--', lw=0.9, alpha=0.9, label='$\overline{x}+\sigma$')  
axs[0,0].set_xlabel('Pasos', fontsize='13')  
axs[0,0].set_ylabel('Distancia recorrida', fontsize='13')
axs[0,0].set_title(f'{caminantes*3} caminantes en 1D', fontsize='15')
axs[0,0].legend()

# Estética de la gráfica 2D:
axs[0,1].set_xlabel('Distancia en x', fontsize='13')  
axs[0,1].set_ylabel('Distancia en y', fontsize='13')
axs[0,1].set_title(f'{caminantes} caminantes 2D', fontsize='15')
axs[0,1].legend()

# Estética de la gráfica de la distancia promedio (1D):
axs[1,0].axhline(prom_val+std_val, color='g', ls='--', label='$\overline{x}+\sigma$')  
axs[1,0].axhline(prom_val, color='purple', ls='-', label= '$\overline{x}$')  
axs[1,0].axhline(prom_val-std_val, color='g', ls='--', label='$\overline{x}+\sigma$') 
axs[1,0].set_title('Desplazamiento promedio (1D)', fontsize='15')
axs[1,0].plot(promedio/15, color='brown', alpha=0.5)
axs[1,0].set_ylabel('Distancia promedio', fontsize='13')  
axs[1,0].set_xlabel('Pasos', fontsize='13')  
axs[1,0].legend()

# Hstograma del promedio de la distancia (1D):
axs[1,1].axvline(prom_val+std_val, color='g', ls='--', label='$\overline{x}+\sigma$')  
axs[1,1].axvline(prom_val, color='purple', ls='-',  label= '$\overline{x}$')  
axs[1,1].axvline(prom_val-std_val, color='g', ls='--', label='$\overline{x}+\sigma$') 
axs[1,1].set_title('Histograma desplazamiento promedio (1D)', fontsize='15')
axs[1,1].hist(promedio/15, 80, color ='brown', alpha=0.5)
axs[1,1].set_xlabel('Pasos', fontsize='15')  
axs[1,1].set_ylabel('frecuencia', fontsize='15')  
axs[1,1].legend()

# Estética de la gráfica 3D:
ax.set_xlabel('x', fontsize='15')  
ax.set_ylabel('y', fontsize='15')
ax.set_zlabel('z', fontsize='15')
ax.set_title(f'{caminantes} caminantes aleatorios en 3D', fontsize='15')
ax.legend()

plt.show()


