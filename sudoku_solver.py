sudoku = [	[0,4,0,0,0,7,1,0,0],
			[5,3,0,0,9,0,0,7,0],
			[0,0,7,0,6,0,9,4,0],
			[4,0,6,0,8,0,7,5,1],
			[0,1,0,0,0,0,6,9,0],
			[0,5,3,0,1,0,0,0,2],
			[9,6,0,0,3,0,0,1,0],
			[3,7,0,0,5,1,0,0,0],
			[1,0,0,2,0,9,3,6,7]]

def slove(bo):
	find = find_empty(bo)
	if not find:
		return True
	else:
		row,column = find
	for i in range(1,10):
		if check_valid(bo,i,(row,column)):
			bo[row][column] = i
			if slove(bo):
				return True
			bo[row][column] = 0
	return False	
	
	
def check_valid(bo,num,position):
	# row check
	for i in range(len(bo[0])):
		if bo[position[0]][i]  == num and i != position[0]:
			return False
	#column check	
	for i in range(len(bo)):
		if bo[i][position[1]] == num and i != position[1]:
			return False
	#check box
	for i in range((position[0]//3)*3,(position[0]//3)*3 + 3):
		for j in range((position[1]//3)*3,(position[1]//3)*3 + 3):
			if bo[i][j] == num and (i,j) != position:
				return False
	return True
	

def print_board(bo):
	for i in range(len(bo)):
		if i % 3 == 0 and i != 0:
			print("--------------------")
		for j in range(len(bo[0])):
			if j % 3 == 0 and j != 0:
				print(" | ",end="")
			if j==8:
				print(bo[i][j])
			else:
				print(str(bo[i][j]) + " ",end="")
	
def find_empty(bo):
	for i in range(len(bo)):
		for j in range(len(bo[0])):
			if bo[i][j] == 0:
				return (i,j)	# raw, column
			
	return None
				
print_board(sudoku)
slove(sudoku)
print("--------------------------")
print("--------------------------")
print_board(sudoku)		
