import math

class Ship():
    def __init__(self):
        self.x, self.y, self.angle = 0.0, 0.0, 0.0
        self.codes = {
            "N" : self.shift_y,
            "E" : self.shift_x,
            "S" : lambda s: self.shift_y(-s),
            "W" : lambda s: self.shift_x(-s),
            "L" : lambda d: self.turn(d),
            "R" : lambda d: self.turn(-d),
            "F" : self.forward
        }
        
    def shift_x(self, shift): self.x += shift
    def shift_y(self, shift): self.y += shift
    def turn(self, degrees): self.angle = (self.angle + degrees) % 360.0
    
    def forward(self, shift):
        rad = math.radians(self.angle)
        self.x += shift * math.cos(rad)
        self.y += shift * math.sin(rad)
    
    def solve(self, instructions):
        for code, value in instructions: self.codes[code](value)
        return math.fabs(self.x) + math.fabs(self.y)
        
class Ship2(Ship):
    def __init__(self):
        super().__init__()
        self.way_x, self.way_y = 10.0, 1.0
        
    def shift_x(self, shift): self.way_x += shift
    def shift_y(self, shift): self.way_y += shift
    
    def turn(self, degrees):
        self.angle = (math.degrees(math.atan2(self.way_y, self.way_x)) + degrees) % 360.0
        rad = math.radians(self.angle)
        hyp = math.sqrt(self.way_x ** 2 + self.way_y ** 2)
        self.way_x = hyp * math.cos(rad)
        self.way_y = hyp * math.sin(rad)

    def forward(self, shift):
        self.x += shift * self.way_x
        self.y += shift * self.way_y

with open("input.txt", "r") as f:
    instructions = [(ln[0], int(ln[1:])) for ln in f if ln.strip() != ""]
s, s2 = Ship(), Ship2()
print(f"Pt1: {s.solve(instructions)}\nPt2: {s2.solve(instructions)}")