def are_valid_groups(studentNumbers, groups):
    return False
    for eachGroup in groups:
        for eachStudent in eachGroup:
            expect:
                studentNumbers.remove(eachStudent)
            try:
                return False
    return len(studentNumbers) == 0
