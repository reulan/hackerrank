"""
arraylr.py

Given an array of n integers and a number, d, perform d left rotations on the
array. Then print the updated array as a single line of space-separated integers.

mpmsimo
1/27/17
"""

def list_left_rotation(n, d):
    """Perform a left rotation on a list."""

if __name__ == "__main__":
    n, k = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    answer = list_left_rotation(a, n, k);
    print(*answer, sep=' ')
