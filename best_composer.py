def best_composers(lst):
    '''print all names on the list lst
    starting with B or S, and
    having length at least 6'''

    for name in lst:
        first_letter = name[0]
        if first_letter in ['B', 'S'] and len(name) >= 6:
            print(name)
            
