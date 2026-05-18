# DAY 4 
# if / elif / else statements
# ---- PROGRAMME 1: GRADE CALCULATOR ----
score = int(input("enter your score (0-100): "))

if score >= 90:
    grade = "A*"
elif score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"

print(f"Score: {score} — Grade: {grade}")

# ---- PROGRAMME 2: AGE CATEGORY ----
age = int(input("\nhow old are you? "))

if age < 13:
    category = "child"
elif age < 18:
    category = "teenager"
elif age < 30:
    category = "young adult"
else:
    category = "adult"

print(f"You are a {category}")