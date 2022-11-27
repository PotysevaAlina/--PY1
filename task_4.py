import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(input_FILE, delimetr=",") -> list[dict]:
    exit_list=[]
    with open(input_FILE) as f:

        for i,ii in enumerate(f):
            if i==0:
                headers=ii[:-1].split(delimetr)
            else:
                Dict_values=dict.fromkeys(headers,1)
                for it,itt in enumerate(Dict_values):
                    Dict_values[itt]=ii[:-1].split(delimetr)[it]
                exit_list.append(Dict_values)
    return (exit_list)

...  # TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))