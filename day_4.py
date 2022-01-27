#Write a program which will return names(names should be sorted) of students with 2nd lowest grade
#input should be a list containing elements as list with student name and his score
#Example: students = [ [name,score], [name,score], ... ]
#Input: students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#Output: 
# Berry
# Harry
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

values_list = []

for i in students:
    values_list.append(i[1])

values_list = list(set(values_list))

values_list.sort()
second_lowest_grade = values_list[1]

names_list = []

for i in students:
    if i[1] == second_lowest_grade:
        names_list.append(i[0])

names_list.sort()
for i in names_list:
    print(i)