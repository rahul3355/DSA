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
		prefix = spaces + "|--" if self.parent else ""

		print(prefix + self.data)
		
		if len(self.children):
			for child in self.children:
				child.print_tree()


def build_product_tree():
	root = TreeNode("Electronics")

	laptop = TreeNode("Laptop")
	laptop.add_child(TreeNode("Mac"))
	laptop.add_child(TreeNode("Surface"))
	laptop.add_child(TreeNode("ThinkPad"))
	laptop.add_child(TreeNode("Samsung"))

	
	cellphoone = TreeNode("Cell Phone")
	cellphoone.add_child(TreeNode("iPhone"))
	cellphoone.add_child(TreeNode("Google Pixel"))
	cellphoone.add_child(TreeNode("Vivo"))
	cellphoone.add_child(TreeNode("Samsung"))

	
	tv = TreeNode("TV")
	tv.add_child(TreeNode("Onida"))
	tv.add_child(TreeNode("OnePlus"))


	root.add_child(laptop)
	root.add_child(cellphoone)
	root.add_child(tv)
	
	return root


if __name__ == '__main__':
	root = build_product_tree()
	#print(root.get_level())
	root.print_tree()
	pass