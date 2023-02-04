import os

directory = input()
data = {}

for i in os.listdir(directory):
    file = os.path.join(directory, i)
    if os.path.isdir(file):
        os.chdir(i)
        files_inside_folder = os.listdir()
        for current_file in files_inside_folder:
            extension = current_file.split(".")[-1]
            data[extension] = data.get(extension, [])
            data[extension].append(current_file)

    elif os.path.isfile(file):
        extension = file.split('.')[-1]
        file = file.replace(".", "", 1).replace("\\", "")
        data[extension] = data.get(extension, [])
        data[extension].append(file)

data = sorted(data.items(), key=lambda x: (x[0], x[1]))
result = []

for key, files in data:
    result.append(f".{key}")
    for file in files:
        result.append(f"- - - {file}")

os.chdir("..")
with open("files/report.txt", 'w') as f:
    f.write("\n".join(result))
