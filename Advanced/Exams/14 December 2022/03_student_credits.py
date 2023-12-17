def students_credits(*args):
    credits_collected = 0
    data = {}
    for arg in args:
        course_name, credit, max_test_points, diyan_points = [int(x) if x.isdigit() else x for x in arg.split("-")]
        percent = diyan_points / max_test_points
        credits_collected += credit * percent
        credit_now = credit * percent
        data[course_name] = credit_now

    output = []
    if credits_collected >= 240:
        output.append(f"Diyan gets a diploma with {credits_collected:.1f} credits.")
    else:
        output.append(f"Diyan needs {240 - credits_collected:.1f} credits more for a diploma.")

    for k, v in sorted(data.items(), key=lambda x: -x[1]):
        output.append(f"{k} - {v:.1f}")

    return "\n".join(output)


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
