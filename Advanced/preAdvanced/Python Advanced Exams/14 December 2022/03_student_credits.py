def students_credits(*args):
    info = {}
    sum_credit = 0
    for x in args:
        x = x.split("-")
        course_name, credit, max_test_points, diyan_points = x[0], int(x[1]), int(x[2]), int(x[3])
        diyan_credit = diyan_points / max_test_points
        diyan_credit = diyan_credit * credit
        info[course_name] = diyan_credit
        sum_credit += diyan_credit

    output_student_info = []
    if sum_credit >= 240:
        output_student_info.append(f"Diyan gets a diploma with {sum_credit:.1f} credits.")
    else:
        output_student_info.append(f"Diyan needs {240 - sum_credit:.1f} credits more for a diploma.")

    for c_name, c_credit in sorted(info.items(), key=lambda x: -x[1]):
        output_student_info.append(f"{c_name} - {c_credit:.1f}")

    return '\n'.join(output_student_info)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
