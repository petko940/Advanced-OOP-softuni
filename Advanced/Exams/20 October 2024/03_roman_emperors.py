def list_roman_emperors(*args, **kwargs):
    successful_emperors = {}
    unsuccessful_emperors = {}

    for name, success_status in args:
        rule_length = kwargs.get(name, 0)
        if success_status:
            successful_emperors[name] = rule_length
        else:
            unsuccessful_emperors[name] = rule_length

    successful_emperors = sorted(successful_emperors.items(), key=lambda x: (-x[1], x[0]))
    unsuccessful_emperors = sorted(unsuccessful_emperors.items(), key=lambda x: (x[1], x[0]))

    result = [f"Total number of emperors: {len(args)}"]

    if successful_emperors:
        result.append(f"Successful emperors:")
        for emperor, rule_length in successful_emperors:
            result.append(f"****{emperor}: {rule_length}")

    if unsuccessful_emperors:
        result.append(f"Unsuccessful emperors:")
        for emperor, rule_length in unsuccessful_emperors:
            result.append(f"****{emperor}: {rule_length}")

    return '\n'.join(result)
