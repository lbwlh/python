lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(lst):
    sum = 0.0
    num = 0
    for item in lst :
        sum += item
        num += 1
    return sum / num

def get_average(student):
    return average(student["homework"]) * 0.1 + average(student["quizzes"]) * 0.3 + average(student["tests"]) * 0.6
    
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif 80 <= score < 90: 
        return "B"
    elif 70 <= score < 80: 
        return "C"
    elif 60 <= score < 70: 
        return "D"
    elif score < 60: 
        return "F"

def get_class_average(class_list):
    average_list = []
    for item in class_list:
        average_list.append(get_average(item))
    return average(average_list)

students = [lloyd, alice, tyler]

print get_class_average(students)
print get_letter_grade(get_class_average(students))
