class Node:
	def __init__(self,key):
		self.val = key
		self.next = None

class Linkedlist():
	def __init__(self):
		self.head = None

	def append(self, key):
		if not self.head:
				self.head = Node(key)
				return self
		curr = self.head
		while curr.next:
				curr = curr.next
		curr.next = Node(key)
		return self

	def print(self):
		res = []
		curr = self.head
		while curr:
				res.append(curr.val)
				curr = curr.next
		print(res)
		return self

	def delete(self,key):
			curr = self.head
			prev = None

			while curr:
					if curr.val == key:
							prev.next = curr.next
							curr = None
							return self
					else:
							prev = curr
							curr = curr.next
			return self






ll = Linkedlist()
ll.append(12).append(24).append(24).append(54).append(64).append(84).print().delete(64).delete(24).delete(114).print().append(44).print()