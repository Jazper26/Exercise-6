# Iterate through the given list of numbers and print only those divisible by 5.
def print_divisible_by_5(nums):

    print("Given list is ", nums)
    print("Divisible by 5")

    # Iterate through the list of numbers
    for num in nums:
        # Check if the number is divisible by 5
        if num % 5 == 0:
            # Print the number if divisible by 5
            print(num)

# Given list of numbers
numbers_list = [10, 20, 33, 46, 55]

# Call the function with the given list
print_divisible_by_5(numbers_list)