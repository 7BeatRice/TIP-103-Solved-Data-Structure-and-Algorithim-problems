"""You are a pilot navigating a new airport and have a map of the airport
represented as an undirected star graph with n nodes where each node 
represents a terminal in the airport labeled from 1 to n. 
You want to find the center terminal in the airport 
where the pilots' lounge is located.

Given a 2D integer array terminals where each 
terminals[i] = [u, v] indicates that there is a path (edge) 
between terminal u and v, return the center of the given airport.

A star graph is a graph where there is one center node
and exactly n-1 edges connecting the center node ot every other node."""


"""
UMPIRE:
Understand: 
    Input: edge list of star graph
    Output: value of the  node indicating the center of airport
    Edge: only one edge connecting two different nodes -> return either
    empty list return none 
    Match: 
    - every other vertex that is not the center has only one edge connecting it to center
    therefore I only need to check 2 different edges  and  return val of node that is in both edge
Plan:
    handle edge case
    check 2 different edges and return val of node that is in both edge

Implementation: see below
Evaluation:
Time: O(1) only checking exactly 2 edges and all edge are an array of 2 elements
Space: O(1): no additional data structure was created 
"""
def find_center(terminals):
    if len(terminals) == 0:
        return None
    if len(terminals) == 1:
        return terminals[0][0]
    a, b = terminals[0]
    if a in terminals[1]:
        return a
    else:
        return b 
terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]
terminals3 = []
terminals4 = [[1,2]]

print(find_center(terminals1))
print(find_center(terminals2))
print(find_center(terminals3))
print(find_center(terminals4))
"""
Example Output:

2
1
None
1
"""