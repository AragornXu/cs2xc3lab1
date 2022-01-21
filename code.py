def are_valid_groups(studentNumbers, groups):
    sns = studentNumbers
    gs = groups
    for group in gs:
        for studentNumber in group:
            try:
                sns.remove(studentNumber)
            except:
                return False
    return len(sns) == 0
