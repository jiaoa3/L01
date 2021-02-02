def quicksort_inplace_rec(L, low, high):
    if high is None:
        high = len(L) - 1
    if low < high:
        i = low - 1
        pivot = L[high]
        for j in range(low, high):
            if L[j] <= pivot:
                i += 1
                L[i], L[j] = L[j], L[i]
                L[i + 1], L[high] = L[high], L[i + 1]
        p = i + 1
    quicksort_inplace_rec(L, low, p-1)
    quicksort_inplace_rec(L, p+1, high)


def quicksort_inplace(L):
    return quicksort_inplace_rec(L, 0, None)


def dual_pivot_quicksort(L):
    if len(L) <= 1:
        return L
    elif len(L) == 2:
        return quicksort_inplace(L)
    pivots = quicksort_inplace([L[0], L[1]])
    parts = [[], [], []]
    for element in L[2:]:
        if element < pivots[0]:
            parts[0].append(element)
        elif element < pivots[1]:
            parts[1].append(element)
        else:
            parts[2].append(element)
    return (dual_pivot_quicksort(parts[0]) + [pivots[0]]
            + dual_pivot_quicksort(parts[1]) + [pivots[1]]
            + dual_pivot_quicksort(parts[2]))


def tri_pivot_quicksort(L):
    if len(L) <= 1:
        return L
    elif len(L) <= 3:
        return quicksort_inplace(L)
    pivots = quicksort_inplace([L[0], L[1], L[2]])
    parts = [[], [], [], []]
    for element in L[3:]:
        if element < pivots[0]:
            parts[0].append(element)
        elif element < pivots[1]:
            parts[1].append(element)
        elif element < pivots[2]:
            parts[2].append(element)
        else:
            parts[3].append(element)
    return (tri_pivot_quicksort(parts[0]) + [pivots[0]]
            + tri_pivot_quicksort(parts[1]) + [pivots[1]]
            + tri_pivot_quicksort(parts[2]) + [pivots[2]]
            + tri_pivot_quicksort(parts[3]))


def quad_pivot_quicksort(L):
    if len(L) <= 1:
        return L
    elif len(L) <= 4:
        return quicksort_inplace(L)
    pivots = quicksort_inplace([L[0], L[1], L[2], L[3]])
    parts = [[], [], [], [], []]
    for element in L[4:]:
        if element < pivots[0]:
            parts[0].append(element)
        elif element < pivots[1]:
            parts[1].append(element)
        elif element < pivots[2]:
            parts[2].append(element)
        elif element < pivots[3]:
            parts[3].append(element)
        else:
            parts[4].append(element)
    return (quad_pivot_quicksort(parts[0]) + [pivots[0]]
            + quad_pivot_quicksort(parts[1]) + [pivots[1]]
            + quad_pivot_quicksort(parts[2]) + [pivots[2]]
            + quad_pivot_quicksort(parts[3]) + [pivots[3]]
            + quad_pivot_quicksort(parts[4]))