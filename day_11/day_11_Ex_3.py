def add_all_nums(*nums):
    total = 0
    for num in nums:
        if isinstance(num, (int, float)):
            total += num
        else:
            print(f"Warning: {num} is not a number and will be ignored.")
    return total
print(add_all_nums(2, 'h', 4))