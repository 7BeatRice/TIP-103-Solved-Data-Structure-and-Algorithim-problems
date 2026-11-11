"""You are applying to become a pilot for CodePath Airlines, and you must complete a series
   of flight training courses. There are a total of num_courses flight courses you have
to take, labeled from 0 to num_courses - 1. Some courses have prerequisites that must be 
completed before you can take the next one.

You are given an array flight_prerequisites where flight_prerequisites[i] = [a, b]
indicates that you must complete course b first in order to take course a.

For example, the pair ["Advanced Maneuvers", "Basic Navigation"] indicates that to take 
"Advanced Maneuvers", you must first complete "Basic Navigation".

Return True if it is possible to complete all flight training courses. 
Otherwise, return False.


UMPIRE:
Understand: 
    Input: Integer indicating num of course required to take
   and a list of list where the inner list has 2 element, the first is the couse and 
   the second is its prequisite course/
    

    output:a boolean indcating whether you can take the given number of course or not
   Edge case: There is a requirement where multiple diffrent courses require same prerquist
   ; with global visited set it would detect this as a cycle, so we need a pre dfs visited set
   -There are multiple connected components-> iterate through entire courses

   
    Match: prerequisits -> cycle detection -> dfs
    
   
Plan:
    -create a set of all the courses
    -create adjacency list key = course elem = visited
    -iterate through set
    -dfs on element adding it to global visited set, while having a local visited set for 
    -dfs should return the numer of course, if cycle ever exit in dfs, set num of courses to zero and return 0
    - have a max num of couses, and compare each time dfs is runned 



Implementation: see below
Evaluation:
Time: O(V+E) for every vertices we explore all its edges
Space: O(V^2): at most v dfs call that holds at most |localVisited| = v elements


"""



from collections import defaultdict 
def can_complete_flight_training(num_courses, flight_prerequisites):
    courses = set()
    visited = set()
    adjacency = defaultdict(list)

    for a, b in flight_prerequisites:
        courses.add(a)
        courses.add(b)
        adjacency[a].append(b)
    
  
    def dfs(curr, locVisted):
        if curr in locVisted:
            return False
        if curr not in adjacency:
            return True
        locVisted.add(curr) 
        visited.add(curr)
        for elem in adjacency[curr]:
            return dfs(elem, locVisted)
                

    
    for course in courses:
        if course not in visited:
           localVisited = set()
           valid = dfs(course, localVisited)
           if not valid:
               return valid
           

    return True       
           

flight_prerequisites_1 = [['Advanced Maneuvers', 'Basic Navigation']]
flight_prerequisites_2 = [['Advanced Maneuvers', 'Basic Navigation'], ['Basic Navigation', 'Advanced Maneuvers']]
flight_prerequisites_3 = [['Advanced Maneuvers', 'Basic Navigation'], ['Basic Navigation', 'Advanced Maneuvers'], ["Algo", "data"]]

print(can_complete_flight_training(2, flight_prerequisites_1))
print(can_complete_flight_training(2, flight_prerequisites_2))
print(can_complete_flight_training(4, flight_prerequisites_3))


"""True
Example 1 Explanation: There are 2 flight training courses. To take *Advanced Maneuvers*, 
you must first complete *Basic Navigation*. This is possible.
False
Example 1 Explanation: There are 2 flight training courses. To take *Advanced Maneuvers*, 
you must first complete *Basic """