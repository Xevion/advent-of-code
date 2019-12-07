import os
import sys

class IntCodeExit(Exception):
    pass

class IntCodeStatus(Exception):
    def __init__(self, code):
        self.code = code
        return super().__init__(f"Status code '{self.code}' was raised by the Intcode Computer.")

class IntcodeComputer(object):
    def __init__(self, memory, _input=[], pointer=0, silent=True):
        self.memory = memory
        self._input = iter(_input)
        self.pointer = pointer
        self.silent = silent

        self.READ_MODES = {
            0: (self.point, self.point, self.point),
            100: (self.point, self.point, self.value),
            10: (self.point, self.value, self.point),
            110: (self.point, self.value, self.value),
            1: (self.value, self.point, self.point),
            101: (self.value, self.point, self.value),
            11: (self.value, self.value, self.point),
            111: (self.value, self.value, self.value),
        }

        self.OP_CODES = {
            1 : (self.op_add, 3),
            2 : (self.op_multiply, 3),
            3 : (self.op_input, 1),
            4 : (self.op_print, 1),
            5 : (self.op_jit, 2),
            6 : (self.op_jif, 2),
            7 : (self.op_lth, 3),
            8 : (self.op_eq, 3),
            99 : (self.op_exit, 0)
        }

    def hasNext(self):
        return self.pointer < len(self.memory)

    def next(self):
        op, params, offset = self.read(self.pointer)
        self.pointer += offset
        op(*params)
    
    def run(self):
        statuses = []
        while self.hasNext():
            try:
                self.next()
            except IntCodeStatus as s:
                statuses.append(s.code)
            except IntCodeExit:
                return statuses[-1]

    def read(self, pointer):
        code = self.memory[pointer]
        readmodes, opcode = divmod(code, 100)
        op, nargs = self.OP_CODES[opcode]
        argument_functions = self.READ_MODES[readmodes][:nargs]
        parameters = [f(ptr) for f, ptr in zip(argument_functions, range(pointer+1, pointer+4))]
        return op, parameters, nargs + 1

    def op_add(self, param1, param2, param3):
        self.memory[param3] = self.memory[param1] + self.memory[param2]

    def op_multiply(self, param1, param2, param3):
        self.memory[param3] = self.memory[param1] * self.memory[param2]

    def op_input(self, param1):
        self.memory[param1] = next(self._input)

    def op_print(self, param1):
        if not self.silent:
            print(self.memory[param1])
        raise IntCodeStatus(self.memory[param1])

    def op_exit(self):
        raise IntCodeExit()

    def op_jit(self, param1, param2):
        if self.memory[param1] != 0:
            self.pointer = self.memory[param2]

    def op_jif(self, param1, param2):
        if self.memory[param1] == 0:
            self.pointer = self.memory[param2]

    def op_lth(self, param1, param2, param3):
        self.memory[param3] = 1 if self.memory[param1] < self.memory[param2] else 0

    def op_eq(self, param1, param2, param3):
        self.memory[param3] = 1 if self.memory[param1] == self.memory[param2] else 0

    def value(self, location):
        return location
    
    def point(self, location):
        ptr = self.memory[location]
        return ptr

def day5(memory, _input, silent=True):
    computer = IntcodeComputer(memory.copy(), _input=_input, silent=silent)
    print(computer.run())

path = os.path.join(sys.path[0], '..', 'input')
data = list(map(int, open(path, 'r').read().split(',')))

day5(data, _input=[1])
day5(data, _input=[5])