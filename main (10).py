
items = [23, 41, 11, 17, 34, 56]
n=len(items) - 1

swapped = True
while swapped:
    swapped = False
    for index in range(0, n):
        if items[index] > items[index+1]:
            temp = items[index]
            items[index] = items[index+1]
            items[index+1] = temp
            swapped = True

print(items)