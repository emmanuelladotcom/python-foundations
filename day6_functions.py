# DAY 6
# Functions: define, parameters, return values, defaults

# ---- BASIC FUNCTION ----
def greet():
    print("Hello from a function!")

greet()

# ---- FUNCTION WITH PARAMETER ----
def greet_name(name):
    print(f"Hello {name.upper()}!")

greet_name("Emmanuella")
greet_name("Future NLP engineer")
# ---- MULTIPLE PARAMETERS ----
def introduce(name, age, goal):
    print(f"\nName: {name}")
    print(f"Age: {age}")
    print(f"Goal: {goal}")

introduce("Emmanuella", 20, "NLP engineer")

# ---- DEFAULT PARAMETER ----
def greet_default(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_default("Emmanuella")
greet_default("Emmanuella", "Welcome back")

# ---- RETURN VALUES ----
def add(a, b):
    return a + b

def square(n):
    return n ** 2

print(f"\n3 + 7 = {add(3, 7)}")
print(f"5 squared = {square(5)}")

# ---- FUNCTIONS CALLING FUNCTIONS ----
def count_words(sentence):
    return len(sentence.split())

def count_chars(sentence):
    return len(sentence)

def count_vowels(sentence):
    return sum(1 for c in sentence if c.lower() in "aeiou")

def analyse_text(sentence):
    w = count_words(sentence)
    c = count_chars(sentence)
    v = count_vowels(sentence)
    print(f"\nSentence: '{sentence}'")
    print(f"Words: {w}")
    print(f"Characters: {c}")
    print(f"Vowels: {v}")
    print(f"Avg word length: {c/w:.1f}")

analyse_text("Emmanuella is going to graduate in 2027")
analyse_text("Python is the language of NLP")