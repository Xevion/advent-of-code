class ComputationFinished(Exception):
    pass

class Computer:
    def __init__(self, memory, input_=(), pointer=0):
        self.memory = memory
        self.pointer = pointer
        self.input = iter(input_)
        
        self.READ_MODES = {
            0: (self.point, self.point, self.point),
            100: (self.point, self.point, self.value),
            10: (self.point, self.value, self.point),
            110: (self.point, self.value, self.value),
            1: (self.value, self.point, self.point),
            101: (self.value, self.point, self.value),
            11: (self.value, self.value, self.point),
            111: (self.value, self.value, self.value),}
    
        self.OP_CODES = {
            1: (self.op_add, 3),
            2: (self.op_mul, 3),
            3: (self.op_input, 1),
            4: (self.op_print, 1),
            5: (self.op_jit, 2),
            6: (self.op_jif, 2),
            7: (self.op_lt, 3),
            8: (self.op_eq, 3),
            99: (self.op_exit, 0), }

    def step(self):
        op, parameters, offset = self.read_opcode(self.pointer)
        self.pointer += offset
        op(*parameters)
        
    def read_opcode(self, pointer):
        code = self.memory[pointer]
        readmodes, opcode = divmod(code, 100)
        op, nargs = self.OP_CODES[opcode]
        argument_functions = self.READ_MODES[readmodes][:nargs]
        parameters = [f(ptr) for f, ptr in zip(argument_functions, range(pointer+1, pointer+4))]
        return op, parameters, nargs + 1
        
    def op_add(self, par1, par2, par3):
        self.memory[par3] = self.memory[par1] + self.memory[par2]
        
    def op_mul(self, par1, par2, par3):
        self.memory[par3] = self.memory[par1] * self.memory[par2]
        
    def op_input(self, par1):
        self.memory[par1] = next(self.input)
        
    def op_print(self, par1):
        print(self.memory[par1])
        
    def op_exit(self,):
        raise ComputationFinished
        
    def op_jit(self, par1, par2):
        if self.memory[par1] != 0:
            self.pointer = self.memory[par2]
    
    def op_jif(self, par1, par2):
        if self.memory[par1] == 0:
            self.pointer = self.memory[par2]
    
    def op_lt(self, par1, par2, par3):
        self.memory[par3] = int(self.memory[par1] < self.memory[par2])
        
    def op_eq(self, par1, par2, par3):
        self.memory[par3] = int(self.memory[par1] == self.memory[par2])
    
    def value(self, location):
        return location
    
    def point(self, location):
        ptr = self.memory[location]
        return ptr
    
    def run(self):
        try:
            while True:
                self.step()
        except ComputationFinished:
            return


def day5(data, input_=(1,)):
    tape = list(map(int, data.split(",")))
    computer = Computer(tape, input_=input_)
    computer.run()

day5(open("F://Programming//advent-of-code//2019//day-5//input").read())
day5(open("F://Programming//advent-of-code//2019//day-5//input").read(), input_=(5,))