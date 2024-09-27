# 5x + 20y = 300
# ax + by = c
# x >=5
# y >= 2

sol = []
a = 5
b = 20
c = 300
for x in range((c//a) + 1):
    for y in range(c//b +1):
        if a*x + b*y - c == 0:
            if x >= 5:
                if y >= 2:
                    sol.append([x, y])

print(sol)