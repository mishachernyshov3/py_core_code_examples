# Підрахувати потенціальну енергію за формулою F = m * g * h,
# змінним вказати підказки типів
G: float = 9.81

m: float = float(input('Enter the mass: '))
h: float = float(input('Enter the height: '))

potential_energy = round(m * G * h, 2)
print(f'Potential energy is {potential_energy} (kg * m2) / s2')
