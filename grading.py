import gui


def history_grade(history_num):
    # determines grade based on the number of points achieved and returns to toplevel window
    if history_num >= 90:
        history_grade = "A"
    elif history_num >= 80:
        history_grade = "B"
    elif history_num >= 70:
        history_grade = "C"
    elif history_num < 70:
        history_grade = "D"
    else:
        history_grade = "Failing Grade"

    gui.Gui.grades.append(history_grade)

    return history_grade


def math_grade(math_num):
    # determines grade based on the number of points achieved and returns to toplevel window
    if math_num >= 90:
        math_grade = "A"
    elif math_num >= 80:
        math_grade = "B"
    elif math_num >= 70:
        math_grade = "C"
    elif math_num < 70:
        math_grade = "D"
    else:
        math_grade = "Failing Grade"

    gui.Gui.grades.append(math_grade)
    return math_grade


def science_grade(science_num):
    # determines grade based on the number of points achieved and returns to toplevel window
    if science_num >= 90:
        science_grade = "A"
    elif science_num >= 80:
        science_grade = "B"
    elif science_num >= 70:
        science_grade = "C"
    elif science_num < 70:
        science_grade = "D"
    else:
        science_grade = "Failing Grade"

    gui.Gui.grades.append(science_grade)

    return science_grade


def english_grade(english_num):
    # determines grade based on the number of points achieved and returns to toplevel window
    if english_num >= 90:
        english_grade = "A"
    elif english_num >= 80:
        english_grade = "B"
    elif english_num >= 70:
        english_grade = "C"
    elif english_num < 70:
        english_grade = "D"
    else:
        english_grade = "Failing Grade"

    gui.Gui.grades.append(english_grade)

    return english_grade


def gpa(grades):
    credit_hours = 3
    credit_total = 12
    quality_points = 0

    # got help with my for loop here (https://codereview.stackexchange.com/questions/175832/python-gpa-calculator)
    # determines the amount of points each pf the four grades is worth and divides by credit hours to calc GPA
    # returns gpa to toplevel window
    for element in grades:
        if element == "A":
            quality_points = quality_points + (4 * credit_hours)
        elif element == "B":
            quality_points = quality_points + (3 * credit_hours)
        elif element == "C":
            quality_points = quality_points + (2 * credit_hours)
        elif element == "D":
            quality_points = quality_points + (1 * credit_hours)
        else:
            quality_points = quality_points + 0
    answer = quality_points / credit_total
    gpa = round(answer, 2)
    if gpa > 4.0:
        gpa = 4.0

    return gpa
