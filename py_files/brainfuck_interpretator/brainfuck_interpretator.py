from numpy import zeros
import sys

MAIN_P = 'Hello_world_with_cycle.bf'

def Execute(command_line):
    print("------- Start -------")    
    memory = zeros(30000)
    j = 0
    brc = 0
    command_line = command_line.read()
    for i in range(len(command_line)):
        if command_line[i] == '>':
            j += 1
        if command_line[i] == '<':
            j -= 1
        if command_line[i] == '+':
            memory[j] += 1
        if command_line[i] == '-':
            memory[j] -= 1
        if command_line[i] == '.':
            print(chr(int(memory[j])), end = '')
        if command_line[i] == ',':
            memory[j] = ord(int(input()))
        if command_line[i] == '[':
            if not memory[j]:
                brc += 1
                while brc:
                    i += 1
                    if command_line[i] == '[':
                        brc += 1
                    if command_line[i] == ']':
                        brc -= 1
                else:
                    continue
            elif command_line[i] == ']':
                if not memory[j]:
                    continue
                else:
                    if command_line[i] == ']':
                        brc += 1
                    while brc:
                        i -= 1
                        if command_line[i] == '[':
                            brc -= 1
                        if command_line[i] == ']':
                            brc += 1
                i -= 1
                
    print()
    print("------- End -------")
                       
def Main():
    with open(MAIN_P) as commands:
        Execute(commands)    
    '''
    while True:
        user_input = input('Type a command allowed coomands: quit, execute \n')
        if user_input == 'quit':
            return
        if user_input == 'execute':
            try:
                with open(input('Type name of programm: ')) as commands:
                    Execute(Concat(commands))
            except FileNotFoundError:
                print('Programm does not exist')
    '''

if __name__ == '__main__':
    Main()
    sys.exit()