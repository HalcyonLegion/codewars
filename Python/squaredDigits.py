def square_digits(num):
    # we need to split out the individual numbers then square them,
    # the result should be each number concatenated. Using str (tostring is JavaScript!) seems to be how others online approached this.
    
    # This should create a string from the numbers.
    num_str = str(num)
    
    # An empty variable to store the results.
    result_str = ""
    
    # Iterates through each individual digit and Squares them
    for digit in num_str:
        squared_digit = str(int(digit) ** 2)
        result_str += squared_digit
        
    return int(result_str)
