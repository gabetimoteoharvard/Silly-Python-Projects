

import math

class AlgorithmSolver:
    def __init__(self):
        self.name = 'Gerald'


    def dijkstra_shortest_path(self, nodes, graph, first_node, ending_node):
        "apply dijkstra's shortest path algorithm to find the shortest distance between two nodes in a graph"
         
        nodes = list(nodes) #list of all our nodes.
        distances = {} #distance of each node from the starting node.

        #sets up our initial distance estimates, which we will change as the algorithm progresses.
        for n in nodes: 
            if n == first_node:
                distances[n] = 0
            else:
                distances[n] = math.inf

        current_node = first_node #this variable refers to the current node we're looking at in our algorithm, this will be updated as the algorithm goes on.
        visited_nodes = set() #this set will keep track of what nodes we've already visited.

        
        while True:

            next_node = -1 #this variable keeps track of what node we will go to next.
            min_distance = math.inf #we will use this variable to see which node has the smallest distance from the initial node.

            for node in graph[current_node].keys(): #this will look at each neighbor of our current_node.
                if node not in visited_nodes: #the neighbor must be unvisited
                    distance = distances[current_node] + int(graph[current_node][node]) #we calculate the distance by adding our current distance to the distance between our current node and its neighbor.
                    if distance < distances[node]:
                        distances[node] = distance #if the distance is smaller than its previous distance, then we update it, otherwise we do nothing.

            visited_nodes.add(current_node) #after we visit all of the current node's neighbors and update their distances, we are done with it and mark it as a visited node.


            #we choose the next node we'll go to by taking the unvisited node with the minimum distance to the starting node.
            for node in distances:
                if distances[node] < min_distance and node not in visited_nodes:
                    min_distance = distances[node]
                    next_node = node

            #change our current node
            current_node = next_node

            #if this current node is our destination, then we are done with the algorithm and can break out of it. Otherwise, keep going with it.
            if current_node == ending_node:
                break


        return distances[ending_node] #will return the distance of our starting node to the ending node
                     
               


def main():

    solver = AlgorithmSolver()
    nodes = set()
    graph = {} #shows each node and what other nodes they're connected to

    print(f'Enter an edge in the form of XY Z, for example if the edge is from A to B and their distance is 3, then enter it as AB 3.') #explanation for input

    while True:
        print(f'\nEnter an edge of your graph? y/n \n')
        answer = input()

        if answer.lower().strip() == 'n':
            break
        elif answer.lower().strip() == 'y':
            edge = "".join(input("\n").split())

            nodes.add(edge[0])
            nodes.add(edge[1])

            if edge[0] not in graph:
                graph[edge[0]] = {edge[1]: edge[2:]}
            else:
                graph[edge[0]][edge[1]] = edge[2:]

    starting_node = input("Enter starting point: \n").strip().upper()
    ending_node = input("Enter ending point: \n").strip().upper()

    
    length = solver.dijkstra_shortest_path(nodes, graph, starting_node, ending_node)
    print(length)


if __name__ == '__main__':
    main()




