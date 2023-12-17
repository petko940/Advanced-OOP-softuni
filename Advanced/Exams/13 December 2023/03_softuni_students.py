def softuni_students(*args, **kwargs):
    students = {}

    for course_id, username in args:
        students[username] = course_id

    sorted_students = sorted(students.items(), key=lambda x: x[0])

    courses = {}
    for course_id, course_name in kwargs.items():
        courses[course_id] = course_name

    valid_students, invalid_students = [], []
    for username, course_id in sorted_students:
        if course_id in courses.keys():
            valid_students.append(f"*** A student with the username {username} "
                                  f"has successfully finished the course {courses[course_id]}!")
        else:
            invalid_students.append(username)

    output = list(valid_students)
    if invalid_students:
        output.append(f'!!! Invalid course students: {", ".join(invalid_students)}')
    return '\n'.join(output)
