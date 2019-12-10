#19690720
orig = [1,95,7,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,5,23,2,13,23,27,1,10,27,31,2,6,31,35,1,9,35,39,2,10,39,43,1,43,9,47,1,47,9,51,2,10,51,55,1,55,9,59,1,59,5,63,1,63,6,67,2,6,67,71,2,10,71,75,1,75,5,79,1,9,79,83,2,83,10,87,1,87,6,91,1,13,91,95,2,10,95,99,1,99,6,103,2,13,103,107,1,107,2,111,1,111,9,0,99,2,14,0,0]
#
# # def loop(arr):
# #
# #     run = True
# #     a = 0
# #     b = 4
# #
# #     while run:
# #
# #         mini_arr = arr[a:b]
# #
# #         print(mini_arr)
# #
# #         val1 = arr[mini_arr[1]]
# #         val2 = arr[mini_arr[2]]
# #
# #         if mini_arr[0] == 1:
# #             arr[mini_arr[3]] = val1 + val2
# #             a += 4
# #             b += 4
# #         elif mini_arr[0] == 2:
# #             arr[mini_arr[3]] = val1 * val2
# #             a += 4
# #             b += 4
# #         else:
# #             run = False
# #
# #     return arr
#
# # for noun in range(100):
# #     for verb in range(100):
# #
# #         arr = orig
# #
# #         arr[2] = verb
# #         arr[1] = noun
#
# arr = orig
#
# run = True
# a = 0
# b = 4
#
# while run:
#
#     mini_arr = arr[a:b]
#
#     print(mini_arr)
#
#     val1 = arr[mini_arr[1]]
#     val2 = arr[mini_arr[2]]
#
#     if mini_arr[0] == 1:
#         arr[mini_arr[3]] = val1 + val2
#         a += 4
#         b += 4
#     elif mini_arr[0] == 2:
#         arr[mini_arr[3]] = val1 * val2
#         a += 4
#         b += 4
#     else:
#         run = False
#         a += 4
#         b += 4
#
# print(arr[0])
#
#         # if result[0] == 19690720:
#         #     print(arr)


def get_program(file):
    with open(file) as f:
        return list(map(int, f.read().split(',')))


def run_program(program, noun, verb):
    program[1] = noun
    program[2] = verb
    pc = 0
    while pc < len(program):
        opcode = program[pc]
        op1 = program[program[pc + 1]]
        op2 = program[program[pc + 2]]
        dest = program[pc + 3]
        if opcode == 1 or opcode == 2:
            program[dest] = op1 + op2 if opcode == 1 else op1 * op2
            pc += 4
        elif opcode == 99:
            break
        else:
            print('unknown opcode')
            break
    return program[0]


def part_one():
    return run_program(get_program('day2input.txt'), 12, 2)


def part_two(output):
    program = get_program('day2input.txt')
    for noun in range(100):
        for verb in range(100):
            if run_program(program.copy(), noun, verb) == output:
                return 100 * noun + verb
    return 'not found'


print(part_one())
print(part_two(19690720))


