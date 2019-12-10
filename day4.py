L = 147981
U = 691423
# c = 0
#
# # 543442 total possibilities
# # 219495 total with duplicates
#
# print(U - L)
#
# dup = []
#
# for num in range(L,U):
#     I = list(str(num))
#     if int(I[1] <= I[0]):
#         if int(I[2] <= I[1]):
#             if int(I[3] <= I[2]):
#                 if int(I[4] <= I[3]):
#                     if int(I[5] <= I[4]):
#                         c+=1
# print(c)

p1_counter, p2_counter = 0, 0
for n in range(L, U):
    ns = str(n)
    repeats = [ns.count(d) for d in set(ns)]
    if ns == ''.join(sorted(ns)) and max(repeats) >= 2:
        p1_counter += 1
        if 2 in repeats:
            p2_counter += 1 # part 2 needs a double

print(f"Part 1: {p1_counter}. Part 2: {p2_counter}")
