import pygame
import matplotlib.pyplot as plt
from math import sin, cos

class Graphics():
    """
    Define o módulo de demonstrações visuais.

    - show_simulation mostra a animação do pêndulo em movimento
    - show_graphics mostra os gráficos de angulo e velocidade angular em função do tempo.

    """
    def __init__(self, scrx, scry, t, data):
        self.scrx = scrx # tamanho da tela em x
        self.scry = scry # tamanho da tela em y
        self.t = t       # linspace de tempo usado na simulação
        self.data = data # valores de theta e omega resultados da simulação

    def show_simulation(self, line_size = 7, line_color = (0,0,255)):
        # Iniciando o pygame e a tela inicial
        pygame.init()
        timer = pygame.time.Clock()
        screen = pygame.display.set_mode([self.scrx, self.scry])
        screen.fill((255,255,255))

        # Condições de início e fim
        running = 0
        end = len(self.t)

        # Enquanto todos os valores de tempo ainda não forem percorridos
        while running != end:
            screen.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            # Essa lei pode mudar. Padronizei o tamanho da barra em 100 pixels, mas talvez possa mudar.
            pygame.draw.line(screen, line_color, (self.scrx/2, self.scry/2), (self.scrx/2 + 100*sin(self.data[running,1]),self.scry/2 + 100*cos(self.data[running,1])), line_size)
            running += 1
            pygame.display.flip()
            timer.tick(60)

        pygame.quit()

    def show_graphics(self):
        plt.plot(self.t, self.data[:, 0], 'b', label='theta(t)')
        plt.plot(self.t, self.data[:, 1], 'g', label='omega(t)')
        plt.legend(loc='best')
        plt.xlabel('t')
        plt.grid()
        plt.show()
