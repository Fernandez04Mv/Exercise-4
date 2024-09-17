# Function to check if a number is even
def is_even(number):
    # Condition: Check if the number is divisible by 2
    if number % 2 == 0:
        return True
    else:
        return False

# Test the function with different numbers
test_numbers = [10, 15, 22, 33, 44]

# Print results for each test number
for num in test_numbers:
    result = is_even(num)
    print(f'Is {num} even? {result}')



# List
my_list = [1, "apple", True, 3.14, "banana"]
print("List:")
for item in my_list:
    print(f"Item: {item}, Type: {type(item)}")

# Tuple
my_tuple = (42, "orange", False, 2.71)
print("\nTuple:")
for item in my_tuple:
    print(f"Item: {item}, Type: {type(item)}")

# Set
my_set = {1, "grape", True, 3.14, 42}
print("\nSet:")
for item in my_set:
    print(f"Item: {item}, Type: {type(item)}")

# Dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "is_student": False,
    "favorite_numbers": [7, 14, 21]
}
print("\nDictionary:")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}, Type of Value: {type(value)}")
