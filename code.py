def are_valid_groups(studentNumbers, groups):
    for eachGroup in groups:
        for eachStudent in eachGroup:
            try:
                studentNumbers.remove(eachStudent)
            except:
                return False
    return len(studentNumbers) == 0
