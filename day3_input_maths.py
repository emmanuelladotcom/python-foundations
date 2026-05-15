# DAY 3 — MATHS
# input(), type conversion, string formatting, maths

# ---- SECTION 1: input() ----
name = input("What is your name? ")
birth_year = int(input("What year were you born? "))

# ---- SECTION 2: MATHS ----
current_year = 2026
age = current_year - birth_year
graduation_year = 2027
years_to_graduation = graduation_year - current_year

# ---- SECTION 3: FORMATTED OUTPUT ----
print(f"\nHello {name.upper()}!")
print(f"You are {age} years old.")
print(f"Graduation target: {graduation_year} — that is {years_to_graduation} year(s) away.")

# ---- SECTION 4: ALL 7 OPERATORS ----
x = age
y = 7
print(f"\n--- Maths with my age ---")
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y:.2f}")
print(f"{x} // {y} = {x // y}")
print(f"{x} % {y} = {x % y}")
print(f"{x} ** 2 = {x ** 2}")

# ---- SECTION 5: FLOAT INPUT ----
height = float(input("\nYour height in metres (e.g. 1.65): "))
weight = float(input("Your weight in kg (e.g. 500): "))
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.1f}")