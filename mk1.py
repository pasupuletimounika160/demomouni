# Function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Main function to drive the program
def main():
    try:
        # Ask the user for input
        number = int(input("Enter a positive integer: "))
        
        # Check if the input is a positive integer
        if number < 0:
            print("Please enter a positive integer.")
        else:
            # Calculate and display the factorial
            result = factorial(number)
            print(f"The factorial of {number} is {result}.")
    
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Execute the main function
if __name__ == "__main__":
    main()
