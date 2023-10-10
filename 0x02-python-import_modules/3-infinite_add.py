#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Exclude the script name from the arguments
    arguments = sys.argv[1:]

    # Convert arguments to integers and calculate the sum
    total = sum(int(arg) for arg in arguments)

    # Print the result
    print(total)
