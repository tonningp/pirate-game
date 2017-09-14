#!/usr/bin/env python3

file = open('trivia.txt')
print('questions = [')
count=0
lines = file.readlines()
lines_length = len(lines)
for l in lines:
    lst = tuple([x.strip().replace('"','\\"') for x in l.split(':')])
    try:
        print('{"question":"%s","answer":"%s"}' % lst),
        if count < lines_length-1:
            print(','),
    except:
        print('error')
    count += 1
print(']')
