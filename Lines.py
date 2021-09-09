import pygame


class X:

    def __init__(self, position_x, screen):
        self.screen = screen
        self.position_x = position_x

    # draw x
    def draw_x(self):
        # first row
        if self.position_x == 1:
            # first diagonal
            pygame.draw.line(self.screen, (255, 255, 255), (50, 50), (150, 150), 15)
            # second diagonal
            pygame.draw.line(self.screen, (255, 255, 255), (50, 150), (150, 50), 15)
        elif self.position_x == 2:
            # first diagonal
            pygame.draw.line(self.screen, (255, 255, 255), (250, 50), (350, 150), 15)
            # second diagonal
            pygame.draw.line(self.screen, (255, 255, 255), (250, 150), (350, 50), 15)
        elif self.position_x == 3:
            # first diagonal
            pygame.draw.line(self.screen, (255, 255, 255), (450, 50), (550, 150), 15)
            # second diagonal
            pygame.draw.line(self.screen, (255, 255, 255), (450, 150), (550, 50), 15)

        # second row
        elif self.position_x == 4:
            # first diagonal
            pygame.draw.line(self.screen, (255, 255, 255), (50, 250), (150, 350), 15)
            # second diagonal
            pygame.draw.line(self.screen, (255, 255, 255), (50, 350), (150, 250), 15)
        elif self.position_x == 5:
            # first diagonal
            pygame.draw.line(self.screen, (255, 255, 255), (250, 250), (350, 350), 15)
            # second diagonal
            pygame.draw.line(self.screen, (255, 255, 255), (250, 350), (350, 250), 15)
        elif self.position_x == 6:
            # first diagonal
            pygame.draw.line(self.screen, (255, 255, 255), (450, 250), (550, 350), 15)
            # second diagonal
            pygame.draw.line(self.screen, (255, 255, 255), (450, 350), (550, 250), 15)

        # third row
        elif self.position_x == 7:
            # first diagonal
            pygame.draw.line(self.screen, (255, 255, 255), (50, 450), (150, 550), 15)
            # second diagonal
            pygame.draw.line(self.screen, (255, 255, 255), (50, 550), (150, 450), 15)
        elif self.position_x == 8:
            # first diagonal
            pygame.draw.line(self.screen, (255, 255, 255), (250, 450), (350, 550), 15)
            # second diagonal
            pygame.draw.line(self.screen, (255, 255, 255), (250, 550), (350, 450), 15)
        elif self.position_x == 9:
            # first diagonal
            pygame.draw.line(self.screen, (255, 255, 255), (450, 450), (550, 550), 15)
            # second diagonal
            pygame.draw.line(self.screen, (255, 255, 255), (450, 550), (550, 450), 15)


class C:

    def __init__(self, position_c, screen):
        self.position_c = position_c
        self.screen = screen

    def draw_c(self):

        if self.position_c == 1:
            pygame.draw.circle(self.screen, (255, 255, 255), (100, 100), 50, 10)
        elif self.position_c == 2:
            pygame.draw.circle(self.screen, (255, 255, 255), (300, 100), 50, 10)
        elif self.position_c == 3:
            pygame.draw.circle(self.screen, (255, 255, 255), (500, 100), 50, 10)
        elif self.position_c == 4:
            pygame.draw.circle(self.screen, (255, 255, 255), (100, 300), 50, 10)
        elif self.position_c == 5:
            pygame.draw.circle(self.screen, (255, 255, 255), (300, 300), 50, 10)
        elif self.position_c == 6:
            pygame.draw.circle(self.screen, (255, 255, 255), (500, 300), 50, 10)
        elif self.position_c == 7:
            pygame.draw.circle(self.screen, (255, 255, 255), (100, 500), 50, 10)
        elif self.position_c == 8:
            pygame.draw.circle(self.screen, (255, 255, 255), (300, 500), 50, 10)
        elif self.position_c == 9:
            pygame.draw.circle(self.screen, (255, 255, 255), (500, 500), 50, 10)


class Line:

    def __init__(self, screen):
        self.screen = screen

    # draw board game
    def draw_lines(self):
        # horizontal line
        pygame.draw.line(self.screen, (255, 255, 255), (30, 200), (570, 200), 15)
        pygame.draw.line(self.screen, (255, 255, 255), (30, 400), (570, 400), 15)

        # vertical line
        pygame.draw.line(self.screen, (255, 255, 255), (200, 30), (200, 570), 15)
        pygame.draw.line(self.screen, (255, 255, 255), (400, 30), (400, 570), 15)
