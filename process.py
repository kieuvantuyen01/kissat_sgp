#!/usr/bin/python3
import sys
import re

message = sys.stdin.read()


def normalize(str_):
    return re.sub('\s+', ' ', str_).strip()

# get substring from string
# Example: 'c parsed \'p cnf 79916 603037' header' -> p 79916
def get_substring1(input_string):
    start_index = input_string.find('parsed') + len('parsed')
    end_index = input_string.find('header', start_index)
    if start_index >= 0 and end_index >= 0:
        substring = input_string[start_index:end_index].strip()
        # remove "'" in substring
        substring = substring.replace("'", "")
        elements = substring.split()
        # return string is joined by 1st and 3rd elements of elements
        return ' '.join([elements[0], elements[2]]) if len(elements) >= 3 else None       
    else:
        return None

# get substring from string
# Example: 'c parsed 'p cnf 79916 603037' header' -> 'cnf 603037'
def get_substring2(input_string):
    start_index = input_string.find('parsed') + len('parsed')
    end_index = input_string.find('header', start_index)
    if start_index >= 0 and end_index >= 0:
        substring = input_string[start_index:end_index].strip()
        # remove "'" in substring
        substring = substring.replace("'", "")
        elements = substring.split()
        # return string is joined by 2nd and 4th elements of elements
        return ' '.join([elements[1], elements[3]]) if len(elements) >= 4 else None  
    else:
        return None

def handleOne(message):
    result = []
    lines = message.splitlines()
    number_lines = len(lines)
    if len([line for line in lines if line.startswith('c ---- [ result ]')]) > 0:
        for i in range(number_lines):
            if lines[i].startswith('c opened and reading DIMACS file:'):
                result.append(normalize(lines[i + 2]))
            # if lines[i] starts with 'c parsed 'p cnf '
            if lines[i].startswith('c parsed \'p cnf '):
                result.append(get_substring1(lines[i]))
                result.append(get_substring2(lines[i]))
            if lines[i].startswith('c ---- [ result ]'):
                result_text = normalize(lines[i + 2])
                result.append(result_text)
            #     for j in range (i + 3, number_lines):
            #         if lines[j].startswith('v'):
            #             result.append(lines[j])
            if lines[i].startswith('c process-time'):
                result.append(normalize(lines[i]))
        return result
    else:
        for i in range(number_lines):
            if lines[i].startswith('c opened and reading DIMACS file:'):
                result.append(normalize(lines[i + 2]))
            # if lines[i] starts with 'c parsed 'p cnf '
            if lines[i].startswith('c parsed \'p cnf '):
                result.append(get_substring1(lines[i]))
                result.append(get_substring2(lines[i]))
            if lines[i].startswith('c process-time'):
                result.append(normalize(lines[i]))
        result.append('UNKNOWN')
        return result


def handleMany(message_inp):
    lst_message = re.split('c exit 10\n|c exit 0\n', message_inp)
    result = []
    for message in lst_message:
        result.append(handleOne(message))
    return result


def serialize(data):
    result = ''
    for item in data:
        result += '\n'.join(item)
        result += '\n-----\n'
    return result


print(serialize(handleMany(message)))
