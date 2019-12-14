class IntCodeRunner:
    def __init__(self, code):
        self.code = code[:]
        self.output = []

    def get_param(self, param_idx):
        params_mode = self.code[self.ins_pointer] // 100
        param_mode = (params_mode // (10 ** (param_idx - 1))) % 10

        if param_mode == 0:
            return self.code[self.code[self.ins_pointer + param_idx]]
        if param_mode == 1:
            return self.code[self.ins_pointer + param_idx]

    def add(self):
        self.code[self.code[self.ins_pointer + 3]] = self.get_param(1) + self.get_param(2)
        self.ins_pointer += 4

    def multiply(self):
        self.code[self.code[self.ins_pointer + 3]] = self.get_param(1) * self.get_param(2)
        self.ins_pointer += 4

    def read_input(self, input):
        self.code[self.code[self.ins_pointer + 1]] = input
        self.ins_pointer += 2

    def append_output(self):
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
        self.code[self.code[self.ins_pointer + 3]] =  1 if self.get_param(1) < self.get_param(2) else 0            
        self.ins_pointer += 4

    def equals(self):
        self.code[self.code[self.ins_pointer + 3]] =  1 if self.get_param(1) == self.get_param(2) else 0            
        self.ins_pointer += 4

    def run(self, input):
        self.ins_pointer = 0
        while self.ins_pointer < len(self.code):
            op_code = self.code[self.ins_pointer] % 100
            if op_code == 1:
                self.add()
            if op_code == 2:
                self.multiply()
            if op_code == 3:
                self.read_input(input)
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