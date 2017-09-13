#!/usr/bin/env python3

file = open('trivia.txt')

for l in file.readlines():
    lst = tuple([x.strip() for x in l.split(':')])
    try:
        print('%s %s' % lst)
    except:
        print('error')
