"""There are n airports numbered from 0 to n - 1 and n - 1 direct
flight routes between airports such that there is exactly one way to travel
between any two airports (this network forms a tree). Last year, the aviation
authority decided to orient the flight routes in one direction due to air traffic regulations.

Flight routes are represented by connections, where connections[i] = [airport_a, airport_b]
represents a one-way flight route from airport airport_a to airport airport_b.

This year, there will be a major aviation event at the central hub (airport 0), 
and many flights need to reach this hub.

Your task is to reorient some flight routes so that every airport can 
send flights to airport 0. Return the minimum number of flight routes that 
need to be reoriented.

It is guaranteed that after the reordering, each airport will be able to
send a flight to airport 0.

UMPIRE:
Understand: 
   Input: input an integer representing the number of airports/elements, a list of list
    where the inner elements contains two elements, the first is the source airport  
    the second is the destination airport
    

   Output:an interger reprseting the number of connections that need to be redirectd to be able to 
   reach airport 0 from every other airport   
   Edge case: all elements are already orientated to 0, return 0

   
Match: 
-Graph traversal, 
-orientated to 0 is finding path to zero->dfs

Constraint:
- The number of edges are exactly n-1 
    
   
Plan:
    -create a set of all the courses
    -create a set of pairs where the connections is a pair 
    -create Visited set
    -have a variable to track the number of reorientations: redirects
    -create adjacency list: where for every connection add 2 key -value pairs:
    source: dest and dest:source (this allows for every possible path from a node 
    to 0 to be explore even if the path didn't exist in the original connections)
    -iterate through set
    -dfs on element adding it to visited set,
    -include parent in dfs argument
    -for every element if (parent, element) exists in the set 
    of original pairs,  increment redirects. This is because in the graph the edge 
    is pointing away from zero, so we have to change its direction to point towards zero   
    -we start dfs on 0
    -at end return redirects 



Implementation: see below

Evaluation:
Time: O(V+E) for every vertices we explore all its edges
Space: O(V+E): store all the connections which also contains edges


"""
from collections import defaultdict
def min_reorient_flight_routes(n, connections):
    allConnections = defaultdict(set)
    ogConnections = set()
    redirects = 0
    visited = set()

    for start, end in connections:
        allConnections[start].add(end)
        allConnections[end].add(start)
        ogConnections.add((start, end))

    
    def dfs(val, parent):
        nonlocal redirects
        visited.add(val)
        if (parent, val) in ogConnections:
            redirects += 1
        
        for elem in allConnections[val]:
            
            if elem not in visited:
               
                if (parent, elem) in ogConnections:
                    redirects += 1
                dfs(elem, val)

    dfs(0, -1) 
    return redirects





n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
connections2 = [[6, 0], [1, 6], [2, 1], [5, 2], [9, 8], [3, 8], [3, 0], [0,4]]

print(min_reorient_flight_routes(n, connections))
print(min_reorient_flight_routes(9, connections2))
"""Example Output:

3
Explanation: 
- Initially, the flight routes are: 0 -> 1, 1 -> 3, 2 -> 3, 4 -> 0, 4 -> 5
- We need to reorient the routes [1, 3], [2, 3], and [4, 5] to ensure that
every airport can send a flight to airport 0""" 