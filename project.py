print("welcome to the interactive persoal data coolector!")

name=input("please enter your name:")
age=int(input("please enter your age:"))
height=float(input("Please enter your hegight in miters:"))
favourite_number=int(input("please enter your favourite number:"))

print("\n thank you! here is the information we collected:")

print(f"name: {name} (type:{name}, memory address:{id(name)})")
print(f"age: {age} (type:{age}, memory address:{id(age)})")
print(f"height: {height} (type:{height}, memory addreess:{id(height)})")
print(f"favourite number: {favourite_number} (type:{favourite_number}"
      f"memory address:{id(favourite_number)})")
birth_year= 2026 - age

print(f"\nyour birth year is approximately: {birth_year}"
      f"(based on your age of {age})")

print("\nthank your for using the personal data collector. goodbye!")      
