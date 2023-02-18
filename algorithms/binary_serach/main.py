# Name              :   Binary Search
# Version           :   Python 3.x
# Description       :   Implementation of Binary Search (Iterative Method)
# Time Complexity   :   Best - O(1), Average - O(log(n)) and Worst - O(log(n))
# Space Complexity  :   Worst - O(1)

# binary search function definition, accepts sorted(ascending here) list and element to be searched as parameter
def binary_search(param_list, param_search_element):
    low, high = 0, len(param_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if param_list[mid] == param_search_element:
            return mid
        # if the element to be searched is less than mid-element, then we need to search in left half of the list
        elif param_list[mid] > param_search_element:
            high = mid - 1
        # else, only case is, when searching element is greater than mid-element,
        # then we need to search in right half of the list
        else:
            low = mid + 1

    return -1   # when element not found


# main
num_list = []
try:
    # get the list from user
    while True:
        n = int(input("Input number in a list: "))
        num_list.append(n)
except ValueError:
    # sort the list
    num_list.sort()
    print(num_list)

    # get the element that is to be searched
    search_element = int(input("Enter search Element: "))
    result = binary_search(num_list, search_element)
    if result == -1:
        print("Not found")
    else:
        print(f"Element present at index: {result}")


'''
Few points about binary search
- Efficient, after each iteration it reduces the list size to half
- Sorted list/array of numbers must be passed in function
'''