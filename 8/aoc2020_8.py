with open("input.txt", 'r') as f: 
    instructions = (ln.split(" ") for ln in f)
    instructions = [(opcode.strip().lower(), int(op.strip())) for opcode, op in instructions]

class MachineState():

    def __init__(self): 
        self.acc, self.pc = 0, 0
        self.translation_table = {
            "acc" : self.accumulate,
            "jmp" : self.jump,
            "nop" : self.no_op
        }
        
    def reset_state(self): self.__init__()
    def accumulate(self, op): self.acc += op 
    def jump(self, op): self.pc += (op - 1)
    def no_op(self, op): pass
    
    def run_machine(self, instructions):
        self.reset_state()
        while(self.pc != len(instructions)):
            opcode, op = instructions[self.pc]
            self.translation_table[opcode](op)
            self.pc += 1
        return self.acc
    
    def pt1(self):
        self.reset_state()
        visited = set()
        while(True): 
            if(self.pc in visited): return self.acc
            visited.add(self.pc)
            opcode, op = instructions[self.pc]
            self.translation_table[opcode](op)
            self.pc += 1
    
    '''Model the problem as a digraph, where there is an edge x -> y if instruction y would be executed directly after instruction x is executed.
    Two subgraphs will be A: all vertices reachable from the initial state and B: all vertices from which the goal state (index of which is last instruction + 1).
    Once we have constructed these subgraphs, we need only find the instruction in A that when changed from jmp to nop (or vice-versa) will connect A to B.
    '''
    def pt2(self):
    
        def destination(x):
            i, (opcode, op) = x
            if(opcode == "jmp"): return i + op
            else: return i + 1
        digraph = [destination(x) for x in enumerate(instructions)]
        
        results = [(False, False, False) for _ in instructions]
        
        def traversal_a(i):
            visited, _, _ = results[i]
            if(visited): return
            results[i] = (True, True, False)
            traversal_a(digraph[i])
            
        def traversal_b(i):
            if(i == len(instructions)): return True
            visited, start_reaches, reaches_end = results[i]
            if(visited):
                results[i] = (True, start_reaches, reaches_end)
                return reaches_end
            results[i][0] = True
            reaches_end = traversal_b(digraph[i])
            results[i] = True, start_reaches, reaches_end
            return reaches_end
            
        traversal_a(0)
        for i in range(1, len(instructions)): traversal_b(i)
        
        def connects(i):
            if(not results[i][1]): return False
            opcode, op = instructions[i]
            if(opcode == "jmp"): return results[i + 1][2]
            elif(opcode == "nop"): return results[i + op - 1][2]
            return False
            
        def new_instructions(i):
            opcode, op = instructions[i]
            if(opcode == "jmp"):
                instructions[i] = ("nop", op)
                acc = self.run_machine(instructions)
                instructions[i] = ("jmp", op)
                return acc
            elif(opcode == "nop"):
                instructions[i] = ("jmp", op)
                acc = self.run_machine(instructions)
                instructions[i] = ("nop", op)
                return acc
            return -1
        
        return [new_instructions(i) for i, _ in enumerate(instructions) if connects(i)]
    
machine = MachineState()
print("pt1: {}\npt2: {}".format(machine.pt1(), machine.pt2()))