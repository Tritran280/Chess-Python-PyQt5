from IconChanger import IconChanger


def is_movable(board, row, col, target_color):
	try:
		if board[row][col]=='no' or (target_color in board[row][col]):
			return True
		else:
			return False
	except: return False

def get_possible_moves(board, row, col, horizontal_dir, vertical_dir, target_color) -> list:
	possible_moves = []
	for i in range(1, 8):
		curr_r = row + i*horizontal_dir
		curr_c = col + i*vertical_dir
		try:
			if board[curr_r][curr_c]=='no':
				possible_moves.append((curr_r, curr_c))
			else:
				if (target_color in board[curr_r][curr_c]):
					possible_moves.append((curr_r, curr_c))
				break
		except: break
	return possible_moves


class Chessman():
	def __init__(self) -> None:
		self.icon_changer = IconChanger()

class Pawn(Chessman):
	def find_possible_moves(self, board, column, row, direction, endPos, color) -> list:
		possible_moves = []
		for i in range(row+direction, endPos+direction, direction):
			if board[i][column]=='no':
				possible_moves.append((i, column))
			else: break
		if (column-direction>=0 and column-direction<8) and (color in board[row+direction][column-direction]): 
			possible_moves.append((row+direction, column-direction))

		if (0<=column+direction and column+direction<8) and (color in board[row+direction][column+direction]):
			possible_moves.append((row+direction, column+direction))

		return possible_moves

	def check_all__(self, layout, board, r, c, col):
		possible_moves = []
		if col =='b':
			possible_moves = self.find_possible_moves(board, c, r, -1, (r-2 if(r==6) else r-1), 'b')
		if col =='w':
			possible_moves = self.find_possible_moves(board, c, r, 1, (r+2 if(r==1) else r+1), 'w')
		self.icon_changer.changer_color__(layout, possible_moves, 'YL0')
		return possible_moves


class Knight(Chessman):
	def check_all__(self, layout, board, r, c, col):
		possible_moves = []
		knightMoves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
		for m in knightMoves:
			endRow = r + m[0]
			endCol = c + m[1]
			if is_movable(board, endRow, endCol, col):
				possible_moves.append((endRow, endCol))

		self.icon_changer.changer_color__(layout, possible_moves, 'YL0')
		return possible_moves


class Bishop(Chessman):
	def check_all__(self, layout, board, r, c, col):
		possible_moves = []
		directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))
		for d in directions:
			possible_moves.extend(get_possible_moves(board, r, c, d[0], d[1], col))

		self.icon_changer.changer_color__(layout, possible_moves, 'YL0')
		return possible_moves


class Rook(Chessman):
	def check_all__(self, layout, board, r, c, col):
		possible_moves = []
		directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
		for d in directions:
			possible_moves.extend(get_possible_moves(board, r, c, d[0], d[1], col))

		self.icon_changer.changer_color__(layout, possible_moves, 'YL0')
		return possible_moves


class Queen(Chessman):
	def check_all__(self, layout, board, r, c, col):
		possible_moves = []
		directions = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
		for d in directions:
			possible_moves.extend(get_possible_moves(board, r, c, d[0], d[1], col))

		self.icon_changer.changer_color__(layout, possible_moves, 'YL0')
		return possible_moves


class King(Chessman):
	def check_all__(self, layout, board, r, c, col):
		possible_moves = []
		KingMoves = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
		for m in KingMoves:
			endRow = r + m[0]
			endCol = c + m[1]
			if is_movable(board, endRow, endCol, col):
				possible_moves.append((endRow, endCol))

		self.icon_changer.changer_color__(layout, possible_moves, 'YL0')
		return possible_moves