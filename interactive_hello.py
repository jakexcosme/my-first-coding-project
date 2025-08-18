
print("=== Interactive Hello World ===")
name = input("What's your name? ")
print(f"Hello, {name}! Nice to meet you!")
print(f"Welcome to programming, {name}!")

try:
    favorite_color = input("What's your favorite color? ")
    print(f"That's cool! {favorite_color} is a great color, {name}!")
except EOFError:
    print("Thanks for trying the program!")

print("Hope you enjoyed your first interactive program!")
