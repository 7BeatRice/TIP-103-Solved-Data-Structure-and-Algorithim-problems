"""if you implemented find_itinerary() in the previous problem without using Depth First Search,
 solve it using DFS. If you solved it using DFS, try solving it using an alternative 
 approach.
 
 UMPIRE:
  Understand: 
  Input: I am given an array of  pairs where the first element is the source and the second is
  the destination. 
  Ouptut: output of airport in the order they are visited from start to destination
  Edgecase:if there were multiple routes from source to destination, choosing one requires 
  dfs
  Constraint: 
  Match: Since we are given a list of edges and asked to find the path from source to destination 
  this indicates this is  a form of path finding which usually uses adjacency list

  Plan: 
    -first find the source airport by creating a set of destination ad seeing which airport 
    is not in it
    -Next, create adjacency list where key is departure_airport and value is departure_airport  of each edge
    -set the current element to start, ]
    -call dfs, passing 
    -use adjacency list to visit the value in the addjacnecy list of curr element
    -in dfs add element to array
    -return output


    Evaluation:
    Time Complexity: O(v) - since the description states that each airport is visted exactly once,
      this means there are exactly v-1 edges where v is the vertex. so V is greater.
      my solution visits the vertices once usingrecursion so its O(v).
      Creating the adjacency list was O(m)

      Space Complexity: O(V+E) the adjacency list and the destination set was the additional data structure
      
 """

from collections import defaultdict 
def find_itinerary(boarding_passes):
    destinations = [elem[1] for elem in boarding_passes]
    adjacecnyList = defaultdict()
    output = [] 
    start = None

    for source, dest in boarding_passes:
        adjacecnyList[source] = dest
        if source not in destinations:
            start = source

   

    def dfs(curr):
        output.append(curr)
        if curr in adjacecnyList:
            dfs(adjacecnyList[curr])

    dfs(start)
    return output        



boarding_passes_1 = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

print(find_itinerary(boarding_passes_1))
print(find_itinerary(boarding_passes_2))
"""

['LAX', 'SFO', 'JFK', 'ATL', 'ORD']
['LHR', 'DFW', 'JFK', 'LAX', 'DXB']
"""