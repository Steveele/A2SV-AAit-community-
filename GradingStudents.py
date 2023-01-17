def gradingStudents(grades):
    output = []
    for i in grades:
        if (i >= 38) and (i % 5 >= 3):
            i += (5 - (i % 5))
        output.append(i)
    return output
