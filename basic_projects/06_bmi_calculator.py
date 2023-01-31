height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in Kilograms: "))
height = height/100
bmi = weight/(height**2)
if bmi > 0:
    if bmi <= 16:
        print(f"your bmi is{bmi} and your are severely underweigth")
    elif bmi < 18.5:
        print(f"your bmi is{bmi} and your are underweigth")
    elif bmi <= 25:
        print(f"your bmi is{bmi} and your are healthy")
    elif bmi <= 30:
        print(f"your bmi is{bmi} and your are overweight")
    else:
        print(f"your bmi is{bmi} and your are severely overweight")
else:
    print("Please enter valid details")
