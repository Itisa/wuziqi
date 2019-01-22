# python3 /users/haoransong/Desktop/python/5qi.py

import json

def wuziqi():

	a = make_board()
	x = []
	for i in range(13):
		x.append([])
		for i1 in range(13):
			x[-1].append(0)
	y = x[:]
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
			move = robot([x,y,z1,z2],bw%2+1)
			if not move:
				move = input('next?\n').lower()

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

		if move[0] in b:
			xx = int(move[1:])-1
			yy = b.index(move[0])
			# print(xx,yy)
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
				a[xx][yy] = btn
		
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

def robot(a,bw):
	all_ma = ['02222','22220','22022','01111','11110','11011','022200','002220','020220','022020','011100','001110','010110','011010','22200','02220','20220','22020','000220','022000','002200','020200','002020','11100','01110','10110','11010','000110','011000','001100','010100','001010']
	b = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
	all_ind = []
	print('aaaaaa')
	
	for i in range(len(a)):
		for i1 in range(len(a[i])):
			num = ''
			for i2 in a[i][i1]:
				num += '%s' % i2
			# print(num)
			
			for o in all_ma:
				if o in num:
					print('in')
					for t in range(len(o)):
						if o[t] == '0':
							all_ind.append(t)
					lo = num.index(o)
					print(lo,t)
					return(loc(lo+all_ind[-1],i,i1,b))
							

def loc(lo,i,i1,b):

	print(lo,i,i1)
	if i == 1:
		return '%s' % b[i1] + '%s' % (lo)
	elif i == 0:
		return '%s' % b[lo-1] + '%s' % (i1+1)
	elif i == 2:
		pass

if __name__ == '__main__':
	wuziqi()
