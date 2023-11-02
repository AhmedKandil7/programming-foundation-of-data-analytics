def is_valid_grade(grade):
    return 0 <= grade <= 100

grades = input("Enter a list of student grades separated by spaces: ").split()
grades = [int(grade) for grade in grades]

invalid_count = 0
for grade in grades:
    if is_valid_grade(grade):
            print("Valid")
    else:
            print("Invalid")
            invalid_count += 1


valid_flags = [1 if is_valid_grade(grade) else 0 for grade in grades]
print("Output list:", valid_flags)


if len(grades) > 0:
    average_grade = sum(grades) / len(grades)
    print("Average grade:", average_grade)
else:
    print("No grades entered.")


if len(grades) > 0:
    max_grade = max(grades)
    min_grade = min(grades)
    max_locations = [i for i, grade in enumerate(grades) if grade == max_grade]
    min_locations = [i for i, grade in enumerate(grades) if grade == min_grade]

    print("Highest grade:", max_grade, "at positions:", max_locations)
    print("Lowest grade:", min_grade, "at positions:", min_locations)


students_above_85 = [grade for grade in grades if grade > 85]
print("Students with grades greater than 85%:", students_above_85)
print("Count of students above 85%:", len(students_above_85))


if len(grades) > 0:
    students_above_average = [grade for grade in grades if grade > average_grade]
    print("Students with grades above the average:", students_above_average)
    print("Count of students above the average:", len(students_above_average))
