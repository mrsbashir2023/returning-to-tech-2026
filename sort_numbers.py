# sort_numbers.py - Day 5 - C++ array vs Python List
# Your C++ logic in Python

def sort_numbers():
    print("=== Sort 10 Numbers - C++ vs Python ===")
    # In C++ you did int arr[10]; with loops. In Python:
    numbers = []
    for i in range(10):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)

    print(f"Original: {numbers}")
    numbers.sort() # No need for bubble sort like in C++ 2007!
    print(f"Sorted (smallest to largest): {numbers}")
    print(f"Largest: {max(numbers)} | Smallest: {min(numbers)} | Average: {sum(numbers)/len(numbers):.2f}")

if __name__ == "__main__":
    sort_numbers()