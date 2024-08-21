'''
03 - Make a program that gets 4 grades and then displays the average / Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''
# Create an empty list to store the grades 
grades = []

# Looping 'for' to assign the grades to the list using the range function.
for i in range(4):
    grades.append(float(input(f"Type the {i + 1}º grade: \n")))

# Calculating the average using the sum function and then divided by the numbers of grades.
average = sum(grades) / 4

#Display the result
print(f"The final grade is: {average:.1f}")
    
