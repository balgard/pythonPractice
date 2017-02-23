import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = 5  # the number of temperatures to analyse
temps = "7 5 9 1 4"  # the n temperatures expressed as integers ranging from -273 to 5526
x = temps.split(" ")


if n != 0:
    baseNumber = int(x[0])
    i = 0
    baseDifference = abs(int(x[0]))
    while i < n:
        newNumber = abs(int(x[i]))
        if newNumber < abs(baseNumber):
            baseNumber = int(x[i])
        if newNumber == baseDifference:
            if int(x[i]) > 0 and baseNumber < 0:
                baseNumber = int(x[i])
                
        i += 1
    print(baseNumber)
else:
    print("0")
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

