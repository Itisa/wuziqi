# E:/newpy/wuziqi/wuziqi.py

import json

def wuziqi():
	with open('E:/newpy/wuziqi/qipu.txt','r') as f:
		x = f.read()
		if x != '':
			a = json.loads(x)
		else:
			a = make_board()
		f.close()

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
		elif move[0] in b:
			if a[int(move[1:])-1][b.index(move[0])] != '.':
				print('error')
				continue
			else:
				a[int(move[1:])-1][b.index(move[0])] = btn
		else:
			if a[int(move[:-1])-1][b.index(move[-1])] != '.':
				print('error')
				continue
			else:
				a[int(move[:-1])-1][b.index(move[-1])] = btn
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
		board = '__'.join(board)
		if x < 10:
			print(' ',x,'',board,'',x)
		else:
			print('',x,'',board,'',x)
	print('    ','A','','B','','C','','D','','E','','F','','G','','H','','I','','J','','K','','L','','M')
	# print('board')

if __name__ == '__main__':
	wuziqi()