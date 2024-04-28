import re


def main(input_string):
    data = {}
    line_pattern = re.compile(r'variable list\((.*?)\) to \'(.*?)\';')

    prepared_input = input_string.replace('\n', ' ')
    lines = prepared_input.split('. {')
    for line in lines:
        match = line_pattern.search(line)
        if match:
            key = match.group(2)
            values = [v.strip().strip('"') for v in
                      match.group(1).split(',')]
            data[key] = values

    return data

