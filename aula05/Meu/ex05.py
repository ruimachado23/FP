def countDigits():
    str = input("String:")
    count = 0
    for i in str:
        if i.isdigit():
            count += 1
    return count

print(countDigits())
