def task(input_list):
    # Check if the list length is a multiple of 10
    if len(input_list) % 10 != 0:
        raise ValueError("Error: The list is not a multiple of 10 in length.")
    
    # Initialize an empty list for the result
    res = []
    
    # Iterate over the list using index
    for i in range(len(input_list)):
        # Check if the position (index + 1) is not a multiple of 2 or 3
        if (i + 1) % 2 != 0 and (i + 1) % 3 != 0:
            # Append the item to the filtered list
            res.append(input_list[i])
    
    # Return the filtered list
    return res

# Function to test the program with various inputs
def test_program():
    test_cases = [
        ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], "Test Case 1 - Valid: "),
        ([1, 2, 3], "Test Case 2 - Error: "),
        ([i for i in range(1, 101)], "Test Case 3 - Valid: "),
        ([10], "Test Case 4 - Error: "),
        ([], "Test Case 5 - Valid: Empty list: ")
    ]

    for case, description in test_cases:
        try:
            result = task(case)
            if isinstance(result, list):
                print(f"{description}Passed. Output: {result}")
            else:
                print(f"{description}Failed. {result}")
        except ValueError as e:
            print(f"{description}Failed with exception: {e}")

# Run the tests
test_program()
