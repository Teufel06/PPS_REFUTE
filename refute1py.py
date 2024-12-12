def sum_of_odds(numbers):
    return sum(num for num in numbers if num % 2 != 0)

# Test cases
print(sum_of_odds([1, 2, 3, 4, 5]))  # Expected output: 9
print(sum_of_odds([2, 4, 6, 8]))  # Expected output: 0

