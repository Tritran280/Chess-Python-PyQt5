from PyQt5.QtGui import QIcon, QPixmap

class IconChanger():
	def changer_img__(self, layout, r, c, img):
		imgdict_ = { 'Pb': "./Img/Pawn_Black.png",
					 'Pw': "./Img/Pawn_White.png",
					 'Nb': "./Img/Knight_Black.png", 
					 'Nw': "./Img/Knight_White.png",
					 'Bb': "./Img/Bishop_Black.png",
					 'Bw': "./Img/Bishop_White.png",
					 'Rb': "./Img/Rook_Black.png",
					 'Rw': "./Img/Rook_White.png",
					 'Qb': "./Img/Queen_Black.png",
					 'Qw': "./Img/Queen_White.png",
					 'Kb': "./Img/King_Black.png",
					 'Kw': "./Img/King_White.png",
					 'no': "" }
		layout.itemAtPosition(r, c).widget().setIcon(QIcon(QPixmap(imgdict_[img])))

	def make_move(self, layout, r, c, rh, ch, col):
		
		self.changer_img__(layout, r, c, col)
		self.changer_img__(layout, rh, ch, 'no')
		

	def changer_color__(self, layout, list, c):
		colorlist_ = { 'YL0': "#6d7351", 'YL1': "#cfd999", 'BLK': "#4a4a4a", 'WHT': "#eaeaea" }
		for val in list:
			try:
				x, y = val[0], val[1]
				col = ('YL0'if (x+y)%2 else 'YL1') if ('Y' in c) else ('BLK' if (x+y)%2 else 'WHT')
				layout.itemAtPosition(x, y).widget().setStyleSheet("background-color: " + colorlist_[col])
			except: pass