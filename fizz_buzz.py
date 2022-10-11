"""
    Write a program that prints the numbers from 1 to 100.
    But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
    For numbers which are multiples of both three and five print "FizzBuzz".
"""

def main():
    # If true it prints the word; otherwise, it prints the number. The "+" will concatenate the words if both are true.
    for i in range(1, 101): print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i)

main()