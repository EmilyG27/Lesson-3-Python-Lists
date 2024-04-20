# Task 1
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort()
grades.reverse()
print(grades)

# Task 2
average = sum(grades) / len(grades)
print(average)

# Task 3
grades.remove(78)
grades.remove(76)
grades.remove(72)
grades.append("Failed, Failed, Failed")
print(grades)