# E:/newpy/wuziqi/wuziqi/wuziqi.py

import json

def wuziqi():
	with open('E:/newpy/wuziqi/qipu.txt','r') as f:
		x = f.read()
		if x != '':
			a = json.loads(x)
		else:
			a = make_board()
		f.close()

	x = []
	for i in range(13):
		x.append([])
		for i1 in range(13):
			x[-1].append(0)
	y = x[:]
	z1 = []
	for i in range(25):
		z1.append([])
		if i <= 13:
			n = i+1
		else:
			n = 25-i
		for i1 in range(n):
			z1[-1].append(0)
	z2=z1[:]
	b = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
	# b1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
	bw = 0
	


	while True:
		print_board(a)
		move = input('next?\n').lower()
		btn = bw%2+1


		if move == 'aaa':
			with open('E:/newpy/wuziqi/qipu.txt','w') as f:
				f.close()
				break
		
		elif move == 'save':
			with open('E:/newpy/wuziqi/qipu.txt','w') as f:
				f.write(json.dumps(a))
				f.close()
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
		
		if if_win([x,y,z1,z2],bw%2+1):
			bwf = bw%2+1
			print_board(a)
			print('%s win' % bwf)
			
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
	# print('board')

def if_win(a,bw):
	# pass
	fi = 0
	for i in a:
		for i1 in i:
			for i2 in i1:
				
				if i2 == bw:
					fi += 1
					if fi == 5:
						# print(a)
						# print(i1)
						# print(i2)
						# print(bw,fi)

						return True
				else:
					fi = 0
def robot():
	pass

if __name__ == '__main__':
	wuziqi()