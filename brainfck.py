import sys

class Bf:
    """
    brainfuker class
    """
    def __init__(self, mode_record=1):
        """
        initialization
        mode_record: record progress steps
        """
        self.mode_record = mode_record
        self.m = [0]
        self.steps = []
        
    def log(self):
        """
        view recorded progress steps
        """
        for st in self.steps:
            print(st[0], "\t", st[1], "\t", st[2],"\t", st[3], flush=True)

    def clear(self):
        """
        clear recorded progress steps
        """
        self.m = [0]
        self.steps = []
        
    def exe(self, code, clear=0):
        """
        execute given program code
        """
        if clear:
            self.clear()
        p = 0
        c = 0
        
        while 1:
            if code[c] in "><+-.,:;[]" and self.mode_record == 1:
                self.steps.append([c, code[c], p, self.m[:]])
                
            if code[c] == ">":
                p += 1
                if len(self.m) <= p:
                    self.m.append(0)
            elif code[c] == "<":
                p -= 1 
            elif code[c] == "+":
                self.m[p] += 1
            elif code[c] == "-":
                self.m[p] -= 1
            elif code[c] == ".":
                print(chr(self.m[p]), end="", flush=True)
            elif code[c] == ",":
                self.m[p] = ord(input())
            elif code[c] == ":":
                print(self.m[p], end="", flush=True)
            elif code[c] == ";":
                self.m[p] = int(input())
            elif code[c] == "[":
                if self.m[p] == 0:
                    k = 0
                    for i in range(c, len(code)):
                        if code[i] == "[":
                            k += 1
                        if code[i] == "]":
                            k -= 1
                        if k == 0:
                            c = i
                            break
            elif code[c] == "]":
                k = 0
                for i in range(c, -1, -1):
                    if code[i] == "]":
                        k += 1
                    if code[i] == "[":
                        k -= 1
                    if k == 0:
                        c = i-1
                        break
            
            if c < len(code)-1:
                c += 1
            else:
                break
        
def bf(code, mode_record=1, mode_viewlog=0):
    """
    execute given brainfuck program code
    mode_record: record progress steps
    mode_viewlog: 1: print recorded progress steps after program finished
                  2: return recorded progress steps after program finished
    """
    b = Bf(mode_record)
    b.exe(code)
    if mode_viewlog == 1:
        print("\n\nlog data...")
        b.log()
    elif mode_viewlog == 2:
        return b.steps

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        if len(sys.argv) < 3:
            mode_viewlog = "0"
        else:
            mode_viewlog = int(sys.argv[2])
        bf(sys.argv[1], mode_viewlog, mode_viewlog)
        print("\npress Enter to quit...")
        input()
        sys.exit()

    plus = """
    ;>
    ++++++[>+++++++<-]>+.<++++++++++.
    ;>
    [-]++++++[>++++++++++<-]>+.<++++++++++.[-]
    <<[->+<]>:
    """
    
    times = """
    ;>
    ++++++[>+++++++<-]>.<++++++++++.
    ;>
    [-]++++++[>++++++++++<-]>+.<++++++++++.[-]
    <<
    [->->+>+<<<]
    """

    fibo = """
    >++++[-<+++++++++++>]<>
    +:<.>>+:<<.>>
    [<[->>>+<<<]>[->+>+<<]>>:
    <<<<.>>>>
    [-<<+>>]<[-<<+>>]<]
    """

    b = Bf(0)
    b.exe(fibo)
    #b.exe(plus)
    #b.exe(times)
    
