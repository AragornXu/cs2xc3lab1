def are_valid_groups(list1, list2):
    for eachGroup in list2:
        for eachStudent in eachGroup:
            try:
                list1.remove(eachStudent)
            except:
                return False
    return len(list1) == 0