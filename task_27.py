from os import sep

number_evenNumbers = int(input("Enter a number of even numbers: "))
empty = []
for n in range(1,(number_evenNumbers + 1)):
    empty.append(2*n)
evenNumbers = str(empty) [1:-1]
print(f"evenNumbers = {evenNumbers}")

