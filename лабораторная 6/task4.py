import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimeter=",", new_line="\n") -> list[dict]:
    # TODO реализовать конвертер из csv в json
    dictionaries = []
    with open(filename) as file:  # TODO реализовать конвертер из csv в json
        file_text = "".join(file.readlines())
        strings_ = [string_.strip().split(delimeter) for string_ in file_text.split(new_line)]

    for data in strings_[1:]:
        dictionaries.append({strings_[0][i]: data[i] for i in range(len(data))})

    return dictionaries


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
