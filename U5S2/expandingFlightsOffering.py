"""CodePath Airlines wants to expand their flight offerings so that for
any airport they operate out of, it is possible to reach all other airports. 
They track their current flight offerings in an adjacency dictionary flights 
where each key is an airport i and flights[i] is an array indicating that there 
is a flight from destination i to each destination in flights[i]. Assume that if 
there is flight from airport i to airport j, the reverse is also true.

Given flights, return the minimum number of flights (edges) that need to be
added such that there is flight path from each airport in flights to every 
other airport.

UMPIRE:
Understand: 
    Input: adjacecy list, where flights[key] is a list of string
    indicating theres a direct flight from key of to string representing 
    airport 

    output:an integer representing the min  number of flights needed to connect
    all airports, so every airport is reachable from every other airport
    Edge case: an airport is only reachable to itself -> increment number of flights by 1

   
    Match: when represeting this in graph notation, its a number of edges needed to be added
    to make all the connected components connected which is bfs + traversal
    
   
Plan:
    -create visited set
    -var count representing the number of flights needed to be added
     -iterate through keys of flights, if elemnt not in visitied
    -increment count b/c it means that the element wsn't reachable
    - stop recursion when len(visited) == len(flights), indicating 
    every element could be visited 
    





Implementation: see below
Evaluation:
Time: O(V+E) for every vertices,  we explore all its edges
Space: O(V): visited set

"""
from collections import deque
def min_flights_to_expand(flights):
    visited = set()
    flightsAdded = -1

    def bfs(elem):
        visited.add(elem)
        queue = deque([elem])
        while queue:
            curr = queue.popleft()
            for elem in flights.get(curr, []):
                if elem not in visited:
                    visited.add(elem)
                    queue.append(elem)

    for elem in flights.keys():
        if len(visited) == len(flights.keys()):
            return flightsAdded
        if elem not in visited:
            bfs(elem)
            flightsAdded += 1

    return flightsAdded                         




    

flights = {
 
    'JFK': ['LAX', 'SFO'],
    'LAX': ['JFK', 'SFO'],
    'SFO': ['JFK', 'LAX'],
    'ORD': ['ATL'],
    'ATL': ['ORD']
}

flights2 = {
    'JFK': ['LAX', 'SFO'],
    'LAX': ['JFK', 'SFO'],
    'SFO': ['JFK', 'LAX'],
    'ORD': ['ATL'],
    'ATL': ['ORD'],
    'TEX': ['MEX'],
    'MEX': ['TEX'],
    'CHI': ['CHI'],
    'TOK': ['KOR'],
    'KOR': ['TOK']

}
print(min_flights_to_expand(flights))
print(min_flights_to_expand(flights2))


"""
1
4
"""