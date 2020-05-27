import matplotlib.animation as animation
import matplotlib.pyplot as plt
from math import sin, cos

class Graphics():
    """
    Define o módulo de demonstrações visuais.

    - show_simulation mostra a animação do pêndulo em movimento
    - show_graphics mostra os gráficos de angulo e velocidade angular em função do tempo.

    """
    def __init__(self, pend):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, aspect='equal', autoscale_on = False, xlim = (-2,2), ylim = (-2,2))
        self.ax.grid()
        self.line, = self.ax.plot([],[], 'o-', lw=2)
        self.time_text = self.ax.text(0.02, 0.95, '', transform=self.ax.transAxes)
        self.theta_text = self.ax.text(0.02, 0.90, '', transform=self.ax.transAxes)
        self.omega_text = self.ax.text(0.02, 0.85, '', transform=self.ax.transAxes)
        self.pendulum = pend

    def init_anim(self):
        """initialize animation"""
        self.line.set_data([], [])
        self.time_text.set_text('')
        self.theta_text.set_text('')
        self.omega_text.set_text('')
        return self.line, self.time_text, self.theta_text, self.omega_text

    def animate(self):
        self.pendulum.solve(0.01, (9.81,))

        self.line.set_data(*self.pendulum.get_position())
        self.time_text.set_text('time = %.1f' % self.pendulum.time_elapsed)
        self.theta_text.set_text('theta = %.1f' % self.pendulum.get_theta())
        self.omega_text.set_text('omega = %.1f' % self.pendulum.get_omega())

        return self.line, self.time_text, self.theta_text, self.omega_text

    def show_animation(self):
        interval = 10
        ani = animation.FuncAnimation(self.fig, Graphics.animate(self), frames=300, interval=interval, blit=True, init_func = Graphics.init_anim(self))
        plt.show()


    def show_graphics(self):
        plt.plot(self.t, self.data[:, 0], 'b', label='theta(t)')
        plt.plot(self.t, self.data[:, 1], 'g', label='omega(t)')
        plt.legend(loc='best')
        plt.xlabel('t')
        plt.grid()
        plt.show()
