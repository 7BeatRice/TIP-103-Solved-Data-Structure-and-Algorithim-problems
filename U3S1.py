"""


# You're working at a deli, and need to count the layers of a sandwich to make sure you made the order correctly. 
# Each layer is represented by a nested list. Given a list of lists sandwich where each list [] represents a sandwich layer,
#  write a recursive function count_layers() that returns the total number of sandwich layers.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale 
# for why you believe your solution has the stated time and space complexity.


# U: Input: nested list of an interger as first element, and list as 2nd element
#     Output: the number of layers, aka number of list present
#     Constraint: must be implemented recuresivly
#     edgecase: a layer contains multiple list, would have to choose the max nested layer
#         input does not permit this, so I won't handle
#         if i was to handle For each element in a list that is a list, recruivelt add the max of the recursive solution
#         to current call. ex if a list has an element, list1, list2, I would add the max of the number of layers in list1 and list2


# Match: recursion, making the problem smaller each iteration, stoping at smalles unit where I can't recurse again
# Plan:
#     recurse over the size of the list
#     base case:
#         lenght of sandwhich is 1 (no more layers), return 1
#         call count_layers on second element in list
#         return 1 (for current layer) + the output of next recursion

# Implement & Review:


def count_layers(sandwich):
    if len(sandwich) <= 1:
        return len(sandwich)
    if len(sandwich) == 2:
        return 1 + count_layers(sandwich[1])
    else:
            return 1 + max(count_layers(sandwich[i]) for i in range(1, len(sandwich)))
    

    



sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]
sandwich3 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]], ["lettuce", ["tomato", ["bread"]]]]]]
sandwich4 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]], ["lettuce", ["tomato", ["bread"], ["lettuce", ["tomato", ["bread"]]]]]]]]

print(count_layers(sandwich1))
print(count_layers(sandwich2))
print(count_layers(sandwich3))
print(count_layers(sandwich4))

#Evaluate:
# Time Complexity: O(l) where l is the number of layers
# Space Complaxity: O(l)
# Expected Output:

# 4
# 5
# 6
# 8
"""


