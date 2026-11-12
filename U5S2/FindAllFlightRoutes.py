"""You are given a flight network represented as a directed acyclic graph (DAG) with n airports, 
labeled from 0 to n - 1. Your goal is to find all possible flight paths from airport 0 
(the starting point) to airport n - 1 (the final destination) and return them in any order.

The flight network is given as follows: flight_routes[i] is a list of all
airports you can fly to directly from airport i (i.e., there is a one-way flight
                                                  from airport i to airport 
                                                  flight_routes[i][j]).

Write a function that returns all possible flight paths from 
airport 0 to airport n - 1.



UMPIRE:
Understand: 
   Input: a list of list where the ith index of outer list contains a list 
   of all the airport where theres a flight from airport i  
    

   Output:an integer representing the number of connections that need to be redirected to be able to 
   reach airport 0 from every other airport   
   Edge case: an element in one path is also in a seperated path -> have a visited list for each path

   
Match: 
-Graph traversal, 
-find every route from a source to a certain destination->
    dfs but keep track of every possible route it takes 


 
    
   
Plan:
    -dfs have a varaible representing the visted set for current path
    -if the current element equals n-1, add the local visted set to the output list;
    this ensures only paths that reaches n-1 are included
    -otherwise call dfs on neightbor, passing the current local set with a new empty set
        this is to track new path because every neighbor is a path to be explored



Implementation: see below

Evaluation:
Time: O(V+E) for every vertices we explore all its edges
Space: O(V^2): recusion stack which can get up to V size contains local
 set which can also be at worst v. V is number of vertices

"""

def find_all_flight_routes(flight_routes):
    output = []
    def dfs(curr, locVisited):
        
        locVisited.add(curr)
        if curr == len(flight_routes) - 1:
            output.append(list(locVisited))
            return
        
        for elem in flight_routes[curr]:
            if elem not in locVisited:
                newLocal = set()
                dfs(elem, locVisited.union(newLocal))

    dfs(0, set())
    return output
    


flight_routes_1 = [[1, 2], [3], [3], []]

print(find_all_flight_routes(flight_routes_1))


"""[[0, 1, 3], [0, 2, 3]]
Explanation: 
- There are two possible paths from airport 0 to airport 3.
- The first path is: 0 -> 1 -> 3
- The second path is: 0 -> 2 -> 3
Example Usage 2:"""



flight_routes_2 = [[4,3,1],[3,2,4],[3],[4],[]]

print(find_all_flight_routes(flight_routes_2))
"""Example Output 2:

[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]"""