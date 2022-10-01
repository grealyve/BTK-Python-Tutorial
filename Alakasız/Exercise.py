# Write a Python function that takes two lists and returns True if they have at least one common member

def common(list1, list2):
    c = 0
    for i in  list1:
        if i in list2:
            c += 1
    if c >= 1:
        result = True
    else:
        result = False
    return result

# Write a Python program to get the cumulative sum of the elements of a given list.
def cumulative(liste):
    l = []
    x = 0
    for i in range(len(liste)):
        x += liste[i]
        l.append(x)

    return l

l1 = [1, 2, 3, 4]
print(cumulative(l1))

# Write a Python program to generate a list, containing the Fibonacci sequence, up until the nth term.

def fibonacci(x):
    l = [0,1]
    a = 0
    for i in range(x-1):
        a = l[i] + l[i+1]
        l.append(a)

    return l

print(fibonacci(50))