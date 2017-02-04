"""
array-ds.py - List rotation.
mpmsimo
2/4/17
"""

# Given list A containing N integers, print each element in reverse order as a
# single line of space-seperated ints.

def print_list_elements(a, n):
    "a = list of ints, n = int with how many numbers in a"
    element_string = ""
    a.reverse()
    if check_int(n):
        for i in a:
            if n >= i and check_ele(i):
                element_string += (str(i) + ' ')
        print(element_string)

def check_int(n):
    if (1 <= n and n <= 10**3):
        return True
    else:
        return False

def check_ele(n):
    if (1 <= n and n <= 10**4):
        return True
    else:
        return False

# Constraints
# 1 <= N <= 10^3
# 1 <= Ai <= 10^4, where Ai is the ith int in A.

if __name__ == '__main__':
    # The first line contains an integer, N (no of ints in A).
    # The second line contains N space-sperated integers describeing A.
    print_list_elements([1,2,3], 3)
