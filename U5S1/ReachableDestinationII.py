"""You are a travel coordinator for CodePath Airlines, and 
you're helping a customer find all possible destinations they
can reach from a starting airport. The flight connections between 
airports are represented as an adjacency dictionary flights,
where each key is a destination, and the corresponding value is a 
list of other destinations that are reachable through a direct flight.

Given a starting location start, write a function get_all_destinations() 
that uses Depth First Search (DFS) to return a list of all destinations 
that can be reached from start. The list should include both direct and 
connecting flights and should be ordered based on the order in which airports 
are visited in DFS."""


"""
UMPIRE:
Understand: 
    Input: adjacency list and a start value
    Output: list of values of nodes reachable from start
   Edge case: empty list return empty list
        Cycle: have visted set
          
    Match: 
    mentions dfs> dfs
  Plan:
    create visited set
    add start to visited
    dfs helper
    add each element to output when you visit it
    return output

Implementation: see below
Evaluation:
Time: O(V+E) for every vertices that is reachable, we explore all its edges
Space: O(V): output list, queue and visited set could potentially store all vertices
"""

def get_all_destinations(flights, start):
    visited = set([start])
    output = [start]

    def dfs(start):
        if start in flights:
            for elem in flights[start]:
                if elem not in visited:
                    visited.add(elem)
                    output.append(elem)
                    dfs(elem) 
    dfs(start)            
    return output            


flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"]   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))
"""
Example Output:

['Beijing', 'Mexico City', 'Sydney', 'Tokyo', 'Helsinki', 'Cairo', 'Reykjavik', 
'New York']
['Helsinki', 'Cairo', 'Reykjavik', 'New York']
"""