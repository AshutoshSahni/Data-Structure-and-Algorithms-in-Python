# Name              :   Linear Search
# Version           :   Python 3.x
# Description       :   Implementation of Linear Search
# Time Complexity   :   Best - O(1), Average - O(n) and Worst - O(n)
# Space Complexity  :   Worst - O(1)

# linear search function definition
def linear_search(param_my_list, param_search_element):
    position = 0
    while position < len(param_my_list):
        # return position of search element if found in list
        if param_my_list[position] == param_search_element:
            return position

        position += 1
    # return -1 if element not present in list
    return -1


# main
test = {
    'my_list': [2, 4, 9, 3, 0, 2, 10, 44, -5],
    'search_element': 2
}

result = linear_search(test['my_list'], test['search_element'])
print(f"Element present at index {result}")


'''
Few points about linear search
- It is very basic searching algorithm
- Not efficient, as in worst case we have to iterate through whole list to find an element
'''
