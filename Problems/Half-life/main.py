initial_atoms = int(input())
final_atoms = int(input())
days = 0
while initial_atoms >= final_atoms:
    days += 1
    initial_atoms /= 2
print(days * 12)
