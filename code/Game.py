import pygame

from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT, ICON

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.icon = pygame.display.set_icon(ICON)
        self.title = pygame.display.set_caption('Crystal Legacy') # Altera o Título da Janela

    def run(self):
         
         while True:
            menu = Menu(self.window)
            menu.run()
        
           