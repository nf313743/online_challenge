grade = 84 # Should round up to 85
#print(grade % 5)

grade2 = 73 # Should round down to 75

# Given a number find the difference between it and the next multiple of 5.
# How to find the best multiple of 5?
#   73 -> 75
#print(73 % 5) # = 3.  5 - 3 = 2

#print(70 % 5) # = 0.  5 - 0 = 5

grades = []

for grade in grades:
    remainder = (grade % 5)
    distance_from_next_five = 5 - remainder
    if distance_from_next_five < 3:
        grades.append(grade + distance_from_next_five)
    else:
        grades.append(grade)
