# python3 /users/haoransong/Desktop/python/5qi.py

import random

def play_wuziqi():

	a = make_board()
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
		btn = bw%2+1		
		print_board(a)
		if btn == 1:
			move = input('next?\n').lower()
		else:
			move = robot([x,y,z1,z2],bw%2+1,bw,b)
			if not move:
				move = input('nextwhite?\n').lower()

		if move == 'aaa':
				break			
		elif move == 'save':
			break
		
		if move[0] in b:
			if int(move[1:]) <= 13:
				pass
			else:
				print('error')
				continue		
		else:	
			print('error')
			continue
		if len(move) == 2 or len(move) == 3:
			if move[0] in b or move[-1] in b:
				pass
			else:
				print('error')
				continue
		else:
			print('error')
			continuex

		if move[0] in b:
			xx = int(move[1:])-1
			yy = b.index(move[0])
			if a[xx][yy] != '.':
				print('error')
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
				if btn == 1:
					a[xx][yy] = 'O'
				else:
					a[xx][yy] = 'X'
		
		else:
			xx = int(move[:-1])-1
			yy = b.index(move[-1])
			if a[xx][yy] != '.':
				print('error')
				continue
			else:
				x[xx][yy] = btn
				y[yy][xx] = btn
				z1[xx+yy][13-xx] = btn
				z2[12+xx-yy][xx] = btn
				a[xx][yy] = btn
		
		
		if if_win([x,y,z1,z2],btn):
			print_board(a)
			print('%s win' % btn)
			break
		

		bw += 1

def make_board():
	a = []	
	for i in range(13):
		a.append([])
		for i1 in range(13):
			a[-1].append('.')
	return a

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
	if bw1 == 1:
		if a[0][6][6] == 0:
			return('g7')
		else:
			move_all = ['f6','g6','h6','f7','h7','f8','g8','h8']
			return(move_all[random.randint(0,7)])
	all_ma0 = ['02222','22220','22022','20222','22202','01111','11110','11011','11101','10111']
	all_ma1 = ['022200','002220','020220','022020']
	all_ma2 = ['2011100','0011102','010110','011010','01110']
	all_ma3 = ['22200','02220','20220','22020']
	all_ma4 = ['02200','2020','11100','01110','10110','11010','01100','00111']#,'000110','011000','001100','010100','001010']
	all_ma5 = ['20']
	all_ma = [all_ma0,all_ma1,all_ma2,all_ma3,all_ma4,all_ma5]
	for i in range(len(all_ma)):
		if i == 1:
			move = robot_h(all_ma[i],a,1)
		elif i == 2:
			move = robot_h(all_ma[i],a,2)
		else:
			move = robot_h(all_ma[i],a,0)
		if move:
			if move.index(' ') == 1:
				return '%s' % b[int(move[0])] + '%s' % (int(move[1:])+1)
			else:
				return '%s' % b[int(move[:2])] + '%s' % (int(move[3:])+1)


def robot_h(all_ma,a,nu):
	b = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
	all_ind = []
	all_move = []
	for li in range(len(a)):
		for i1 in range(len(a[li])):
			num = ''
			for i2 in a[li][i1]:
				num += '%s' % i2
			
			for o in all_ma:
				if o in num:
					print('in',o,li)
					if nu == 1:
						ind = 0
						for t in o:
							if t == 0:
								ind += 1
								if ind == 2:
									return loc(num.index(o)+t,li,i1)

					for t in range(len(o)):
						if o[t] == '0':							
							all_move.append(loc(num.index(o)+t,li,i1))
					if len(all_move) == 1:
						return all_move[0]
					return choose(all_move,a)
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
			z1 = a[2][int(i[0])+int(i[1:])]
			z2 = a[3][12+int(i[0])-int(i[1:])]
		else:
			x = a[0][int(i[:2])]
			y = a[1][int(i[3:])]
			z1 = a[2][int(i[:2])+int(i[3:])]
			z2 = a[3][12+int(i[:2])-int(i[3:])]
		print(x,y,z1,z2)
		grade_all.append(x.count(2)*2+x.count(1)+y.count(2)*2+y.count(1)+z1.count(2)*2+z1.count(1)+z2.count(2)*2+z2.count(1))

	ma = 0
	for i in grade_all:
		if i > ma:
			ma = i
	co = grade_all.count(ma)
	print(grade_all,ma,co,all_move,end = '')
	if co == 1:
		return all_move[grade_all.index(ma)]
	else:
		ind = random.randint(1,co)
		print(ind)
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
