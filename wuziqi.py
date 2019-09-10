# python3 /users/haoransong/Desktop/python/5qi.py

import random

def play_wuziqi():
	first = 1 #1:player first 2:computer first
	board = make_board()
	x = []
	for i in range(13):
		x.append([])
		for i1 in range(13):
			x[-1].append(0)
	y = []
	for i in range(13):
		y.append([])
		for i1 in range(13):
			y[-1].append(0)

	z1 = []
	for i in range(25):
		z1.append([])
		if i <= 12:
			n = i+1
		else:
			n = 25-i
		for i1 in range(n):
			z1[-1].append(0)
	# z2=z1[:]
	z2 = []
	for i in range(25):
		z2.append([])
		if i <= 12:
			n = i+1
		else:
			n = 25-i
		for i1 in range(n):
			z2[-1].append(0)
	
	b = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
	bw = 0
	
	while True:
		btn = bw%2+first%2
		print('btn:',btn)
		print_board(board)
		if btn == 1:
			move = input('next?\n').lower()
		else:
			move = robot([x,y,z1,z2],bw%2+1,bw,b)
			print(move)
			if not move:
				move = input('nextwhite?\n').lower()
			xx = int(move[1:])-1
			yy = b.index(move[0])
			if board[xx][yy] != '.':
				print('Error:there has been placed')
				move = input('nextwhite?\n').lower()

		if move == 'aaa':
			break			
		elif move == 'save':
			break
		
		if move[0] in b:
			if int(move[1:]) <= 13:
				pass
			else:
				print('Error:input type error')
				continue		
		else:
			print('Error:input type error')
			continue

		if move[0] in b:
			xx = int(move[1:])-1
			yy = b.index(move[0])
			if board[xx][yy] != '.':
				print('Error:there has been placed')
				continue
			else:
				if xx+yy >= 12:
					z1[xx+yy][12-yy] = btn
				else:
					z1[xx+yy][yy] = btn
				if 12+xx-yy >= 12:
					z2[12+xx-yy][yy] = btn
				else:
					z2[12+xx-yy][xx] = btn
				x[xx][yy] = btn
				y[yy][xx] = btn
				if btn == first:
					board[xx][yy] = 'O'
				else:
					board[xx][yy] = 'X'
				# print('X'*50)
				# for line in x:
				# 	print(line)
				# print('X'*50)
		
		else:
			xx = int(move[:-1])-1
			yy = b.index(move[-1])
			if board[xx][yy] != '.':
				print('Error:there has been placed')
				continue
			else:
				x[xx][yy] = btn
				y[yy][xx] = btn
				z1[xx+yy][13-xx] = btn
				z2[12+xx-yy][xx] = btn
				board[xx][yy] = btn
		
		
		if if_win([x,y,z1,z2],btn):
			print_board(board)
			if btn == first:
				if first == 1:
					print('win')
				else:
					print('lose')	
			else:
				if first == 1:
					print('lose')
				else:
					print('win')
			break
		

		bw += 1

def make_board():
	board = []	
	for i in range(13):
		board.append([])
		for i1 in range(13):
			board[-1].append('.')
	return board

def print_board(a):
	print('\n','   ','A','','B','','C','','D','','E','','F','','G','','H','','I','','J','','K','','L','','M')
	x = 0
	for i in a:
		x += 1
		board = []
		for i1 in i:
			board.append('%s' % i1)
		board = '  '.join(board)
		if x < 10:
			print(' ',x,'',board,'',x)
		else:
			print('',x,'',board,'',x)
	print('    ','A','','B','','C','','D','','E','','F','','G','','H','','I','','J','','K','','L','','M')

def if_win(a,bw):
	if bw == 0:
		bw = 2
	fi = 0
	for i in a:
		for i1 in i:
			for i2 in i1:				
				if i2 == bw:
					fi += 1
					if fi == 5:
						return True
				else:
					fi = 0

def robot(a,bw,bw1,b):
	def locate(i,i1,s1,line,reverse=False):
		if reverse == True:
			if i <= 1:
				lo = '%s' % (12-line.find(s1)-s1.find('0'))
			else:
				if i >= 12:
					lo = '%s' % (26-i1-line.find(s1)-s1.find('0'))
				else:
					lo = '%s' % (i1-line.find(s1)-s1.find('0'))					
		else:
			lo = '%s' % (line.find(s1)+s1.find('0'))
		if i == 0:
			move = b[int(lo)] + '%s' % ((int(i1))+1)
			# b[i1] + '%s' % (int(lo)+1)
		elif i == 1:
			move = b[i1] + '%s' % (int(lo)+1)
		elif i == 2:
			if i1 < 12:
				move = b[int(lo)] + '%s' %(i1-int(lo)+1)
			else:
				move = b[(12-int(lo))] + '%s' %(i1-11+int(lo))
		elif i == 3:
			if i1 >= 12:
				move = b[int(lo)] + '%s' % (i1-11+int(lo))
			else:
				move = b[(12-i1+int(lo))] + '%s' % (int(lo)+1)
		print('move:',move)
		print('i:',i,'i1:',i1,'s1:',s1,'line:',line,'lo:',lo,reverse)
		return move
	
	def robot_h(all_ma):
		all_ind = []
		all_move = []
		for li in range(len(a)):
			for i1 in range(len(a[li])):
				num = []
				for i2 in a[li][i1]:
					num.append('%s' % i2)
				numr = num[:]
				numr.reverse()
				numr = ''.join(numr)
				num = ''.join(num)
				for s1 in all_ma:
					if s1 in num:
						return locate(li,i1,s1,num)
					elif s1 in numr:
						return locate(li,i1,s1,numr,True)
						# print('in',s1,li)
						# for t in range(len(s1)):
							# if o[t] == '0':							
								# all_move.append(loc(num.index(s1)+t,li,i1))
						
						# all_move.append(locate(li,i1,s1,num))
						# if len(all_move) == 1:
							# return all_move[0]
						# return choose(all_move,a)

	if bw1 <= 1:
		if a[0][6][6] == 0:
			return('g7')
		else:
			move_all = ['f6','g6','h6','f7','h7','f8','g8','h8']
			return(move_all[random.randint(0,7)])
	all_ma0 = ['02222','22220','22022','20222','22202','01111','11110','11011','11101','10111']
	all_ma1 = ['02220','22200','00222','22020','01110','10110','11010']
	all_ma2 = ['22200','02220','20220','22020']
	all_ma3 = ['11100','01110','02200','2020','10110','11010','01100','00111']#,'000110','011000','001100','010100','001010']
	all_ma4 = ['20']
	
	move = robot_h(all_ma0)
	print(0)
	if move:
		return move
		# if move.index(' ') == 1:
		# 	return '%s' % b[int(move[0])] + '%s' % (int(move[1:])+1)
		# else:
		# 	return '%s' % b[int(move[:2])] + '%s' % (int(move[3:])+1)
	
	def if_4zi():
		line = ''
		for i in range(len(a)): #i:each board
			for i1 in range(len(a[i])): #i1:each board's line
					
				line = ''
				for s1 in a[i][i1]:
					line += '%s' % s1
				for s in all_ma0:
					if s in line:
						move = locate(i,i1,s,line)
	# if_4zi()

	move = robot_h(all_ma1)
	print(1,move)
	if move:
		return move

	move = robot_h(all_ma2)
	print(2,move)
	if move:
		return move
	
	move = robot_h(all_ma3)
	print(3)
	if move:
		return move

	move = robot_h(all_ma4)
	print(4)
	if move:
		return move
	
def loc(lo,i,i1):
	print(lo,i,i1)
	if i == 1:
		move = '%s' % i1 + ' ' + '%s' % (lo)
		print(move)
		return move
	elif i == 0:
		move = '%s' % lo + ' ' + '%s' % (i1)
		print(move)
		return move
	elif i == 2:
		if i1 < 12:
			move = '%s' % lo + ' ' + '%s' %(i1-lo)
		else:
			move = '%s' % (12-lo) + ' ' + '%s' %(i1-12+lo)
		print(move)
		return move
	elif i == 3:
		if i1 >= 12:
			move = '%s' % lo + ' ' + '%s' % (i1-12+lo)
		else:
			move = '%s' % (12-i1+lo) + ' ' +'%s' % (lo)
		print(move)
		return move


def choose(all_move,a):
	grade_all = []
	for i in all_move:
		if i.index(' ') == 1:
			x = a[0][int(i[0])]
			y = a[1][int(i[1:])]
		else:
			x = a[0][int(i[:2])]
			y = a[1][int(i[3:])]

		grade_all.append(x.count('2')-x.count('1')+y.count('2')-y.count('1'))

	ma = 0
	for i in grade_all:
		if i > ma:
			ma = i
	co = grade_all.count(ma)
	print(grade_all,ma,co,all_move)
	if co == 1:
		return all_move[grade_all.index(ma)]
	else:
		ind = random.randint(1,co)
		ix = 0
		i1 = -1
		for i in grade_all:
			i1 += 1
			if i == ma:
				ix += 1
				if ix == ind:
					return all_move[i1]


if __name__ == '__main__':
	play_wuziqi()
