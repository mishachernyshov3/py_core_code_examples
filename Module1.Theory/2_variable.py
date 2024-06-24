# Підрахувати потенціальну енергію за формулою F = m * g * h
G = 9.81

m = float(input('Enter the mass: '))
h = float(input('Enter the height: '))

potential_energy = m * G * h, 2
print(f'Potential energy is {potential_energy} (kg * m2) / s2')
