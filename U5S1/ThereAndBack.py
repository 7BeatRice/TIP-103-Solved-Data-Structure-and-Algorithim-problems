
"""As a flight coordinator for CodePath airlines, you have a 0-indexed adjacency
   list flights with n nodes where each node represents the ID of a different
    destination and flights[i] is an integer array indicating that there is a 
    flight from destination i to each destination in flights[i]. Write a function
    bidirectional_flights() that returns True if for every flight from a destination 
    i to a destination j there also exists a flight from destination j to destination i.
    Return False otherwise."""

"""
UMPIRE:
Understand: 
    Input: adjacency list
    Output: boolean indicating whether every index i has a flight back to it from the integers it can reach
    Edge: empty input -> return false
    There exist an indirect path back to i -> return false because problem askes for a flight from j to i,
    so it must be an adjacency set
Match: 
    - direct flight -> adjacency list
Plan:
    iterate through keys of adjacency matrix i:
        for each i iterate through each of its neighbor j
        check if i in j's neighbor
            if not return false         
         return true at end
Implementation: see below
Evaluation:
Time: O(V + E * deg(n)) n represents the len of the neighbor list of a particular neighbor of v. 
Space: O(1): no additional data structure was created    

"""        
def bidirectional_flights(flights):
    for i in range(len(flights)):
        for j in flights[i]:
            if i not in flights[j]:
                return False
    return True        


flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]
flights3 = [[1, 2], [3], [0], [2]]
print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))
print(bidirectional_flights(flights3))
"""Example Output:

True
False"""
