"""
El método de euler se basa en la definición de la derivada dx/dt = f. Tomando h suficientemente pequeña puede omitirse el límite aunque la igualdad pasa a ser una aproximación:

                 f = dx/dt ~ [x(t+h)-x(t)]/h     si y solo si     x(t+h) ~ x(t) + fh 

La aproximación mejora conforme h es pequeña.  

Este programa se enfoca en resolver la ecuación f = m(d^2x/dt^2) mediante el método de Euler. La ecuación de segundo orden se reescribe como el sistema de primer orden:

          F = f/m = (dv/dt)              aplicando euler:          v(t+h) ~ v(t) + Fh   
                v = dx/dt                                          x(t+h) ~ x(t) + v(t)h
"""
from math import sin, pi
from pandas import DataFrame
import matplotlib.pyplot as plt


#--------------------------------------------------------------------------------------
# Definicion de f:
#--------------------------------------------------------------------------------------
# Paso
h = 0.01
# Constantes
l = 0.5
g = 9.81
beta = 0.3

# Títulos de gráficas:
titulo   = 'Péndulo'
x_titulo = '$\\theta$  [rad]'
v_titulo = '$\omega$  $\left[\\frac{rad}{s}\\right]$'

# Condiciones iniciales:
x = pi/2
v = 18

# Función de fuerza:
def F(g, l, th, w):
    return (-g/l*sin(th)-beta*w) 

# Almacenar info:
velocidad = [v];  posicion = [x];  tiempo = [0]

# Método de Euler:
for t in range (2000):

    v = v + F(g=g, l=l, th=x, w=v)*h
    x = x + v*h

    velocidad.append(v)
    posicion.append(x)
    tiempo.append((t+1)/100)

#--------------------------------------------------------------------------------------
# DISTRIBUCIÓN DE V O DE X
#--------------------------------------------------------------------------------------

frecuencia = DataFrame(velocidad)
info = frecuencia.describe()
promedio = info[0]['mean']
sigma = info[0]['std']

print(f'Estadistica de los valores de {v_titulo}\n\n', info)

#--------------------------------------------------------------------------------------
# GRÁFICAS
#--------------------------------------------------------------------------------------

# Panel 4 gráficas:
fig, axs = plt.subplots(2, 2)
fig.suptitle(titulo, fontsize='20')

# V vs. t
axs[0,0].plot(tiempo, velocidad, color='#6346af', ls='-', lw=1, alpha=0.8, label='Método de Euler')
axs[0,0].grid(linestyle='--', color='purple', alpha=0.5, lw=0.6)
axs[0,0].set_title('Velocidad vs. tiempo', fontsize='17')
axs[0,0].set_xlabel('Tiempo [s]', fontsize='15')
axs[0,0].set_ylabel(v_titulo, fontsize='15')
axs[0,0].legend()

# X vs. t:
axs[0,1].plot(tiempo, posicion, color='#6346af',ls='-', lw=1, alpha=0.8, label='Método de Euler')
axs[0,1].grid(linestyle='--', color='purple', alpha=0.5, lw=0.6)
axs[0,1].set_title('Posición vs. tiempo', fontsize='17')
axs[0,1].set_xlabel('Tiempo [s]', fontsize='15')
axs[0,1].set_ylabel(x_titulo, fontsize='15')
axs[0,1].legend()

# Espacio fase:
axs[1,0].plot(posicion, velocidad, color='#6346af',ls='-', lw=1, alpha=0.8, label='Método de Euler')
axs[1,0].grid(linestyle='--', color='purple', alpha=0.5, lw=0.6)
axs[1,0].set_title(' Espacio fase', fontsize='17')
axs[1,0].set_xlabel(x_titulo, fontsize='15')
axs[1,0].set_ylabel(v_titulo, fontsize='15')
axs[1,0].legend()

# Distribución:
axs[1,1].hist(frecuencia, 200, density=True,  color='cyan', alpha=0.8, label='ocurrencias')
axs[1,1].axvline(x=promedio, color='blue', ls='-', lw=1.1, alpha=0.8, label='promedio')
axs[1,1].axvline(x=promedio+sigma, color='red', ls='--', lw=1.1, alpha=0.8, label='$\sigma$')
axs[1,1].axvline(x=promedio-sigma, color='red', ls='--', lw=1.1, alpha=0.8)
axs[1,1].grid(linestyle='--', color='purple', alpha=0.5, lw=0.6)
axs[1,1].set_title('Dristibución de la posición', fontsize='17')
axs[1,1].set_xlabel(x_titulo, fontsize='15')
axs[1,1].set_ylabel('Frecuencia', fontsize='15')
axs[1,1].legend()

fig.tight_layout()

# Gráfica del espacio fase considerando el tiempo:
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot(posicion, velocidad, tiempo, ls='-',lw=1, alpha=0.8, label='Método de Euler')
ax.set_title(f'{titulo}\n Espacio fase en el tiempo', fontsize='20')
ax.set_xlabel(x_titulo, fontsize='18')
ax.set_ylabel(v_titulo, fontsize='18')
ax.set_zlabel('Tiempo [s]', fontsize='18')
ax.legend()

plt.show() 




    
