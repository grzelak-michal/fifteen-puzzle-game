import sys, pygame
from board import Board
import copy

TILESIZE = 50
FPS = 30
WINDOWWIDTH = 800
WINDOWHEIGHT = 800
TEXTPOS = (20, 20)
XOFFSET = 100
YOFFSET = 100

#                 R    G    B
BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
GREEN =         (  0, 204,   0)
RED =           (204,   0,   0)

class Game(object):
    def __init__(self, board: Board, initial_board):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        self.timer = pygame.time.Clock()
        self.board = copy.deepcopy(board)
        self.board.board = initial_board
        self.font = pygame.font.SysFont('Arial', 20)
        self.current_state = 0
        self.frame_color = RED
        self.draw()
    
    def draw(self):
        self.screen.fill((0,0,0))

        for y in range(len(self.board.board)):
            for x in range(len(self.board.board[y])):
                if self.board.board[y][x] == 0:
                    continue
                rect = pygame.draw.rect(self.screen, WHITE, (XOFFSET + x * TILESIZE + x * 2, YOFFSET + y * 2 + y * TILESIZE, TILESIZE, TILESIZE))
                self.screen.blit(self.font.render('{}'.format(self.board.board[y][x]), True, BLACK), (rect.left + TILESIZE/ 2, rect.top  + TILESIZE / 2))
        

        
        if self.current_state == len(self.board.move_history):
            self.frame_color = GREEN
        else:
            self.frame_color = RED

        shape = self.board.board.shape
        pygame.draw.rect(self.screen, self.frame_color, (XOFFSET, YOFFSET, shape[0] * TILESIZE + shape[0] * 2, shape[1] * TILESIZE + shape[1] * 2), 10)

        self.screen.blit(self.font.render("LEFT CLICK: move forward, RIGHT CLICK: move backward", True, WHITE), TEXTPOS)

    def update(self):
        self.draw()
    
    def move(self):
        if self.current_state < len(self.board.move_history):
            self.board.move(self.board.move_history[self.current_state], False)
            self.current_state += 1
            self.update()
    
    def undo_move(self):
        if self.current_state > 0:
            self.current_state -= 1
            self.board.move(self.get_opposite_move(self.board.move_history[self.current_state]), False)
            self.update()
    
    def get_opposite_move(self, direction):
        return {
            'L': 'R',
            'R': 'L',
            'U': 'D',
            'D': 'U'
        }[direction]
        
    def show(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.MOUSEBUTTONUP: 
                    if event.button == 1: self.move()
                    if event.button == 3: self.undo_move()
            
            pygame.display.update()
            self.timer.tick(FPS)
