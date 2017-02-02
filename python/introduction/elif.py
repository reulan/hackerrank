"""
elif.py - Simple if else script in Python.
mpmsimo
1/27/17
"""

def check_if_weird(n):
    """Checks to see if a certain number is weird or not."""

    # If remainder is 0 when n(modulo 2) then number is even.
    if (n % 2 == 0):
        # If n is even and in the inclusive range of 2 to 5, print Not Weird
        if (n >= 2 and n <= 5):
            print("Not Weird")
        # If n is even and in the inclusive range of 6 to 20, print Weird
        elif (n >= 6 and n <= 20):
            print("Weird")
        # If n is even and greater than 20, print Not Weird
        elif (n > 20):
            print("Not Weird")
    else:
        # If n is odd, print Weird
        print("Weird")

if __name__ == "__main__":
    n = int(input())
    check_if_weird(n)
