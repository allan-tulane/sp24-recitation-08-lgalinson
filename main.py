from collections import deque
import heapq

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    shortest_paths = {vertex: (float('inf'), float('inf')) for vertex in graph}
    shortest_paths[source] = (0, 0)  # Distance and edges to source is zero
    
    # priority queue to keep track of the minimum path and edges (weight, edges, vertex)
    priority_queue = [(0, 0, source)]
    
    while priority_queue:
        current_distance, current_edges, current_vertex = heapq.heappop(priority_queue)
        
        # for each neighbor in the graph's current vertex
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            edges = current_edges + 1
            
            # check if found a shorter path, or same length but fewer edges
            if (distance < shortest_paths[neighbor][0]) or (distance == shortest_paths[neighbor][0] and edges < shortest_paths[neighbor][1]):
                shortest_paths[neighbor] = (distance, edges)
                heapq.heappush(priority_queue, (distance, edges, neighbor))
                
    return shortest_paths
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    parents = {source: None}
    queue = deque([source])

    while queue:
      current_node = queue.popleft()
      for neighbor in graph[current_node]:
          if neighbor not in parents:  
              parents[neighbor] = current_node  
              queue.append(neighbor)  

    return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    path = []
  
    while parents[destination] is not None:
        path.append(parents[destination])
        destination = parents[destination]
    
    return ''.join(path[::-1])
