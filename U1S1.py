"""# Write a function linear_search() to help Winnie the Pooh locate his lost items. 
# The function accepts a list items and a target value as parameters. 
# The function should return the first index of target in items
# , and -1 if target is not in items. Do not use any built-in functions.

# UMPIRE:
# Understand: 
#     Input: array of strings called items and a string called target
#     Output: index of target in liarray st, if it exist or -1
#     Edge Case: -Empty List, return -1
#             -target doesn't have same type as items in array, then it won't match using equality
#             it would result in a -1 return Value
# Match: 
#     since index is needed, simple array transversal works
# Plan: transverse array using index, if value at index match return index, at end return -1
# Implement & Result: below
# Evaluate: Time: O(n) simple array traversal
# Space: O(1) no extra data structure

def linear_search(items, target):
	for i in range(len(items)):
		if items[i] == target:
			return i
	return -1


items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(linear_search(items, target))

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(linear_search(items, target))
# Example Output:

# 3
# -1



"""
"""

# Tigger has developed a new programming language Tiger with only four operations
#  and one variable tigger.

# bouncy and flouncy both increment the value of the variable tigger by 1.
# trouncy and pouncy both decrement the value of the variable tigger by 1.
# Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.


# UMPIRE:
# Understand: 
#     Input: array of strings called operations
#     Output: int val representing the final value of triggers
#     Edge Case: oparation in input, is not one of the 4 operations: don't increment or decrement

# Match: 
#     simple match statement since input is limited
# Plan: set trigger as 1, and create 4 case of the 4 operations and decrement or incrment
#       Iterate through value and decrement 
# Implement & Result: below
# Evaluate: Time: O(n) simple array traversal
# Space: O(1) no extra data structure
def final_value_after_operations(operations):
    tigger = 1
    for operation in operations:
        match operation:
            case "bouncy" | "flouncy":
                tigger += 1
            case "trouncy" | "pouncy":
                tigger -= 1
    return tigger


operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))
# Example Output:

# 2
# 4
"""




# Problem 3: T-I-Double Guh-Er II
# T-I-Double Guh-Er: That spells Tigger!
#  Write a function tiggerfy() that accepts a string word 
# and returns a new string that removes any substrings t, i, gg,
# and er from word. The function should be case insensitive.

def tiggerfy(word):
	pass


word = "Trigger"
tiggerfy(word)

word = "eggplant"
tiggerfy(word)

word = "Choir"
tiggerfy(word)
# Example Output:

# "r"
# "eplan"
# "chor"