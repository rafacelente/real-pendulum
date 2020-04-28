import pendulum
import pendulum_graphics as graphics
import numpy as np


estado_inicial = np.array([np.pi/3, 0])
t = np.linspace(0., 10, 1000)
pend = pendulum.Pendulum(1, 1, 0.1, 0.1, estado_inicial)
results = pend.solve(t, (9.81,))

animation = graphics.Graphics(500, 500, t, results)
animation.show_simulation()
animation.show_graphics()
