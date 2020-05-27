from numpy import sin
from scipy import integrate
import math


class Pendulum:
    """
    Definição da classe do Pêndulo.
    As caracterísiticas físicas do pêndulo, assim como sua dinâmica estão nessa classe.
    """

    def __init__(self, mass, length, c1, c2, initial_state):
        self.m = mass
        self.l = length
        self.c1 = c1
        self.c2 = c2
        self.state = initial_state
        self.time_elapsed = 0

    def dynamic(self, y, t, g):
        """
        Equação diferencial do movimento do pêndulo com arrasto linear e quadrático:

        \ddot{\theta} = -(\frac{1.5g\sin \theta}{L}) - c1\dot{theta} - c2\dot{theta}|\dot{theta}|

        Aqui nós vamos ter como input um vetor de estados de theta e theta ponto e
        retornaremos um vetor de estados de theta ponto e theta ponto ponto.
        """
        theta, theta_p = y

        return [theta_p, -(1.5)*g*sin(theta)/self.l - self.c1*theta_p - self.c2*theta_p*abs(theta_p)]

    def get_position(self):
        return (100*math.sin(self.state[0]), 100*math.cos(self.state[0]))

    def get_theta(self):
        return 180*self.state[0]/math.pi
    def get_omega(self):
        return self.state[1]

    def solve(self, dt,  entradas):
        self.state = integrate.odeint(self.dynamic, self.state, [0,dt], args=entradas)[1]
        self.time_elapsed += dt
