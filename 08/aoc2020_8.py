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
    
    def pt1(self, instructions, fetch_op=None):
        if(fetch_op is None): fetch_op = lambda i: instructions[i]
        self.reset_state()
        visited = set()
        while(self.pc != len(instructions)): 
            if(self.pc in visited): return False, self.acc
            visited.add(self.pc)
            opcode, op = fetch_op(self.pc)
            self.translation_table[opcode](op)
            self.pc += 1
        return True, self.acc
    
    def pt2(self, instructions):
        '''
        Model the problem as a digraph, where there is an edge x -> y if instruction y would be executed directly after instruction x is executed.
        Two subgraphs will be A: all vertices reachable from the initial state and B: all vertices from which the goal state (index of which is last instruction + 1).
        Once we have constructed these subgraphs, we need only find the instruction in A that when changed from jmp to nop (or vice-versa) will connect A to B.
        '''
        
        digraph = [(i + op) if (opcode == "jmp") else (i + 1) for i, (opcode, op) in enumerate(instructions)]    
        results = [(False, False) for _ in instructions]
        connected = False
            
        def traversal_B(i):
            if(i == len(instructions)): return True
            visited, reaches_end = results[i]
            if(not visited):
                results[i] = (True, reaches_end)
                reaches_end = traversal_B(digraph[i])
                results[i] = (True, reaches_end)
            return reaches_end
        
        def connect(i):
            nonlocal connected
            opcode, op = instructions[i]
            if(connected): return (opcode, op)
            if(opcode == "jmp" and results[i + 1][1]):
                connected = True
                return ("nop", op)
            elif(opcode == "nop" and results[i + op - 1][1]):
                connected = True
                return ("jmp", op)
            return (opcode, op)
        
        for i in range(1, len(instructions)): traversal_B(i)
        return self.pt1(instructions, fetch_op=connect)

with open("input.txt", 'r') as f: 
    instructions = (ln.split(" ") for ln in f)
    instructions = [(opcode.strip().lower(), int(op.strip())) for opcode, op in instructions]    
machine = MachineState()
print(f"Pt1: {machine.pt1(instructions)}\nPt2: {machine.pt2(instructions)}")