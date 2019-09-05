#Author: Dinh-Mao Bui, Anh-Tu Nguyen
#Rule of traversing: Alphabetical ordered, then left to right,
#Points: 2
def traverse(tree, init):
	queue = [init]
	traversed = []
	while queue:
		'''
			Student fixes the loopy path from here to the end of this function
		'''
		node = queue.pop(0)
		traversed.append(node)
		leaves = tree[node]
		for leaf in leaves:
			if leaf in traversed or leaf in queue:
				continue
			queue.append(leaf)
	return traversed

#Points: 3
def pathfinder(tree, init, goal):
	traversed = []
	queue = [init]
	predecessor = {}
	if init == goal:
		return "No kidding, pls"
	while queue:
		'''
			You implement the path finder from here
		'''
		node = queue.pop(0)
		if node == goal:
			final_path = [node]
			while node != init:
				node = predecessor[node]
				final_path.insert(0, node)
			return final_path

		traversed.append(node)
		leaves = tree[node]
		for leaf in leaves:
			if leaf in traversed or leaf in queue:
				continue
			predecessor[leaf] = node
			queue.append(leaf)
	return "No such path exists"

