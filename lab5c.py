#!/usr/bin/env python3
# Author ID: fowuhumiakpo

def add(number1, number2):
    try:
        return int(number1) + int(number2)
    except:
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                    # 15
    print(add('10', 5))                 # 15
    print(add('abc', 5))                # error
    print(read_file('seneca2.txt'))     # should return list of lines
    print(read_file('file10000.txt'))   # error
