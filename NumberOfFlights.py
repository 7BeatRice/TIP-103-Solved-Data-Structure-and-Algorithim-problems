"""You are a travel planner and have an adjacency matrix flights with n airports labeled 0 to n-1 where flights[i][j] indicates CodePath Airlines offers a flight from airport i to airport j. You are planning a trip for a client and want to know the minimum number of flights (edges) it will take to travel from airport start to their final destination airport destination on CodePath Airlines.

Return the minimum number of flights needed to travel from airport i to airport j. If it is not possible to fly from airport i to airport j, return -1.

UMPIRE:
Understand: 
    Input: adjacency matrix, where elemeint flights[i][j] = 1 means theres a flight from i to j
    i the start and j the destionation
    output:an integer representing the minimum  number of flights from i to j
    
    Edge case: i = j -> return 0 
    a cycle exist -> use visited set
   
    Match: 
    shortest path -> bfs  
   
Plan:
    -create visted set
    -bfs from start to dest
    -pass in current level in each bfs call, updating it each call
     -when element is destination (j), stop bsf amd return current level  


Implementation: see below
Evaluation:
Time: O(V+E) for every vertices that is reachable, we explore all its edges
Space: O(V): queue and set

"""
from collections import deque
def counting_flights(flights, i, j):
    queue = deque([i])
    visited = set([i])

    def bfs(queue, level):
        if not queue:
           return -1
        
        curr = queue.popleft()

        if curr == j:
            return level
        for m in range(len(flights[curr])):
           
            if flights[curr][m] == 1 and  m not in visited:
                
                visited.add(m)
                queue.append(m)
                return bfs(queue, level+1)
        return -1     

    return bfs(queue, 0)       
        
        
         
        

# Example usage
flights = [
    [0, 1, 1, 0, 0], # Airport 0
    [0, 0, 1, 0, 0], # Airport 1
    [0, 0, 0, 1, 0], # Airport 2
    [0, 0, 0, 0, 1], # Airport 3
    [0, 0, 0, 0, 0]  # Airport 4
]

print(counting_flights(flights, 0, 2))  
print(counting_flights(flights, 0, 4))
print(counting_flights(flights, 4, 0))
"""
Example Output:

1 
Example 1 Explanation: Flight path: 0 -> 2
3
Example 2 Explanation: Flight path 0 -> 2 -> 3 -> 4
-1
Explanation: Cannot fly from Airport 4 to Airport 0
"""