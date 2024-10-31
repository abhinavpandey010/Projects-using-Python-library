import numpy as np

def create_array():
    """Function to create an array based on user input."""
    while True:
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            if rows <= 0 or cols <= 0:
                print("Rows and columns must be positive integers.")
                continue
            else:
                break
        except ValueError:
            print("Please enter valid integers for rows and columns.")
    while True:
        elements = input(f"Enter {rows * cols} elements separated by space: ").split()
        try:
            data = np.array([int(x) for x in elements]).reshape(rows, cols)
            print("Array created:\n", data)
            break
        except ValueError:
            print(f"Please enter exactly {rows * cols} integers.")
             
    return data

def display_menu():
    """Display menu options for the user to choose an operation."""
    print("\n--- Array Statistics Dashboard ---")
    print("1. Calculate Mean")
    print("2. Calculate Median")
    print("3. Calculate Standard Deviation")
    print("4. Calculate Variance")
    print("5. Reshape Array")
    print("6. Sort Array")
    print("7. Exit")

def calculate_statistics(data):
    """Function to perform various calculations based on user choice."""
    while True:
        display_menu()
        option = int(input('Choose an option:'))
        match option:
            case 1:
                print("Mean:", np.mean(data))
            case 2:
                print("Median:", np.median(data))
            case 3:
                print("Standard Deviation:", np.std(data))
            case 4:
                print("Variance:", np.var(data))        
            case 5:
                while True:
                    try:
                        new_shape = input("Enter new shape as 'rows columns': ")
                        rows, cols = map(int, new_shape.split())
                        print("Reshaped Array:\n", data.reshape(rows, cols))
                        break
                    except ValueError:
                            print("Error: Shape does not match the number of elements.")
            case 6:
                while True:
                    try:
                        axis = int(input("Enter axis to sort (0 for columns, 1 for rows): "))
                        print("Sorted Array:\n", np.sort(data, axis=axis))
                        break
                    except:
                        print("Invalid axis.")
            case 7:
                print("Exiting the dashboard.")
                break
            case default:
                print("Invalid choice. Please try again.")
           
# Main program
if __name__ == "__main__":
    while True:
        data = create_array()
        calculate_statistics(data)
        restart = input("Would you like to create a new array? (y/n): ").strip().lower()
        if restart != 'y':
            print("Thank you for using the Array Statistics Dashboard!")
            break

