"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(list):
    frequencies= {}

    if len(list) == 0:
        print("Empty list")
    else:

        items =[str(x) for x in list]
        items.sort()
        current_state = items[0]
        counter = 0

        for i in range(0,len(items)):
            if items[i] == current_state:
                counter+=1
            else:
                frequencies[current_state] = counter
                current_state = items[i]
                counter = 1

            frequencies[current_state] = counter

    return frequencies
