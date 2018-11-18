from maximum_subarray import maximum_subarray

def main():
    data = [100, 113, 110, 85, 105,
            102, 86,  63,  81, 101,
            94,  106, 101, 79, 94,
            90,  97]

    change = diff(data)

    lo, hi, val = maximum_subarray(change)

def diff(l):
    lst = []
    for i in range(1, len(l)):
        lst.append(l[i] - l[i-1])

    return lst
