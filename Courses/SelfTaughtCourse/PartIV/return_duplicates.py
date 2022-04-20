def return_duplicates(lst_obj):
    dups = []
    a_set = set()

    for item in lst_obj:
        length_one = len(a_set)
        a_set.add(item)
        length_two = len(a_set)

        if length_one == length_two:
            dups.append(item)

    return dups


a_list = [1, 1, 2, 3, 4, 4, 5, 6]
dups = return_duplicates(a_list)

print(dups)
