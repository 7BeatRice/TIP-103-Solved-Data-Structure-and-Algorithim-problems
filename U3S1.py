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

# Implement & Review: below
#Evaluate:
        # Time: O(m * n) where m is the deepest layers and n is the number of nested layer in a single layer
        # Space: O(m * n) recursion stack would be size m with n stacks



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


# Expected Output:

# 4
# 5
# 6
# 8
"""
"""

# The deli counter is busy, and orders have piled up. 
# To serve the last customer first, you need to reverse the order
# of the deli orders. Given a string orders where each individual 
# order is separated by a single space, write a recursive function
# reverse_orders() that returns a new string with the orders reversed.

# Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you 
# believe your solution has the stated time and space complexity.


# U: Input: a string of words
#     Output: a string with the word order reversed
#     Constraint: must be implemented recuresivly
#     edgecase: lenght of word is 0 or 1: return string as it is
#        

# Match: recursion, list from string
#     recurse over the index
#         base case:
# #         i == len(list) - 1
#             return last element
#         if not base case:
#             return recusion + space + current elemeny at i
# Implement & Review: below
#Evaluate:
        # Time: O(n) recusive helper executes in o(1) * O(n) which is the  number of recusive call
        # Space: O(n): converted list to a string and recursive stack


def reverse_orders(orders):
    if (len(orders) == 0):
        return ""
    orderList = orders.split()
    def reverseHelper(orderList, i):
        if i==len(orderList) - 1:
            return orderList[i]
        return reverseHelper(orderList, i+1) + " " + orderList[i]
    return reverseHelper(orderList, 0)

print(reverse_orders("Bagel Sandwich Coffee"))
print(reverse_orders(""))
print(reverse_orders("Bagel"))
# Example Output:

# Coffee Sandwich Bagel
"""


"""

# The deli staff is in desperate need of caffeine to keep them going through their shift
# and has decided to divide the coffee supply equally among themselves. Each batch of coffee 
# is stored in containers of different sizes and must remain whole when distributed among n staff.
# Write a recursive function can_split_coffee() that accepts a list of integers coffee representing
# the volume of each batch of coffee and returns True if the coffee can be split evenly by volume 
# among n staff and False otherwise.

# Evaluate the time and space complexity of your solution. Define your variables and provide a 
# rationale for why you believe your solution has the stated time and space complexity.

# U: Input: list of int representingt size of a batch of coffee which can't be split and int 
#           representing number if members
#     Output: a boolean indicating whether coffee can be split evenly amonf n people
#     Constraint: must be implemented recuresivly
                    # - a given int representiing the volume of a container/batch of coffer
                    # and it must remain whole, meaning the individual int in the array can
                    # not be split
        
#     edgecase: length of array is 0; return false 
                

# Match: recursion and partition: subset sum
#     recurse over the partion of the coffee array
#        recursive helper
#Plan:  get sum  of coffee
#         if total not dividible by n, return False
#         get total / n, we want n partions where sum of partion each equal total/n (our target)
#         create recursive helper with coffee, n representing number of partions left, target 
#         which is the sum we want each partition to be, and current_sum of the current partition
        # Base case:
        # n == 0, no more partions needed return True

        # recursive function
        # if current sum is equal to target, Reduce number of partition left by 1 (n) 
        # and reset current sum to 0. 
        # recursively include or exclude current element of array from partition


# #Evaluate:
        # Time: O(2^n) tree like calls with include or exclude
        # Space: O(n^2): recusrive stack could at worst be n and each hold n elements since we sliced

def can_split_coffee(coffee, n):
    if len(coffee) == 0:
        if n== 0:
            return True
        else:
            return False
    total = sum(coffee)
    if total % n != 0:
        return False
    target = total//n

   
    

    def partition_sum(coffee, n, target, current_sum):
        if n == 0:
            return True
        
        if current_sum == target:
            return partition_sum(coffee, n-1, target, 0)
        if not coffee:
            return False
        include = partition_sum(coffee[1:], n, target, current_sum + coffee[0])
        exclude = partition_sum(coffee[1:], n, target, current_sum)
        return include or exclude
   
    
    return partition_sum(coffee, n, target, 0)

print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([7, 4, 1], 2))
print(can_split_coffee([5, 10, 15], 4))
# Example Output:

# True
# False
"""
