def param(mode, pr, arg):
    if mode == 0:
        return pr[arg]
    elif mode == 1:
        return arg

def is_new_instruction(instr):
    length = len(instr)
    if not (instr[length - 1] in ["1", "2", "5", "6", "7", "8"]):
        return False
    if length >= 3 and instr[length - 2] != "0":
        return False
    for i in range(0, length - 2):
        if not (instr[i] == "0" or instr[i] == "1"):
            return False
    return True

def normalize(instr):
    length = len(instr)
    if length == 1:
        return "0000" + instr
    if length == 2:
        return "000" + instr
    elif length == 3:
        return "00" + instr
    elif length == 4:
        return "0" + instr

def compute(pr, input):
    output = []
    i = 0
    while i < len(pr):
        n = pr[i]
        instr = str(n)
        if is_new_instruction(instr):
            instr = normalize(instr)
            opcode = int(instr[-2:])
            m1 = int(instr[2])
            m2 = int(instr[1])

            if opcode == 1:
                p1 = param(m1, pr, pr[i + 1])
                p2 = param(m2, pr, pr[i + 2])
                pr[pr[i + 3]] = p1 + p2
                i = i + 4
            elif opcode == 2:
                p1 = param(m1, pr, pr[i + 1])
                p2 = param(m2, pr, pr[i + 2])
                pr[pr[i + 3]] = p1 * p2
                i = i + 4
            elif opcode == 5:
                p1 = param(m1, pr, pr[i + 1])
                p2 = param(m2, pr, pr[i + 2])
                if p1 != 0:
                    i = p2
                else:
                    i = i + 3
            elif opcode == 6:
                p1 = param(m1, pr, pr[i + 1])
                p2 = param(m2, pr, pr[i + 2])
                if p1 == 0:
                    i = p2
                else:
                    i = i + 3
            elif opcode == 7:
                p1 = param(m1, pr, pr[i + 1])
                p2 = param(m2, pr, pr[i + 2])
                if p1 < p2:
                    pr[pr[i + 3]] = 1
                else:
                    pr[pr[i + 3]] = 0
                i = i + 4
            elif opcode == 8:
                p1 = param(m1, pr, pr[i + 1])
                p2 = param(m2, pr, pr[i + 2])
                if p1 == p2:
                    pr[pr[i + 3]] = 1
                else:
                    pr[pr[i + 3]] = 0
                i = i + 4
        elif n == 3:
            pr[pr[i + 1]] = input
            i = i + 2
        elif n == 4:
            output.append(pr[pr[i + 1]])
            i = i + 2
        elif n == 99:
            break
        else:
            i = i + 1
    return output

# part 1
assert(is_new_instruction("01") == True)
assert(is_new_instruction("02") == True)
assert(is_new_instruction("102") == True)
assert(is_new_instruction("101") == True)
assert(is_new_instruction("1101") == True)
assert(is_new_instruction("10102") == True)
assert(is_new_instruction("202") == False)
assert(is_new_instruction("-1786") == False)

p = [3,0,4,0,99]
compute(p, 1)
assert(p == [1,0,4,0,99])

p = [1002,4,3,4,33]
compute(p, 1)
assert(p == [1002,4,3,4,99])

print("Part 1:")
print(compute([3,225,1,225,6,6,1100,1,238,225,104,0,1102,46,47,225,2,122,130,224,101,-1998,224,224,4,224,1002,223,8,223,1001,224,6,224,1,224,223,223,1102,61,51,225,102,32,92,224,101,-800,224,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1101,61,64,225,1001,118,25,224,101,-106,224,224,4,224,1002,223,8,223,101,1,224,224,1,224,223,223,1102,33,25,225,1102,73,67,224,101,-4891,224,224,4,224,1002,223,8,223,1001,224,4,224,1,224,223,223,1101,14,81,225,1102,17,74,225,1102,52,67,225,1101,94,27,225,101,71,39,224,101,-132,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1002,14,38,224,101,-1786,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1,65,126,224,1001,224,-128,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1101,81,40,224,1001,224,-121,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,344,101,1,223,223,1107,677,677,224,102,2,223,223,1005,224,359,1001,223,1,223,1108,226,226,224,1002,223,2,223,1006,224,374,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,389,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,419,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,434,1001,223,1,223,108,226,677,224,102,2,223,223,1006,224,449,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,464,1001,223,1,223,1007,677,226,224,1002,223,2,223,1006,224,479,1001,223,1,223,1007,677,677,224,1002,223,2,223,1005,224,494,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,524,1001,223,1,223,7,226,226,224,102,2,223,223,1005,224,539,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,554,101,1,223,223,107,677,226,224,102,2,223,223,1006,224,569,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,584,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,614,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,629,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226], 1))

# part 2
assert(compute([3,9,8,9,10,9,4,9,99,-1,8], 8) == [1])
assert(compute([3,9,8,9,10,9,4,9,99,-1,8], 123) == [0])

assert(compute([3,9,7,9,10,9,4,9,99,-1,8], 5) == [1])
assert(compute([3,9,7,9,10,9,4,9,99,-1,8], 123) == [0])

assert(compute([3,3,1108,-1,8,3,4,3,99], 8) == [1])
assert(compute([3,3,1108,-1,8,3,4,3,99], 123) == [0])

assert(compute([3,3,1107,-1,8,3,4,3,99], 5) == [1])
assert(compute([3,3,1107,-1,8,3,4,3,99], 123) == [0])

assert(compute([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 0) == [0])
assert(compute([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 1) == [1])

assert(compute([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 0) == [0])
assert(compute([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 1) == [1])

#assert(compute([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], 6) == [999])
assert(compute([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], 8) == [1000])
assert(compute([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], 9) == [1001])

print("Part 2:")
print(compute([3,225,1,225,6,6,1100,1,238,225,104,0,1102,46,47,225,2,122,130,224,101,-1998,224,224,4,224,1002,223,8,223,1001,224,6,224,1,224,223,223,1102,61,51,225,102,32,92,224,101,-800,224,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1101,61,64,225,1001,118,25,224,101,-106,224,224,4,224,1002,223,8,223,101,1,224,224,1,224,223,223,1102,33,25,225,1102,73,67,224,101,-4891,224,224,4,224,1002,223,8,223,1001,224,4,224,1,224,223,223,1101,14,81,225,1102,17,74,225,1102,52,67,225,1101,94,27,225,101,71,39,224,101,-132,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1002,14,38,224,101,-1786,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1,65,126,224,1001,224,-128,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1101,81,40,224,1001,224,-121,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,344,101,1,223,223,1107,677,677,224,102,2,223,223,1005,224,359,1001,223,1,223,1108,226,226,224,1002,223,2,223,1006,224,374,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,389,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,419,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,434,1001,223,1,223,108,226,677,224,102,2,223,223,1006,224,449,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,464,1001,223,1,223,1007,677,226,224,1002,223,2,223,1006,224,479,1001,223,1,223,1007,677,677,224,1002,223,2,223,1005,224,494,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,524,1001,223,1,223,7,226,226,224,102,2,223,223,1005,224,539,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,554,101,1,223,223,107,677,226,224,102,2,223,223,1006,224,569,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,584,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,614,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,629,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226], 5))