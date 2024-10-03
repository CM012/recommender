weight = float(input("Enter your weight in KG: "))
weight = weight * 2.20462
height = float(input("Enter your height in M: "))
height = height * 39.3701
age = int(input("Enter your age: "))
sex = input("Enter your sex (male or female): ")
activity_level = input("Enter your activity level (sedentary, lightly active, moderately active, very active): ")

if type(age) != int:
    print('Error, please input an integer of your age, for example 19')

if sex != 'male' or 'female':
    print('Error, please follow the instruction of the prompt')

#if activity_level != 'sedentar' or 'lightly activ' or 'moderately active' or 'very active':
#    print('Error, please follow the exact prompt')

#protein_intake = input("Do you need high protein option or balanced option, enter h for high protein and b for balanced option")

#if protein_intake == 'b':
#    carbon_intake = input("Do you need low carbon option or balanced option, enter l for low protein option and n for balanced option")


#if carbon_intake == 'n':
#    fat_intale = input("Do you want to choose low fat option or normal option, enter l for low fat option and n for normal option")


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

#protein_intake_lower = calories * 0.1
#protein_intake_upper = calories * 0.15

#carbon_intake_lower = calories * 0.55
#carbon_intake_mid = calories * 0.6
#carbon_intake_upper = calories * 0.75

#fat_intake_lower = calories * 0.15
#fat_intake_mid = calories * 0.25
#fat_intake_upper = calories * 0.3

protein_intake = calories * 0.4
carbon_intake = calories * 0.4
fat_intake = calories * 0.2


print("Your daily calorie needs are: ", calories)
print("Your protein intake should be", protein_intake/4,'grams per day')
print("Your carbohydrates intake should be", carbon_intake/4, 'grams per day')
print("Your fat inatke should be", fat_intake/9, "grams per day")







