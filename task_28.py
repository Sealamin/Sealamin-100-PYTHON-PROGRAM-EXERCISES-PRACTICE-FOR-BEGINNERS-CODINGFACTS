from os import sep

number_oddNumbers = int(input("Enter a number of odd numbers: "))
empty = []
for n in range(0, number_oddNumbers):
    empty.append(2*n+1)
oddNumbers = str(empty) [1:-1]
print(f"oddNumbers = {oddNumbers}")