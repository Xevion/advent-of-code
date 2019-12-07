import os
import sys

PATH = os.path.join(sys.path[0], '..', 'input')
memory = list(open(PATH, 'r').read().split(','))

def getParams(pos, opcode, type1, type2, type3):
    params = []
    if opcode in ['03', '04']:
        params.append(memory[pos + 1])
        # if type1 == '0':
            # params[-1] = memory[int(params[-1])]
    elif opcode in ['01', '02']:
        params.append(memory[pos + 1])
        if type1 == '0':
            params[-1] = memory[int(params[-1])]
        params.append(memory[pos + 2])
        if type2 == '0':
            params[-1] = memory[int(params[-1])]
        params.append(memory[pos + 3])
        # if type3 == '0':
            # params[-1] = memory[int(params[-1])]
        # print(memory[pos:pos+4])
    elif opcode in ['99']:
        pass
    return params

inputs = [1]
pos = 0

while pos < len(memory) - 4:
    if len(memory[pos]) < 5:
        memory[pos] = ('0' * (5 - len(memory[pos]))) + memory[pos]
    opcode = memory[pos][-2:]

    type1 = memory[pos][-3]
    type2 = memory[pos][-4]
    type3 = memory[pos][-5]

    params = getParams(pos, opcode, type1, type2, type3)
    if opcode == '01':
        memory[int(params[2])] = str(int(params[0]) + int(params[1]))
        pos += 4
    elif opcode == '02':
        memory[int(params[2])] = str(int(params[0]) * int(params[1]))
        pos += 4
    elif opcode == '03':
        memory[int(params[0])] = str(inputs.pop(0))
        pos += 2
    elif opcode == '04':
        print(f'OUTPUT: {params[0]}')
        pos += 2
    elif opcode == '99':
        print('PROGRAM BREAK')
        pos += 1
        break
    else:
        print(f'Unknown Opcode "{opcode}"')
        break
    print(f'#{pos // 4} {type3}{type2}{type1}{opcode} {params}')