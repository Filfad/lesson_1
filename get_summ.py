def get_sum(one, two, delimiter="&"):
    one = str(one)
    two = str(two)
    sum = one + delimiter + two


    return sum.upper()

print(get_sum("Learn", "python"))