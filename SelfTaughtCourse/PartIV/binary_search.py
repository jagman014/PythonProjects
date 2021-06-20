def binary_search(lst_obj, item):
    first = 0
    last = len(lst_obj) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2

        if lst_obj[mid] == item:
            found = True
        else:
            if item < lst_obj[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


this = range(1, 101)
print(binary_search(this, 72))
