import sys
import numpy as np
    
class Memory:
    
    def __init__(self, size):
        self.cells = np.zeros(size)
        self.current_cell = 0
    
    def inc(self):
        self.current_cell += 1
        
    def dec(self):
        self.current_cell -= 1
        
    def inc_current_cell(self):
        self.cells[self.current_cell] += 1
        
    def dec_current_cell(self):
        self.cells[self.current_cell] -= 1    
        
    def show_cells(self):
        print(self.cells)
        
    def show_current_cell(self):
        print(chr(int(self.cells[self.current_cell])), end = '')
        
    def getchar(self):
        self.cells[self.current_cell] = ord(int(input()))
        
    @property
    def get_current_cell(self):
        return self.cells[self.current_cell]

CELLS = Memory(30000)

Commands = {
    '>': CELLS.inc,
    '<': CELLS.dec,
    '+': CELLS.inc_current_cell,
    '-': CELLS.dec_current_cell,
    '.': CELLS.show_current_cell,
    ',': CELLS.getchar,
}
#'[': '###start_cycle###',
#']': '###break_cycle###',
   

def Parse(command_line):
    
    def execute(command):
        last = -1
        for i in range(len(command)):
            char = command[i]
            if char == '[':
                for j in range(i, len(command)):
                    if command[j] == ']':
                        last = j - 1
                        break 
                to_parse = command[i:j]
                while CELLS.get_current_cell:
                    execute(to_parse)
            elif i > last and char in Commands:
                Commands[char]()  
    
    print("------- Start -------")
    for command in command_line:
        execute(command)
    print()
    print("------- End -------")
                       
def Main():
    while True:
        user_input = input('Type a command allowed coomands: quit, execute \n')
        if user_input == 'quit':
            return
        if user_input == 'execute':
            try:
                with open(input('Type name of programm: ')) as programm:
                    Parse(programm)
            except FileNotFoundError:
                print('Programm does not exist')

if __name__ == '__main__':
    Main()
    sys.exit()