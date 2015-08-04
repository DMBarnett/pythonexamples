







class LinkNode():
	def __init__(self, key, next):
		self.key = key
		self.next = next

class LinkedList():
	def __init__(self):
		self.head = None
	def pop(self):
		if self.head == None:
			return None
		popper = self.head
		self.head = self.head.next
		return popper.key
	def remove(self, key):
		current = self.head
		# 1 -> 2 -> 3 -> 4
		while current.next != None:
			if current.key == key:
				current.key = current.next.key
				current.next = current.next.next				
				return None
			elif current.next.key == key:
				if current.next.next == None:
					current.next = None
					return None
				else:
					current = current.next
			else:
				current = current.next	
	def add(self, key):
		self.head = LinkNode(key, self.head)
	def printList(self):
		current = self.head
		while current.next != None:
			print current.key
			current = current.next
		print current.key
	
our_list = LinkedList()
our_list.add(27)
our_list.add(3)
our_list.add(2)
our_list.add(1)
our_list.printList()