import BST
print("1.Design a BST class with methods to add element, search element, number of elements anddelete requested element. Provide test cases.")
b=BST.BST()
#ADD
b.add_node(8)
b.add_node(3)
b.add_node(10)
b.add_node(1)
b.add_node(6)
b.add_node(4)
b.add_node(7)
b.add_node(14)
b.add_node(13)

#print(b.inOrder())
#COUNT
print(b.node_count())
print(b.isEmpty())

#DELETE
b.delete_node(13)

print("SEARCH")
print(b.Lookup(8))
print(b.Lookup(3))
print(b.Lookup(10))
print(b.Lookup(1))
print(b.Lookup(6))
print(b.Lookup(4))
print(b.Lookup(7))
print(b.Lookup(14))
print(b.Lookup(13))

#NEGATIVE SEARCH
print(b.Lookup(12))
print(b.Lookup(100))

print("2.Add methods to in-order, pre-order, post-order and level-order traversals")
print("IN ORDER")
print(b.inOrder())
print("PRE-ORDER")
b.preOrder()
print("LEVEL ORDER")
print(b.level_order())
print("POST ORDER")
b.postOrder()

print("3.Add methods to display the traversal in ascending and descending order.")
print("ASCENDING")
b.inOrder()
print("DESCENDING")
b.desc()

print('4.Add method to find the height of binary search tree. Provide test cases.')
print("HEIGHT")
print(b.height())
assert(b.height()==4)

print("5.Add method to count the number of terminal nodes in BST. Provide test cases.")

print(b.terminalNodes())
assert(b.terminalNodes()==4)


print("6.Add methods to find max and min element in BST. Provide test cases.")

print(b.findMin())
print(b.findMax())
assert(b.findMin()==1)
assert(b.findMax()==14)

print("8. Add method to count number of nodes in the left sub tree and number of nodes in right subtree. Provide test cases.")

print(b.treecount())
assert(b.treecount()==(5,2))

#b.subtreecount(14)

print("9.Add method the check whether two BSTs are same. Provide test cases.")
b1=BST.BST()
b1.add_node(8)
b1.add_node(3)
b1.add_node(10)
b1.add_node(1)
b1.add_node(6)
b1.add_node(4)
b1.add_node(7)
b1.add_node(14)
b1.add_node(13)

b2=BST.BST()
b2.add_node(8)
b2.add_node(3)
b2.add_node(10)
b2.add_node(1)
b2.add_node(6)
b2.add_node(4)
b2.add_node(7)
b2.add_node(14)
b2.add_node(13)



def same(t1,t2): 
	if t1.isEmpty()==True and t2.isEmpty()==True: 
		return True 
	else:
		a=list(t1.level_order())
		b=list(t2.level_order())
		print(a)
		print(b)
		if a==b:
			return True
		else:
			False

print(same(b1,b2))
assert(same(b1,b2)==True)