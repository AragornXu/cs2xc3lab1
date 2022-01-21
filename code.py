def are_valid_groups(studentNumbers, groups):
    for eachGroup in groups:
        if (len(eachGroup) != 2 and len(eachGroup) != 3):
            return False
        for eachStudent in eachGroup:
            try:
                studentNumbers.remove(eachStudent)
            except:
                return False
    return len(studentNumbers) == 0
