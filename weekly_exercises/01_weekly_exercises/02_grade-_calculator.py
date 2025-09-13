def grade_calc():
    exam_point = int(input("How many exam points did you get (0-24)?"))
    assignmen_point = int(input("How many assignment points did you get (0-12)?"))

    total_point = exam_point + assignmen_point

    if not (0 <= total_point <= 36):
        print("The value is outside the range!")
        return

    if 32 <= total_point <= 36:
        grade = 5
    elif 28 <= total_point < 32:
        grade = 4
    elif 24 <= total_point < 28:
        grade = 3
    elif 18 <= total_point < 24:
        grade = 2
    elif 15 <= total_point < 18:
        grade = 1
    else:
        grade = 0
    
    print(f"With total points {total_point}, the final grade was {grade}")

grade_calc()    