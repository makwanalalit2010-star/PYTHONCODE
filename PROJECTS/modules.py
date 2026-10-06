# import datetime
# import time
# import math
# import random
# import uuid
# import functools


# # 1. datetime Module

# print("--- 1. DATETIME MODULE ---")

# # Calculate age in days
# birthday = datetime.date(2000, 5, 15)
# today = datetime.date.today()
# age_in_days = today - birthday
# print("Days lived:", age_in_days.days)

# # Extract specific components from current time
# now = datetime.datetime.now()
# print(f"Current Year: {now.year}, Hour: {now.hour}, Minute: {now.minute}")

# # Convert a text date string into a datetime object (strptime)
# date_string = "12/10/2026"
# parsed_date = datetime.datetime.strptime(date_string, "%d/%m/%Y")
# print("Parsed Object:", parsed_date)
# print()



# # 2. time Module

# print("--- 2. TIME MODULE ---")

# # Measure execution time
# start_time = time.time()
# for _ in range(1_000_000):
#     pass
# end_time = time.time()
# print("Loop execution time:", end_time - start_time, "seconds")

# # Get local formatted time string directly
# current_local_time = time.ctime()
# print("Readable time:", current_local_time)
# print()



# # 3. math Module
# print("--- 3. MATH MODULE ---")

# # Calculate hypotenuse of a right-angled triangle
# hypotenuse = math.hypot(3, 4)
# print("Hypotenuse of 3 and 4:", hypotenuse)

# # Trigonometry (Sine of 90 degrees)
# angle_degrees = 90
# angle_radians = math.radians(angle_degrees)
# print("Sin(90°):", math.sin(angle_radians))

# # Precise floating-point summation
# float_list = [0.1] * 10
# print("Accurate sum of ten 0.1s:", math.fsum(float_list))
# print()


# # 4. random Module

# print("--- 4. RANDOM MODULE ---")

# # Simulate rolling two six-sided dice
# dice_roll = random.randint(1, 6) + random.randint(1, 6)
# print("Dice total:", dice_roll)

# # Generate a random float within a range
# price = random.uniform(5.5, 10.5)
# print("Random price:", round(price, 2))

# # Reproducible randomness using seed
# random.seed(42)
# print("Deterministic random number (seed 42):", random.randint(1, 100))
# print()


# # 5. uuid Module
# print("--- 5. UUID MODULE ---")

# # Generate a URL/Namespace based UUID (UUIDv5)
# namespace = uuid.NAMESPACE_URL
# user_id = uuid.uuid5(namespace, "user_account_123")
# print("Deterministic UUIDv5:", user_id)

# # Extract raw hexadecimal representation of a random UUID (UUIDv4)
# new_id = uuid.uuid4()
# print("Hex string format:", new_id.hex)
# print()


# # 
# # 6. Higher-Order Functions
# print("--- 6. HIGHER-ORDER FUNCTIONS ---")

# # Sorting a list of dictionaries by a key using lambda
# students = [
#     {"name": "Alice", "grade": 88},
#     {"name": "Bob", "grade": 95},
#     {"name": "Charlie", "grade": 78}
# ]
# sorted_students = sorted(students, key=lambda student: student["grade"], reverse=True)
# print("Top student:", sorted_students[0]["name"])

# # Using map to convert strings to uppercase
# names = ["alice", "bob", "charlie"]
# capitalized = list(map(str.upper, names))
# print("Capitalized names:", capitalized)

# # Using filter to extract words longer than 4 letters
# words = ["tree", "python", "cat", "script", "code"]
# long_words = list(filter(lambda w: len(w) > 4, words))
# print("Words longer than 4 chars:", long_words)

# # Using reduce to find the maximum value
# numbers = [15, 82, 43, 91, 27]
# max_number = functools.reduce(lambda x, y: x if x > y else y, numbers)
# print("Maximum value using reduce:", max_number)


import time 
n = int(input("enter a number:"))
for i in range(n, 0, -1):
    print(i)
    time.sleep(1)
    print("good morning")







