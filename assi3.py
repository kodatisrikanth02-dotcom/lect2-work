Gender = input("Please enter your gender : ")
Hemoglobin = int(input("Please enter your hemoglobin level: "))
if Gender == "Male" and Hemoglobin < 134:
    print("Hemoglobin level is Low")
elif Gender == "Male" and Hemoglobin <= 167:
    print("Hemoglobin level is Normal")
elif Gender == "Male" and Hemoglobin > 167:
    print("Hemoglobin level is High")
elif Gender == "Female" and Hemoglobin < 117:
    print("Hemoglobin level is Low")
elif Gender == "Female" and Hemoglobin <= 155:
    print("Hemoglobin level is Normal")
elif Gender == "Female" and Hemoglobin > 155:
    print("Hemoglobin level is High")
else:
    print("Invalid gender")