"""You are given an adjacency dictionary flights where for any location source,
   flights[source] is a list of tuples in the form (destination, cost)
indicating that there exists a flight from source to destination at ticket
price cost.

Given a starting location start and a final destination dest return the
total cost of flying from start to dest. If it is not possible to fly from
start to dest, return -1. If there are multiple possible paths from start
to dest, return any of the possible answers.

UMPIRE:
Understand: 
    Input: adjacecy list, where values are a list of uples where the first element is a destination
    and the second elment in the tuple is the cost to reach the destination from key

    output:an integer representing the cost from source to dest

    Edge case: dest is disconnected from source -> return -1

   
    Match: finding a path(any) from source to node -> dfs
    
   
Plan:
    -create visited set
    -dfs helper function, where cost is passed in as an argument
    -everytime a node is visited add to visited
    -increment cost argument by cost of destination we are going to
    -return cost when we reach the end



Implementation: see below
Evaluation:
Time: O(V+E) for every vertices that is reachable, we explore all its edges
Space: O(V): visited set

"""

def calculate_cost(flights, start, dest):
    visited = set()

    def dfs(source, cost):
        visited.add(source)
        if source == dest:
            return cost
        
        
        for elem, price in flights.get(source, []):
            if elem not in visited:
                val = dfs(elem, cost+price)
                if val != -1:
                    return val

        return -1
    return dfs(start, 0) 
flights = {
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50), ('ORD', 100), ('ERW', 210)],
    'ERW': [('SFO', 210), ('ORD', 300)],
    'ORD': [('ERW', 300), ('SFO', 100), ('MIA', 400)],
    'MIA': [('ORD', 400)]
}

print(calculate_cost(flights, 'LAX', 'MIA'))

flights = {
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50)],
    'MIA': []
}
print(calculate_cost(flights, 'LAX', 'MIA'))
"""Example Output:

550
Explanation: There is a path from LAX -> SFO -> ORD -> MIA
with ticket prices 50 + 100 + 400 = 550
960 would also be an acceptable answer following the path from LAX -> SFO -> ERW -> ORD -> MIA"""