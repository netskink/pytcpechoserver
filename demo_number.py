#!/usr/bin/python

largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" :
        break

    try :
        x = int(num)

    except ValueError:
        print "Invalid input"
        continue

    if largest == None:
        largest = x

    if smallest == None:
        smallest = x


    if x > largest:
        largest = x

    if x < smallest:
        smallest = x


print "Maximum", largest
print "Minimum", smallest