import os


def get_extention(data):
    result_list = []
    list_files = []
    if isinstance(data, str):
        dir_ = os.walk(data)
        for i in dir_:
            for j in i[2]:
                list_files.append(j)
        result_list = validate_ext(list_files)
    else:
        result_list = validate_ext(data)
    return result_list


def validate_ext(extensions):
    result_list = []
    for i in extensions:
        name_file = os.path.splitext(i)
        result = name_file[1].replace('.','')
        if result == '':
            raise EOFError("Расширение отсутсвует")
        result_list.append(result)
    return result_list
print(get_extention(["da.docx", "dj.txt", "df.csv"]))