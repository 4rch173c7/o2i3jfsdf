#!/bin/python

import sys


n = int(raw_input().strip())

arr = [[' ' for i in range(n)] for j in range(n)]
rec = n-1
counter = 1
for line in arr:
    while rec != n:
        line[rec]='#'
        rec+=1
    counter+=1
    rec = n-counter

string = ''
for line in arr:
    for entry in line:
        string+=entry
    string+='\n'
print string
