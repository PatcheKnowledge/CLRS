def maximum_subarray(a, lo, hi):
    """
    >>> a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    >>> maximum_subarray(a, 0, len(a))
    (7, 10, 43)
    """
    if hi - lo < 2:
        return lo, hi, a[lo]

    mid = lo + (hi - lo) // 2
    lo_l, hi_l, val_l = maximum_subarray(a, lo, mid)
    lo_r, hi_r, val_r = maximum_subarray(a, mid, hi)

    # find max crossing subarray
    l_v = 0
    l_lo = mid

    l_max = 0
    for i in reversed(range(0, mid)):
        l_v += a[i]

        if l_v > l_max:
            l_max = l_v
            l_lo = i
    
    r_v = 0
    r_hi = mid

    r_max = 0
    for i in range(mid, hi):
        r_v += a[i]

        if r_v > r_max:
            r_max = r_v
            r_hi = i

    lo_m, hi_m, val_m = l_lo, r_hi, l_max + r_max

    maxv = max(val_l, val_r, val_m)
    if maxv == val_l:
        return lo_l, hi_l, val_l
    elif maxv == val_m:
        return lo_m, hi_m, val_m
    elif maxv == val_r:
        return lo_r, hi_r, val_r

def main():
    import doctest

    doctest.testmod()

if __name__ == '__main__':
    main()
