"""
You are a traveler about to embark on a multi-leg journey with multiple flights
 to arrive at your final travel destination. You have all your boarding passes,
   but their order has gotten all messed up! You want to organize your boarding
     passes in the order you will use them, from your first flight all the way
       to your last flight that will bring you to your final destination.

Given a list of edges boarding_passes where each element boarding_passes[i]
 = (departure_airport, arrival_airport) represents a flight from departure_airport to
   arrival_airport, return an array with the itinerary listing out the airports you will
     pass through in the order you will visit them. Assume that departure is scheduled from
       every airport except the final destination, and each airport is visited only once
         (i.e., there are no cycles in the route).



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
    -while the current element is in the keys of the adjacency list
    -add it to the array, and set it to the value of the current key in the adjacycny list
    -when the while loop ends, curr would be the destination airport, since it won't be in the keys
    which are the departure_airport.
    -finally, add curr to array and return the array



    Evaluation:
    Time Complexity: O(v) - since the description states that each airport is visted exactly once,
      this means there are exactly v-1 edges where v is the vertex. so V is greater.
      my solution visits the vertices once using a while loop so its O(v).
      Creating the adjacency list was O(m)

      Space Complexity: O(V+E) the adjacency list and the destination set was the additional data structure
      

             """
from collections import defaultdict 
def find_itinerary(boarding_passes):
    destinations = set([elem[1] for elem in boarding_passes])
    sourceToMap = defaultdict()
    start = None

    output = []
    for source, dest in boarding_passes:
      if source not in destinations:
          start = source
      sourceToMap[source] = dest
    
       
        
   
    curr = start

    while curr in sourceToMap:
      output.append(curr)
      curr = sourceToMap[curr]
      
    output.append(curr)
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
Example Output:

['LAX', 'SFO', 'JFK', 'ATL', 'ORD']
['LHR', 'DFW', 'JFK', 'LAX', 'DXB']
"""