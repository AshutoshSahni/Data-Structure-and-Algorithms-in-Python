# Name              :   Linear Search
# Author            :   Ashutosh Sahni
# Version           :   Python 3.x
# Description       :   Implementation of Linear Search
# Time Complexity   :   Best - O(1), Average - O(n) and Worst - O(n)
# Space Complexity  :   Worst - O(1)

# linear search function definition
def linear_search(param_my_list, param_search_element):
    position = 0
    while True:
        # return position of search element if found in list
        if param_my_list[position] == param_search_element:
            return position

        position += 1
        # return -1 if search element not in list
        if position == len(param_my_list):
            return -1


# main
test = {
    'my_list': [2, 4, 9, 3, 0, 2, 10, 44, -5],
    'search_element': 3
}

result = linear_search(test['my_list'], test['search_element'])
print(f"Element present at index {result}")
