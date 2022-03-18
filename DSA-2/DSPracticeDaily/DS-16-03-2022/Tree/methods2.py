class TreeNode:
	def __init__(self, data):
		self.data = data
		self.children = []
		self.parent = None
	
	def add_child(self, child):
		child.parent = self
		self.children.append(child)

	def get_level(self):
		level = 0
		p = self.parent
		while p:
			level += 1
			p = p.parent
		
		return level

	def print_tree(self):
		spaces = " " * self.get_level() * 3
		prefix = spaces + " |-- " if self.parent else ""
		
		print(prefix + self.data)
		
		if len(self.children):
			for child in self.children:	
				child.print_tree()


def build_exercise_tree():
	root = TreeNode("Sessions")

	pull = TreeNode("Pull")
	pull.add_child(TreeNode("Barbell row"))
	pull.add_child(TreeNode("Lat Pulldown"))

	push = TreeNode("Push")
	push.add_child(TreeNode("Push-Ups"))
	push.add_child(TreeNode("Bench Press"))

	legs = TreeNode("Legs")
	legs.add_child(TreeNode("Squats"))
	legs.add_child(TreeNode("Lunges"))

	root.add_child(pull)
	root.add_child(push)
	root.add_child(legs)
		
	return root

if __name__ == "__main__":
	b = build_exercise_tree()
	b.print_tree()


		