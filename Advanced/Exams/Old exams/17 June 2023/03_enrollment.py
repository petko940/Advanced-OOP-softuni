def gather_credits(*args):
    number_of_credits = args[0]
    courses = []
    result = 0

    for course_name, course_credit in args[1:]:
        if course_name in courses:
            continue

        if result < number_of_credits:
            courses.append(course_name)
            result += course_credit

            if result >= number_of_credits:
                break

    if result < number_of_credits:
        return f"You need to enroll in more courses! You have to gather {number_of_credits - result} credits more."
    else:
        courses = sorted(courses)
        return f"Enrollment finished! Maximum credits: {result}.\n" \
               f"Courses: {', '.join(x for x in courses)}"
