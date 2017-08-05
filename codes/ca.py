import pygame, sys, random
from pygame.locals import *

Cells = {}
HEIGHT = 600
WIDTH = 600

class classCell:
    
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.w = 10
        self.h = 10
        self.Lneigh = 0
        self.Dneigh = 0
        self.state = state

    def getState(self):
        return self.state
    
    def AddNeigh(self, state):
        if state == 1:
            self.Lneigh += 1
        elif state == 0:
            self.Lneigh += 0
            
    def getNeigh(self):
        return self.Lneigh
    
    def Draw(self, surf):
        if self.state == 0:
            self.col = (255, 255, 255)
        elif self.state == 1:
            self.col = (0, 0, 0)
        pygame.draw.rect(surf, self.col, (self.x * self.w, self.y * self.h, self.w, self.h), 0)

def UpdateNeighs():
    x = 0
    y = 0
    for y in range(0, (HEIGHT / 10)):
        for x in range(0, (WIDTH / 10)):
            Cells[x, y].Lneigh = 0 
            if y - 1 > -1 and x - 1 > -1 and x + 1 < 40 and y + 1 < 40:
                Cells[x, y].AddNeigh(Cells[(x - 1), (y - 1)].state)   #Top Left
                Cells[x, y].AddNeigh(Cells[(x), (y - 1)].state)       #Top
                Cells[x, y].AddNeigh(Cells[(x + 1), (y - 1)].state)   #Top Right
                Cells[x, y].AddNeigh(Cells[(x - 1), (y + 1)].state)   #Bottom Left
                Cells[x, y].AddNeigh(Cells[(x), (y + 1)].state)       #Bottom
                Cells[x, y].AddNeigh(Cells[(x + 1), (y + 1)].state)   #Bottom Right
                Cells[x, y].AddNeigh(Cells[(x - 1), (y)].state)       #Left
                Cells[x, y].AddNeigh(Cells[(x + 1), (y)].state)       #Right

def UpdateStates():
    """ the logic of the game """
    x = 0
    y = 0
    for y in range(0, (HEIGHT / 10)):
        for x in range(0, (WIDTH / 10)):

            if Cells[x, y].Lneigh != 2 and Cells[x, y].Lneigh != 3:    # Under/Over populated
                Cells[x, y].state = 0
            elif Cells[x, y].Lneigh == 2 and Cells[x, y].Lneigh == 3:  #Lives to next cycle
                Cells[x, y].state = 1
            elif Cells[x, y].state == 0 and Cells[x, y].Lneigh == 3:  #Dead cell comes to life
                print ("a new cell is born")
                Cells[x, y].state = 1

class Cursor:
    
    def __init__(self, x, y, w, h, col):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = col
    
    def Move(self, x, y):
        self.x = x
        self.y = y
    
    def Draw(self, surf):
        pygame.draw.rect(surf, self.col, (self.x * self.w, self.y * self.h, self.w, self.h), 1)
        
def drawGrid(surf, size):
    surf.fill((255, 255, 255))
    x = 0
    y = 0
    for y in range(0, (HEIGHT / size)):
        for x in range(0, (WIDTH / size)):
            Cells[x, y] = classCell(x, y, 0)
            pygame.draw.line(surf, (230, 230, 230), (x * size, 0), (x * size, HEIGHT))
            pygame.draw.line(surf, (230, 230, 230), (0, y * size), (WIDTH, y * size))

def main():
    pygame.init()
    clock=pygame.time.Clock()
    clock.tick(20) # 20 frames per second
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Cellular Automata Simulation')
    grid = pygame.surface.Surface((WIDTH, HEIGHT))
    surf_buf = pygame.surface.Surface((WIDTH, HEIGHT))

    CursRect = Cursor(0, 0, 10, 10, (255, 0, 0))
    drawGrid(grid, 10)
    Cycle = 0
    mouse_state = False
    continous = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                # exiting ..
                pygame.quit()
                sys.exit()
                return
            
            elif event.type == MOUSEMOTION:
                mx, my = pygame.mouse.get_pos()
                mx = (mx / 10)
                my = (my / 10)
                CursRect.Move(mx, my)
                if mouse_state:
                    Cells[mx, my].state = 1
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print ("Cell %i, %i = 1" % (mx, my))
                    Cells[mx, my].state = 1
                elif event.button == 1:
                    print Cells[mx, my].Lneigh
                    
                mouse_state = not mouse_state
                    
            elif event.type == pygame.KEYUP:
                # pressing TAB clears the world
                if event.key == K_TAB:
                    print ("tab pressed!, display grid goes forward for one Cycle!")
                    Cycle = Cycle + 1
                    print "Cycle ", Cycle
                    UpdateNeighs()
                    UpdateStates()
                    continous = False
                if event.key == K_RETURN:
                    continous = not continous
                
            if continous:
                UpdateNeighs()
                UpdateStates()
        x = 0
        y = 0
        for y in range(0, (HEIGHT / 10)):
            for x in range(0, (WIDTH / 10)):
                Cells[x, y].Draw(screen)

        CursRect.Draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main() 
