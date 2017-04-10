import Queue





def runBFS(start, graph):
	seenNodes = [start]
	queue = Queue.Queue()
	queue.put(start)
	nodeHops = {x: -1 for x in range(1,len(graph.keys()) + 1)}
	nodeHops[start] = 0

	while not queue.empty():
		node = queue.get()
		#get all children
		children = graph[node]
		for c in children:
			#check if child already been seen
			if not c in seenNodes:
				queue.put(c)
				seenNodes.append(c)
				nodeHops[c] = nodeHops[node] + 1


	#BFS Ran
	nodeHops.pop(start)
	hopsList = nodeHops.items()
	hopsList.sort(key=lambda x: x[0])
	#convert the list
	hopsList = [(x,y * 6)  if y != -1 else (x,y) for (x,y) in hopsList]
	#print the list
	distances = [str(x[1]) for x in hopsList]
	print ' '.join(distances)



#Make graph a dictionary
def createGraphs():
	allGraphs = []
	numGraphs = input()
	currentIndex = 1
	for i in range(numGraphs):
		[n, m] = map(int, raw_input().split(' '))
		currentIndex += 1
		#Initialize newgraph
		newGraph = {x: [] for x in range(1,n+1)}
		for j in range(currentIndex, m + currentIndex):
			[a, b] = map(int, raw_input().split(' '))
			newGraph[a].append(b)
			newGraph[b].append(a)
			currentIndex += 1
		s = input()
		currentIndex += 1
		allGraphs.append((newGraph, s))
	return allGraphs





allGraphs = createGraphs()
for graph in allGraphs:
	runBFS(graph[1], graph[0])




