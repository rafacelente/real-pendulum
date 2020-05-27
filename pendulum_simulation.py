import pendulum
import pendulum_graphics as graphics
import numpy as np


dt = 1/100
estado_inicial = np.array([np.pi/3, 0])
pend = pendulum.Pendulum(1, 1, 0.1, 0.1, estado_inicial)

animation = graphics.Graphics(pend)
animation.show_animation()
#animation.show_graphics()
