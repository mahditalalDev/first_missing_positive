def first_missing_positive(numbers):
    # Sort the list in ascending order
    numbers.sort()
    print(numbers)
    missing = 1 # missing positive should start from 1
    for num in numbers:
        # no need for negative number just ignore it
        if num < missing:
            continue
        # if current num == missing then this not the missing number ,incremnt missing by 1
        elif num == missing:
            missing += 1
    
    return missing
print(first_missing_positive([3, 4, -1, 1]))
print(first_missing_positive([1, 2, 0]))