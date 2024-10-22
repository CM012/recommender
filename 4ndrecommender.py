from gekko import GEKKO
import sys
import argparse
import math

m = GEKKO()

parser = argparse.ArgumentParser(description='The differences in intakes')
parser.add_argument('f', type=float, help='Difference in the targeted fat intake') #Fat
parser.add_argument('p', type=float, help='Difference in the targeted protein intake') #Protein
parser.add_argument('c', type=float, help='Difference in the targeted carb intake') #Carbon
parser.add_argument('-m', type=float, help='List of the margin') #margin
parser.add_argument('-pf', type=int, nargs='+', help='List of the preference weight') #preference_weight
args = parser.parse_args()
#option = parser.parse_args()
print(args.m)
print(args.pf)



#What nutrition we need
#eg 100 40 50
fat = args.f
protein = args.p
carb = args.c

#margin= [5, 10, 20] #three stages
margin= args.m
#preference_weight=[0, 1]
preference_weight= args.pf

#Nutrition facts [carbon, protein, fat]
sweetpotato_nu = [20, 1.45, 0]
redlentils_nu = [20.1, 9.02, 0.38]
avocado_nu = [9, 2, 15]

sweetpotato = m.Var(lb=0) #x1
redlentils = m.Var(lb=0) #x2
avocado = m.Var(lb=0) #x3

m.Equation(sweetpotato_nu[0]*sweetpotato + redlentils_nu[0]*redlentils + avocado_nu[0]*avocado <= carb + margin)
m.Equation(sweetpotato_nu[0]*sweetpotato + redlentils_nu[0]*redlentils + avocado_nu[0]*avocado >= carb - margin) 
m.Equation(sweetpotato_nu[1]*sweetpotato + redlentils_nu[1]*redlentils + avocado_nu[1]*avocado <= protein + margin)
m.Equation(sweetpotato_nu[1]*sweetpotato + redlentils_nu[1]*redlentils + avocado_nu[1]*avocado >= protein - margin)
m.Equation(sweetpotato_nu[2]*sweetpotato + redlentils_nu[2]*redlentils + avocado_nu[2]*avocado <= fat + margin)
m.Equation(sweetpotato_nu[2]*sweetpotato + redlentils_nu[2]*redlentils + avocado_nu[2]*avocado >= fat - margin)

m.Maximize(preference_weight[1]*sweetpotato + preference_weight[0]*redlentils + preference_weight[1]*avocado)
#m.Maximize(x1 + x2 + x3)
m.solve(disp=False)
#m.solve()
print("Value of sweetpotato is", sweetpotato.value[0])
print("Value of redlentils is", redlentils.value[0])
print("Value of avocado is", avocado.value[0])

print(-m.options.OBJFCNVAL)