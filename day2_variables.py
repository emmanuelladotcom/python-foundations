# DAY 2 — PYTHON BASICS: VARIABLES, DATA TYPES, AND PRINT STATEMENTS
# Variables, data types, and print statements

# ---- YOUR INFO ----
name = "Emmanuella"
age = 20
university = "UCL"
degree = "Experimental Linguistics"
is_nlp_engineer = True
target_year = 2027
favourite_number = 3.14 # update with real number
# ---- PRINTING ----
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Degree: {degree} at {university}")
print(f"NLP engineer by {target_year}: {is_nlp_engineer}")

# ---- DATA TYPES ----
print("\n--- Data Types ---")
print(f"'{name}' is a {type(name)}")
print(f"{age} is a {type(age)}")
print(f"{favourite_number} is a {type(favourite_number)}")
print(f"{is_nlp_engineer} is a {type(is_nlp_engineer)}")

# ---- BONUS: MATHS WITH VARIABLES ----
years_until_faang = target_year - 2026
print(f"\nYears until FAANG: {years_until_faang}")