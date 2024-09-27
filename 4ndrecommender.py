from gekko import GEKKO
m = GEKKO()

x1 = m.Var(lb=0)
x2 = m.Var(lb=0)
x3 = m.Var(lb=0)

m.Equation(5*x1 + 3*x2 + 4*x3 <= 50)
m.Equation(2*x1 + 2*x2 + 6*x3 <= 40) 
m.Equation(2*x1 + x2 + 3*x3 <= 110)

m.Maximize(1.5*x1 + 2*x2 + 3*x3)
#m.Maximize(x1 + x2 + x3)
m.solve(disp=False)
print("Value of X is", x1.value[0])
print("Value of Y is", x2.value[0])
print("Value of Z is", x3.value[0])

print(-m.options.OBJFCNVAL)