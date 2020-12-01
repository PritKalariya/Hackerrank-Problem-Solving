#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    time = s[-2:]
    
    if time == 'PM' and s[:2] != '12':
        s = str(12 + int(s[:2])) + s[2:]
    elif time == 'AM' and s[:2] == '12':
        s = '00' + s[2:]
    
    return s[:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()