
print("=== Simple Calculator ===")
print("Let's do some math together!")

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number

print(f"\nResults:")
print(f"{first_number} + {second_number} = {addition}")
print(f"{first_number} - {second_number} = {subtraction}")
print(f"{first_number} × {second_number} = {multiplication}")

if second_number != 0:
    division = first_number / second_number
    print(f"{first_number} ÷ {second_number} = {division}")
else:
    print("Cannot divide by zero!")

print("\nGreat job! You just used a calculator you programmed yourself!")
