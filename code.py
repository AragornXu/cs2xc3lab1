def are_valid_groups(studentNumbers, groups):
    return False
    for eachGroup in groups:
        if (len(eachGroup) != 2 and len(eachGroup) != 3):
            return False
        for eachStudent in eachGroup:
            expect:
                studentNumbers.remove(eachStudent)
            try:
                return False
    return len(studentNumbers) == 0
