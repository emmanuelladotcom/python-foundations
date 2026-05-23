# DAY 5
# for loops, while loops, range(), break, continue

# ---- FOR LOOP: through a list ----
print("--- K-pop Groups ---")
groups = ["aespa", "IVE", "NewJeans", "BLACKPINK"]
for group in groups:
    print(f"  {group.upper()}")

# ---- FOR LOOP: through a string ----
print("\n--- letters in your name ---")
name = "Emmanuella"
count = 0
for letter in name:
    if letter.lower() in "aeiou":
        count += 1
print(f"Vowels in {name}: {count}")

# ---- RANGE: basic ----
print("\n--- range(1, 6) ---")
for i in range(1, 6):
    print(f"  {i}")

# ---- RANGE: with step ----
print("\n--- Counting in 10s ---")
for i in range(0, 51, 10):
    print(f"  {i}")

# ---- RANGE: 90-day tracker ----
print("\n--- Week milestones ---")
for day in range(1, 91):
    if day % 7 == 0:
        print(f"  Day {day} — week {day // 7} complete")

# ---- WHILE LOOP ----
print("\n--- GitHub streak ---")
streak = 0
while streak < 5:
    streak += 1
    print(f"  Day {streak} — green square earned")

# ---- BREAK ----
print("\n--- break example ---")
for i in range(1, 10):
    if i == 4:
        print(f"  Stopping at {i}")
        break
    print(f"  {i}")

# ---- CONTINUE ----
print("\n--- continue example (skip 3) ---")
for i in range(1, 7):
    if i == 3:
        continue
    print(f"  {i}")