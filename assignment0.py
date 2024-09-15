def add_numbers(x,y):
    return x + y

def main():
    try:
        num1 = float(input("Num1:"))
        num2 = float(input("Num2"))
        
        sum = add_numbers(num1, num2)

        print(f"The sum of {num1} and {num2} is {sum}.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()