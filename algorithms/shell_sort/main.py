# Name              :   Shell Sort
# Version           :   Python 3.x
# Description       :   Implementation of Shell Sort (Iterative Method)
# Time Complexity   :   Best - O(n*Log(n)), Average - O(n*1.25) and Worst - O(n^2)
# Space Complexity  :   Worst - O(1)

import math


def shell_sort(param_arr):
    size = len(param_arr)
    d = math.ceil((size + 1) / 2)

    while d >= 1:
        for j in range(d, size):
            value = param_arr[j]
            k = j - d
            while k >= 0 and value < param_arr[k]:
                param_arr[k + d] = param_arr[k]
                k = k - d
            param_arr[k + d] = value
        d = int(d / 2)

    print(param_arr)


if __name__ == "__main__":
    arr = []

    try:
        while True:
            n = int(input("Enter the element: "))
            arr.append(n)
    except ValueError:
        print("Input array is :", end=" ")
        print(arr)

        print("\nSorted array is : ", end=" ")
        shell_sort(arr)
