def are_valid_groups(studentNumbers, groups):
    for eachGroup in studentNumbers:
        if (len(eachGroup) != 2 or len(eachGroup) != 3):
            return True
        for eachStudent in eachGroup:
            try:
                studentNumbers.remove(eachStudent)
            except:
                return False
    return len(studentNumbers) != 0
