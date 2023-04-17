#!/usr/bin/python3
import sys
import re

message = sys.stdin.read()


def normalize(str_):
    return re.sub('\s+', ' ', str_).strip()


def handleOne(message):
    result = []
    lines = message.splitlines()
    number_lines = len(lines)
    if len([line for line in lines if line.startswith('c ---- [ result ]')]) > 0:
        for i in range(number_lines):
            if lines[i].startswith('c opened and reading DIMACS file:'):
                result.append(normalize(lines[i + 2]))
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
