"""Given an adjacency dictionary of flights flights where each key is 
an airport i and flights[i] is an array indicating that there is a 
flight from destination i to each destination in flights[i], return an 
array with the flight path from a given source location to a given destination location.

If there are multiple flight paths from the source to destination, 
return any flight path.


UMPIRE:
Understand: 
    Input: adjacecy list, source string, destnation string

    output:array of valid path from source to destination

    Edge case: dest is disconnected from source -> return []

   
    Match: finding a path(any) from source to node -> dfs
    
   
Plan:
    -create visited set
    -dfs helper function
    -everytime a node is visited add to visited
    -if dest is not in visited return []
    
Implementation: see below
Evaluation:
Time: O(V+E) for every vertices that is reachable, we explore all its edges
Space: O(V): visited set


"""

def get_itinerary(flights, source, destination):
    visited = set()
    output = []
    def dfs(curr):
        visited.add(curr)
        output.append(curr)
        if curr == destination:
            return
        for elem in flights[curr]:
            if elem not in visited:
                dfs(elem)

    dfs(source)
    if destination not in visited:
        return []
    return output

flights = {
    'LAX': ['SFO'],
    'SFO': ['LAX', 'ORD', 'ERW'],
    'ERW': ['SFO', 'ORD'],
    'ORD': ['ERW', 'SFO', 'MIA'],
    'MIA': ['ORD']
}

print(get_itinerary(flights, 'LAX', 'MIA'))


"""['LAX', 'SFO', 'ORD', 'MIA']
Explanation: ['LAX', 'SFO', 'ERW', 'ORD', 'MIA'] is also a valid answer"""