def get_program(file):
    with open(file) as f:
        return list(map(int, f.read().split(',')))


# def run_program(program, noun, verb):
#     program[1] = noun
#     program[2] = verb
#     pc = 0
#     opcode = program[0]
#
#     while opcode != 99:
#         opcode = int(str(program[0])[-2:])
#
#         mode1 = int(str(program[0])[-3])
#         mode2 = int(str(program[0])[-4])
#         if len(str(program[0])) < 5:
#             mode3 = 0
#         else:
#             mode3 = int(str(program[0])[-5])
#
#         if opcode == 1 or opcode == 2:
#             op1 = program[program[pc + 1]]
#             op2 = program[program[pc + 2]]
#             dest = program[pc + 3]
#             program[dest] = op1 + op2 if opcode == 1 else op1 * op2
#             pc += 4
#         elif opcode == 3:
#             op1 = program[program[pc + 1]]
#             dest = program[program[pc + 1]]
#             program[dest] = op1
#         elif opcode == 4:
#             dest = program[program[pc + 1]]
#             return program[dest]
#         elif opcode == 99:
#             break
#         else:
#             print('unknown opcode')
#             break
#     return program[0]
#
#
# def part_one():
#     return run_program([1002,4,3,4,33], 12, 2)
#
#
# def part_two(output):
#     program = get_program('day5input.txt')
#     for noun in range(100):
#         for verb in range(100):
#             if run_program(program.copy(), noun, verb) == output:
#                 return 100 * noun + verb
#     return 'not found'


# print(part_one())
# print(part_two(19690720))

program = get_program('day5input.txt')
pc = 0
code = program[0]

def get_oplist(code):
    op = list(str(code))[::-1]
    #remove leading 0 from opcode (eg, 02)
    op.remove(op[1])
    for i, v in enumerate(op):
        op[i] = int(v)
    if op[0] in [1,2] and len(op) < 4:
        return check_oplist_len(op, 4)
    elif op[0] in [3,4] and len(op) < 2:
        return check_oplist_len(op,2)
    else:
        return op

def check_oplist_len(oplist, n):
    x = n-len(oplist)
    z = [0] * x
    final = oplist + z
    return final

def pos_or_imm(program, mode, pc):
    if mode == 0:
        return program[program[pc]]
    elif mode == 1:
        return program[pc]

def get_value(program, oplist, pc, pos):
    if len(oplist) > 0:
        mode = oplist[pos]
    else:
        mode = 0
    value = pos_or_imm(program, mode, pc)
    return value

while pc < len(program):

    code = program[pc]

    if len(str(code)) > 1:
        oplist = get_oplist(code)
        opcode = oplist[0]

    else:
        oplist = []
        opcode = code

    if opcode == 1 or opcode == 2:
        op1 = get_value(program, oplist, pc+1, 1)
        op2 = get_value(program, oplist, pc+2, 2)
        dest = program[pc + 3]
        program[dest] = op1 + op2 if opcode == 1 else op1 * op2
        pc += 4
    elif opcode == 3:
        op1 = int(input('input: '))
        dest = program[pc+1]
        program[dest] = op1
        pc +=2
    elif opcode == 4:
        dest = program[pc+1]
        print(program[dest])
        pc +=2
    elif opcode == 99:
        break
    else:
        print('unknown opcode')
        break
