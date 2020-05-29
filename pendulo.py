"""
Simulação e animação de um pêndulo real com amortecimento devido à forças
aerodinâmicas.

A dinâmica é baseada no artigo "Real-world damping of a physical
pendulum".
http://www.fis.ita.br/labfis26/temas/oscilacao/03_apoio/artigos/artigos/07_Real-world%20damping%20of%20a%20physical%20pendulum.pdf

A simulação é feita utilizando o método de Runge-Kutta de quarta ordem com
passo constante através da função odeint biblioteca Scipy.
https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html

As figuras e animações são feitas utilizando a biblioteca Matplotlib e são
adaptadas do código de Jake Vanderplas para a animação de um pêndulo duplo.
https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/

autor: Rafael Celente ITA T-23
email: rafael.celente@ga.ita.br
"""

######################################################################################
######################################################################################
########################## DEFINIÇÃO DE PARÂMETROS ###################################
# Incialização dos elementos físicos do pendulo
estado_inicial = [60, 100]    # Estado inicial do pêndulo (theta, omega)
c1 = 0.1                    # coeficiente de arrasto linear
c2 = 0.1                    # coeficiente de arrasto quadratico
massa = 1                   # massa do pendulo em kg
l = 1                       # tamanho do pendulo em metros

######################################################################################
######################################################################################
######################################################################################


from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
import math

class Pendulum:
    """
    Classe do Pendulum

    Define os parametros físicos do pêndulo para um determinado tempo t
    init_state é [theta, omega] em graus
    """
    def __init__(self,
                 init_state = [60, 0],
                 L=1.0,  # tamanho do pendulo em m
                 M=1.0,  # massa do pendulo em kg
                 G=9.8,  # gravidade
                 C1=0.03, # coeficiente de arrasto linear
                 C2=0.03, # coeficiente de arrasto quadratico
                 origin=(0, 0)):
        self.init_state = np.asarray(init_state, dtype='float')
        self.params = (L, M, G, C1, C2)
        self.origin = origin
        self.time_elapsed = 0
        self.data = [[], [],[]]

        self.state = self.init_state * np.pi / 180.

    def get_theta(self):
        return self.state[0]
    def get_omega(self):
        return self.state[1]

    def position(self):
        """Computa a posição do pêndulo no gráfico"""
        (L,M,G, C1, C2) = self.params

        x = np.cumsum([self.origin[0], L* sin(self.state[0])])
        y = np.cumsum([self.origin[1],-L* cos(self.state[0])])
        return (x, y)

    def derivada(self, state, t):
        """
        Equação diferencial do movimento do pêndulo com arrasto linear e quadrático:

        \ddot{\theta} = -(\frac{1.5g\sin \theta}{L}) - c1\dot{theta} - c2\dot{theta}|\dot{theta}|

        Aqui nós vamos ter como input um vetor de estados de theta e theta ponto e
        retornaremos um vetor de estados de theta ponto e theta ponto ponto.
        """
        (L,M,G,C1,C2) = self.params
        self.data[0].append(self.time_elapsed)
        self.data[1].append(state[0])
        self.data[2].append(state[1])
        dydx = np.zeros_like(state)
        theta, theta_p = state

        dydx[0] = theta_p
        dydx[1] = -(1.5)*G*sin(theta)/L - C1*theta_p - C2*theta_p*abs(theta_p)

        return dydx


    def step(self, dt):
        """Executa um passo de integração e dá update no estado"""
        self.state = integrate.odeint(self.derivada, self.state, [0, dt])[1]
        self.time_elapsed += dt



pendulum = Pendulum(init_state = estado_inicial, C1 = c1, C2 = c2, M = massa, L = l)
dt = 1./30 # 30 fps

#------------------------------------------------------------
# Figuras e animação
fig = plt.figure(num=0, figsize = (12,8))
ax = plt.subplot2grid((2,2),(0,0), colspan=1, rowspan=2) # Animação
ax2 = plt.subplot2grid((2,2),(0,1))                      # Gráfico do theta
ax3 = plt.subplot2grid((2,2),(1,1))                      # Gráfico do omega

###################################
# Limites dos gráficos
ax.set_title('Animação - C1 = {} e C2 = {}'.format(c1, c1))
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)

ax2.set_title('Ângulo vs tempo')
ax2.set_ylabel('theta (rad)')
ax2.set_xlim(0,20)
ax2.set_ylim(-estado_inicial[0]*math.pi/90,estado_inicial[0]*math.pi/90)

ax3.set_title('Velocidade angular vs tempo')
ax3.set_xlabel('t (s)')
ax3.set_ylabel('omega (rad/s)')
ax3.set_xlim(0,20)
ax3.set_ylim(-10,10)

ax.grid()
ax2.grid()
ax3.grid()
###################################

line, = ax.plot([], [], '-', lw=4, color='r')
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
theta_text = ax.text(0.02, 0.90, '', transform=ax.transAxes)
omega_text = ax.text(0.02, 0.85, '', transform=ax.transAxes)

theta_line, = ax2.plot([], [], lw=2)

omega_line, = ax3.plot([],[], lw=2)

def init():
    """initialize animation"""
    theta_line.set_data([],[])
    omega_line.set_data([],[])
    line.set_data([], [])
    time_text.set_text('')
    theta_text.set_text('')
    omega_text.set_text('')
    return theta_line, omega_line, line, time_text, theta_text, omega_text

def animate(i):
    """perform animation step"""do pendulo
estado_inicial = [60, 100]    # Estado inicial do pêndulo (theta, omega)
c1 = 0.1                    # coeficiente de arrasto linear
c2 = 0.1
    global pendulum, dt
    pendulum.step(dt)

    theta_line.set_data(pendulum.data[0], pendulum.data[1])
    omega_line.set_data(pendulum.data[0], pendulum.data[2])
    line.set_data(*pendulum.position())
    time_text.set_text('Tempo = %.1f' % pendulum.time_elapsed)
    theta_text.set_text('Theta = %.3f rad' % pendulum.get_theta())
    omega_text.set_text('Omega = %.3f rad/s' % pendulum.get_omega())
    return theta_line, omega_line, line, time_text, theta_text, omega_text

# choose the interval based on dt and the time to animate one step
from time import time
t0 = time()
animate(0)
t1 = time()
interval = 1000 * dt - (t1 - t0)

ani = animation.FuncAnimation(fig, animate, frames=300,
                              interval=interval, blit=True, init_func=init)

#ani.save('animacao.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
