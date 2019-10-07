#Assignment 2
from as2_tree import Tree
class Result:
	def __init__(self, sol=[], val=-1000):
			self.solution = sol
			self.value = val
			
class MNX:
	def __init__(self, data_list):
		self.tree = Tree()	
		self.tree.init_tree(data_list)
		self.root = self.tree.root
		self.currentNode = None
		self.successors = []		
		return
        
	def terminalTest(self, node):
		assert node is not None
		return len(node.children) == 0

	def utilityChecking(self, node):
		assert node is not None
		return node.value

	def getChildren(self, node):
		assert node is not None
		return node.children

	def minimax(self):		
		terminal_val = self.max_v(self.root)
		traversed=[]
		res=Result()
		temp_node = self.root
		while( temp_node != None):
			traversed.append(temp_node.Name)
			child_node = None
			for descendant in self.getChildren(temp_node):
				if(self.utilityChecking(descendant) == terminal_val):
					child_node = descendant
					break
			temp_node = child_node

#################  Return the solution here  #################
		res.value=terminal_val #you put the best terminal value for root node here
		res.solution=traversed #you put the solution_array here
#################  Return the solution here  #################



		return res


	def max_v(self, node):		
		if self.terminalTest(node):
			return self.utilityChecking(node)
		max_v = -1000 #1
		deeper_layer = self.getChildren(node)
		for deeper_node in deeper_layer:
			max_v = max(max_v, self.min_v(deeper_node))#2
		node.value = max_v
		return max_v

	def min_v(self, node):		
		if self.terminalTest(node):
			return self.utilityChecking(node)
		min_v = 1000 #3
		deeper_layer = self.getChildren(node)
		for deeper_node in deeper_layer:
			min_v = min(min_v, self.max_v(deeper_node))#4
		node.value = min_v
		return min_v