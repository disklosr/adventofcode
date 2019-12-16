import queue

class IntCodeRunner:
    def __init__(self, code):
        self.code = code
        self.reset()
        

    def reset(self):
        self.memory = self.code[:] + [0 for i in range(0,500)]
        self.output = []
        self.input = queue.Queue()
        self.ins_pointer = 0
        self.relative_base = 0

    def get_param(self, param_idx):
        params_mode = self.memory[self.ins_pointer] // 100
        param_mode = (params_mode // (10 ** (param_idx - 1))) % 10

        if param_mode == 0:
            return self.memory[self.memory[self.ins_pointer + param_idx]]
        if param_mode == 1:
            return self.memory[self.ins_pointer + param_idx]
        if param_mode == 2:
            return self.memory[self.memory[self.ins_pointer + param_idx] + self.relative_base]

    def set_param(self, param_idx, value):
        params_mode = self.memory[self.ins_pointer] // 100
        param_mode = (params_mode // (10 ** (param_idx - 1))) % 10

        if param_mode == 0:
            self.memory[self.memory[self.ins_pointer + param_idx]] = value
        if param_mode == 1:
            raise Exception("Immediate param mode (0) cannot be written to")
        if param_mode == 2:
            self.memory[self.memory[self.ins_pointer + param_idx] + self.relative_base] = value

    def add(self):
        self.set_param(3, self.get_param(1) + self.get_param(2))
        self.ins_pointer += 4

    def multiply(self):
        self.set_param(3, self.get_param(1) * self.get_param(2))
        self.ins_pointer += 4

    def read_input(self):
        #print("reading input...")
        self.set_param(1, self.input.get(False))
        self.ins_pointer += 2

    def append_output(self):
        #print("outputing...")
        self.output.append(self.get_param(1))
        self.ins_pointer += 2

    def jump_if_true(self):
        if self.get_param(1) != 0:
            self.ins_pointer = self.get_param(2)
        else:
            self.ins_pointer += 3

    def jump_if_false(self):
        if self.get_param(1) == 0:
            self.ins_pointer = self.get_param(2)
        else:
            self.ins_pointer += 3

    def less_than(self):
        self.set_param(3, 1 if self.get_param(1) < self.get_param(2) else 0)
        self.ins_pointer += 4

    def adjust_relative_base(self):
        self.relative_base += self.get_param(1)
        self.ins_pointer += 2

    def equals(self):
        self.set_param(3, 1 if self.get_param(1) == self.get_param(2) else 0)
        self.ins_pointer += 4

    def run(self, inputs):
        self.ins_pointer = 0
        [self.input.put(element) for element in inputs]
        return self.execute()

    def resume(self, inputs):
        [self.input.put(element) for element in inputs]
        return self.execute2()

    def execute(self):
        while self.ins_pointer < len(self.memory):
            op_code = self.memory[self.ins_pointer] % 100
            if op_code == 1:
                self.add()
            if op_code == 2:
                self.multiply()
            if op_code == 3:
                if(self.input.qsize() == 0):
                    #print("waiting for input...")
                    return -1
                self.read_input()
            if op_code == 4:
                self.append_output()
            if op_code == 5:
                self.jump_if_true()
            if op_code == 6:
                self.jump_if_false()
            if op_code == 7:
                self.less_than()
            if op_code == 8:
                self.equals()
            if op_code == 99:
                return self.output

    def execute2(self):
        while self.ins_pointer < len(self.memory):
            op_code = self.memory[self.ins_pointer] % 100
            if op_code == 1:
                self.add()
            if op_code == 2:
                self.multiply()
            if op_code == 3:
                if(self.input.qsize() == 0):
                    return -1
                self.read_input()
            if op_code == 4:
                self.append_output()
            if op_code == 5:
                self.jump_if_true()
            if op_code == 6:
                self.jump_if_false()
            if op_code == 7:
                self.less_than()
            if op_code == 8:
                self.equals()
            if op_code == 9:
                self.adjust_relative_base()
            if op_code == 99:
                return 0