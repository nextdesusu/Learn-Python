import pygame as pg
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class main:
    
    def __init__(self):
        pg.init()
        pg.display.set_caption('draw') 
        self.screen = pg.display.set_mode((500, 500))
        self._clock = pg.time.Clock()
        self._done = False
        
    def make_segment(self, x1, x2, y1, y2):
        #line(Surface, color, start_pos, end_pos, width=1) 
        pg.draw.line(self.screen, BLACK, (x1, x2), (y1, y2), 1)
    
    
    def check_exit(self):
        for event in pg.event.get():
            if event.type  == pg.QUIT:
                self._done = True
                pg.quit() 
                sys.exit()
    
    def show(self):
        while not self._done:
            self.check_exit()
            self.screen.fill(WHITE)
            self.make_segment(10, 13, 44, 100)
            self._clock.tick(60)
            pg.display.flip()  

if __name__ == "__main__":
    main().show()
