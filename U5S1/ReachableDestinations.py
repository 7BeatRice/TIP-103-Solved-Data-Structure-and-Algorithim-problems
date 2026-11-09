"""You are a travel coordinator for CodePath Airlines, and you're helping
   a customer find all possible destinations they can reach from a starting airport. 
The flight connections between airports are represented as an adjacency dictionary flights, 
where each key is a destination, and the corresponding value is a list of other destinations 
that are reachable through a direct flight.

Given a starting location start, return a list of all destinations reachable from the start 
location either through a direct flight or connecting flights with layovers. The list should be 
provided in ascending order by number of layovers required."""

"""
UMPIRE:
Understand: 
    Input: adjacency list and a start value
    Output: list of values of nodes reachable from start, sorted by the number of layovers
    between start node and the value 
    Edge case: empty list return empty list
    Cycle: have visted set
          
    Match: 
    reachability  in graph-> dfs or bfs
    order by number of layovers from start node to given node reachble from start -> BFS WE WANT TO process closest nodes first
Plan:
    create visited set
    add start to visited
    bfs
    add each element to output when you visit it
    return output

Implementation: see below
Evaluation:
Time: O(V+E) for every vertices that is reachable, we explore all its edges
Space: O(V): output list, queue and visited set could potentially store all vertices
"""

from collections import deque
def get_all_destinations(flights, start):
    output = [start]
    queue = deque([start])
    visited = set([start])
    while queue:
        curr = queue.popleft()
        for elem in flights[curr]:
            if elem not in visited:
                visited.add(elem)
                output.append(elem)
                queue.append(elem)
    return output           

flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": ["Helsinki", "Reykjavik"]   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))
"""

['Beijing', 'Mexico City', 'Helsinki', 'Sydney', 'Cairo', 'New York', 'Tokyo', 
'Reykjavik']
['Helsinki', 'Cairo', 'New York', 'Reykjavik']
"""