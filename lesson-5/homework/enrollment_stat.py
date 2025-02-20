universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    students = []
    tuition = []

    for university in universities:
        students.append(university[1])
        tuition.append(university[2])

    return students, tuition

def mean(values):
    return sum(values) / len(values)

def median(values):
    values.sort()
    n = len(values)
    if n % 2 == 1:
        return values[n // 2]
    else:
        return (values[(n // 2) - 1] + values[n // 2]) / 2

students, tuition = enrollment_stats(universities)

total_students = sum(students)
total_tuition = sum(tuition)
mean_students = mean(students)
median_students = median(students)
mean_tuition = mean(tuition)
median_tuition = median(tuition)

print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")

print()
print(f"Student mean: {mean_students:,.2f}")
print(f"Student median: {median_students:,}")

print(f"Tuition mean: $ {mean_tuition:,.2f}")
print(f"Tuition median: $ {median_tuition:,.2f}")
print("******************************")
