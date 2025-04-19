def add_numbers(a, b):
    """
    @brief Adds two numbers and returns the result.
    
    @param a The first number (int or float)
    @param b The second number (int or float)
    @return The sum of the two numbers (int or float)
    
    @details This function takes two numbers as input and returns their sum.
    It can handle both integer and floating-point numbers.
    """
    return a + b

def subtract_numbers(a, b):
    """
    @brief Subtracts the second number from the first and returns the result.
    
    @param a The first number (int or float)
    @param b The second number (int or float)
    @return The result of the subtraction (int or float)
    
    @details This function subtracts the second number from the first number
    and returns the result. It can handle both integer and floating-point numbers.
    """
    return a - b

def main():
    """
    @brief Main function to demonstrate the add_numbers and subtract_numbers functions.
    
    @details This function prompts the user to enter two numbers, then demonstrates
    both addition and subtraction operations using the add_numbers and subtract_numbers
    functions. The results are printed to the console.
    """
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    sum_result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {sum_result}")
    
    subtraction_result = subtract_numbers(num1, num2)
    print(f"The result of subtracting {num2} from {num1} is {subtraction_result}")

if __name__ == "__main__":
    main()