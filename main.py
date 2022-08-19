
from IconChanger import IconChanger
from Chessman import*
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton
from PyQt5.QtCore import QSize


class Chess(QMainWindow):
	def __init__(self):
		super().__init__()
		loadUi('board.ui', self)
		self.Pawn = Pawn()
		self.Knight = Knight()
		self.Bishop = Bishop()
		self.Rook = Rook()
		self.Queen = Queen()
		self.King = King()
		self.glayout = QGridLayout(self.frame)
		self.glayout.setSpacing(0)
		self.board = [['Rb', 'Nb', 'Bb', 'Qb', 'Kb', 'Bb', 'Nb', 'Rb'],
					  ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
					  ['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'],
					  ['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'],
					  ['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'],
					  ['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'],
					  ['Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw'],
					  ['Rw', 'Nw', 'Bw', 'Qw', 'Kw', 'Bw', 'Nw', 'Rw']]
		self.dict = {
						'P': self.Pawn.check_all__, 'N': self.Knight.check_all__,
						'B': self.Bishop.check_all__, 'R': self.Rook.check_all__,
						'Q': self.Queen.check_all__, 'K': self.King.check_all__,
					}
		self.icon_changer = IconChanger()
		self.banco = self.create()
		self.show()


	def create(self):
		for i in range(8):
			for j in range(8):
				self.ChessBox = QPushButton()
				self.ChessBox.clicked.connect(lambda _, r=i, c=j: self.on_click(r, c))
				self.ChessBox.setFixedSize(100, 100)
				self.glayout.addWidget(self.ChessBox, i, j)
				self.glayout.itemAtPosition(i, j).widget().setIconSize(QSize(100, 100))
				self.glayout.itemAtPosition(i, j).widget().setStyleSheet(f"background-color: {'#4a4a4a' if (i+j)%2 else '#eaeaea'}")
				self.icon_changer.changer_img__(self.glayout, i, j, self.board[i][j])


	def on_click(self)-> None: pass
	def on_click_phai(self) -> None: pass



class ChessGameplay(Chess):
	def __init__(self):
		Chess.__init__(self)
		self.rch = ()
		self.Numclick = 0
		self.possible_moves = []
		self.Player = 'white'
	

	def on_click(self, r, c):
		self.icon_changer.changer_color__(self.glayout, self.possible_moves, 'B')
		if self.Numclick==0:
			if self.board[r][c] == 'no':
				self.possible_moves = []
				return
			
			namechess = self.board[r][c]
			
			if self.Player == 'white' and ('w' in namechess):
						self.possible_moves = self.dict[namechess[:1]](self.glayout, self.board, r, c, 'b')
			elif self.Player == 'black' and ('b' in namechess):
						self.possible_moves = self.dict[namechess[:1]](self.glayout, self.board,  r, c, 'w')
			self.rch = (r, c)
			self.Numclick = 1

		elif self.Numclick==1:
			rh, ch = self.rch
			if self.possible_moves==[]:
				self.Numclick = 0
				return

			if (r, c) in self.possible_moves:
				col = self.board[rh][ch]
				self.Player = 'white' if self.Player=='black' else 'black'

				if ('P' in col) and (r == 0 or r == 7):
					col = 'Q' + col[1]
					self.board[r][c] = 'Q'+col[1]
				else:
					self.board[r][c] = col
				self.icon_changer.make_move(self.glayout, r, c, rh, ch, col)
				self.board[rh][ch] = 'no'
				self.possible_moves.clear()
				self.Numclick = 0
			
			else:
				self.Numclick = 0
				self.on_click(r, c)


if __name__ == '__main__':
	app = QApplication([])
	window = ChessGameplay()
	app.exec_()