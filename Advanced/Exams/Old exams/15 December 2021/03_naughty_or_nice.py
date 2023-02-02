# def naughty_or_nice_list(*args, **kwargs):
#     data = {
#         "Nice": [],
#         "Naughty": [],
#         "Not found": []
#     }
#     info_kids = [x for x in args[0]]
#     info_kids_copy = info_kids.copy()
#     for x in args[1:]:
#         num, type = [int(x) if x.isdigit() else x for x in x.split("-")]
#         for i in info_kids:
#             if num in i:
#                 data[type].append(i[1])
#                 info_kids_copy.remove(i)
#
#     for key, value in kwargs.items():
#         for v in data.values():
#             if key in v:
#                 v.remove(key)
#                 data[value].append(key)
#                 break
#
#     for x in info_kids_copy:
#         data["Not found"].append(x[1])
#
#     output = []
#     for k,v in data.items():
#         if v:
#             remove = ", ".join(v)
#             output.append(f"{k}: {remove}")
#     return '\n'.join(output)


def naughty_or_nice_list(*args, **kwargs):
    result = {"Nice": [], "Naughty": [], "Not found": []}
    output, list_with_names = "", args[0]
    for data in args[1:]:
        number, type_ = data.split("-")
        total_numbers = 0
        if sum(1 for num, name in list_with_names if int(number) == num) == 1:
            for pos, (num, name) in enumerate(list_with_names):
                if int(number) == num:
                    total_numbers += 1
                    result[type_].append(name)
                    del list_with_names[pos]
    for k_name, v_type in kwargs.items():
        if sum(1 for num, name in list_with_names if k_name == name) == 1:
            for pos, (num, name) in enumerate(list_with_names):
                if k_name == name:
                    del list_with_names[pos]
                    result[v_type].append(name)

    result["Not found"] = [not_found_name for _, not_found_name in list_with_names]
    for p_type, p_names in result.items():
        if p_names:
            output += f"{p_type}: {', '.join(p_names)}\n"

    return output

