import numpy as np 
from scipy.optimize import minimize
import argparse

parser = argparse.ArgumentParser(description='The differences in intakes')
parser.add_argument('-c', '-carbon', type=float, default=100, help='Current carb intake') #Carbon
parser.add_argument('-p', '-protein', type=float, default=20, help='Current protein intake') #Protein
parser.add_argument('-f', '-fat', type=float, default=20, help='Current fat intake') #Fat
parser.add_argument('--NS', action='store_true', help='Difference in the targeted fat intake') #Without Sweetpotato
parser.add_argument('--NR', action='store_true', help='Difference in the targeted fat intake') #Without Redlentils
parser.add_argument('--NA', action='store_true', help='Difference in the targeted fat intake') #Without Avocado
args = parser.parse_args()

weight = float(input("Enter your weight in KG: "))
weight = weight * 2.20462 #convert to ft
height = float(input("Enter your height in M: "))
height = height * 39.3701 #convert to lb

age = int(input("Enter your age: "))
if type(age) != int:
    print('Error, please input an integer of your age, for example 19')

sex = input("Enter your sex (male or female): ")
#if sex != 'male' or 'female':
    #print('Error, please follow the instruction of the prompt')

activity_level = input("Enter your activity level (sedentary, lightly active, moderately active, very active): ")
diet_plan = input("Enter the diet plan you wish to have, balance; low fat; low carb; high protein")




def calculate_bmr(weight, height, age, sex):
    if sex == "male":
        bmr = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
    else:
        bmr = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
    return bmr

def calculate_daily_calories(bmr, activity_level):
    if activity_level == "sedentary":
        calories = bmr * 1.2
    elif activity_level == "lightly active":
        calories = bmr * 1.375
    elif activity_level == "moderately active":
        calories = bmr * 1.55
    else:
        calories = bmr * 1.725
    return calories

bmr = calculate_bmr(weight, height, age, sex)

calories = calculate_daily_calories(bmr, activity_level)

if diet_plan == "balance":
    carbon_intake = calories * 0.65 /4
    protein_intake = calories * 0.125 / 4
    fat_intake = calories * 0.225 / 9
elif diet_plan == "low fat":
    carbon_intake = calories * 0.725 /4
    protein_intake = calories * 0.125 / 4
    fat_intake = calories * 0.15 / 9
elif diet_plan == "low carb":
    carbon_intake = calories * 0.55 / 4
    protein_intake = calories * 0.15 / 4
    fat_intake = calories * 0.30 / 9
elif diet_plan == "high protein":
    carbon_intake = calories * 0.725 /4
    protein_intake = calories * 0.15 / 4
    fat_intake = calories * 0.125 / 9

print("Your daily calorie needs are: ", calories)
print("Your protein intake should be", protein_intake,'grams per day')
print("Your carbohydrates intake should be", carbon_intake, 'grams per day')
print("Your fat intake should be", fat_intake, "grams per day")

protein_needed = protein_intake - args.p
carbon_needed = carbon_intake - args.c
fat_needed = fat_intake - args.f

#print(protein_needed, carbon_needed, fat_needed)

# Nutrition Weights Matrix
# [         sweetpotato redlentils  avocado ]
# [ carbon                                  ]
# [ protein                                 ]
# [ fat                                     ]
# W = np.array([[0 if args.NS else 20, 0 if args.NR else 20.1, 0 if args.NA else 9], 
#               [0 if args.NS else 1.45, 0 if args.NR else 9.02, 0 if args.NA else 2], 
#               [0 if args.NS else 0, 0 if args.NR else 0.38, 0 if args.NA else 15]])
W = np.array([[20, 20.1, 9], 
              [1.45, 9.02, 2], 
              [0, 0.38, 15]])
#print(W)

# Nutrition Target Matrix
# [ carbon  protein  fat ]
y = np.array([carbon_needed, protein_needed, fat_needed])
n = len(y)
print("nutrition needed:", y)

# Nutrition Weights Matrix
# [ sweetpotato redlentils  avocado ]
fun = lambda x: np.linalg.norm(np.dot(W, x) - y)
sol = minimize(fun, np.zeros(n), method='L-BFGS-B', bounds=[(0.,None) for x in range(n)])
x = sol['x']
# res = np.linalg.solve(W, y, assume_a='pos', overwrite_a=True, overwrite_b=True, check_finite=False) 
print("We need to print following amount:", x)
#print(W @ x)